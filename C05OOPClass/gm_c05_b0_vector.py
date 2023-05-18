## gm_c05_b0_vector.py: coded by Kinya MIURA 230517
# -----------------------------------------------------------------------------
print('\n*** (GMVector) class for vector ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: (GMVector) importing items from module ---')
from numpy import (
    square, sqrt, sin, cos, arccos as acos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d,
    ndarray, array, dot, cross as crs, tensordot as tsr )

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVector) defining class ---')
class GMVector():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVector) initializing class instance ---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVector) setting and getting functions ---')
    ## setting functions
    def set_xxyy(self, xxyy: tuple) -> None:
        self.__xxyy = array(xxyy)
    def set_rrth(self, rrth: tuple, cnv: bool = True) -> None:
        if len(rrth) == 2:
            rr, th = rrth
            if cnv: th = d2r(th)
            self.__xxyy = rr * array((cos(th), sin(th)))
        elif len(rrth) == 3:
            rr, th, ph = rrth
            if cnv: th, ph = d2r(th), d2r(ph)
            self.__xxyy = rr * array((sin(ph)*cos(th), sin(ph)*sin(th), cos(ph)))
        else:
            self.__xxyy = None
    def set_vector(self,
            xxyy: tuple = None, rrth: tuple = None, cnv: bool = True) -> None:
        if rrth is not None:
            self.set_rrth(rrth)
        elif xxyy is not None:
            self.set_xxyy(xxyy)
        else: pass

    ## getting functions
    def xxyy(self) -> ndarray:
        return self.__xxyy
    def rrth(self, cnv: bool = True) -> ndarray:
        rr = sqrt(dot(self.__xxyy,self.__xxyy))
        if len(self.__xxyy) == 2:
            xx, yy = self.__xxyy
            th = atan2(yy, xx)
            if cnv: th = r2d(th)
            return array((rr, th))
        elif len(self.__xxyy) == 3:
            xx, yy, zz = self.__xxyy
            th, ph = atan2(yy,xx), acos(zz/rr)
            if cnv: th, ph = r2d(th), r2d(ph)
            return array((rr, th, ph))
        else: return None

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMVector) string function for print() ---')
    def __str__(self) -> str:
        if (len(self.__xxyy)) == 2:
            xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
            return (
                f'GMVector:: (xx,yy) = ({xx:g}, {yy:g}), '
                f'(rr,th) = ({rr:g}, {th:g})' )
        elif len(self.__xxyy) == 3:
            xx, yy, zz = self.__xxyy; rr, th, ph = self.rrth(cnv=True)
            return (
                f'GMVector:: (xx,yy,zz) = ({xx:g}, {yy:g}, {zz:g}), '
                f'(rr,th,ph) = ({rr:g}, {th:g}, {ph:g})' )

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVector) operating vectors ---')
    def cnvvect(self, vect: object = None) -> ndarray:
        if type(vect) in (int, float, complex): return vect
        elif type(vect) in (list, tuple, ndarray): return array(vect)
        else: return vect.xxyy()
    def add(self, vect: object = None) -> ndarray:
        self.__xxyy += self.cnvvect(vect); return self.xxyy()
    def sub(self, vect: object = None) -> ndarray:
        self.__xxyy -= self.cnvvect(vect); return self.xxyy()
    def mul(self, vect: object = None) -> ndarray:
        self.__xxyy *= self.cnvvect(vect); return self.xxyy()
    def div(self, vect: object = None) -> ndarray:
        self.__xxyy /= self.cnvvect(vect); return self.xxyy()

    # -----------------------------------------------------------------------------
    print('## --- section_a5: (GMVector) overloading arithmetic operators ---')
    def __add__(self, vect): return GMVector(xxyy=self.__xxyy+self.cnvvect(vect))
    def __radd__(self, vect): return GMVector(xxyy=self.cnvvect(vect)+self.__xxyy)
    def __sub__(self, vect): return GMVector(xxyy=self.__xxyy-self.cnvvect(vect))
    def __rsub__(self, vect): return GMVector(xxyy=self.cnvvect(vect)-self.__xxyy)
    def __mul__(self, vect): return GMVector(xxyy=self.__xxyy*self.cnvvect(vect))
    def __rmul__(self, vect): return GMVector(xxyy=self.cnvvect(vect)*self.__xxyy)
    def __truediv__(self, vect): return GMVector(xxyy=self.__xxyy/self.cnvvect(vect))
    def __rtruediv__(self, vect): return GMVector(xxyy=self.cnvvect(vect)/self.__xxyy)

    def __iadd__(self, vect): self.__xxyy+=self.cnvvect(vect); return self
    def __isub__(self, vect): self.__xxyy-=self.cnvvect(vect); return self
    def __imul__(self, vect): self.__xxyy*=self.cnvvect(vect); return self
    def __itruediv__(self, vect): self.__xxyy/=self.cnvvect(vect); return self

    def __pos__(self):  self.__xxyy = + self.__xxyy; return self
    def __neg__(self):  self.__xxyy = - self.__xxyy; return self

    # -----------------------------------------------------------------------------
    print('## --- section_a6: (GMVector) calculating unit vector and products ---')
    def unitvect(self) -> ndarray:
        rr, *_ = self.rrth()
        return self.__xxyy / rr if rr > 0. else None
    def dottprod(self, vect: object) -> ndarray:  # dot product (inner)
        return dot(self.__xxyy, vect.xxyy())
    def crosprod(self, vect: object) -> ndarray:  # cross product (outer)
        return crs(self.__xxyy, vect.xxyy())
    def tnsrprod(self, vect: object) -> ndarray:  # tensor product
        return tsr(self.__xxyy, vect.xxyy(), axes=0)

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print('\n## --- section_b: creating class instances ---')
    vecta = GMVector(xxyy=(1., 1.)); print('vecta: ', vecta)
    vectb = GMVector(xxyy=(3., 4.)); print('vectb: ', vectb)

    # -----------------------------------------------------------------------------
    print('\n## --- section_c: arithmetic calculation of vectors ---')
    print('vecta + vectb = ', vecta + vectb)
    print('vecta - vectb = ', vecta - vectb)
    print('vecta * vectb = ', vecta * vectb)
    print('vecta / vectb = ', vecta / vectb)

    # -----------------------------------------------------------------------------
    print('\n## --- section_d: calculating unit vectors and products ---')
    print(f'{vecta.unitvect() = }')
    print(f'{vecta.dottprod(vectb) = }, {vecta.crosprod(vectb) = }')
    print(f'{vecta.tnsrprod(vectb) = }')
    print(f'{vectb.unitvect() = }')
    print(f'{vectb.dottprod(vecta) = }, {vectb.crosprod(vecta) = }')
    print(f'{vectb.tnsrprod(vecta) = }')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMVector) class for vector ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMVector) importing items from module ---
    ## --- section_a: (GMVector) defining class ---
    ## --- section_a1: (GMVector) initializing class instance ---
    ## --- section_a2: (GMVector) setting and getting functions ---
    ## --- section_a3: (GMVector) string function for print() ---
    ## --- section_a4: (GMVector) operating vectors ---
    ## --- section_a5: (GMVector) overloading arithmetic operators ---
    ## --- section_a6: (GMVector) calculating unit vector and products ---
    
    ## --- section_b: creating class instances ---
    vecta:  GMVector:: (xx,yy) = (1, 1), (rr,th) = (1.41421, 45)
    vectb:  GMVector:: (xx,yy) = (3, 4), (rr,th) = (5, 53.1301)
    
    ## --- section_c: arithmetic calculation of vectors ---
    vecta + vectb =  GMVector:: (xx,yy) = (4, 5), (rr,th) = (6.40312, 51.3402)
    vecta - vectb =  GMVector:: (xx,yy) = (-2, -3), (rr,th) = (3.60555, -123.69)
    vecta * vectb =  GMVector:: (xx,yy) = (3, 4), (rr,th) = (5, 53.1301)
    vecta / vectb =  GMVector:: (xx,yy) = (0.333333, 0.25), (rr,th) = (0.416667, 36.8699)
    
    ## --- section_d: calculating unit vectors and products ---
    vecta.unitvect() = array([0.70710678, 0.70710678])
    vecta.dottprod(vectb) = 7.0, vecta.crosprod(vectb) = array(1.)
    vecta.tnsrprod(vectb) = array([[3., 4.],
           [3., 4.]])
    vectb.unitvect() = array([0.6, 0.8])
    vectb.dottprod(vecta) = 7.0, vectb.crosprod(vecta) = array(-1.)
    vectb.tnsrprod(vecta) = array([[3., 3.],
           [4., 4.]])
    '''
