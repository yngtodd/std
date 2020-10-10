import numpy as np


def accuracy(pred, target):
    r"""Calculate accuracy

    Args:
        pred: numpy array of predictions
        target: numpy array of target values

    Examples::

        >>> pred = np.random.randn(25, 1)
        >>> target = np.random.randint(low=0, high=10, size=(25,)) 
        >>> acc = accuracy(pred, target)
    """
    outputs = np.argmax(pred, axis=1)
    return np.sum(outputs==target) / float(target.size)

