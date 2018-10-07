def compute_mse(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    e = y - (tx @ w)
    return (e.T @ e) / (2 * len(y))

def compute_mae(y, tx, w):
    """Calculate the loss for mae.
    """
    e = y - (tx @ w)
    return np.sum(np.abs(e)) / len(y)