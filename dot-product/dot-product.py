import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    sum = 0
    for i in range(0,len(x)):
        sum += x[i]*y[i]

    sum = float(sum)
    return sum


    pass