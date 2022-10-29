'''experiment draw according to practice'''
import matplotlib.pyplot as plt
import pandas as pd
from config import CFG
import numpy as np

def draw_pk():
    plt.figure(figsize=(10, 10))
    plt.suptitle('PK')
    plt.xlabel('opponent')
    plt.ylabel('times')

    ax = plt.subplot(1, 1, 1)
    ax.set_title('AlphaReversi VS Human')
    names = ['Win', 'Lose', 'Tie']
    x = range(len(names))
    y = [21, 19, 10]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(range(0, 51, 10))
    plt.show()

def draw_loss(filename):
    loss_file = filename
    data = pd.read_csv(loss_file, header = None, delimiter = '|')
    data = data.values.tolist()
    pi_loss_list = [loss[0] for loss in data]
    v_loss_list = [loss[1] for loss in data]

    plt.plot(pi_loss_list, color='red', label='pi_loss')
    plt.plot(v_loss_list, color='green', label='vi_loss')
    plt.legend()
    plt.suptitle('loss')
    plt.show()
    

def draw_epsilon_parameters():
    '''data according to experiment'''
    plt.figure(figsize=(10, 10))
    plt.suptitle(r'$\epsilon$ experiment')

    ax = plt.subplot(2, 3, 1)
    ax.set_title(r'$\epsilon$=0 AlphaReversi')
    names = [r'$\epsilon$=0.25', r'$\epsilon$=0.5', 'Human']
    x = range(len(names))
    y = [0.20, 0.30, 0.30]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')
    plt.ylabel('win ratio')

    ax = plt.subplot(2, 3, 2)
    ax.set_title(r'$\epsilon$=0.25 AlphaReversi')
    names = [r'$\epsilon$=0', r'$\epsilon$=0.5', 'Human']
    x = range(len(names))
    y = [0.70, 0.70, 0.50]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')


    ax = plt.subplot(2, 3, 3)
    ax.set_title(r'$\epsilon$=0.5 AlphaReversi')
    names = [r'$\epsilon$=0', r'$\epsilon$=0.25', 'Human']
    x = range(len(names))
    y = [0.80, 0.30, 0.333]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')

    plt.show()


def draw_n_parameters():
    '''data according to experiment'''
    plt.figure(figsize=(10, 10))
    plt.suptitle('n experiment')

    ax = plt.subplot(2, 3, 1)
    ax.set_title('n=10 AlphaReversi')
    names = ['n=30', 'n=100', 'Human']
    x = range(len(names))
    y = [0.4, 0.2, 0.]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')
    plt.ylabel('win ratio')

    ax = plt.subplot(2, 3, 2)
    ax.set_title('n=30 AlphaReversi')
    names = ['n=10', 'n=100', 'Human']
    x = range(len(names))
    y = [0.6, 0.3, 0.1]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')


    ax = plt.subplot(2, 3, 3)
    ax.set_title('n=100 AlphaReversi')
    names = ['n=10', 'n=30', 'Human']
    x = range(len(names))
    y = [0.8, 0.7, 0.5]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')

    plt.show()

def draw_cpuct_parameters():
    '''data according to experiment'''
    plt.figure(figsize=(10, 10))
    plt.suptitle(r'$c_{puct}$ experiment')

    ax = plt.subplot(2, 3, 1)
    ax.set_title(r'$c_{puct}$=1 AlphaReversi')
    names = [r'$c_{puct}$=5', r'$c_{puct}$=20', 'Human']
    x = range(len(names))
    y = [0.30, 0.50, 0.20]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')
    plt.ylabel('win ratio')

    ax = plt.subplot(2, 3, 2)
    ax.set_title(r'$c_{puct}$=5 AlphaReversi')
    names = [r'$c_{puct}$=1', r'$c_{puct}$=20', 'Human']
    x = range(len(names))
    y = [0.70, 0.90, 0.50]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')


    ax = plt.subplot(2, 3, 3)
    ax.set_title(r'$c_{puct}$=20 AlphaReversi')
    names = [r'$c_{puct}$=1', r'$c_{puct}$=5', 'Human']
    x = range(len(names))
    y = [0.50, 0.10, 0.333]
    plt.bar(range(len(names)), y, color='black')
    plt.xticks(x, names, rotation=45)
    plt.yticks(np.arange(0, 1.01, 0.1))
    plt.xlabel('opponent')
    plt.show()


draw_loss(CFG.model_directory + '/loss.txt')
draw_pk()
draw_cpuct_parameters()
draw_n_parameters()
draw_epsilon_parameters()

