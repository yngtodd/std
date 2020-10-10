import torch


def accuracy(pred, target):
    r"""Calculate accuracy

    Args:
        pred: Tensor of arbitrary shape
        target: Tensor of the same shape as input

    Examples::

        >>> pred = torch.randn(25, 1)
        >>> target = torch.randint(low=0, high=10, size=(25,)) 
        >>> acc = accuracy(pred, target)
    """
    return pred.argmax(1).eq(target).double().mean().item()

