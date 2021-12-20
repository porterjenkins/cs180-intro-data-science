import argparse
import numpy as np

def rmse(y_hat, y_true):

    err = (y_hat - y_true)
    return np.sqrt(np.mean(np.power(err, 2)))

def get_vals(fpath):
    with open(fpath, "r") as f:
        vals = f.readlines()
    return np.array(vals, dtype=float)



parser = argparse.ArgumentParser('Model')
parser.add_argument('--pred', type=str, help='filepath to predictions')
parser.add_argument('--true', type=str, help='filepath to ground truth')


args = parser.parse_args()


y_true = get_vals(args.true)
y_hat = get_vals(args.pred)

output = rmse(y_hat, y_true)

print("RMSE: {:.4f}".format(output))
