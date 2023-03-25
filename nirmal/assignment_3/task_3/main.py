import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn

import sys
sys.path.append('../task_1')
import autoencoder_classifier as aec

num_classes = 10
num_epochs = 10

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5,), (0.5,))])

trainset = torchvision.datasets.FashionMNIST(root='./data', train=True,
                                        download=True, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=32,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.FashionMNIST(root='./data', train=False,
                                       download=True, transform=transform)

testloader = torch.utils.data.DataLoader(testset, batch_size=32,
                                         shuffle=False, num_workers=2)


model = aec.AutoencoderClassifier(num_classes=10)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
mse_loss_fn = nn.MSELoss()
ce_loss_fn = nn.CrossEntropyLoss()

for epoch in range(num_epochs):
    for batch_idx, (data, target) in enumerate(trainloader):
        optimizer.zero_grad()
        reconstructed, classified = model(data)
        mse_loss = mse_loss_fn(reconstructed, data)
        ce_loss = ce_loss_fn(classified, target)
        loss = mse_loss + ce_loss
        loss.backward()
        optimizer.step()
