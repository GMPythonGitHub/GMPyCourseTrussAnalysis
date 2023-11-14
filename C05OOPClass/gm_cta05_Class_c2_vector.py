# gm_cta05_Class_c2_vector.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** class GMVector for vector: ver. 2 ***')
print('  *** introducing list and ndarray ***')

print('# -----------------------------------------------------------------------------')
print('## --- section__: (GMVector2) importing item from module ---')
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d, ndarray, array )

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVector2) declaring class ---')
class GMVector2():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVector2) initializing class instance---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None  # declaring instance variables
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVector2) setting and getting functions ---')
    ## setting functions
    def set_vector(self,
            xxyy: tuple = None, rrth: tuple = None, cnv: bool = True) -> None:
        if rrth is not None:
            xxyy = None; rr, th = rrth
            if cnv: th = d2r(th)
            self.__xxyy = rr * array([cos(th), sin(th)])
        if xxyy is not None: self.__xxyy = array(xxyy)
    ## getting functions
    def xxyy(self) -> ndarray:
        return self.__xxyy
    def rrth(self, cnv: bool = True) -> ndarray:
        rr, th = sqrt(sum(square(self.__xxyy))), atan2(self.__xxyy[1], self.__xxyy[0])
        if cnv: th = r2d(th)
        return array((rr, th))

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMVector2) string function for print() ---')
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
        return f'(xx,yy) = ({xx:g},{yy:g}), (rr,th) = ({rr:g},{th:g})'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVector2) calculating unit vector ---')
    def uvct(self) -> ndarray:
        rr, _ = self.rrth()
        return array([self.__xxyy[0] / rr, self.__xxyy[1] / rr])

# =============================================================================
# =============================================================================
print('\n## --- section_b: creating class instance ---')
vecta = GMVector2(rrth=(2., 0.)); print('vecta: ', vecta)
vectb = GMVector2(rrth=(2., 30.)); print('vectb: ', vectb)
vectc = GMVector2(rrth=(2., 90.)); print('vectc: ', vectc)

# -----------------------------------------------------------------------------
print('\n## --- section_c: calculating unit vectors ---')
print(f'{vecta.uvct() = }')
print(f'{vectb.uvct() = }')
print(f'{vectc.uvct() = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVector for vector: ver. 2 ***
  *** introducing list and ndarray ***
# -----------------------------------------------------------------------------
## --- section__: (GMVector2) importing item from module ---
## --- section_a: (GMVector2) declaring class ---
## --- section_a1: (GMVector2) initializing class instance---
## --- section_a2: (GMVector2) setting and getting functions ---
## --- section_a3: (GMVector2) string function for print() ---
## --- section_a4: (GMVector2) calculating unit vector ---

## --- section_b: creating class instance ---
vecta:  (xx,yy) = (2,0), (rr,th) = (2,0)
vectb:  (xx,yy) = (1.73205,1), (rr,th) = (2,30)
vectc:  (xx,yy) = (1.22465e-16,2), (rr,th) = (2,90)

## --- section_c: calculating unit vectors ---
vecta.uvct() = array([1., 0.])
vectb.uvct() = array([0.8660254, 0.5      ])
vectc.uvct() = array([6.123234e-17, 1.000000e+00])
'''
