# gm_cta05_Class_a4_geometry(move)_c_class.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 4 with class ***')
print('   *** converting coordinate system: shift, scale and revolve ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d, deg2rad as d2r)

# -----------------------------------------------------------------------------
print('\n## --- class ---')
class GMPoint:
    def __init__(self) -> None:
        self.xx, self.yy = None, None
        # initializing xx, yy: instance variables
    def set_rrth(self, rr, th) -> None:
        self.xx, self.yy = rr * cos(th), rr * sin(th)
    def xxyy(self) -> tuple:
        return self.xx, self.yy
        # xx, yy: instance variables
    def rrth(self) -> tuple:
        rr, th = sqrt(self.xx**2+self.yy**2), atan2(self.yy, self.xx)
        return rr, th
        # rr, th: local variables
    def shift(self, ssx, ssy) -> None:
        self.xx += ssx; self.yy += ssy
    def scale(self, ccx, ccy) -> None:
        self.xx *= ccx; self.yy *= ccy
    def revolve(self, ps) -> None:
        self.xx, self.yy = self.xx * cos(ps) - self.yy * sin(ps), self.xx * sin(ps) + self.yy * cos(ps)

# =============================================================================
# =============================================================================
print('\n## --- main sentences ---')
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')
point = GMPoint()  # creating instance of class GMPoint
point.xx, point.yy = xx, yy  # setting instance variables
rr, th = point.rrth()
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}')
point.set_rrth(rr, th)  # setting rr, th
xx, yy = point.xxyy()
print(f'xx = {xx:g}, yy = {yy:g}')

print('\n--- shifting point ---')
ssx, ssy = 2, 1
point.shift(ssx, ssy)
print(f'ssx = {ssx:g}, ssy = {ssy:g}')
xx, yy = point.xxyy()
print(f'xx = {xx:g}, yy = {yy:g}')
print('\n--- scaling point ---')
ccx, ccy = 2, 3
point.scale(ccx, ccy)
print(f'ccx = {ccx:g}, ccy = {ccy:g}')
xx, yy = point.xxyy()
print(f'xx = {xx:g}, yy = {yy:g}')
print('\n--- revolving point ---')
ps = d2r(90)
point.revolve(ps)
print(f'ps(deg) = {r2d(ps):g}')
xx, yy = point.xxyy()
print(f'xx = {xx:g}, yy = {yy:g}')

