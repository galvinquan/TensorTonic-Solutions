import numpy as np

def expected_value_discrete(x, p):
    x = np.array(x)
    p = np.array(p)
    
    # check shape
    if len(x) != len(p):
        raise ValueError("x and p must have same length")
    
    # check sum(p) ≈ 1
    if not np.isclose(np.sum(p), 1, atol=1e-6):
        raise ValueError("Probabilities must sum to 1")
    
    return float(np.sum(x * p))