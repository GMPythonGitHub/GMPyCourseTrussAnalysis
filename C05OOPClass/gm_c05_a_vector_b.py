# gm_c05_a_vector_b.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** class GMVector for vector: ver. b ***')
print('  *** introducing list and ndarray ***')

print('# -----------------------------------------------------------------------------')
print('## --- section__: (GMVectorB) importing item from module ---')
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d, ndarray, array )

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVectorB) defining class ---')
class GMVectorB():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVectorB) initializing class instance---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None  # declaring instance variables
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVectorB) setting and getting functions ---')
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
    print('## --- section_a3: (GMVectorB) string function for print() ---')
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
        return f'(xx,yy) = ({xx:g},{yy:g}), (rr,th) = ({rr:g},{th:g})'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVectorB) calculating unit vector ---')
    def uvct(self) -> ndarray:
        rr, _ = self.rrth()
        return array([self.__xxyy[0] / rr, self.__xxyy[1] / rr])

# =============================================================================
print('\n## --- section_b: (GMVectorB) creating class instance ---')
vecta = GMVectorB(xxyy=(1., 1.)); print('vecta: ', vecta)
vectb = GMVectorB(rrth=(2., 30.)); print('vectb: ', vectb)
vectc = GMVectorB(rrth=(2., 120.)); print('vectb: ', vectb)

# -----------------------------------------------------------------------------
print('\n## --- section_c: calculating unit vectors ---')
print(f'{vecta.uvct() = }')
print(f'{vectb.uvct() = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVector for vector: ver. b ***
  *** introducing list and ndarray ***
# -----------------------------------------------------------------------------
## --- section__: (GMVectorB) importing item from module ---
## --- section_a: (GMVectorB) defining class ---
## --- section_a1: (GMVectorB) initializing class instance---
## --- section_a2: (GMVectorB) setting and getting functions ---
## --- section_a3: (GMVectorB) string function for print() ---
## --- section_a4: (GMVectorB) calculating unit vector ---

## --- section_b: (GMVectorB) creating class instance ---
vecta:  (xx,yy) = (1,1), (rr,th) = (1.41421,45)
vectb:  (xx,yy) = (1.73205,1), (rr,th) = (2,30)
vectb:  (xx,yy) = (1.73205,1), (rr,th) = (2,30)

## --- section_c: calculating unit vectors ---
vecta.uvct() = array([0.70710678, 0.70710678])
vectb.uvct() = array([0.8660254, 0.5      ])
'''
