# gm_cta05_Class_a0_geometry(r2c)_c_class.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 0 with class ***')
print('   *** converting coordinate system: from rectangular to circular ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, arctan2 as atan2, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- class ---')
class GMCoord:
    def __init__(self) -> None:
        self.xx, self.yy = None, None
        # initializing xx, yy: instance variables
    def rrth(self) -> tuple:
        rr, th = sqrt(self.xx**2+self.yy**2), atan2(self.yy, self.xx)
        return rr, th
        # rr, th: local variables

# =============================================================================
# =============================================================================
print('\n## --- main sentences ---')
xx, yy = 3, 4
print(f'xx = {xx:g}, yy = {yy:g}')

coord = GMCoord()  # creating instance of class GMCoord
coord.xx, coord.yy = xx, yy  # setting instance variables
rr, th = coord.rrth()
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}')

