import argparse
import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from trainer import ModelTrainer

def main(args):
    # Transformations for the MNIST Fashion dataset
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # MNIST Fashion dataset
    train_dataset = datasets.FashionMNIST('data', train=True, download=True, transform=transform)
    val_dataset = datasets.FashionMNIST('data', train=False, download=True, transform=transform)
    test_dataset = datasets.FashionMNIST('data', train=False, download=True, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size, num_workers=args.num_workers)


    # Data loaders
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, num_workers=args.num_workers)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size, num_workers=args.num_workers)

    # Model
    model = ModelTrainer()

    # Logger
    logger = TensorBoardLogger(save_dir=args.logging_dir, name="my_model")

    # Trainer
    trainer = pl.Trainer(
        max_epochs=args.epochs,
        fast_dev_run=args.fast_dev_run,
        logger=logger
    )

    # Train the model
    trainer.fit(model, train_loader, val_loader)
    # Test the model
    trainer.test(model, dataloaders=test_loader)


    # Save the model weights
    trainer.save_checkpoint(f"{args.logging_dir}/model_weights.ckpt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PyTorch Lightning MNIST Example")

    parser.add_argument('--batch_size', type=int, default=64, help='input batch size for training (default: 64)')
    parser.add_argument('--epochs', type=int, default=10, help='number of epochs to train (default: 10)')
    parser.add_argument('--num_workers', type=int, default=4, help='number of workers for data loading (default: 4)')
    parser.add_argument('--logging_dir', type=str, default='logs', help='logging directory path')
    parser.add_argument('--fast_dev_run', action='store_true', help='Run a fast dev run if set')

    args = parser.parse_args()
    main(args)
