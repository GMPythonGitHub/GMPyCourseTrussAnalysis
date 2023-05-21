# gm_c05_c0_point_vector.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMPointVector) class for position vector ***")
print("  *** class GMPoint is inherited; class GMVector is embedded as vect ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMPointVector) importing items from module ---")
from numpy import (
    ndarray, array, dot as dott, cross as cros, tensordot as tnsr )
from gm_c05_b0_vector import GMVector
from gm_c05_b1_point import GMPoint

# -----------------------------------------------------------------------------
print("## --- section_a: (GMPointVector) declaring class ---")
class GMPointVector(GMPoint):  # inheriting GMPoint
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMPointVector) initializing class instance ---")
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True,
            vect: GMVector = GMVector()):
        super().__init__(xxyy, rrth, cnv=cnv)
        self._vect = vect

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMPointVector) string function for print() ---")
    def __str__(self) -> str:
        return super().__str__()
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMPrint ::\n'
            + '  (sup) GMVector:' + self.__str__() + '\n'
            + '  vect: GMVector:' + self._vect.__str__())

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMPoint) calculating position vector ---")
    def tipvect(self) -> ndarray:
        return self.xxyy() + self._vect.xxyy()
    def dottprod_pint2vect(self) -> ndarray:
        return dott(self.xxyy(),self._vect.xxyy())
    def crosprod_pint2vect(self) -> ndarray:
        return cros(self.xxyy(), self._vect.xxyy())


# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    pintvecta = GMPointVector(xxyy=(1., 2.), vect=GMVector((3., 1.)))
    pintvecta.prtcls('pintvecta -> ')
    pintvectb = GMPointVector(xxyy=(2., 1.), vect=GMVector((1., 3.)))
    pintvectb.prtcls('pintvectb -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: calculating tip vectors and products ---")
    pintvecta.set_xxyy((1., 2.)); pintvecta._vect.set_xxyy((2., -1.))
    pintvecta.prtcls('pintvecta -> ')
    pintvectb.set_xxyy((2., 1.)); pintvectb._vect.set_xxyy((-1., 2.))
    pintvecta.prtcls('pintvectb -> ')
    print(f'{pintvecta.tipvect() = }')
    print(f'{pintvectb.tipvect() = }')
    print(f'{pintvecta.dottprod_pint2vect() = }')
    print(f'{pintvectb.dottprod_pint2vect() = }')
    print(f'{pintvecta.crosprod_pint2vect() = }')
    print(f'{pintvectb.crosprod_pint2vect() = }')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMPointVector) class for position vector ***
      *** class GMPoint is inherited; class GMVector is embedded as vect ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMPointVector) importing items from module ---
    
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
    
    *** (GMPoint) class for point ***
      *** class GMVector is inherited ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMPoint) importing items from module ---
    ## --- section_a: (GMPoint) declaring class ---
    ## --- section_b: (GMPoint) initializing class instance ---
    ## --- section_c: (GMPoint) string function for print() ---
    ## --- section_d: (GMPoint) calculating relation with point ---

    ## --- section_a: (GMPointVector) declaring class ---
    ## --- section_b: (GMPointVector) initializing class instance ---
    ## --- section_c: (GMPointVector) string function for print() ---
    ## --- section_d: (GMPoint) calculating behavior of position vector ---
    
    ## --- section_ma: creating class instances ---
    pintvecta -> :: GMPrint ::
      (sup) GMVector:: (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
      vect: GMVector:: (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349)
    pintvectb -> :: GMPrint ::
      (sup) GMVector:: (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651)
      vect: GMVector:: (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651)
    
    ## --- section_mb: calculating unit vectors and products ---
    pintvecta -> :: GMPrint ::
      (sup) GMVector:: (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
      vect: GMVector:: (xx,yy) = (2, -1) : (rr,th) = (2.23607, -26.5651)
    pintvectb -> :: GMPrint ::
      (sup) GMVector:: (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
      vect: GMVector:: (xx,yy) = (2, -1) : (rr,th) = (2.23607, -26.5651)
    pintvecta.tipvect() = array([3., 1.])
    pintvectb.tipvect() = array([1., 3.])
    pintvecta.dottprod_pint2vect() = 0.0
    pintvectb.dottprod_pint2vect() = 0.0
    pintvecta.crosprod_pint2vect() = array(-5.)
    pintvectb.crosprod_pint2vect() = array(5.)
    '''
