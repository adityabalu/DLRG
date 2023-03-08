import argparse
import os
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from pytorch_lightning import Trainer, seed_everything
from pytorch_lightning.loggers import TensorBoardLogger
import pytorch_lightning as pl
import trainer


# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', type=str, default='data', help='Path to the dataset directory')
parser.add_argument('--log_dir', type=str, default='logs', help='Path to the log directory')
parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
parser.add_argument('--num_workers', type=int, default=16, help='Number of workers for data loading')
parser.add_argument('--fast_dev_run', action='store_true', help='Whether to run a fast development check')
parser.add_argument('--max_epochs', type=int, default=10, help='Maximum number of epochs to train for')

# Parse the arguments
args = parser.parse_args()

# Set the seed for reproducibility
seed_everything(42)

# Define the data transforms
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

# Load the datasets
train_set = datasets.MNIST(root=args.data_dir, train=True, transform=transform, download=True)
val_set = datasets.MNIST(root=args.data_dir, train=False, transform=transform, download=True)

# Define the data loaders
train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, num_workers=args.num_workers)
val_loader = DataLoader(val_set, batch_size=args.batch_size, shuffle=False, num_workers=args.num_workers)

# Initialize the logger
logger = TensorBoardLogger(args.log_dir, name='mnist')

# initialize models
my_models = trainer.MyModel()

# initialize trainer
my_trainer = pl.Trainer(
    logger=logger,
    max_epochs=args.max_epochs,
    fast_dev_run=args.fast_dev_run,
    gpus=1 if torch.cuda.is_available() else 0,
)

# train models
my_trainer.fit(my_models, train_loader, val_loader)


# save models
torch.save(my_models.big_cnn, 'big_cnn.pt')
torch.save(my_models.little_cnn, 'little_cnn.pt')
torch.save(my_models.mlp, 'mlp.pt')