'''
Created on 2017/07/08

@author: mine
'''
#import
import numpy as np
import chainer
from chainer import cuda, Function, gradient_check, Variable, optimizers, serializers, utils
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
import time
from matplotlib import pyplot as plt
import chainer.computational_graph as cg

def get_dataset(N):
    #linspace(start,stop,num=50,endpoint=True,retstop=False,dtype=None) toukankaku
    x = np.linspace(0, 2 * np.pi, N)
    y = np.sin(x)
    return x, y

class MyChain(Chain):
    def __init__(self, n_units=10):
        super(MyChain, self).__init__(
             l1=L.Linear(1, n_units),
             l2=L.Linear(n_units, n_units),
             l3=L.Linear(n_units, 1))

    def __call__(self, x_data, y_data):
        x = Variable(x_data.astype(np.float32).reshape(len(x_data),1)) #     
        y = Variable(y_data.astype(np.float32).reshape(len(y_data),1)) # 
        return F.mean_squared_error(self.predict(x), y)

    def  predict(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        h3 = self.l3(h2)
        return h3

    def get_predata(self, x):
        return self.predict(Variable(x.astype(np.float32).reshape(len(x),1))).data


if __name__ == '__main__':
    print "hello"
    N = 1000
    x_train, y_train = get_dataset(N)

