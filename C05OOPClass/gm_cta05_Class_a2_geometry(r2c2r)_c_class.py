# gm_cta05_Class_a2_geometry(r2c2r)_c_class.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 2 with class ***')
print('   *** converting coordinate system: between rectangular and circular ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

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

# =============================================================================
# =============================================================================
print('\n## --- main sentences ---')
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')

point = GMPoint()  # creating instance of class GMCoord
point.xx, point.yy = xx, yy  # setting instance variables
rr, th = point.rrth()
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}')

point.set_rrth(rr, th)  # setting rr, th
xx, yy = point.xxyy()
print(f'xx = {xx:g}, yy = {yy:g}')

