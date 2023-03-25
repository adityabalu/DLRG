
'''
For the Fashion MNIST dataset, train a model such that given the input image,
you reconstruct the image back and simultaneously classify the images. I.e. a combined
model which can act as an autoencoder and a classifier simultaneously.
'''

import torch
import torch.nn as nn

class AutoencoderClassifier(nn.Module):
    def __init__(self, num_classes):
        super(AutoencoderClassifier, self).__init__()

        # Encoder
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        # Decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(16, 1, kernel_size=2, stride=2),
            nn.Sigmoid()
        )

        # Classifier
        self.classifier = nn.Sequential(
            nn.Linear(576, 32),
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
