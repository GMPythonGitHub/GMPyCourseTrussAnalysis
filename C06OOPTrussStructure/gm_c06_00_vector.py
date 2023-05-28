## gm_c06_00_vector.py: coded by Kinya MIURA 230523
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
            xxyy: tuple = (1., 1.), rrth: tuple = None,
            unt: float = 1., cnv: bool = True):
        self.__xxyy, self.__unt = None, None
        if isinstance (xxyy, GMVector):
            self.set_vector(xxyy=xxyy.xxyy(False), rrth=None, unt=xxyy.unt(), cnv=False)
        else:
            self.set_vector(xxyy, rrth, unt=unt, cnv=cnv)

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMVector) setting and getting functions ---")
    ## setting functions
    def set_xxyy(self, xxyy: tuple, cnv: bool = True) -> None:
        self.__xxyy = array(xxyy)
        if cnv: self.__xxyy = self.__xxyy * self.__unt
    def set_rrth(self, rrth: tuple, cnv: bool = True) -> None:
        if len(rrth) == 2:
            rr, th = rrth
            if cnv: rr, th = rr * self.__unt, d2r(th)
            self.__xxyy = rr * array((cos(th), sin(th)))
        elif len(rrth) == 3:
            rr, th, ph = rrth
            if cnv: rr, th, ph = rr * self.__unt, d2r(th), d2r(ph)
            self.__xxyy = rr * array((sin(ph)*cos(th), sin(ph)*sin(th), cos(ph)))
        else:
            self.__xxyy = None
    def set_vector(self,
            xxyy: tuple = None, rrth: tuple = None,
            unt: float = None, cnv: bool = True) -> None:
        if unt is not None: self.__unt = unt
        if rrth is not None:
            self.set_rrth(rrth, cnv=cnv)
        elif xxyy is not None:
            self.set_xxyy(xxyy, cnv=cnv)

    ## getting functions
    def unt(self):
        return self.__unt
    def xxyy(self, cnv: bool = True) -> ndarray:
        if cnv: return self.__xxyy / self.__unt
        else: return self.__xxyy
    def rrth(self, cnv: bool = True) -> ndarray:
        rr = sqrt(dott(self.__xxyy,self.__xxyy))
        if len(self.__xxyy) == 2:
            xx, yy = self.__xxyy
            th = atan2(yy, xx)
            if cnv: rr, th = rr / self.__unt, r2d(th)
            return array((rr, th))
        elif len(self.__xxyy) == 3:
            xx, yy, zz = self.__xxyy
            th, ph = atan2(yy,xx), acos(zz/rr)
            if cnv: rr, th, ph = rr / self.__unt, r2d(th), r2d(ph)
            return array((rr, th, ph))
        else: return None

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMVector) string function for print() ---")
    def __str__(self) -> str:
        if (len(self.__xxyy)) == 2:
            xx, yy = self.xxyy(); rr, th = self.rrth(cnv=True); unt = self.__unt
            return (
                f': (xx,yy) = ({xx:g}, {yy:g}) '
                f': (rr,th) = ({rr:g}, {th:g}) '
                f': unt = {unt:g}' )
        elif len(self.__xxyy) == 3:
            xx, yy, zz = self.xxyy(); rr, th, ph = self.rrth(cnv=True); unt = self.__unt
            return (
                f': (xx,yy,zz) = ({xx:g}, {yy:g}, {zz:g}) '
                f': (rr,th,ph) = ({rr:g}, {th:g}, {ph:g}) '
                f': unt = {unt:g}')
        else: return None
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMVector ::\n'
            + self.__str__() )

    # -----------------------------------------------------------------------------
    print("## --- section_e: (GMVector) operating vectors ---")
    def cnvvect(self, vect: object = None) -> ndarray:
        if type(vect) in (int, float, complex): return vect
        elif type(vect) in (list, tuple, ndarray): return array(vect)
        else: return vect.xxyy(cnv=False)
    def add(self, vect: object = None) -> None:
        self.__xxyy += self.cnvvect(vect)
    def sub(self, vect: object = None) -> None:
        self.__xxyy -= self.cnvvect(vect)
    def mul(self, vect: object = None) -> None:
        self.__xxyy *= self.cnvvect(vect)
    def div(self, vect: object = None) -> None:
        self.__xxyy /= self.cnvvect(vect)

    # -----------------------------------------------------------------------------
    print("## --- section_f: (GMVector) calculating vector ---")
    def unitvect(self, cnv: bool = True) -> ndarray:
        rr, *_ = self.rrth(False)
        unitvect = self.__xxyy / rr if rr > 0. else array((1., 0.))
        if cnv: return unitvect / self.__unt
        else: return unitvect
    def dottprod(self, vect: object, cnv: bool = True) -> ndarray:  # dot product (inner)
        dottprod = dott(self.__xxyy, vect.xxyy(False))
        if cnv: return dottprod / self.__unt / self.__unt
        else: return dottprod
    def crosprod(self, vect: object, cnv: bool = True) -> ndarray:  # cross product (outer)
        crosprod = cros(self.__xxyy, vect.xxyy(False))
        if cnv: return crosprod / self.__unt / self.__unt
        else: return crosprod
    def tnsrprod(self, vect: object, cnv: bool = True) -> ndarray:  # tensor product
        tnsrprod = tnsr(self.__xxyy, vect.xxyy(False), axes=0)
        if cnv: return tnsrprod / self.__unt / self.__unt
        else: return tnsrprod

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    vecta = GMVector(xxyy=(1., 1.), unt=10.); vecta.prtcls('vecta -> ')
    vectb = GMVector(xxyy=(3., 4.), unt=10.); vectb.prtcls('vectb -> ')
    vectbc = GMVector(vectb); vectbc.prtcls('vectbc -> ')
    vectc = GMVector(xxyy=(1.,2.)); vectc.prtcls('vectc -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: calculating unit vector and product ---")
    print(f'{vecta.unitvect(False) = }')
    print(f'{vecta.dottprod(vectb) = }, {vecta.crosprod(vectb) = }')
    print(f'{vecta.tnsrprod(vectb) = }')
    print(f'{vectb.unitvect(False) = }')
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
