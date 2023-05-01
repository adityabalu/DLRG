import torch
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision.transforms import Grayscale
import torchvision.utils as vutils
import matplotlib.pyplot as plt
from VAE_conv4 import VAE
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
parser.add_argument('--max_epochs', type=int, default=100, help='Number of epochs to train for')
parser.add_argument('--task', type=str, default=None)

args = parser.parse_args()
if args.task is None:
    args.task = f'conv4_epoch{args.max_epochs}_no_dropout'

data_dir = '/work/mech-ai/nirmal/projects/DLRG/data/2D_square/'

transform = transforms.Compose([Grayscale(num_output_channels=1),transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,))])

train_dataset = ImageFolder(root = os.path.join(data_dir, 'train'), transform=transform)
val_dataset = ImageFolder(root = os.path.join(data_dir, 'val'), transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)


# logging and call backs
wandb_logger = pl.loggers.WandbLogger(project='2D_morph_generation', log_model=True, name=args.task)
checkpoint_callback = ModelCheckpoint(
    monitor='val_loss',
    dirpath='./backup/checkpoints/',
    filename=args.task,
    save_top_k=5,
    mode='min',
)

model = VAE()
trainer = pl.Trainer(max_epochs=args.max_epochs, logger=wandb_logger, callbacks=[checkpoint_callback])

trainer.fit(model, train_loader, val_loader)
torch.save(model.state_dict(), args.task + '.pt')

def generate_samples(model, num_samples=64, device='cpu'):
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():  # No need to track gradients when generating samples
        # Generate latent vectors from a standard normal distribution
        z = torch.randn(num_samples, 16).to(device)

        # Generate images using the decoder
        samples = model.decoder(z)

        return samples

# Set the number of samples you want to generate
num_samples = 64

# Set the device to 'cuda' if you have a GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Move the model to the appropriate device
model.to(device)

# Generate samples using the trained VAE model
samples = generate_samples(model, num_samples, device)

# Convert the generated samples to a grid of images
grid = vutils.make_grid(samples, nrow=8, padding=2, normalize=True)

# Plot the generated images
plt.figure(figsize=(8, 8))
plt.axis("off")
plt.title("Generated Samples")
plt.imshow(transforms.ToPILImage()(grid.cpu()))
plt.savefig(args.task + '.png')
plt.show()
