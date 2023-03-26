import torch
from torch.utils.data import DataLoader
import pytorch_lightning as pl
from torchvision import datasets, transforms
from pytorch_lightning import seed_everything
from pytorch_lightning.loggers import WandbLogger

import sys 
sys.path.append('../task_1/')
from models import LittleCNN, MLP

from argparse import Namespace
import argparse

import individual_trainer as it

'''
This script is used to train the LittleCNN and MLP models on the MNIST dataset.
run the script with the following command:
python main.py --model LittleCNN --optimizer Adam --learning_rate 0.001 --batch_size 32 --max_epochs 10
python main.py --batch_size 32 --max_epochs 10 --model LittleCNN --optimizer Adam --learning_rate 0.001

'''

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Training script for LittleCNN/MLP')

# Add arguments for hyperparameters and Parse the command-line arguments
parser.add_argument('--data_dir', type=str, default='../task_1/data', help='Path to the dataset directory')
parser.add_argument('--log_dir', type=str, default='logs', help='Path to the log directory')
parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
parser.add_argument('--num_workers', type=int, default=16, help='Number of workers for data loading')
parser.add_argument('--fast_dev_run', action='store_true', help='Whether to run a fast development check')
parser.add_argument('--max_epochs', type=int, default=10, help='Maximum number of epochs to train for')
parser.add_argument('--model', type=str, default='LittleCNN', help='Model to use (LittleCNN or MLP)')
parser.add_argument('--optimizer', type=str, default='Adam',  help='Optimizer to use (SGD or Adam)')
parser.add_argument('--learning_rate', type=float, default=0.001, help='Learning rate for the optimizer')
args = parser.parse_args()

# Create an instance of the Trainer class with the parsed arguments
model_and_optimizer=Namespace(
    model=args.model,
    optimizer=args.optimizer,
    learning_rate=args.learning_rate,
)

print(f'models: {model_and_optimizer.model}')
print(f'optimizer: {model_and_optimizer.optimizer}')


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

# Create an instance of the Trainer class with the parsed arguments
model = it.MyModel(model_and_optimizer)

task_name = (f'{model_and_optimizer.model}_{model_and_optimizer.optimizer}'
        f'_lr_{model_and_optimizer.learning_rate}'
        f'_batch_{args.batch_size}_epochs_{args.max_epochs}')
logger = WandbLogger(project='DLRG', name=task_name, log_model=True)

# initialize trainer
trainer = pl.Trainer(
    logger=logger,
    max_epochs=args.max_epochs,
    fast_dev_run=args.fast_dev_run,
    gpus=1 if torch.cuda.is_available() else 0,
)

# train models
trainer.fit(model, train_loader, val_loader)

