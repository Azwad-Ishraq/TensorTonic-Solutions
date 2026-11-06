import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    sum = 0
    for i in range(len(x)):
        sum = sum + (x[i]*p[i])
    sum = float(sum)

    return sum
    pass