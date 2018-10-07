# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    X = x if x.ndim > 1 else x.reshape(-1,1)
    return np.concatenate([np.ones((x.shape[0],1))] + [X**j for j in range(1, degree+1)], axis=1)
    #return np.concatenate([X**j for j in range(1, degree+1)], axis=1)
