# gm_cta05_Class_a4_geometry(move)_b_func.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 2 with function ***')
print('   *** converting coordinate system: shift, scale and revolve ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d, deg2rad as d2r)

# -----------------------------------------------------------------------------
print('\n## --- function ---')
def xxyy2rrth(xx, yy):
    rr, th = sqrt(xx**2+yy**2), atan2(yy, xx)
    return rr, th
def rrth2xxyy(rr, th):
    xx, yy = rr * cos(th), rr * sin(th)
    return xx, yy
def shift(xx, yy, ssx, ssy):
    xx += ssx; yy += ssy
    return xx, yy
def scale(xx, yy, ccx, ccy):
    xx *= ccx; yy *= ccy
    return xx, yy
def revolve(xx, yy, ps):
    xx, yy = xx * cos(ps) - yy * sin(ps), xx * sin(ps) + yy * cos(ps)
    return xx, yy

# -----------------------------------------------------------------------------
print('\n## --- main sentences ---')
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')
rr, th = xxyy2rrth(xx, yy)
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}')
xx, yy = rrth2xxyy(rr, th)
print(f'xx = {xx:g}, yy = {yy:g}')

print('\n--- shifting point ---')
ssx, ssy = 2, 1
xx, yy = shift(xx, yy, ssx, ssy)
print(f'ssx = {ssx:g}, ssy = {ssy:g}')
print(f'xx = {xx:g}, yy = {yy:g}')
print('\n--- scaling point ---')
ccx, ccy = 2, 3
xx, yy = scale(xx, yy, ccx, ccy)
print(f'ccx = {ccx:g}, ccy = {ccy:g}')
print(f'xx = {xx:g}, yy = {yy:g}')
print('\n--- revolving point ---')
ps = d2r(90)
xx, yy = revolve(xx, yy, ps)
print(f'ps(deg) = {r2d(ps):g}')
print(f'xx = {xx:g}, yy = {yy:g}')

