# gm_cta05_Class_a1_geometry(r2s)_b_func.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 1 with function ***')
print('   *** converting coordinate system: from rectangular to spherical ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, arctan2 as atan2, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- function ---')
def xxyyzz2rrthph(xx, yy, zz):
    rr, th, ph = sqrt(xx**2+yy**2+zz**2), atan2(yy, xx), atan2(sqrt(xx**2+yy**2), zz)
    return rr, th, ph

# -----------------------------------------------------------------------------
print('\n## --- main sentences ---')
xx, yy, zz = 3, 4, 5
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')

rr, th, ph = xxyyzz2rrthph(xx, yy, zz)
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}, ph(deg) = {r2d(ph):g}')

