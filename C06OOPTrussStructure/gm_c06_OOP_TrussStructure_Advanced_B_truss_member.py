# gm_c06_OOP_TrussStructure_Advanced_B_truss_member.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMTrussMemberAdvanced) class for segment ***")
print("  *** class GMTrussNodeAdvanced is embedded as nodea and nodeb ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMTrussMemberAdvanced) importing items from module ---")
from numpy import (
    square, sqrt,
    ndarray, append, dot as dott, tensordot as tnsr )
from gm_c06_OOP_TrussStructure_Advanced_A_truss_node import (GMTrussNodeAdvanced)

# -----------------------------------------------------------------------------
print("## --- section_a: (GMTrussMemberAdvanced) declaring class ---")
class GMTrussMemberAdvanced():
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMTrussMemberAdvanced) initializing class instance ---")
    def __init__(self,
            nodea: GMTrussNodeAdvanced, nodeb: GMTrussNodeAdvanced,
            area: float = 10., yong: float = 205., cnv: bool = True ):
        self._nodea, self._nodeb = nodea, nodeb
        self.__area, self.__yong = 0., 0.
        self.__delt, self.__epsl, self.__sigm, self.__axfc = 0., 0., 0., 0.
        self.set_truss_member(area=area, yong=yong, cnv=cnv )

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMTrussMemberAdvanced) setting and getting functions ---")
    ## setting functions
    def set_truss_member(self,
            area: float = None, yong: float = None,
            delt: float = None, epsl: float = None,
            sigm: float = None, axfc: float = None,
            cnv: bool = True ) -> None:
        if area is not None:
            self.__area = area * 1e-4 if cnv else area  # (cm^2)
        if yong is not None:
            self.__yong = yong * 1e+9 if cnv else yong  # (kN/mm^2)
        if delt is not None:
            self.__delt = delt * 1e-3 if cnv else delt  # (mm)
        if epsl is not None:
            self.__epsl = epsl * 1e-3 if cnv else epsl  # (1/1000)
        if sigm is not None:
            self.__sigm = sigm * 1e+3 if cnv else sigm  # (kN/m^2)
        if axfc is not None:
            self.__sigm = axfc * 1e+3 if cnv else axfc  # (kN)

    ## getting functions
    def area(self, cnv: bool = True) -> float:
        return self.__area / 1e-4 if cnv else self.__area  # (cm^2)
    def yong(self, cnv: bool = True) -> float:
        return self.__yong / 1e+9 if cnv else self.__yong  # (kN/mm^2)
    def delt(self, cnv: bool = True) -> float:
        return self.__delt / 1e-3 if cnv else self.__delt  # (mm)
    def epsl(self, cnv: bool = True) -> float:
        return self.__epsl / 1e-3 if cnv else self.__epsl  # (1/1000)
    def sigm(self, cnv: bool = True) -> float:
        return self.__sigm / 1e+3 if cnv else self.__sigm  # (kN/m^2)
    def axfc(self, cnv: bool = True) -> float:
        return self.__axfc / 1e+3 if cnv else self.__axfc  # (kN)

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMTrussMemberAdvanced) string function for print() ---")
    def __str__(self) -> str:
        st = (
            f'area (cm^2) = {self.area():g}, yong (kN/mm^2) = {self.yong():g} \n'
            f'delt (mm) = {self.delt():g}, epsl (1/1000) = {self.epsl():g}, '
            f'sigm (kN/m^2) = {self.sigm():g}, axfc(kN) = {self.axfc():g} ' )
        return st
    def prtcls(self, idx: str = '') -> None:
        print(idx + ':: GMTrussMemberAdvanced ::')
        print(self.__str__())
        self._nodea.prtcls('nodea -> ')
        self._nodeb.prtcls('nodeb -> ')

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMTrussMemberAdvanced) calculating segment ---")
    def leng(self, cnv: bool = True) -> float:  # length
        leng = sqrt(sum(square(self._nodea.vect_2pint(self._nodeb))))
        if cnv: return leng / 1e0
        else: return leng
    def unitvect_na(self) -> ndarray:  # unit vector
        return self._nodeb.unitvect_2pint(self._nodea)
    def unitvect_nb(self) -> ndarray:  # unit vector
        return self._nodea.unitvect_2pint(self._nodeb)
    def unitvect(self) -> ndarray:  # unit vector
        return append(self.unitvect_na(),self.unitvect_nb())
    def locn(self) -> ndarray:  # list of location numbers
        return append(self._nodea.locn(), self._nodeb.locn())

    def buld_stif(self) -> ndarray:  # building stiffness matrix
        leng = self.leng(False)
        unitvect = self.unitvect()
        stif = ( tnsr(unitvect, unitvect, axes=0)
            * self.__yong * self.__area / leng )
        return stif
    def calc_strt(self) -> None:  # calculating stretch
        unitvect = self.unitvect()
        self.__delt = (
            + dott(self.unitvect_na(), self._nodea._disp.xxyy(False))
            + dott(self.unitvect_nb(), self._nodeb._disp.xxyy(False)) )
        self.__epsl = self.__delt / self.leng(False)
        self.__sigm = self.__epsl * self.__yong
        self.__axfc = self.__sigm * self.__area
        self._nodea._rafc.add(self.unitvect_na() * self.__axfc)
        self._nodeb._rafc.add(self.unitvect_nb() * self.__axfc)

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    node_a = GMTrussNodeAdvanced(xxyy=(0., 0.), fixc=(True, True), locn=(0, 1))
    node_b = GMTrussNodeAdvanced(xxyy=(0., 1.), fixc=(False, False), locn=(2, 3))
    node_c = GMTrussNodeAdvanced(xxyy=(1., 0.), fixc=(True, True), locn=(4, 5))

    memb_a = GMTrussMemberAdvanced(nodea=node_a, nodeb=node_b)
    memb_b = GMTrussMemberAdvanced(nodea=node_b, nodeb=node_c)

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: calculating truss member ---")
    node_b._disp.set_vector(xxyy=(1., 0.))
    print(f'{memb_a.unitvect() = }')
    print(f'{memb_a.locn() = }')
    print(f'{memb_a.buld_stif() = }')
    memb_a.calc_strt()
    print(f'{memb_b.unitvect() = }')
    print(f'{memb_b.locn() = }')
    print(f'{memb_b.buld_stif() = }')
    memb_b.calc_strt()
    memb_a.prtcls('memb_a -> ')
    print()
    memb_b.prtcls('memb_b -> ')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMTrussMemberAdvanced) class for segment ***
      *** class GMTrussNodeAdvanced is embedded as nodea and nodeb ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMTrussMemberAdvanced) importing items from module ---
    
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
    ## --- section_a: (GMTrussMemberAdvanced) declaring class ---
    ## --- section_b: (GMTrussMemberAdvanced) initializing class instance ---
    ## --- section_c: (GMTrussMemberAdvanced) setting and getting functions ---
    ## --- section_c: (GMTrussMemberAdvanced) string function for print() ---
    ## --- section_d: (GMTrussMemberAdvanced) calculating segment ---
    
    ## --- section_ma: creating class instances ---
    
    ## --- section_mb: calculating truss member ---
    memb_a.unitvect() = array([ 0., -1.,  0.,  1.])
    memb_a.locn() = array([0, 1, 2, 3])
    memb_a.buld_stif() = array([[ 0.00e+00,  0.00e+00,  0.00e+00,  0.00e+00],
           [ 0.00e+00,  2.05e+08,  0.00e+00, -2.05e+08],
           [ 0.00e+00,  0.00e+00,  0.00e+00,  0.00e+00],
           [ 0.00e+00, -2.05e+08,  0.00e+00,  2.05e+08]])
    memb_b.unitvect() = array([-0.70710678,  0.70710678,  0.70710678, -0.70710678])
    memb_b.locn() = array([2, 3, 4, 5])
    memb_b.buld_stif() = array([[ 72478445.0716211, -72478445.0716211, -72478445.0716211,
             72478445.0716211],
           [-72478445.0716211,  72478445.0716211,  72478445.0716211,
            -72478445.0716211],
           [-72478445.0716211,  72478445.0716211,  72478445.0716211,
            -72478445.0716211],
           [ 72478445.0716211, -72478445.0716211, -72478445.0716211,
             72478445.0716211]])
    memb_a -> :: GMTrussMemberAdvanced ::
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = 0, epsl (1/1000) = 0, sigm (kN/m^2) = 0, axfc(kN) = 0 
    nodea -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1
      fixc: ndarray:[ True  True] 
      locn: ndarray:[0 1]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    nodeb -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[2 3]
      disp: GMVector:: (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (72.4784, -72.4784) : (rr,th) = (102.5, -45) : unt = 1000
    
    memb_b -> :: GMTrussMemberAdvanced ::
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = -0.707107, epsl (1/1000) = -0.5, sigm (kN/m^2) = -102500, axfc(kN) = -102.5 
    nodea -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[2 3]
      disp: GMVector:: (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (72.4784, -72.4784) : (rr,th) = (102.5, -45) : unt = 1000
    nodeb -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unt = 1
      fixc: ndarray:[ True  True] 
      locn: ndarray:[4 5]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (-72.4784, 72.4784) : (rr,th) = (102.5, 135) : unt = 1000
    '''
