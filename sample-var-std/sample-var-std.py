import numpy as np
import math

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    arr = np.array(x)
    mean = np.mean(x)
    sum = 0
    for i in range(len(x)):
        sum += (mean - x[i])*(mean - x[i])

    variance = float(sum/(len(x)-1))
    standard_deviation = float(math.sqrt(variance))

    return {
        "variance": variance,
        "standard_deviation": standard_deviation
    }
    pass