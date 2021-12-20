import argparse
import numpy as np

def rmse(y_hat, y_true):

    err = (y_hat - y_true)
    


parser = argparse.ArgumentParser('Model')
parser.add_argument('--pred', type=str, help='filepath to predictions')
parser.add_argument('--true', type=str, help='filepath to ground truth')


args = parser.parse_args()
