# gm_cta05_Class_d1_point.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMPoint) class for point ***")
print("  *** class GMVector is inherited ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMPoint) importing items from module ---")
from numpy import (ndarray, sqrt, dot as iprd)
import copy
from gm_cta05_Class_d0_vector import GMVector

# -----------------------------------------------------------------------------
print("## --- section_a: (GMPoint) declaring class ---")
class GMPoint(GMVector):  # inheriting GMVector
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMPoint) initializing class instance ---")
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None,
            unit: float = 1., cnv: bool = True):
        super().__init__(xxyy, rrth, unit=unit, cnv=cnv)
        # calling supper class initialization

    print("## --- section_c: (GMPoint) setting and getting functions ---")
    ## setting functions
    def set_point(self,
            xxyy: tuple = None, rrth: tuple = None,
            unit: float = None, cnv: bool = True) -> None:
        self.set_vector(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv)

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMPoint) string function for print() ---")
    def __str__(self) -> str:
        return super().__str__()
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMPoint ::\n'
            + '  (super) GMVector', self.__str__() )

    # -----------------------------------------------------------------------------
    print("## --- section_e: (GMPoint) calculating point ---")
    def copy(self) -> object:
        return copy.deepcopy(self)
    def vect2pint(self, pint: object, cnv: bool = True) -> ndarray:
        return pint.xxyy(cnv) - self.xxyy(cnv)
    def dist2pint(self, pint: object, cnv: bool = True) -> float:
        vect = self.vect2pint(pint,cnv=cnv)
        return sqrt(iprd(vect,vect))
    def unitvect2pint(self, pint: object, cnv: bool = True) -> ndarray:
        vect = self.vect2pint(pint,cnv=cnv)
        dist = self.dist2pint(pint,cnv=cnv)
        return vect / dist

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    pinta = GMPoint(xxyy=(1., 2.), unit=10.); pinta.prtcls('pinta -> ')
    pintb = GMPoint(xxyy=(2., 1.), unit=10.); pintb.prtcls('pintb -> ')
    pintcb = pintb.copy(); pintcb.prtcls('pintcb -> ')
    pintcb.set_point(rrth=(1,45), unit=10); pintcb.prtcls('pintcb -> ')
    pintb.prtcls('pintb -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: calculating unit distance and unit vector ---")
    print(f'{pinta.unitvect() = }')  # GMVecto
    print(f'{pintb.unitvect() = }')  # GMVecto
    print(f'{pinta.vect2pint(pintb) = }')
    print(f'{pintb.vect2pint(pinta) = }')
    print(f'{pinta.dist2pint(pintb) = }')
    print(f'{pintb.dist2pint(pinta) = }')
    print(f'{pinta.unitvect2pint(pintb, cnv=False) = }')
    print(f'{pintb.unitvect2pint(pinta, cnv=False) = }')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mc: calculating inner, outer, and tensor products ---")
    print(f'{pinta.iprd(pintb) = }, {pintb.iprd(pinta) = }')
    print(f'{pinta.oprd(pintb) = }, {pintb.oprd(pinta) = }')
    print(f'{pinta.tprd(pintb) = }, \n{pintb.tprd(pinta) = }')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMPoint) class for point ***
      *** class GMVector is inherited ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMPoint) importing items from module ---
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
    ## --- section_a: (GMPoint) declaring class ---
    ## --- section_b: (GMPoint) initializing class instance ---
    ## --- section_c: (GMPoint) setting and getting functions ---
    ## --- section_d: (GMPoint) string function for print() ---
    ## --- section_e: (GMPoint) calculating point ---
    
    ## --- section_ma: creating class instances ---
    pinta -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349) : unit = 10
    pintb -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unit = 10
    pintcb -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unit = 10
    pintcb -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (0.707107, 0.707107) : (rr,th) = (1, 45) : unit = 10
    pintb -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unit = 10
      
    ## --- section_mb: calculating unit distance and unit vector ---
    pinta.unitvect() = array([0.04472136, 0.08944272])
    pintb.unitvect() = array([0.08944272, 0.04472136])
    pinta.vect2pint(pintb) = array([ 1., -1.])
    pintb.vect2pint(pinta) = array([-1.,  1.])
    pinta.dist2pint(pintb) = 1.4142135623730951
    pintb.dist2pint(pinta) = 1.4142135623730951
    pinta.unitvect2pint(pintb, cnv=False) = array([ 0.70710678, -0.70710678])
    pintb.unitvect2pint(pinta, cnv=False) = array([-0.70710678,  0.70710678])
    
    ## --- section_mc: calculating inner, outer, and tensor products ---
    pinta.iprd(pintb) = 4.0, pintb.iprd(pinta) = 4.0
    pinta.oprd(pintb) = -3.0, pintb.oprd(pinta) = 3.0
    pinta.tprd(pintb) = array([[2., 1.],
           [4., 2.]]), 
    pintb.tprd(pinta) = array([[2., 4.],
           [1., 2.]])
    '''
