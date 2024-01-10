import pytorch_lightning as pl
import torch
import torch.nn.functional as F
from models.big_cnn import BigCNN
from models.little_cnn import LittleCNN
from models.mlp import MLP

class ModelTrainer(pl.LightningModule):
    def __init__(self):
        super(ModelTrainer, self).__init__()
        self.automatic_optimization = False  # Set manual optimization
        self.big_cnn = BigCNN()
        self.little_cnn = LittleCNN()
        self.mlp = MLP()

    def forward(self, x):
        # Return the output from each of the three models
        return self.big_cnn(x), self.little_cnn(x), self.mlp(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        # Get optimizers
        opt1, opt2, opt3 = self.optimizers()

        # Forward pass and loss for BigCNN
        y_hat_big_cnn = self.big_cnn(x)
        loss_big_cnn = F.cross_entropy(y_hat_big_cnn, y)
        self.manual_backward(loss_big_cnn)
        opt1.step()
        opt1.zero_grad()
        self.log('train_loss_big_cnn', loss_big_cnn)

        # Forward pass and loss for LittleCNN
        y_hat_little_cnn = self.little_cnn(x)
        loss_little_cnn = F.cross_entropy(y_hat_little_cnn, y)
        self.manual_backward(loss_little_cnn)
        opt2.step()
        opt2.zero_grad()
        self.log('train_loss_little_cnn', loss_little_cnn)

        # Forward pass and loss for MLP
        y_hat_mlp = self.mlp(x)
        loss_mlp = F.cross_entropy(y_hat_mlp, y)
        self.manual_backward(loss_mlp)
        opt3.step()
        opt3.zero_grad()
        self.log('train_loss_mlp', loss_mlp)

    def validation_step(self, batch, batch_idx):
        x, y = batch
        # Compute and log the loss for each model prediction
        y_hat_big_cnn = self.big_cnn(x)
        loss_big_cnn = F.cross_entropy(y_hat_big_cnn, y)
        self.log('val_loss_big_cnn', loss_big_cnn)

        y_hat_little_cnn = self.little_cnn(x)
        loss_little_cnn = F.cross_entropy(y_hat_little_cnn, y)
        self.log('val_loss_little_cnn', loss_little_cnn)

        y_hat_mlp = self.mlp(x)
        loss_mlp = F.cross_entropy(y_hat_mlp, y)
        self.log('val_loss_mlp', loss_mlp)

    def test_step(self, batch, batch_idx):
        x, y = batch
        y_hat_big_cnn, y_hat_little_cnn, y_hat_mlp = self.forward(x)

        # Test loss and accuracy for BigCNN
        test_loss_big_cnn = F.cross_entropy(y_hat_big_cnn, y)
        _, predicted_big_cnn = torch.max(y_hat_big_cnn, 1)
        correct_big_cnn = (predicted_big_cnn == y).sum().item()
        accuracy_big_cnn = correct_big_cnn / y.size(0)
        self.log('test_loss_big_cnn', test_loss_big_cnn)
        self.log('test_accuracy_big_cnn', accuracy_big_cnn)

        # Test loss and accuracy for LittleCNN
        test_loss_little_cnn = F.cross_entropy(y_hat_little_cnn, y)
        _, predicted_little_cnn = torch.max(y_hat_little_cnn, 1)
        correct_little_cnn = (predicted_little_cnn == y).sum().item()
        accuracy_little_cnn = correct_little_cnn / y.size(0)
        self.log('test_loss_little_cnn', test_loss_little_cnn)
        self.log('test_accuracy_little_cnn', accuracy_little_cnn)

        # Test loss and accuracy for MLP
        test_loss_mlp = F.cross_entropy(y_hat_mlp, y)
        _, predicted_mlp = torch.max(y_hat_mlp, 1)
        correct_mlp = (predicted_mlp == y).sum().item()
        accuracy_mlp = correct_mlp / y.size(0)
        self.log('test_loss_mlp', test_loss_mlp)
        self.log('test_accuracy_mlp', accuracy_mlp)

        return {'test_loss_big_cnn': test_loss_big_cnn, 
                'test_accuracy_big_cnn': accuracy_big_cnn,
                'test_loss_little_cnn': test_loss_little_cnn, 
                'test_accuracy_little_cnn': accuracy_little_cnn,
                'test_loss_mlp': test_loss_mlp, 
                'test_accuracy_mlp': accuracy_mlp}


    def configure_optimizers(self):
        # Initialize an optimizer for each model
        optimizer_big_cnn = torch.optim.Adam(self.big_cnn.parameters(), lr=0.001)
        optimizer_little_cnn = torch.optim.Adam(self.little_cnn.parameters(), lr=0.001)
        optimizer_mlp = torch.optim.Adam(self.mlp.parameters(), lr=0.001)
        return [optimizer_big_cnn, optimizer_little_cnn, optimizer_mlp]
