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
            post: tuple = (1., 1.), fixc: tuple = (False, False), locn: tuple = (0, 1),
            disp: tuple = (0., 0.), exfc: tuple = (0., 0.) ):
        super().__init__(xxyy=post, unt=1., cnv=True)
        self.__fixc, self.__locn = None, None
        self._disp = GMVector(xxyy=disp, unt=1e-3, cnv=True)
        self._exfc = GMVector(xxyy=exfc, unt=1e+3, cnv=True)
        self.set_truss_node(
            post=post, fixc=fixc, locn=locn, disp=disp, exfc=exfc )
        pass

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMTrussNodeAdvanced) setting and getting functions ---")
    ## setting functions
    def set_truss_node(self,
            post: tuple = None, post_rrth: tuple = None,
            fixc: tuple = None, locn: tuple = None,
            disp: tuple = None, disp_rrth: tuple = None,
            exfc: tuple = None, exfc_rrth: tuple = None ) -> None:
        if post is not None: self.set_xxyy(post)
        if post_rrth is not None: self.set_rrth(post_rrth)
        if fixc is not None: self.__fixc = array(fixc)
        if locn is not None: self.__locn = array(locn)
        if disp is not None: self._disp.set_xxyy(disp)
        if disp_rrth is not None: self._disp.set_rrth(disp_rrth)
        if exfc is not None: self._exfc.set_xxyy(exfc)
        if exfc_rrth is not None: self._exfc.set_rrth(exfc_rrth)

    ## getting functions
    def post_xxyy(self, cnv: bool = True) -> ndarray: return self.xxyy(cnv=cnv)
    def post_rrth(self, cnv: bool = True) -> ndarray: return self.rrth(cnv=cnv)
    def fixc(self) -> ndarray: return self.__fixc
    def locn(self) -> ndarray: return self.__locn

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMTrussNodeAdvanced) string function for print() ---")
    def __str__(self) -> str:
        return super().__str__()
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMPrint ::\n'
            + '  post: GMPoint:' + self.__str__() + '\n'
            + '  fixc: ndarray:' + f'{self.__fixc} \n'
            + '  locn: ndarray:' + f'{self.__locn} \n'
            + '  disp: GMVector:' + self._disp.__str__() + '\n'
            + '  exfc: GMVector:' + self._exfc.__str__() + '')

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    nodea = GMTrussNodeAdvanced(post=(1., 2.))
    nodeb = GMTrussNodeAdvanced(post=(2., 1.))
    nodea.prtcls('nodea -> ')
    nodeb.prtcls('nodeb -> ')

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
    ## --- section_c: (GMPoint) string function for print() ---
    ## --- section_d: (GMPoint) calculating point ---

    ## --- section_a: (GMTrussNodeAdvanced) declaring class ---
    ## --- section_b: (GMTrussNodeAdvanced) initializing class instance ---
    ## --- section_c: (GMTrussNodeAdvanced) setting and getting functions ---
    ## --- section_d: (GMTrussNodeAdvanced) string function for print() ---
    
    ## --- section_ma: creating class instances ---
    nodea -> :: GMPrint ::
      post: GMPoint:: (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[0 1] 
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    nodeb -> :: GMPrint ::
      post: GMPoint:: (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[0 1] 
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    '''
