from __future__ import annotations
# gm_cta05_Class_c4_vector.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** class GMVector for vector: ver. 4 ***')
print('  *** introducing overload of operators ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: (GMVector4) importing item from module ---')
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d, ndarray, array )

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVector4) declaring class ---')
class GMVector4():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVector4) initializing class instance ---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVector4) setting and getting functions ---')
    def set_vector(self, xxyy: tuple = None, rrth: tuple = None, cnv: bool = True) -> None:
        if rrth is not None:
            xxyy = None; rr, th = rrth
            if cnv: th = d2r(th)
            self.__xxyy = rr * array([cos(th), sin(th)])
        if xxyy is not None: self.__xxyy = array(xxyy)
    def xxyy(self) -> ndarray:
        return self.__xxyy
    def rrth(self, cnv: bool = True) -> ndarray:
        rr, th = sqrt(sum(square(self.__xxyy))), atan2(self.__xxyy[1], self.__xxyy[0])
        if cnv: th = r2d(th)
        return array([rr, th])

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMVector4) string function for print() ---')
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
        return f'(xx,yy) = ({xx:g},{yy:g}), (rr,th) = ({rr:g},{th:g})'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVector4) operating vectors ---')
    def cnvvect(self, vect: GMVector4 = None) -> ndarray:
        if isinstance(vect, GMVector4): return vect.xxyy()
        elif isinstance(vect, list): return array(vect)
        elif isinstance(vect, tuple): return array(vect)
        elif isinstance(vect, ndarray): return vect
        else: return ndarray([0,0])
    def add(self, vect: GMVector4 = None) -> None: self.__xxyy += self.cnvvect(vect)
    def sub(self, vect: GMVector4 = None) -> None: self.__xxyy -= self.cnvvect(vect)
    def mul(self, vect: GMVector4 = None) -> None: self.__xxyy *= self.cnvvect(vect)
    def div(self, vect: GMVector4 = None) -> None: self.__xxyy /= self.cnvvect(vect)

    # -----------------------------------------------------------------------------
    print('## --- section_a5: (GMVector4) overloading arithmetic operators ---')
    def __add__(self, vect): return GMVector4(xxyy=self.__xxyy+self.cnvvect(vect))
    def __radd__(self, vect): return GMVector4(xxyy=self.cnvvect(vect)+self.__xxyy)
    def __sub__(self, vect): return GMVector4(xxyy=self.__xxyy-self.cnvvect(vect))
    def __rsub__(self, vect): return GMVector4(xxyy=self.cnvvect(vect)-self.__xxyy)
    def __mul__(self, vect): return GMVector4(xxyy=self.__xxyy*self.cnvvect(vect))
    def __rmul__(self, vect): return GMVector4(xxyy=self.cnvvect(vect)*self.__xxyy)
    def __truediv__(self, vect): return GMVector4(xxyy=self.__xxyy/self.cnvvect(vect))
    def __rtruediv__(self, vect): return GMVector4(xxyy=self.cnvvect(vect)/self.__xxyy)
    def __floordiv__(self, vect): return GMVector4(xxyy=self.__xxyy//self.cnvvect(vect))
    def __rfloordiv__(self, vect): return GMVector4(xxyy=self.cnvvect(vect)//self.__xxyy)
    def __mod__(self, vect): return GMVector4(xxyy=self.__xxyy%self.cnvvect(vect))
    def __rmod__(self, vect): return GMVector4(xxyy=self.cnvvect(vect)%self.__xxyy)

    # -----------------------------------------------------------------------------
    print('## --- section_a6: (GMVector4) calculating unit vector and products ---')
    def uvect(self) -> ndarray:
        rr, _ = self.rrth()
        return array([self.__xxyy[0] / rr, self.__xxyy[1] / rr])
    def iprd(self, vect: GMVector4 = None) -> GMVector4:
        cnvvect = self.cnvvect(vect)
        return sum(self.__xxyy * cnvvect)
    def oprd(self, vect: GMVector4 = None) -> GMVector4:
        cnvvect = self.cnvvect(vect)
        return self.__xxyy[0] * cnvvect[1] - self.__xxyy[1] * cnvvect[0]

# =============================================================================
# =============================================================================
print('\n## --- section_b: creating class instances ---')
vecta = GMVector4(xxyy=(1., 1.)); print('vecta: ', vecta)
vectb = GMVector4(xxyy=(3., 4.)); print('vectb: ', vectb)

# -----------------------------------------------------------------------------
print('\n## --- section_c: operating vectors with operators ---')
print(f'vecta + (1, 2): {vecta + (1, 2)}'); print(f'(1, 2) + vecta: {(1, 2) + vecta}')
print(f'vecta + vectb: {vecta + vectb}'); print(f'vectb + vecta: {vectb + vecta}')
print()
print(f'vecta - (1, 2): {vecta - (1, 2)}'); print(f'(1, 2) - vecta: {(1, 2) - vecta}')
print(f'vecta - vectb: {vecta - vectb}'); print(f'vectb - vecta: {vectb - vecta}')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVector for vector: ver. 4 ***
  *** introducing overload of operators ***
# -----------------------------------------------------------------------------
*** class GMVector for vector: ver. d ***
  *** introducing overload of operators ***
# -----------------------------------------------------------------------------
## --- section__: (GMVector4) importing item from module ---
## --- section_a: (GMVector4) declaring class ---
## --- section_a1: (GMVector4) initializing class instance ---
## --- section_a2: (GMVector4) setting and getting functions ---
## --- section_a3: (GMVector4) string function for print() ---
## --- section_a4: (GMVector4) operating vectors ---
## --- section_a5: (GMVector4) overloading arithmetic operators ---
## --- section_a6: (GMVector4) calculating unit vector and products ---

## --- section_b: creating class instances ---
vecta:  (xx,yy) = (1,1), (rr,th) = (1.41421,45)
vectb:  (xx,yy) = (3,4), (rr,th) = (5,53.1301)

## --- section_c: operating vectors with operators ---
vecta + (1, 2): (xx,yy) = (2,3), (rr,th) = (3.60555,56.3099)
(1, 2) + vecta: (xx,yy) = (2,3), (rr,th) = (3.60555,56.3099)
vecta + vectb: (xx,yy) = (4,5), (rr,th) = (6.40312,51.3402)
vectb + vecta: (xx,yy) = (4,5), (rr,th) = (6.40312,51.3402)

vecta - (1, 2): (xx,yy) = (0,-1), (rr,th) = (1,-90)
(1, 2) - vecta: (xx,yy) = (0,1), (rr,th) = (1,90)
vecta - vectb: (xx,yy) = (-2,-3), (rr,th) = (3.60555,-123.69)
vectb - vecta: (xx,yy) = (2,3), (rr,th) = (3.60555,56.3099)
'''
