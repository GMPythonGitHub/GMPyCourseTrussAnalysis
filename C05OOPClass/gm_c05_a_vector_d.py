# gm_c05_a_vector_d.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** class GMVector for vector: ver. d ***')
print('  *** introducing overload of operator ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: (GMVectorD) importing item from module ---')
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d, ndarray, array )

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVectorD) defining class ---')
class GMVectorD():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVectorD) initializing class instance ---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVectorD) setting and getting functions ---')
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
    print('## --- section_a3: (GMVectorD) string function for print() ---')
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
        return f'(xx,yy) = ({xx:g},{yy:g}), (rr,th) = ({rr:g},{th:g})'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVectorD) operating vectors ---')
    def cnv2vect(self, vect: object = None) -> object:
        if type(vect) in (int, float, complex): return vect
        elif type(vect) in (list, tuple, ndarray): return array(vect)
        else: return vect.xxyy()
    def add(self, vect: object = None) -> None: self.__xxyy += self.cnv2vect(vect)
    def sub(self, vect: object = None) -> None: self.__xxyy -= self.cnv2vect(vect)
    def mul(self, vect: object = None) -> None: self.__xxyy *= self.cnv2vect(vect)
    def div(self, vect: object = None) -> None: self.__xxyy /= self.cnv2vect(vect)

    # -----------------------------------------------------------------------------
    print('## --- section_a5: (GMVectorD) overloading arithmetic operators ---')
    def __add__(self, vect): return GMVectorD(xxyy=self.__xxyy+self.cnv2vect(vect))
    def __radd__(self, vect): return GMVectorD(xxyy=self.cnv2vect(vect)+self.__xxyy)
    def __sub__(self, vect): return GMVectorD(xxyy=self.__xxyy-self.cnv2vect(vect))
    def __rsub__(self, vect): return GMVectorD(xxyy=self.cnv2vect(vect)-self.__xxyy)
    def __mul__(self, vect): return GMVectorD(xxyy=self.__xxyy*self.cnv2vect(vect))
    def __rmul__(self, vect): return GMVectorD(xxyy=self.cnv2vect(vect)*self.__xxyy)
    def __truediv__(self, vect): return GMVectorD(xxyy=self.__xxyy/self.cnv2vect(vect))
    def __rtruediv__(self, vect): return GMVectorD(xxyy=self.cnv2vect(vect)/self.__xxyy)
    def __floordiv__(self, vect): return GMVectorD(xxyy=self.__xxyy//self.cnv2vect(vect))
    def __rfloordiv__(self, vect): return GMVectorD(xxyy=self.cnv2vect(vect)//self.__xxyy)
    def __mod__(self, vect): return GMVectorD(xxyy=self.__xxyy%self.cnv2vect(vect))
    def __rmod__(self, vect): return GMVectorD(xxyy=self.cnv2vect(vect)%self.__xxyy)

    # -----------------------------------------------------------------------------
    print('## --- section_a6: (GMVectorD) calculating unit vector and products ---')
    def uvect(self) -> ndarray:
        rr, _ = self.rrth()
        return array([self.__xxyy[0] / rr, self.__xxyy[1] / rr])
    def dotprd(self, vect: object = None) -> object:
        cnvvect = self.cnv2vect(vect)
        if type(cnvvect) is ndarray:
            return sum(self.__xxyy * cnvvect)
        else: return None
    def vctprd(self, vect: object = None) -> object:
        cnvvect = self.cnv2vect(vect)
        if type(cnvvect) is ndarray:
            return self.__xxyy[0] * cnvvect[1] - self.__xxyy[1] * cnvvect[0]
        else: return None

# =============================================================================
print('\n## --- section_b: creating class instances ---')
vecta = GMVectorD(xxyy=(1., 1.)); print('vecta: ', vecta)
vectb = GMVectorD(xxyy=(1., 2.)); print('vectb: ', vectb)

# -----------------------------------------------------------------------------
print('\n## --- section_c: operating vectors with operators ---')
print(f'vecta + 2: {vecta + 2}'); print(f'2 + vecta: {2 + vecta}')
print(f'vecta + [1,2]: {vecta + [1,2]}'); print(f'[1,2] + vecta: {[1,2] + vecta}')
print(f'vecta + vectb: {vecta + vectb}'); print(f'vectb + vecta: {vectb + vecta}')

print(f'vecta - 2: {vecta - 2}'); print(f'2 - vecta: {2 - vecta}')
print(f'vecta - [1,2]: {vecta - [1,2]}'); print(f'[1,2] - vecta: {[1,2] - vecta}')
print(f'vecta - vectb: {vecta - vectb}'); print(f'vectb - vecta: {vectb - vecta}')

print(f'vecta * 2: {vecta * 2}')
print(f'vecta * [1,2]: {vecta * [1,2]}')
print(f'vecta * vectb: {vecta * vectb}')

print(f'vecta / 2: {vecta / 2}')
print(f'vecta / [1,2]: {vecta / [1,2]}')
print(f'vecta / vectb: {vecta / vectb}')

print(f'vecta // 2: {vecta //2}')
print(f'vecta // [1,2]: {vecta // [1,2]}')
print(f'vecta // vectb: {vecta // vectb}')

print(f'vecta % 2: {vecta % 2}')
print(f'vecta % [1,2]: {vecta % [1,2]}')
print(f'vecta % vectb: {vecta % vectb}\n')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVector for vector: ver. d ***
  *** introducing overload of operator ***
# -----------------------------------------------------------------------------
## --- section__: (GMVectorD) importing item from module ---
## --- section_a: (GMVectorD) defining class ---
## --- section_a1: (GMVectorD) initializing class instance ---
## --- section_a2: (GMVectorD) setting and getting functions ---
## --- section_a3: (GMVectorD) string function for print() ---
## --- section_a4: (GMVectorD) operating vectors ---
## --- section_a5: (GMVectorD) overloading arithmetic operators ---
## --- section_a6: (GMVectorD) calculating unit vector and products ---

## --- section_b: creating class instances ---
vecta:  (xx,yy) = (1,1), (rr,th) = (1.41421,45)
vectb:  (xx,yy) = (1,2), (rr,th) = (2.23607,63.4349)

## --- section_c: operating vectors with operators ---
vecta + 2: (xx,yy) = (3,3), (rr,th) = (4.24264,45)
2 + vecta: (xx,yy) = (3,3), (rr,th) = (4.24264,45)
vecta + [1,2]: (xx,yy) = (2,3), (rr,th) = (3.60555,56.3099)
[1,2] + vecta: (xx,yy) = (2,3), (rr,th) = (3.60555,56.3099)
vecta + vectb: (xx,yy) = (2,3), (rr,th) = (3.60555,56.3099)
vectb + vecta: (xx,yy) = (2,3), (rr,th) = (3.60555,56.3099)
vecta - 2: (xx,yy) = (-1,-1), (rr,th) = (1.41421,-135)
2 - vecta: (xx,yy) = (1,1), (rr,th) = (1.41421,45)
vecta - [1,2]: (xx,yy) = (0,-1), (rr,th) = (1,-90)
[1,2] - vecta: (xx,yy) = (0,1), (rr,th) = (1,90)
vecta - vectb: (xx,yy) = (0,-1), (rr,th) = (1,-90)
vectb - vecta: (xx,yy) = (0,1), (rr,th) = (1,90)
vecta * 2: (xx,yy) = (2,2), (rr,th) = (2.82843,45)
vecta * [1,2]: (xx,yy) = (1,2), (rr,th) = (2.23607,63.4349)
vecta * vectb: (xx,yy) = (1,2), (rr,th) = (2.23607,63.4349)
vecta / 2: (xx,yy) = (0.5,0.5), (rr,th) = (0.707107,45)
vecta / [1,2]: (xx,yy) = (1,0.5), (rr,th) = (1.11803,26.5651)
vecta / vectb: (xx,yy) = (1,0.5), (rr,th) = (1.11803,26.5651)
vecta // 2: (xx,yy) = (0,0), (rr,th) = (0,0)
vecta // [1,2]: (xx,yy) = (1,0), (rr,th) = (1,0)
vecta // vectb: (xx,yy) = (1,0), (rr,th) = (1,0)
vecta % 2: (xx,yy) = (1,1), (rr,th) = (1.41421,45)
vecta % [1,2]: (xx,yy) = (0,1), (rr,th) = (1,90)
vecta % vectb: (xx,yy) = (0,1), (rr,th) = (1,90)
'''
