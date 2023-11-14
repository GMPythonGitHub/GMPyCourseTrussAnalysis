# gm_cta05_Class_a2_geometry(r2c2r)_b_func.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 2 with function ***')
print('   *** converting coordinate system: between rectangular and circular ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- function ---')
def xxyy2rrth(xx, yy):
    rr, th = sqrt(xx**2+yy**2), atan2(yy, xx)
    return rr, th
def rrth2xxyy(rr, th):
    xx, yy = rr * cos(th), rr * sin(th)
    return xx, yy

# -----------------------------------------------------------------------------
print('\n## --- main sentences ---')
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')

rr, th = xxyy2rrth(xx, yy)
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}')

xx, yy = rrth2xxyy(rr, th)
print(f'xx = {xx:g}, yy = {yy:g}')

