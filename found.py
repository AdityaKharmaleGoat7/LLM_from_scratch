import numpy as np
from numpy import ndarray
from typing import Callable
from typing import List
import matplotlib.pyplot as plt

Array_Function = Callable[[ndarray], ndarray]

Chain = List[Array_Function]

def test(x: ndarray)->ndarray:
    return (x/2)

def chain_length_2(chain: Chain, x: ndarray)->ndarray:

    '''
    Refer to the usage:

    # Put them into a chain
    my_chain = [square, add_one]

    # Input array
    x = np.array([1, 2, 3])

    # Apply the chain
    result = chain_length_2(my_chain, x)
    print(result)

    '''
    
    assert len(chain) == 2
    
    f1 = chain[0]
    f2 = chain[1]

    return f2(f1(x))

def chain_deriv_2(chain: Chain, input_range: ndarray):
    
    assert len(chain) == 2
    assert len(input_range.ndim) == 2

    f1 = chain[0]
    f2 = chain[1]

    f1_of_x = f1(input_range)

    df1dx = deriv(f1, input_range)

    df2dx = deriv(f2, f1_of_x)

    return df2dx*df1dx


def deriv(func: Callable[[ndarray], ndarray], 
          input_: ndarray, 
          delta: float = 0.001)->ndarray:

    return (func(input_+delta)-func(input_-delta)) / (2*delta)

def square(x: ndarray)->ndarray:
    '''
    Square each element    
    
    '''
    return np.power(x,2)


def sigmoid(x: ndarray)->ndarray:
    return 1/(1 + np.exp(-x))


def leaky_relu(x: ndarray)->ndarray:
    return np.maximum(0.2*x, x)


def multiple_inputs_add(x: ndarray, y: ndarray, sigma: Array_Function)->float:
    assert x.shape == y.shape
    a = x + y
    return sigma(a)

