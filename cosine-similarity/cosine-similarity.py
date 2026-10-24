import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a,dtype=float)
    b = np.asarray(b,dtype=float)

    a_dot_b = np.dot(a,b)

    e_norm_a = np.linalg.norm(a)
    e_norm_b = np.linalg.norm(b)

    if(e_norm_a == 0 or e_norm_b == 0):
        return 0.0
    else:
        result = a_dot_b / (e_norm_a * e_norm_b)
        result = float(result)

        return result

    
    
    
    pass