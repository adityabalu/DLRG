
'''
For the Fashion MNIST dataset, train a model such that given the input image,
you reconstruct the image back and simultaneously classify the images. I.e. a combined
model which can act as an autoencoder and a classifier simultaneously.
'''
import torch
import torch.nn as nn
import pytorch_lightning as pl
import torch.nn.functional as F

class AutoencoderClassifier(pl.LightningModule):
    def __init__(self, num_classes):
        super(AutoencoderClassifier, self).__init__()

        # Encoder
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
        )

        # Decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(16, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 1, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.Sigmoid()
        )

        # Classifier
        self.classifier = nn.Sequential(
            nn.Linear(784, 32),
            nn.ReLU(),
            nn.Linear(32, num_classes)
        )

    def forward(self, x):
        # Encode
        x_encoded = self.encoder(x)

        # Decode
        x_decoded = self.decoder(x_encoded)

        # Classify
        x_flattened = torch.flatten(x_encoded, start_dim=1)
        x_classified = self.classifier(x_flattened)

        return x_decoded, x_classified

    def training_step(self, batch, batch_idx):
            data, target = batch
            reconstructed, classified = self(data)
            mse_loss = self.mse_loss_fn(reconstructed, data)
            ce_loss = self.ce_loss_fn(classified, target)
            loss = mse_loss + ce_loss
            self.log('mse_loss', mse_loss)
            self.log('ce_loss', ce_loss)
            self.log('loss', loss)
            return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        x_decoded, x_classified = self.forward(x)
        mse_loss = nn.MSELoss()(x_decoded, x)
        ce_loss = nn.CrossEntropyLoss()(x_classified, y)
        loss = mse_loss + ce_loss
        self.log('val_loss', loss, prog_bar=True)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.001)
    
    def mse_loss_fn(self, reconstructed, data):
        mse_loss = F.mse_loss(reconstructed, data, reduction='mean')
        return mse_loss

    def ce_loss_fn(self, classified, target):
        ce_loss = F.cross_entropy(classified, target)
        return ce_loss
