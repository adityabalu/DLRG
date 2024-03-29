# -*- coding: utf-8 -*-
"""Assignment2.part2.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12HTZkFizoVCCTfMdqOJTXpAI1md_d0c2
"""

import numpy as np
import matplotlib.pyplot as plt
import os

filepath = os.getcwd()
data1 = os.path.join(filepath, "mnist_test.csv")
data2 = os.path.join(filepath, "mnist_train.csv")

test_data = np.genfromtxt(
    data1, 
    dtype=np.unicode_, 
    delimiter=",", 
    skip_header=1, 
    encoding="utf-8-sig"
)

train_data = np.genfromtxt(
    data2, 
    dtype=np.unicode_, 
    delimiter=",", 
    skip_header=1,
    encoding="utf-8-sig"
)

#part2.2.a:
train_imgs = np.asfarray(train_data[:, 1:]) / 255
test_imgs = np.asfarray(test_data[:, 1:]) / 255

train_labels = np.asfarray(train_data[:, :1])
test_labels = np.asfarray(test_data[:, :1])

np.max(train_imgs), np.min(train_imgs)

np.max(test_imgs), np.min(test_imgs)

#b
batch = train_imgs[:64]
print(np.shape(batch))
imgs = batch.reshape((-1, 28, 28))
print(np.shape(imgs))
mean = np.mean(imgs, axis = (1, 2))
print(mean)

#c
plt.hist(mean)
plt.show()

#d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print(imgs[1].shape)
X = np.linspace(0,28, num = 28)
print(X)

Y = np.linspace(0,28, num = 28)
X, Y = np.meshgrid(X, Y)
Z  = imgs[0]  
print(len(Z))
ax.scatter(X,Y,Z) # plot the point (2,3,4) on the figure

plt.show()

#e
trainlabels = np.array(train_data[:, :1], dtype = int)
batch=trainlabels[:1024]
labels=[]
for i in batch:
    for j in i:
        labels.append(j)

labels = np.sort(labels)
label=[]
print(labels)
for i in labels:
    label.append(i)



#f, g
fig, ax = plt.subplots(10,)
for i in range(10):
    a = np.mean(imgs[labels == i,: ,:], axis = (1, 2))
    ax[i].hist(a)
    #ax[i].set_ylim([0, 100])
plt.show()

#h

mean = np.mean(imgs,axis = (1,2))
print(imgs.shape)
print(mean.shape)
for i in range(imgs.shape[0]):
  dvd = np.divide(imgs[i, :, :], mean[i])
dvd

