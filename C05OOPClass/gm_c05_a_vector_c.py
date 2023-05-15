# gm_c05_a_vector_c.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** class GMVector for vector: ver. c ***')
print('  *** introducing vector operations ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: (GMVectorC) importing item from module ---')
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d, ndarray, array )

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVectorC) defining class ---')
class GMVectorC():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVectorC) initializing class instance---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None  # declaring instance variable
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVectorC) setting and getting functions ---')
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
    print('## --- section_a3: (GMVectorC) string function for print() ---')
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
        return f'(xx,yy) = ({xx:g},{yy:g}), (rr,th) = ({rr:g},{th:g})'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVectorC) operating vectors ---')
    def cnv2vect(self, vect: object = None) -> object:
        if type(vect) in (int, float, complex): return vect
        elif type(vect) in (list, tuple, ndarray): return array(vect)
        else: return vect.xxyy()
    def add(self, vect: object = None) -> None: self.__xxyy += self.cnv2vect(vect)
    def sub(self, vect: object = None) -> None: self.__xxyy -= self.cnv2vect(vect)
    def mul(self, vect: object = None) -> None: self.__xxyy *= self.cnv2vect(vect)
    def div(self, vect: object = None) -> None: self.__xxyy /= self.cnv2vect(vect)

    # -----------------------------------------------------------------------------
    print('## --- section_a5: (GMVectorC) calculating unit vector and products ---')
    def uvect(self) -> ndarray:
        rr, _ = self.rrth()
        return array([self.__xxyy[0] / rr, self.__xxyy[1] / rr])
    def dotprd(self, vect: object = None) -> object:
        cnvvect = self.cnv2vect(vect)
        if type(cnvvect) is ndarray:
            return self.__xxyy[0] * cnvvect[0] + self.__xxyy[1] * cnvvect[1]
        else: return None
    def vctprd(self, vect: object = None) -> object:
        cnvvect = self.cnv2vect(vect)
        if type(cnvvect) is ndarray:
            return self.__xxyy[0] * cnvvect[1] - self.__xxyy[1] * cnvvect[0]
        else: return None

# =============================================================================
print('\n## --- section_b: creating class instances ---')
vecta = GMVectorC(xxyy=(1., 1.)); print('vecta: ', vecta)
vectb = GMVectorC(xxyy=(1., 2.)); print('vectb: ', vectb)

# -----------------------------------------------------------------------------
print('\n## --- section_c: operating vectors ---')
vecta.set_vector(xxyy=(1., 1.))
vecta.add(2); print('vecta.add(2): ', vecta)
vecta.add([1,2]); print('vecta.add([1,2]): ', vecta)
vecta.add(vectb); print('vecta.add(vectb): ', vecta)

vecta.set_vector(xxyy=(1., 1.))
vecta.sub(2); print('vecta.sub(2): ', vecta)
vecta.sub([1,2]); print('vecta.sub([1,2]): ', vecta)
vecta.sub(vectb); print('vecta.sub(vectb): ', vecta)

vecta.set_vector(xxyy=(1., 1.))
vecta.mul(2); print('vecta.mul(2): ', vecta)
vecta.mul([1,2]); print('vecta.mul([1,2]): ', vecta)
vecta.mul(vectb); print('vecta.mul(vectb): ', vecta)

vecta.set_vector(xxyy=(1., 1.))
vecta.div(2); print('vecta.div(2): ', vecta)
vecta.div([1,2]); print('vecta.div([1,2]): ', vecta)
vecta.div(vectb); print('vecta.div(vectb): ', vecta)

# -----------------------------------------------------------------------------
print('\n## --- section_d: calculating unit vectors and products ---')
print(f'{vecta.uvect() = }')
print(f'{vectb.uvect() = }')
print('dot product: ', vecta.dotprd(vectb))
print('vector product: ', vecta.vctprd(vectb))

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVector for vector: ver. c ***
  *** introducing vector operations ***
# -----------------------------------------------------------------------------
## --- section__: (GMVectorC) importing item from module ---
## --- section_a: (GMVectorC) defining class ---
## --- section_a1: (GMVectorC) initializing class instance---
## --- section_a2: (GMVectorC) setting and getting functions ---
## --- section_a3: (GMVectorC) string function for print() ---
## --- section_a4: (GMVectorC) operating vectors ---
## --- section_a5: (GMVectorC) calculating unit vector and products ---

## --- section_b: creating class instances ---
vecta:  (xx,yy) = (1,1), (rr,th) = (1.41421,45)
vectb:  (xx,yy) = (1,2), (rr,th) = (2.23607,63.4349)

## --- section_c: operating vectors ---
vecta.add(2):  (xx,yy) = (3,3), (rr,th) = (4.24264,45)
vecta.add([1,2]):  (xx,yy) = (4,5), (rr,th) = (6.40312,51.3402)
vecta.add(vectb):  (xx,yy) = (5,7), (rr,th) = (8.60233,54.4623)
vecta.sub(2):  (xx,yy) = (-1,-1), (rr,th) = (1.41421,-135)
vecta.sub([1,2]):  (xx,yy) = (-2,-3), (rr,th) = (3.60555,-123.69)
vecta.sub(vectb):  (xx,yy) = (-3,-5), (rr,th) = (5.83095,-120.964)
vecta.mul(2):  (xx,yy) = (2,2), (rr,th) = (2.82843,45)
vecta.mul([1,2]):  (xx,yy) = (2,4), (rr,th) = (4.47214,63.4349)
vecta.mul(vectb):  (xx,yy) = (2,8), (rr,th) = (8.24621,75.9638)
vecta.div(2):  (xx,yy) = (0.5,0.5), (rr,th) = (0.707107,45)
vecta.div([1,2]):  (xx,yy) = (0.5,0.25), (rr,th) = (0.559017,26.5651)
vecta.div(vectb):  (xx,yy) = (0.5,0.125), (rr,th) = (0.515388,14.0362)

## --- section_d: calculating unit vectors and products ---
vecta.uvect() = array([0.9701425 , 0.24253563])
vectb.uvect() = array([0.4472136 , 0.89442719])
dot product:  0.75
vector product:  0.875
'''
