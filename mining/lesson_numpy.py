import numpy as np          # 提供数组

a = np.array([2, 0, 1, 5])
a.sort()
print(a[:3])
print(a.min())

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b*b)


from scipy.optimize import fsolve   # 矩阵

def function_a(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 - 1, x1**2 - x2 - 2]

result = fsolve(function_a, [1, 1])
print(result)
