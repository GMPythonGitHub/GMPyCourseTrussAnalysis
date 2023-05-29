# gm_c06_OOP_TrussStructure_Advanced_A_truss_node.py: coded by Kinya MIURA 230524
# -----------------------------------------------------------------------------
print("\n*** (GMTrussNodeAdvanced) class for truss node ***")
print("  *** class GMPoint is inherited; class GMVector is embedded as vect ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMTrussNodeAdvanced) importing items from module ---")
from numpy import (
    ndarray, array, dot as dott, cross as cros, tensordot as tnsr )
from gm_c06_01_point import (GMPoint, GMVector)

# -----------------------------------------------------------------------------
print("## --- section_a: (GMTrussNodeAdvanced) declaring class ---")
class GMTrussNodeAdvanced(GMPoint):  # inheriting GMPoint
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMTrussNodeAdvanced) initializing class instance ---")
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None,
            unt: float = 1., cnv: bool = True,
            fixc: tuple = (False, False), locn: tuple = (0, 1) ):
        super().__init__(xxyy=xxyy, rrth=rrth, unt=unt, cnv=True)
        self.__fixc, self.__locn = None, None
        self._disp = GMVector(xxyy=(0., 0.), unt=1e-3)
        self._exfc = GMVector(xxyy=(0., 0.), unt=1e+3)
        self._rafc = GMVector(xxyy=(0., 0.), unt=1e+3)
        self.set_truss_node(
            xxyy=xxyy, rrth=rrth, unt=unt, cnv=cnv, fixc=fixc, locn=locn )

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMTrussNodeAdvanced) setting and getting functions ---")
    ## setting functions
    def set_truss_node(self,
            xxyy: tuple = None, rrth: tuple = None,
            unt: float = None, cnv: bool = True,
            fixc: tuple = None, locn: tuple = None ) -> None:
        if unt is not None: self.set_point(unt=unt)
        if xxyy is not None: self.set_xxyy(xxyy, cnv=cnv)
        if rrth is not None: self.set_rrth(rrth, cnv=cnv)
        if fixc is not None: self.__fixc = array(fixc)
        if locn is not None: self.__locn = array(locn)

    ## getting functions
    def fixc(self) -> ndarray: return self.__fixc
    def locn(self) -> ndarray: return self.__locn

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMTrussNodeAdvanced) string function for print() ---")
    def __str__(self) -> str:
        st  = super().__str__() + '\n'
        st += (
            '  fixc: ndarray:' + f'{self.__fixc} \n'
            '  locn: ndarray:' + f'{self.__locn}' )
        return st
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMTrussNodeAdvanced ::\n'
            + '  (super) GMPoint:' + self.__str__() + '\n'
            + '  disp: GMVector:' + self._disp.__str__() + '\n'
            + '  exfc: GMVector:' + self._exfc.__str__() + '\n'
            + '  rafc: GMVector:' + self._rafc.__str__() + '')

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    node_a = GMTrussNodeAdvanced(xxyy=(1., 2.), fixc=(True, True), locn=(0, 1))
    node_a.prtcls('node_a -> ')
    node_b = GMTrussNodeAdvanced(xxyy=(2., 1.), fixc=(False, False), locn=(2, 3))
    node_b.prtcls('node_b -> ')

    node_c = GMTrussNodeAdvanced(xxyy=(2., 1.))
    node_c.set_truss_node(rrth=(1., 45.), fixc=(False,True), locn=(4, 5))
    node_c._disp.set_vector(xxyy=(1., 0.))
    node_c._exfc.set_vector(xxyy=(0., 1.))
    node_c._rafc.set_vector(xxyy=(0., 2.))
    node_c.prtcls('node_c -> ')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMTrussNodeAdvanced) class for truss node ***
      *** class GMPoint is inherited; class GMVector is embedded as vect ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMTrussNodeAdvanced) importing items from module ---
    
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
    ## --- section_f: (GMVector) calculating vector ---
    ## --- section_a: (GMPoint) declaring class ---
    ## --- section_b: (GMPoint) initializing class instance ---
    ## --- section_c: (GMPoint) setting and getting functions ---
    ## --- section_d: (GMPoint) string function for print() ---
    ## --- section_e: (GMPoint) calculating point ---
    ## --- section_a: (GMTrussNodeAdvanced) declaring class ---
    ## --- section_b: (GMTrussNodeAdvanced) initializing class instance ---
    ## --- section_c: (GMTrussNodeAdvanced) setting and getting functions ---
    ## --- section_d: (GMTrussNodeAdvanced) string function for print() ---
    
    ## --- section_ma: creating class instances ---
    node_a -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349) : unt = 1
      fixc: ndarray:[ True  True] 
      locn: ndarray:[0 1]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    node_b -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[2 3]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    node_c -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0.707107, 0.707107) : (rr,th) = (1, 45) : unt = 1
      fixc: ndarray:[False  True] 
      locn: ndarray:[4 5]
      disp: GMVector:: (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 2) : (rr,th) = (2, 90) : unt = 1000
    '''
