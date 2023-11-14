# gm_cta05_Class_a4_geometry(move)_a.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 4 ***')
print('   *** converting coordinate system: shift, scale and revolve ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d, deg2rad as d2r)

# -----------------------------------------------------------------------------
print('\n## --- main sentences ---')
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')
rr, th = sqrt(xx**2+yy**2), atan2(yy, xx)
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}')
xx, yy = rr * cos(th), rr * sin(th)
print(f'xx = {xx:g}, yy = {yy:g}')

print('\n--- shifting point ---')
ssx, ssy = 2, 1
xx += ssx; yy += ssy
print(f'ssx = {ssx:g}, ssy = {ssy:g}')
print(f'xx = {xx:g}, yy = {yy:g}')

print('\n--- scaling point ---')
ccx, ccy = 2, 3
xx *= ccx; yy *= ccy
print(f'ccx = {ccx:g}, ccy = {ccy:g}')
print(f'xx = {xx:g}, yy = {yy:g}')

print('\n--- revolving point ---')
ps = d2r(90)
xx, yy = xx * cos(ps) - yy * sin(ps), xx * sin(ps) + yy * cos(ps)
print(f'ps(deg) = {r2d(ps):g}')
print(f'xx = {xx:g}, yy = {yy:g}')

