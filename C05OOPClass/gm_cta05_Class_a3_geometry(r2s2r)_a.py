# gm_cta05_Class_a3_geometry(r2s)_a.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 3 ***')
print('   *** converting coordinate system: between rectangular and spherical ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- main sentences ---')
xx, yy, zz = 3, 4, 5
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')

rr, th, ph = sqrt(xx**2+yy**2+zz**2), atan2(yy, xx), atan2(sqrt(xx**2+yy**2), zz)
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}, ph(deg) = {r2d(ph):g}')

xx, yy, zz = rr * sin(ph) * cos(th), rr * sin(ph) * sin(th), rr * cos(ph)
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')

