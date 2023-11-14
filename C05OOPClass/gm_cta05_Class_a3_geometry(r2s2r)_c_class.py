# gm_cta05_Class_a3_geometry(r2s2r)_c_class.py: coded by Kinya MIURA 231113
# -----------------------------------------------------------------------------
print('\n*** calculation on coordinate system; ver. 3 with class ***')
print('   *** converting coordinate system: from rectangular to spherical ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- importing items from module ---')
from numpy import (sqrt, cos, sin, arctan2 as atan2, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- class ---')
class GMPoint:
    def __init__(self) -> None:
        self.xx, self.yy, self.zz = None, None, None
        # initializing xx, yy, zz: instance variables
    def set_rrthph(self, rr, th, ph):
        xx, yy, zz = rr * sin(ph) * cos(th), rr * sin(ph) * sin(th), rr * cos(ph)
    def xxyyzz(self) -> tuple:
        return xx, yy, zz
        # xx, yy, zz: instance variables
    def rrthph(self) -> tuple:
        rr, th, ph = (
            sqrt(self.xx**2+self.yy**2+self.zz**2),
            atan2(self.yy, self.xx),
            atan2(sqrt(self.xx**2+self.yy**2), self.zz) )
        return rr, th, ph
        # rr, th, ph: local variables

# =============================================================================
# =============================================================================
print('\n## --- main sentences ---')
xx, yy, zz = 3, 4, 5
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')

point = GMPoint()  # creating instance of class GMCoord
point.xx, point.yy, point.zz = xx, yy, zz  # setting instance variables
rr, th, ph = point.rrthph()
print(f'rr = {rr:g}, th(deg) = {r2d(th):g}, ph(deg) = {r2d(ph):g}')

point.set_rrthph(rr, th, ph)
xx, yy, zz = point.xxyyzz()
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')

