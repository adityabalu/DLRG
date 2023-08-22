import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn

import sys
import autoencoder_classifier as aec

import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
from pytorch_lightning.callbacks import ModelCheckpoint
import argparse


'''
This script trains an autoencoder classifier on the Fashion MNIST dataset.

Example usage:
python main.py --data_dir ./data --log_dir logs --batch_size 32 --num_workers 16 --fast_dev_run --max_epochs 10 --optimizer Adam --learning_rate 0.001 --task_name first_run

common usage:
python main.py --num_workers 16 --fast_dev_run --max_epochs 10  --task_name first_run
'''

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Training Autoencoder Classifier on Fashion MNIST dataset.')

# Add arguments for hyperparameters and Parse the command-line arguments
parser.add_argument('--data_dir', type=str, default='./data', help='Path to the dataset directory')
parser.add_argument('--log_dir', type=str, default='logs', help='Path to the log directory')
parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
parser.add_argument('--num_workers', type=int, default=16, help='Number of workers for data loading')
parser.add_argument('--fast_dev_run', action='store_true', help='Whether to run a fast development check')
parser.add_argument('--max_epochs', type=int, default=10, help='Maximum number of epochs to train for')
parser.add_argument('--optimizer', type=str, default='Adam',  help='Optimizer to use (SGD or Adam)')
parser.add_argument('--learning_rate', type=float, default=0.001, help='Learning rate for the optimizer')
parser.add_argument('--task_name', type=str, default=None, help='Name of the task')
args = parser.parse_args()


# Define transforms
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5,), (0.5,))])

trainset = torchvision.datasets.FashionMNIST(root='./data', train=True,
                                        download=True, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=args.batch_size,
                                          shuffle=True, num_workers=args.num_workers, 
                                          )

testset = torchvision.datasets.FashionMNIST(root='./data', train=False,
                                       download=True, transform=transform)

testloader = torch.utils.data.DataLoader(testset, batch_size=args.batch_size,
                                         shuffle=False, num_workers=args.num_workers)


task_name = args.task_name
wandb_logger = WandbLogger(project='DLRG_HW_3_PB3', name=task_name, log_model=True)

model = aec.AutoencoderClassifier(num_classes=10)


# callbacks
checkpoint_callback = ModelCheckpoint(
    dirpath='checkpoints',
    save_top_k=1,
    monitor='loss',
    mode='min'
)


# Initialize PyTorch Lightning trainer
trainer = pl.Trainer(gpus=1 if torch.cuda.is_available() else 0, 
    max_epochs=args.max_epochs,
    fast_dev_run=args.fast_dev_run,
    logger=wandb_logger,
    callbacks=[checkpoint_callback])

# Start training
trainer.fit(model, trainloader, testloader)

# Save the model
torch.save(model, f'{task_name}.pt')


