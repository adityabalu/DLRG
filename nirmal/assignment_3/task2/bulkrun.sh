#!/bin/bash

#which python
#which conda
# python main.py --model LittleCNN --optimizer Adam --learning_rate 0.001 --batch_size 64 --max_epochs 5
# python main.py --model LittleCNN --optimizer Adam --learning_rate 0.001 --batch_size 128 --max_epochs 5
# python main.py --model LittleCNN --optimizer Adam --learning_rate 0.001 --batch_size 256 --max_epochs 5
# python main.py --model LittleCNN --optimizer Adam --learning_rate 0.001 --batch_size 512 --max_epochs 5

# python main.py --model LittleCNN --optimizer Adam --learning_rate 0.01 --batch_size 32 --max_epochs 5
# python main.py --model LittleCNN --optimizer Adam --learning_rate 0.0001 --batch_size 32 --max_epochs 5
# python main.py --model LittleCNN --optimizer Adam --learning_rate 0.00001 --batch_size 32 --max_epochs 5
# python main.py --model LittleCNN --optimizer Adam --learning_rate 0.000001 --batch_size 32 --max_epochs 5

# python main.py --model LittleCNN --optimizer SGD --learning_rate 0.001 --batch_size 64 --max_epochs 5
# python main.py --model LittleCNN --optimizer RMSProp --learning_rate 0.001 --batch_size 64 --max_epochs 5
# python main.py --model LittleCNN --optimizer Adagrad --learning_rate 0.001 --batch_size 64 --max_epochs 5
# python main.py --model LittleCNN --optimizer Adadelta --learning_rate 0.001 --batch_size 64 --max_epochs 5
# python main.py --model LittleCNN --optimizer RAdam --learning_rate 0.001 --batch_size 64 --max_epochs 5


python main.py --model MLP --optimizer Adam --learning_rate 0.001 --batch_size 64 --max_epochs 5
python main.py --model MLP --optimizer Adam --learning_rate 0.001 --batch_size 128 --max_epochs 5
python main.py --model MLP --optimizer Adam --learning_rate 0.001 --batch_size 256 --max_epochs 5
python main.py --model MLP --optimizer Adam --learning_rate 0.001 --batch_size 512 --max_epochs 5

python main.py --model MLP --optimizer Adam --learning_rate 0.01 --batch_size 32 --max_epochs 5
python main.py --model MLP --optimizer Adam --learning_rate 0.0001 --batch_size 32 --max_epochs 5
python main.py --model MLP --optimizer Adam --learning_rate 0.00001 --batch_size 32 --max_epochs 5
python main.py --model MLP --optimizer Adam --learning_rate 0.000001 --batch_size 32 --max_epochs 5

python main.py --model MLP --optimizer SGD --learning_rate 0.001 --batch_size 64 --max_epochs 5
python main.py --model MLP --optimizer RMSProp --learning_rate 0.001 --batch_size 64 --max_epochs 5
python main.py --model MLP --optimizer Adagrad --learning_rate 0.001 --batch_size 64 --max_epochs 5
python main.py --model MLP --optimizer Adadelta --learning_rate 0.001 --batch_size 64 --max_epochs 5
python main.py --model MLP --optimizer RAdam --learning_rate 0.001 --batch_size 64 --max_epochs 5
