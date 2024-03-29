# gm_Example_Matrix_Equation_bnp: coded by Kinya MIURA 231104
# -----------------------------------------------------------------------------
print('\n*** Matrix Equation Bnp: aa * xx = bb; find xx ***')
print('# -----------------------------------------------------------------------------')
from numpy import (array, linalg)

# -----------------------------------------------------------------------------
aa1 = array([
    [1., 1., 1., 1., 1., 1.],
    [1., 2., 1., 1., 1., 1.],
    [1., 1., 3., 1., 1., 1.],
    [1., 1., 1., 4., 1., 1.],
    [1., 1., 1., 1., 5., 1.],
    [1., 1., 1., 1., 1., 6.] ])
bb1 = array([21., 23., 27., 33., 41., 51.])
aa2 = array([
    [1., 1., 1., 1., 1., 1.],
    [1., 1., 1., 1., 2., 1.],
    [1., 1., 1., 3., 1., 1.],
    [1., 1., 4., 1., 1., 1.],
    [1., 5., 1., 1., 1., 1.],
    [6., 1., 1., 1., 1., 1.] ])
bb2 = array([21., 26., 29., 30., 29., 26.])
xx = array([0., 0., 0., 0., 0., 0.])

xx = linalg.solve(aa2, bb2)

print(f'{aa2 = }')
print(f'{bb2 = }')
print(f'{xx = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation Bnp: aa * xx = bb; find xx ***
# -----------------------------------------------------------------------------
aa2 = array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 2., 1.],
       [1., 1., 1., 3., 1., 1.],
       [1., 1., 4., 1., 1., 1.],
       [1., 5., 1., 1., 1., 1.],
       [6., 1., 1., 1., 1., 1.]])
bb2 = array([21., 26., 29., 30., 29., 26.])
xx = array([1., 2., 3., 4., 5., 6.])
*** Matrix Equation B1: aa * xx = bb; find xx ***
# -----------------------------------------------------------------------------
aa1 = array([[1., 1., 1., 1., 1., 1.],
       [1., 2., 1., 1., 1., 1.],
       [1., 1., 3., 1., 1., 1.],
       [1., 1., 1., 4., 1., 1.],
       [1., 1., 1., 1., 5., 1.],
       [1., 1., 1., 1., 1., 6.]])
bb1 = array([21., 23., 27., 33., 41., 51.])
xx = array([1., 2., 3., 4., 5., 6.])
'''