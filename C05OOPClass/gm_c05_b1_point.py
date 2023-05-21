# gm_c05_b1_point.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMPoint) class for point ***")
print("  *** class GMVector is inherited ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMPoint) importing items from module ---")
from numpy import (ndarray)
from gm_c05_b0_vector import GMVector

# -----------------------------------------------------------------------------
print("## --- section_a: (GMPoint) declaring class ---")
class GMPoint(GMVector):  # inheriting GMVector
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMPoint) initializing class instance ---")
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        if isinstance (xxyy, (GMVector, GMPoint)): xxyy = xxyy.xxyy(); rrth = None
        super().__init__(xxyy, rrth, cnv=cnv)  # calling supper class initialization

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMPoint) string function for print() ---")
    def __str__(self) -> str:
        return super().__str__()
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMPrint ::\n'
            + '  (sup) GMVector', self.__str__() )

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMPoint) calculating point ---")
    def dist_2pint(self, pint: object) -> float:
        rr, *_ = (pint - self).rrth(); return rr
    def unitvect_2pint(self, pint: object) -> ndarray:
        return (pint - self).unitvect()

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    pinta = GMPoint(xxyy=(1., 1.)); pinta.prtcls('pinta -> ')
    pintb = GMPoint(xxyy=(1., 2.)); pintb.prtcls('pintb -> ')
    pintc = GMPoint(pintb); pintc.prtcls('pintc -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: operating points ---")
    print(f'{(pinta + pintb).xxyy() = }')
    print(f'{(pinta - pintb).xxyy() = }')
    print(f'{(pinta * pintb).xxyy() = }')
    print(f'{(pinta / pintb).xxyy() = }')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mc: calculating unit distance and unit vector ---")
    pinta.set_xxyy((1., 1.))
    pintb.set_xxyy((2., 1.))
    print(f'{pinta.unitvect() = }')
    print(f'{pintb.unitvect() = }')
    print(f'{pinta.dottprod(pintb) = }')
    print(f'{pinta.crosprod(pintb) = }')
    print(f'{pinta.dist_2pint(pintb) = }')
    print(f'{pintb.dist_2pint(pinta) = }')
    print(f'{pinta.unitvect_2pint(pintb) = }')
    print(f'{pintb.unitvect_2pint(pinta) = }')

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
      (sup) GMVector : (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45)
    pintb -> :: GMPrint ::
      (sup) GMVector : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
    pintc -> :: GMPrint ::
      (sup) GMVector : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
    
    ## --- section_mb: operating points ---
    (pinta + pintb).xxyy() = array([2., 3.])
    (pinta - pintb).xxyy() = array([ 0., -1.])
    (pinta * pintb).xxyy() = array([1., 2.])
    (pinta / pintb).xxyy() = array([1. , 0.5])
    
    ## --- section_mc: calculating unit distance and unit vector ---
    pinta.unitvect() = array([0.70710678, 0.70710678])
    pintb.unitvect() = array([0.89442719, 0.4472136 ])
    pinta.dottprod(pintb) = 3.0
    pinta.crosprod(pintb) = array(-1.)
    pinta.dist_2pint(pintb) = 1.0
    pintb.dist_2pint(pinta) = 1.0
    pinta.unitvect_2pint(pintb) = array([1., 0.])
    pintb.unitvect_2pint(pinta) = array([-1.,  0.])
    '''
