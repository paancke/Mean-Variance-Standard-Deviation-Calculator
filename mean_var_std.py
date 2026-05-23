import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')
    a = np.array([lst[:3], lst[3:6], lst[6:]])
    def helper(array):
        return [array(a, axis=0).tolist(), array(a, axis=1).tolist(), array(a).tolist()]
    return {'mean': helper(np.mean),
           'variance': helper(np.var),
           'standard deviation': helper(np.std),
           'max': helper(np.max),
           'min': helper(np.min),
           'sum': helper(np.sum)}
