## gm_c05_b0_vector.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMVector) class for vector ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMVector) importing items from module ---")
from numpy import (
    square, sqrt, sin, cos, arccos as acos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d,
    ndarray, array, dot as dott, cross as cros, tensordot as tnsr )

# -----------------------------------------------------------------------------
print("## --- section_a: (GMVector) declaring class ---")
class GMVector():
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMVector) initializing class instance ---")
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None
        if isinstance (xxyy, GMVector): xxyy, rrth = xxyy.xxyy(), None
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMVector) setting and getting functions ---")
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
        rr = sqrt(dott(self.__xxyy,self.__xxyy))
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
    print("## --- section_d: (GMVector) string function for print() ---")
    def __str__(self) -> str:
        if (len(self.__xxyy)) == 2:
            xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
            return (
                f': (xx,yy) = ({xx:g}, {yy:g}) '
                f': (rr,th) = ({rr:g}, {th:g})' )
        elif len(self.__xxyy) == 3:
            xx, yy, zz = self.__xxyy; rr, th, ph = self.rrth(cnv=True)
            return (
                f': (xx,yy,zz) = ({xx:g}, {yy:g}, {zz:g}) '
                f': (rr,th,ph) = ({rr:g}, {th:g}, {ph:g})' )
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMVector ::\n'
            + self.__str__() )

    # -----------------------------------------------------------------------------
    print("## --- section_e: (GMVector) operating vectors ---")
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
    print("## --- section_f: (GMVector) overloading arithmetic operators ---")
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
    print("## --- section_g: (GMVector) calculating vector ---")
    def unitvect(self) -> ndarray:
        rr, *_ = self.rrth()
        return self.__xxyy / rr if rr > 0. else None
    def dottprod(self, vect: object) -> ndarray:  # dot product (inner)
        return dott(self.__xxyy, vect.xxyy())
    def crosprod(self, vect: object) -> ndarray:  # cross product (outer)
        return cros(self.__xxyy, vect.xxyy())
    def tnsrprod(self, vect: object) -> ndarray:  # tensor product
        return tnsr(self.__xxyy, vect.xxyy(), axes=0)

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    vecta = GMVector(xxyy=(1., 1.)); vecta.prtcls('vecta -> ')
    vectb = GMVector(xxyy=(3., 4.)); vectb.prtcls('vectb -> ')
    vectc = GMVector(vectb); vectc.prtcls('vectc -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: operating vectors ---")
    (vecta + vectb).prtcls('vecta + vectb -> ')
    print(f'{(vecta + vectb).xxyy() = }')
    print(f'{(vecta - vectb).xxyy() = }')
    print(f'{(vecta * vectb).xxyy() = }')
    print(f'{(vecta / vectb).xxyy() = }')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mc: calculating unit vector and product ---")
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
    ## --- section_a: (GMVector) declaring class ---
    ## --- section_b: (GMVector) initializing class instance ---
    ## --- section_c: (GMVector) setting and getting functions ---
    ## --- section_d: (GMVector) string function for print() ---
    ## --- section_e: (GMVector) operating vectors ---
    ## --- section_f: (GMVector) overloading arithmetic operators ---
    ## --- section_g: (GMVector) calculating unit vector and products ---
    
    ## --- section_ma: creating class instances ---
    vecta -> :: GMVector ::
    : (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45)
    vectb -> :: GMVector ::
    : (xx,yy) = (3, 4) : (rr,th) = (5, 53.1301)
    vectc -> :: GMVector ::
    : (xx,yy) = (3, 4) : (rr,th) = (5, 53.1301)
    
    ## --- section_mb: operating vectors ---
    vecta + vectb -> :: GMVector ::
    : (xx,yy) = (4, 5) : (rr,th) = (6.40312, 51.3402)
    (vecta + vectb).xxyy() = array([4., 5.])
    (vecta - vectb).xxyy() = array([-2., -3.])
    (vecta * vectb).xxyy() = array([3., 4.])
    (vecta / vectb).xxyy() = array([0.33333333, 0.25      ])
    
    ## --- section_mc: calculating unit vector and product ---
    vecta.unitvect() = array([0.70710678, 0.70710678])
    vecta.dottprod(vectb) = 7.0, vecta.crosprod(vectb) = array(1.)
    vecta.tnsrprod(vectb) = array([[3., 4.],
           [3., 4.]])
    vectb.unitvect() = array([0.6, 0.8])
    vectb.dottprod(vecta) = 7.0, vectb.crosprod(vecta) = array(-1.)
    vectb.tnsrprod(vecta) = array([[3., 3.],
           [4., 4.]])
    '''
