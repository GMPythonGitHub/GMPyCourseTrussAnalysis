# gm_cta05_Class_a0_geometry(r2c)_a.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 0 ***')
print('   *** converting coordinate system: from rectangular to circular ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, arctan2 as atan2, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- main sentences ---')
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')

rr, th = sqrt(xx**2+yy**2), atan2(yy, xx)
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}')

