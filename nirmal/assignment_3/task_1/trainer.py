# trainer.py
import torch
import torch.nn as nn
import pytorch_lightning as pl
from models import BigCNN, LittleCNN, MLP


# create pytorch lightning module
class MyModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.big_cnn = BigCNN()
        self.little_cnn = LittleCNN()
        self.mlp = MLP()
        

    #b. forward()
    # i. Return the output from each of the three models.
    '''
    In PyTorch, calling a module instance like a function (i.e., self.littleCNN(x)) is 
    equivalent to calling the forward function directly (i.e., self.littleCNN.forward(x)). 
    '''
    def forward(self, x):
        big_cnn_out = self.big_cnn(x)
        little_cnn_out = self.little_cnn(x)
        mlp_out = self.mlp(x)
        return big_cnn_out, little_cnn_out, mlp_out
    
    #c. training_step()
    # i. Use the optimizer index to determine which model you are currently optimizing.
    # ii. Log each loss using a built-in logging function.
    
    def training_step(self, batch, batch_idx, optimizer_idx):
        '''
        The batch_idx argument is typically used in PyTorch Lightning's training loop to keep track of the 
        current batch index. It is especially useful for logging purposes, where the batch index can be used 
        to log information like the current batch number, the total number of batches, and the loss for that batch.
        In the training_step() function, the batch_idx argument is used to index into the data loader to retrieve 
        the corresponding batch of data for the current training step.
        '''
        x, y = batch
        big_cnn_out, little_cnn_out, mlp_out = self.forward(x)
        if optimizer_idx == 0:
            loss = nn.functional.cross_entropy(big_cnn_out, y)
            self.log('big_cnn_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        elif optimizer_idx == 1:
            loss = nn.functional.cross_entropy(little_cnn_out, y)
            self.log('little_cnn_loss', loss)
        elif optimizer_idx == 2:
            loss = nn.functional.cross_entropy(mlp_out, y)
            self.log('mlp_loss', loss)
        return loss

        # d. validation_step()
        # i. Compute the loss for each model prediction and log them.

    def validation_step(self, batch, batch_idx):
        x, y = batch

        big_cnn_out, little_cnn_out, mlp_out = self.forward(x)

        big_cnn_loss = nn.functional.cross_entropy(big_cnn_out, y)
        little_cnn_loss = nn.functional.cross_entropy(little_cnn_out, y)
        mlp_loss = nn.functional.cross_entropy(mlp_out, y)

        self.log('val_big_cnn_loss', big_cnn_loss)
        self.log('val_little_cnn_loss', little_cnn_loss)
        self.log('val_mlp_loss', mlp_loss)
        
        return big_cnn_loss, little_cnn_loss, mlp_loss

        # e. configure_optimizers()
        # i. Initialize an optimizer for each model.

    def configure_optimizers(self):
        big_cnn_optimizer = torch.optim.Adam(self.big_cnn.parameters(), lr=0.001)
        little_cnn_optimizer = torch.optim.Adam(self.little_cnn.parameters(), lr=0.001)
        mlp_optimizer = torch.optim.Adam(self.mlp.parameters(), lr=0.001)
        return [big_cnn_optimizer, little_cnn_optimizer, mlp_optimizer]
    
    
