## gm_cta05_Class_d0_vector.py: coded by Kinya MIURA 230523
# -----------------------------------------------------------------------------
print("\n*** (GMVector) class for vector ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMVector) importing items from module ---")
from numpy import (
    square, sqrt, sin, cos, arccos as acos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d,
    ndarray, array, dot as iprd, cross as oprd, tensordot as tprd )
import copy

# -----------------------------------------------------------------------------
print("## --- section_a: (GMVector) declaring class ---")
class GMVector():
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMVector) initializing class instance ---")
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None,
            unit: float = 1., cnv: bool = True):
        self.__xxyy, self.__unit = None, None
        self.set_vector(xxyy, rrth, unit=unit, cnv=cnv)

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMVector) setting and getting functions ---")
    ## setting functions
    def set_xxyy(self, xxyy: tuple, cnv: bool = True) -> None:
        self.__xxyy = array(xxyy)
        if cnv: self.__xxyy = self.__xxyy * self.__unit
    def set_rrth(self, rrth: tuple, cnv: bool = True) -> None:
        if len(rrth) == 2:
            rr, th = rrth
            if cnv: rr, th = rr * self.__unit, d2r(th)
            self.__xxyy = rr * array((cos(th), sin(th)))
        elif len(rrth) == 3:
            rr, th, ph = rrth
            if cnv: rr, th, ph = rr * self.__unit, d2r(th), d2r(ph)
            self.__xxyy = rr * array((sin(ph)*cos(th), sin(ph)*sin(th), cos(ph)))
        else:
            self.__xxyy = None
    def set_vector(self,
            xxyy: tuple = None, rrth: tuple = None,
            unit: float = None, cnv: bool = True) -> None:
        if unit is not None: self.__unit = unit
        if rrth is not None:
            self.set_rrth(rrth, cnv=cnv)
        elif xxyy is not None:
            self.set_xxyy(xxyy, cnv=cnv)

    ## getting functions
    def unit(self):
        return self.__unit
    def xxyy(self, cnv: bool = True) -> ndarray:
        if cnv: return self.__xxyy / self.__unit
        else: return self.__xxyy
    def rrth(self, cnv: bool = True) -> ndarray:
        rr = sqrt(sum(square(self.__xxyy)))
        if len(self.__xxyy) == 2:
            xx, yy = self.__xxyy
            th = atan2(yy, xx)
            if cnv: rr, th = rr / self.__unit, r2d(th)
            return array((rr, th))
        elif len(self.__xxyy) == 3:
            xx, yy, zz = self.__xxyy
            th, ph = atan2(yy,xx), acos(zz/rr)
            if cnv: rr, th, ph = rr / self.__unit, r2d(th), r2d(ph)
            return array((rr, th, ph))

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMVector) string function for print() ---")
    def __str__(self) -> str:
        if len(self.__xxyy) == 2:
            xx, yy = self.xxyy(); rr, th = self.rrth(cnv=True); unit = self.__unit
            return (
                f': (xx,yy) = ({xx:g}, {yy:g}) '
                f': (rr,th) = ({rr:g}, {th:g}) '
                f': unit = {unit:g}' )
        elif len(self.__xxyy) == 3:
            xx, yy, zz = self.xxyy(); rr, th, ph = self.rrth(cnv=True); 
            unit = self.__unit
            return (
                f': (xx,yy,zz) = ({xx:g}, {yy:g}, {zz:g}) '
                f': (rr,th,ph) = ({rr:g}, {th:g}, {ph:g}) '
                f': unit = {unit:g}')
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMVector ::\n'
            + self.__str__() )

    # -----------------------------------------------------------------------------
    print("## --- section_e: (GMVector) operating vectors ---")
    def copy(self) -> object:
        return copy.deepcopy(self)
    def cnvvect(self, vect: object = None) -> object:
        if isinstance(vect, GMVector): return vect.xxyy()
        else: return array(vect)
    def add(self, vect: object = None) -> None:
        self.__xxyy += self.cnvvect(vect)
    def sub(self, vect: object = None) -> None:
        self.__xxyy -= self.cnvvect(vect)
    def mul(self, vect: object = None) -> None:
        self.__xxyy *= self.cnvvect(vect)
    def div(self, vect: object = None) -> None:
        self.__xxyy /= self.cnvvect(vect)

    # -----------------------------------------------------------------------------
    print('## --- section_f: (GMVectorD) overloading arithmetic operators ---')
    def __add__(self, vect): return GMVector(xxyy=self.__xxyy+self.cnvvect(vect), unit=self.__unit)
    def __radd__(self, vect): return GMVector(xxyy=self.cnvvect(vect)+self.__xxyy, unit=self.__unit)
    def __sub__(self, vect): return GMVector(xxyy=self.__xxyy-self.cnvvect(vect), unit=self.__unit)
    def __rsub__(self, vect): return GMVector(xxyy=self.cnvvect(vect)-self.__xxyy, unit=self.__unit)
    def __mul__(self, vect): return GMVector(xxyy=self.__xxyy*self.cnvvect(vect), unit=self.__unit)
    def __rmul__(self, vect): return GMVector(xxyy=self.cnvvect(vect)*self.__xxyy, unit=self.__unit)
    def __truediv__(self, vect): return GMVector(xxyy=self.__xxyy/self.cnvvect(vect), unit=self.__unit)
    def __rtruediv__(self, vect): return GMVector(xxyy=self.cnvvect(vect)/self.__xxyy, unit=self.__unit)
    def __floordiv__(self, vect): return GMVector(xxyy=self.__xxyy//self.cnvvect(vect), unit=self.__unit)
    def __rfloordiv__(self, vect): return GMVector(xxyy=self.cnvvect(vect)//self.__xxyy, unit=self.__unit)
    def __mod__(self, vect): return GMVector(xxyy=self.__xxyy%self.cnvvect(vect), unit=self.__unit)
    def __rmod__(self, vect): return GMVector(xxyy=self.cnvvect(vect)%self.__xxyy, unit=self.__unit)

    def __iadd__(self, vect): self.__xxyy += self.cnvvect(vect); return self
    def __isub__(self, vect): self.__xxyy += self.cnvvect(vect); return self
    def __imul__(self, vect):
        self.__xxyy += self.cnvvect(vect); return self
    def __itruediv__(self, vect):
        self.__xxyy += self.cnvvect(vect); return self
    def __ifloordiv__(self, vect):
        self.__xxyy //= self.cnvvect(vect); return self
    def __imod__(self, vect):
        self.__xxyy %= self.cnvvect(vect); return self

    def __pos__(self):
        self.__xxyy = +self.__xxyy; return self
    def __neg__(self):
        self.__xxyy = -self.__xxyy; return self

    # -----------------------------------------------------------------------------
    print("## --- section_g: (GMVector) calculating vector ---")
    def unitvect(self, cnv: bool = True) -> ndarray:
        rr, *_ = self.rrth(False)
        unitvect = self.__xxyy / rr if rr > 0. else array((1., 0.))
        if cnv: return unitvect / self.__unit
        else: return unitvect
    def iprd(self, vect: object, cnv: bool = True) -> ndarray:  # dot product (inner)
        prod = iprd(self.__xxyy, vect.xxyy(False))
        if cnv: return prod / self.__unit / self.__unit
        else: return prod
    def oprd(self, vect: object, cnv: bool = True) -> ndarray:  # cross product (outer)
        prod = oprd(self.__xxyy, vect.xxyy(False))
        if cnv: return prod / self.__unit / self.__unit
        else: return prod
    def tprd(self, vect: object, cnv: bool = True) -> ndarray:  # tensor product
        prod = tprd(self.__xxyy, vect.xxyy(False), axes=0)
        if cnv: return prod / self.__unit / self.__unit
        else: return prod

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    vecta = GMVector(xxyy=(1., 1.), unit=10.); vecta.prtcls('vecta -> ')
    vectb = GMVector(xxyy=(3., 4.), unit=10.); vectb.prtcls('vectb -> ')
    vectbc = vectb.copy(); vectbc.prtcls('vectbc -> ')
    vectb.set_vector(xxyy=(1., -1.))
    vectb.prtcls('vectb -> '); vectbc.prtcls('vectbc -> ')
    vectc = GMVector(xxyy=(1.,2.)); vectc.prtcls('vectc -> ')
    vectc.set_vector(rrth=(1,45), unit=10); vectc.prtcls('vectc -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: calculating unit vector and product ---")
    print(f'{vecta.unitvect(False) = }')
    print(f'{vecta.iprd(vectb) = }, {vecta.oprd(vectb) = }')
    print(f'{vecta.tprd(vectb) = }')
    print(f'{vectb.unitvect(False) = }')
    print(f'{vectb.iprd(vecta) = }, {vectb.oprd(vecta) = }')
    print(f'{vectb.tprd(vecta) = }')

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
    ## --- section_f: (GMVectorD) overloading arithmetic operators ---
    ## --- section_g: (GMVector) calculating vector ---
    
    ## --- section_ma: creating class instances ---
    vecta -> :: GMVector ::
    : (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45) : unit = 10
    vectb -> :: GMVector ::
    : (xx,yy) = (3, 4) : (rr,th) = (5, 53.1301) : unit = 10
    vectbc -> :: GMVector ::
    : (xx,yy) = (3, 4) : (rr,th) = (5, 53.1301) : unit = 10
    vectb -> :: GMVector ::
    : (xx,yy) = (1, -1) : (rr,th) = (1.41421, -45) : unit = 10
    vectbc -> :: GMVector ::
    : (xx,yy) = (3, 4) : (rr,th) = (5, 53.1301) : unit = 10
    vectc -> :: GMVector ::
    : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349) : unit = 1
    vectc -> :: GMVector ::
    : (xx,yy) = (0.707107, 0.707107) : (rr,th) = (1, 45) : unit = 10
    
    ## --- section_mb: calculating unit vector and product ---
    vecta.unitvect(False) = array([0.70710678, 0.70710678])
    vecta.iprd(vectb) = 0.0, vecta.oprd(vectb) = -2.0
    vecta.tprd(vectb) = array([[ 1., -1.],
           [ 1., -1.]])
    vectb.unitvect(False) = array([ 0.70710678, -0.70710678])
    vectb.iprd(vecta) = 0.0, vectb.oprd(vecta) = 2.0
    vectb.tprd(vecta) = array([[ 1.,  1.],
           [-1., -1.]])
'''
