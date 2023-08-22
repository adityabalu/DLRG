import torch
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision.transforms import Grayscale
import torchvision.utils as vutils
import matplotlib.pyplot as plt
import os
import argparse
from DDPM import DDPM


data_dir = '/home/nirmal/course_work/DLRG/nirmal/project/data/2D_square/'

transform = transforms.Compose([Grayscale(num_output_channels=1),transforms.ToTensor(),
                                transforms.Resize((100,100)),
                                transforms.Normalize((0.5,), (0.5,))])

train_dataset = ImageFolder(root = os.path.join(data_dir, 'train'), transform=transform)
val_dataset = ImageFolder(root = os.path.join(data_dir, 'val'), transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

model = DDPM()
trainer = pl.Trainer(max_epochs=1)
trainer.fit(model, train_loader)