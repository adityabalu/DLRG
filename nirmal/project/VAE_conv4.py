import torch
import torch.nn as nn
import torch.nn.functional as F
import pytorch_lightning as pl

class Encoder(pl.LightningModule):
    def __init__(self):
        super(Encoder, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=4, stride=2, padding=1)  # 101x101 -> 50x50
        self.conv2 = nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=1) # 50x50 -> 25x25
        self.conv3 = nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1) # 25x25 -> 12x12
        self.conv4 = nn.Conv2d(128, 256, kernel_size=4, stride=2, padding=1) # 12x12 -> 6x6
        self.fc_mu = nn.Linear(256 * 6 * 6, 16)
        self.fc_logvar = nn.Linear(256 * 6 * 6, 16)
    
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x)) 
        x = F.relu(self.conv4(x))
        x = x.view(x.size(0), -1)
        mu = self.fc_mu(x)
        logvar = self.fc_logvar(x)
        return mu, logvar

class Decoder(pl.LightningModule):
    def __init__(self):
        super(Decoder, self).__init__()
        self.fc = nn.Linear(16, 256 * 6 * 6)
        self.deconv1 = nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1) # 6x6 -> 12x12
        self.deconv2 = nn.ConvTranspose2d(128, 64, kernel_size=5, stride=2, padding=1) # 12x12 -> 25x25
        self.deconv3 = nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1) # 25x25 -> 50x50
        self.deconv4 = nn.ConvTranspose2d(32, 1, kernel_size=5, stride=2, padding=1) # 50x50 -> 101x101

    def forward(self, x):
        x = self.fc(x)
        x = x.view(x.size(0), 256, 6, 6)
        x = F.relu(self.deconv1(x))
        x = F.relu(self.deconv2(x))
        x = F.relu(self.deconv3(x)) 
        x = torch.sigmoid(self.deconv4(x))
        return x

class VAE(pl.LightningModule):
    def __init__(self):
        super(VAE, self).__init__()
        self.encoder = Encoder()
        self.decoder = Decoder()

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std
    
    def forward(self, x):
        mu, logvar = self.encoder(x)
        z = self.reparameterize(mu, logvar)
        return self.decoder(z), mu, logvar
    
    def _loss(self, x, x_hat, mu, logvar):
        recon_loss = F.binary_cross_entropy(x_hat, x, reduction='sum')
        kl_div = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
        return recon_loss + kl_div

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)

    def training_step(self, batch, batch_idx):
        x, _ = batch
        x_hat, mu, logvar = self(x)
        loss = self._loss(x, x_hat, mu, logvar)
        self.log('train_loss', loss)
        return loss
    
    def validation_step(self, batch, batch_idx):
        x, _ = batch
        x_hat, mu, logvar = self(x)
        loss = self._loss(x, x_hat, mu, logvar)
        self.log('val_loss', loss)
        return loss
    
    def generate_images(self, num_images=1, device="cpu"):
        with torch.no_grad():
            z = torch.randn(num_images, 16).to(device)
            generated_images = self.decoder(z)
            generated_images = generated_images.view(num_images, 1, 101, 101)
        return generated_images