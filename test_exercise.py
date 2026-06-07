import numpy as np

def normalize_array(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)

    if min_val == max_val:
        return np.zeros_like(arr, dtype=float)

    return (arr - min_val) / (max_val - min_val)
