# gm_cta05_Class_a2_geometry(r2s)_a.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 2 ***')
print('   *** converting coordinate system: between rectangular and circular ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- main sentences ---')
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')

rr, th = sqrt(xx**2+yy**2), atan2(yy, xx)
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}')

xx, yy = rr * cos(th), rr * sin(th)
print(f'xx = {xx:g}, yy = {yy:g}')

