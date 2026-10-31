from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    arr = np.array(x)
    mean = float(np.mean(arr))
    median = float(np.median(arr))
    max_val = max(Counter(arr).values())
    all_max_keys = [k for k,v in Counter(arr).items() if v == max_val]
    mode = float(min(all_max_keys))

    mmm = {
        "mean": mean,
        "median" : median,
        "mode" : mode
    }
    return mmm 
    
    pass