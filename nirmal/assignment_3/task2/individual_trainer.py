import torch
import torch.nn as nn
import pytorch_lightning as pl
from models import BigCNN, LittleCNN, MLP

class MyModel(pl.LightningModule):
    def __init__(self, params):
        super().__init__()
        self.params = params

        model_type = self.params.model
        if model_type not in globals():
            raise ValueError(f"Invalid model type specified in hparams: {model_type}")
        self.model = globals()[model_type]()
        print(f"Using model: {model_type}")

        self.loss_fn = torch.nn.CrossEntropyLoss()

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        acc = (y_hat.argmax(dim=1) == y).float().mean()
        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('train_acc', acc, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        acc = (y_hat.argmax(dim=1) == y).float().mean()
        self.log('val_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log('val_acc', acc, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss
    
    def configure_optimizers(self):
        optimizer_class = getattr(torch.optim, self.params.optimizer)
        optimizer = optimizer_class(self.model.parameters(), lr=self.params.learning_rate)
        return {'optimizer': optimizer}

    
