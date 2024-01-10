# Import necessary libraries
import pytorch_lightning as pl
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from pytorch_lightning.callbacks import EarlyStopping
from models.little_cnn import LittleCNN
from models.mlp import MLP

# Load and preprocess the Fashion MNIST dataset
def get_data_loaders(batch_size):
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    train_dataset = datasets.FashionMNIST('./data', train=True, download=True, transform=transform)
    test_dataset = datasets.FashionMNIST('./data', train=False, download=True, transform=transform)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader

# Define the PyTorch Lightning Module for training
class LitModel(pl.LightningModule):
    def __init__(self, model, optimizer_name, learning_rate):
        super().__init__()
        self.model = model
        self.optimizer_name = optimizer_name
        self.learning_rate = learning_rate

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = torch.nn.functional.cross_entropy(y_hat, y)
        self.log('train_loss', loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = torch.nn.functional.cross_entropy(y_hat, y)
        self.log('val_loss', loss)
        return loss

    def configure_optimizers(self):
        if self.optimizer_name == 'SGD':
            optimizer = torch.optim.SGD(self.model.parameters(), lr=self.learning_rate)
        elif self.optimizer_name == 'RMSProp':
            optimizer = torch.optim.RMSprop(self.model.parameters(), lr=self.learning_rate)
        elif self.optimizer_name == 'Adagrad':
            optimizer = torch.optim.Adagrad(self.model.parameters(), lr=self.learning_rate)
        elif self.optimizer_name == 'Adadelta':
            optimizer = torch.optim.Adadelta(self.model.parameters(), lr=self.learning_rate)
        elif self.optimizer_name == 'Adam':
            optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)
        elif self.optimizer_name == 'RAdam':
            optimizer = torch.optim.RAdam(self.model.parameters(), lr=self.learning_rate)
        return optimizer

# Function to initiate training for a model with given configurations
def train_model(model_class, optimizer, learning_rate, batch_size):
    train_loader, val_loader = get_data_loaders(batch_size)
    model = model_class()
    lit_model = LitModel(model, optimizer, learning_rate)

    trainer = pl.Trainer(
        max_epochs=100,
        callbacks=[EarlyStopping(monitor='val_loss', patience=10, mode='min')],
    )

    trainer.fit(lit_model, train_loader, val_loader)

# Main function to execute training experiments
def main():
    optimizers = ['SGD', 'RMSProp', 'Adagrad', 'Adadelta', 'Adam', 'RAdam']
    learning_rates = [1e-2, 1e-3, 1e-4, 1e-5]
    batch_sizes = [32, 64, 128, 256, 512]

    for model_class in [LittleCNN, MLP]:
        for optimizer in optimizers:
            for lr in learning_rates:
                for batch_size in batch_sizes:
                    train_model(model_class, optimizer, lr, batch_size)

if __name__ == "__main__":
    main()
