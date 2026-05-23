import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')
    matrix = np.array(lst).reshape(3, 3)
    def helper(func):
        return [
            func(matrix, axis=0).tolist(),  #axis 0 = columns
            func(matrix, axis=1).tolist(),  #axis 1 = rows
            func(matrix).tolist()           #flattened array
        ]
    return {
        'mean': helper(np.mean),
        'variance': helper(np.var),
        'standard deviation': helper(np.std),
        'max': helper(np.max),
        'min': helper(np.min),
        'sum': helper(np.sum)
    }
