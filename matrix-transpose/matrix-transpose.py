import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    arr = np.array(A)
    arr_tr = np.zeros(arr.shape[::-1])
    for index, value in np.ndenumerate(arr):
        arr_tr[index[1],index[0]] = value

    return np.array(arr_tr)
    pass
