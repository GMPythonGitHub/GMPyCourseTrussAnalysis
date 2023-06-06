# gm_c06_01_point.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMPoint) class for point ***")
print("  *** class GMVector is inherited ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMPoint) importing items from module ---")
from numpy import (ndarray, sqrt, dot as dott)
from gm_c06_00_vector import GMVector

# -----------------------------------------------------------------------------
print("## --- section_a: (GMPoint) declaring class ---")
class GMPoint(GMVector):  # inheriting GMVector
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMPoint) initializing class instance ---")
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None,
            unt: float = 1., cnv: bool = True):
        super().__init__(xxyy, rrth, unt=unt, cnv=cnv)  # calling supper class initialization

    print("## --- section_c: (GMPoint) setting and getting functions ---")
    ## setting functions
    def set_point(self,
            xxyy: tuple = None, rrth: tuple = None,
            unt: float = None, cnv: bool = True) -> None:
        self.set_vector(xxyy=xxyy, rrth=rrth, unt=unt, cnv=cnv)

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
    def vect_2pint(self, pint: object, cnv: bool = True) -> ndarray:
        return pint.xxyy(cnv) - self.xxyy(cnv)
    def dist_2pint(self, pint: object, cnv: bool = True) -> float:
        vect = self.vect_2pint(pint,cnv=cnv)
        return sqrt(dott(vect,vect))
    def unitvect_2pint(self, pint: object, cnv: bool = True) -> ndarray:
        vect = self.vect_2pint(pint,cnv=cnv)
        dist = self.dist_2pint(pint,cnv=cnv)
        return vect / dist

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    pinta = GMPoint(xxyy=(1., 2.), unt=10.); pinta.prtcls('pinta -> ')
    pintb = GMPoint(xxyy=(2., 1.), unt=10.); pintb.prtcls('pintb -> ')
    pintc = GMPoint(pintb); pintc.prtcls('pintc -> ')
    pintc.set_point(rrth=(1,45), unt=10); pintc.prtcls('pintc -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: calculating unit distance and unit vector ---")
    print(f'{pinta.unitvect() = }')  # GMVecto
    print(f'{pintb.unitvect() = }')  # GMVecto
    print(f'{pinta.vect_2pint(pintb) = }')
    print(f'{pintb.vect_2pint(pinta) = }')
    print(f'{pinta.dist_2pint(pintb) = }')
    print(f'{pintb.dist_2pint(pinta) = }')
    print(f'{pinta.unitvect_2pint(pintb, cnv=False) = }')
    print(f'{pintb.unitvect_2pint(pinta, cnv=False) = }')

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
    ## --- section_f: (GMVector) overloading arithmetic operators ---
    ## --- section_g: (GMVector) calculating unit vector and products ---
    ## --- section_a: (GMPoint) declaring class ---
    
    ## --- section_b: (GMPoint) initializing class instance ---
    ## --- section_c: (GMPoint) string function for print() ---
    ## --- section_d: (GMPoint) calculating relation with point ---
    
    ## --- section_ma: creating class instances ---
    pinta -> :: GMPrint ::
      (super) GMVector : (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45)
    pintb -> :: GMPrint ::
      (super) GMVector : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
    pintc -> :: GMPrint ::
      (super) GMVector : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
    pintc -> :: GMPrint ::
      (super) GMVector : (xx,yy) = (0.707107, 0.707107) : (rr,th) = (1, 45) : unt = 10
    
    ## --- section_mb: operating points ---
    (pinta + pintb).xxyy() = array([2., 3.])
    (pinta - pintb).xxyy() = array([ 0., -1.])
    (pinta * pintb).xxyy() = array([1., 2.])
    (pinta / pintb).xxyy() = array([1. , 0.5])
    
    ## --- section_mc: calculating unit distance and unit vector ---
    pinta.unitvect() = array([0.70710678, 0.70710678])
    pintb.unitvect() = array([0.4472136 , 0.89442719])
    pinta.dottprod(pintb) = 3.0
    pinta.crosprod(pintb) = array(1.)
    pinta.dist_2pint(pintb) = 1.0
    pintb.dist_2pint(pinta) = 1.0
    pinta.unitvect_2pint(pintb) = array([0., 1.])
    pintb.unitvect_2pint(pinta) = array([ 0., -1.])
    '''
