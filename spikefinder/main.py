import os
import json
from scipy import corrcoef
from pandas import read_csv

def load(file):
    """
    Load results from a file or string.
    """
    return read_csv(file)
        
def score(a, b, method='corr'):
    """
    Estimate similarity score between two reslts.
    """
    methods = {
      'loglik': _loglik, 
      'info': _info, 
      'corr': _corr, 
      'auc': _auc, 
      'rank': _rank
    }
    if method not in methods.keys():
      raise Exception('scoring method not one of: %s' % ' '.join(methods.keys()))

    func = methods[method]

    result = []
    for column in a:
        result.append(func(a[column], b[column]))
    return result

def _corr(x, y):
    return corrcoef(x, y)[0,1]

def _info(x, y):
    pass

def _rank(x, y):
    pass

def _auc(x, y):
    pass

def _loglik(x, y):
    pass