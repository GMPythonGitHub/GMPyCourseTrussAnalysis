# gm_cta05_Class_c3_vector.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** class GMVector for vector: ver. 3 ***')
print('  *** introducing vector operations ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: (GMVector3) importing item from module ---')
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d, ndarray, array )

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVector3) declaring class ---')
class GMVector3():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVector3) initializing class instance---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None  # declaring instance variable
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVector3) setting and getting functions ---')
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
        return array([rr, th])

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMVector3) string function for print() ---')
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
        return f'(xx,yy) = ({xx:g},{yy:g}), (rr,th) = ({rr:g},{th:g})'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVector3) operating vectors ---')
    def cnvvect(self, vect: object = None) -> object:
        if isinstance(vect, GMVector3): return vect.xxyy()
        else: return array(vect)
    def add(self, vect: object = None) -> None: self.__xxyy += self.cnvvect(vect)
    def sub(self, vect: object = None) -> None: self.__xxyy -= self.cnvvect(vect)
    def mul(self, vect: object = None) -> None: self.__xxyy *= self.cnvvect(vect)
    def div(self, vect: object = None) -> None: self.__xxyy /= self.cnvvect(vect)

    # -----------------------------------------------------------------------------
    print('## --- section_a5: (GMVector3) calculating unit vector and products ---')
    def uvect(self) -> ndarray:
        rr, _ = self.rrth()
        return array([self.__xxyy[0] / rr, self.__xxyy[1] / rr])
    def iprd(self, vect: object = None) -> object:
        cnvvect = self.cnvvect(vect)
        if type(cnvvect) is ndarray:
            return self.__xxyy[0] * cnvvect[0] + self.__xxyy[1] * cnvvect[1]
        else: return None
    def oprd(self, vect: object = None) -> object:
        cnvvect = self.cnvvect(vect)
        if type(cnvvect) is ndarray:
            return self.__xxyy[0] * cnvvect[1] - self.__xxyy[1] * cnvvect[0]
        else: return None

# =============================================================================
# =============================================================================
print('\n## --- section_b: creating class instances ---')
vecta = GMVector3(xxyy=(1., 1.)); print('vecta: ', vecta)
vectb = GMVector3(xxyy=(3., 4.)); print('vectb: ', vectb)

# -----------------------------------------------------------------------------
print('\n## --- section_c: operating vectors ---')
vecta.set_vector(xxyy=(1., 1.))
vecta.add((1, 2)); print('vecta.add((1, 2)): ', vecta)
vecta.add(vectb); print('vecta.add(vectb): ', vecta)

vecta.set_vector(xxyy=(1., 1.))
vecta.sub((1, 2)); print('vecta.sub((1, 2)): ', vecta)
vecta.sub(vectb); print('vecta.sub(vectb): ', vecta)

# -----------------------------------------------------------------------------
print('\n## --- section_d: calculating unit vectors and products ---')
print('inner product: ', vecta.iprd(vectb))
print('outer product: ', vecta.oprd(vectb))

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVector for vector: ver. 3 ***
  *** introducing vector operations ***
# -----------------------------------------------------------------------------
## --- section__: (GMVector3) importing item from module ---
## --- section_a: (GMVector3) declaring class ---
## --- section_a1: (GMVector3) initializing class instance---
## --- section_a2: (GMVector3) setting and getting functions ---
## --- section_a3: (GMVector3) string function for print() ---
## --- section_a4: (GMVector3) operating vectors ---
## --- section_a5: (GMVector3) calculating unit vector and products ---

## --- section_b: creating class instances ---
vecta:  (xx,yy) = (1,1), (rr,th) = (1.41421,45)
vectb:  (xx,yy) = (3,4), (rr,th) = (5,53.1301)

## --- section_c: operating vectors ---
vecta.add((1, 2)):  (xx,yy) = (2,3), (rr,th) = (3.60555,56.3099)
vecta.add(vectb):  (xx,yy) = (5,7), (rr,th) = (8.60233,54.4623)
vecta.sub((1, 2)):  (xx,yy) = (0,-1), (rr,th) = (1,-90)
vecta.sub(vectb):  (xx,yy) = (-3,-5), (rr,th) = (5.83095,-120.964)

## --- section_d: calculating unit vectors and products ---
inner product:  -29.0
outer product:  3.0
'''
