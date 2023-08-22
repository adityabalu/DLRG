import torch, os
import torch.nn.functional as F
import pytorch_lightning as pl
from einops import rearrange

from torchvision.utils import save_image, make_grid

#from modules.networks.UnetViT import UViT
from unet import ContextUnet
from schedulers import linear_beta_schedule



class DDPM(pl.LightningModule):
    def __init__(self,
                 n_T=1000,
                 n_feat=128
                 ):
        super(DDPM, self).__init__()
        # self.nn_model = UViT()
        self.nn_model = ContextUnet(in_channels=1, n_feat=n_feat)

        self.betas = linear_beta_schedule(n_T)

        self.ddpm_schedules = self.register_ddpm_schedules(self.betas)

        for k, v in self.ddpm_schedules.items():
            self.register_buffer(k, v)

        self.n_T = n_T

    def register_ddpm_schedules(self, beta_t):
        """
        Returns pre-computed schedules for DDPM sampling, training process.
        """

        sqrt_beta_t = torch.sqrt(beta_t)
        alpha_t = 1 - beta_t
        log_alpha_t = torch.log(alpha_t)
        alphabar_t = torch.cumsum(log_alpha_t, dim=0).exp()

        sqrtab = torch.sqrt(alphabar_t)
        oneover_sqrta = 1 / torch.sqrt(alpha_t)

        sqrtmab = torch.sqrt(1 - alphabar_t)
        mab_over_sqrtmab_inv = (1 - alpha_t) / sqrtmab

        return {
            "alpha_t": alpha_t,  # \alpha_t
            "oneover_sqrta": oneover_sqrta,  # 1/\sqrt{\alpha_t}
            "sqrt_beta_t": sqrt_beta_t,  # \sqrt{\beta_t}
            "alphabar_t": alphabar_t,  # \bar{\alpha_t}
            "sqrtab": sqrtab,  # \sqrt{\bar{\alpha_t}}
            "sqrtmab": sqrtmab,  # \sqrt{1-\bar{\alpha_t}}
            "mab_over_sqrtmab": mab_over_sqrtmab_inv,  # (1-\alpha_t)/\sqrt{1-\bar{\alpha_t}}
        }

    def forward(self, x, t):
        return self.nn_model(x_t, t / self.n_T)

    def sample_forward_diffusion(self, x, _ts, noise):
        x_t = (
                self.sqrtab[_ts, None, None, None] * x
                + self.sqrtmab[_ts, None, None, None] * noise
        )
        return x_t

    def sample_loop(self, batch):
        x_i = torch.randn_like(batch).to(batch)  # x_T ~ N(0, 1), sample initial noise
        for i in range(self.n_T-1, 0, -1):
            t_is = torch.tensor([i / self.n_T]).to(batch)
            t_is = t_is.repeat(batch.size(0),1,1,1)

            z = torch.randn_like(batch).to(batch) if i > 1 else 0

            eps = self.nn_model(x_i, t_is)
            x_i = (
                    self.oneover_sqrta[i] * (x_i - eps * self.mab_over_sqrtmab[i])
                    + self.sqrt_beta_t[i] * z
            )
        return x_i

    def loss(self, x):
        noise = torch.randn_like(x)  # eps ~ N(0, 1)
        _ts = torch.randint(1, self.n_T, (x.shape[0],)).to(x).long()  # t ~ Uniform(0, n_T)
        x_t = self.sample_forward_diffusion(x, _ts, noise)
        return F.mse_loss(noise, self.nn_model(x_t, _ts / self.n_T))

    def training_step(self, batch, batch_idx):
        images, _ = batch
        loss = self.loss(images)
        self.log('train_loss', loss)
        return loss

    def validation_step(self, batch, batch_idx):
        images, _ = batch
        loss = self.loss(images)
        self.log('val_loss', loss)

    def configure_optimizers(self):
        lr = 1e-4
        opt = torch.optim.Adam(self.nn_model.parameters(), lr=lr)
        return opt