import argparse
import numpy as np
from sklearn.metrics import roc_auc_score


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

output = roc_auc_score(y_true, y_hat)

print("AUC score: {:.4f}".format(output))
