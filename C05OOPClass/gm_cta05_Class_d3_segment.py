# gm_cta05_Class_d3_segment.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMSegment) class for segment ***")
print("  *** class GMPoint is embedded as pinta and pintb ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMSegment) importing items from module ---")
from numpy import (
    ndarray, array, dot as iprd, cross as oprd, tensordot as tprd )
import copy
from gm_cta05_Class_d1_point import GMPoint

# -----------------------------------------------------------------------------
print("## --- section_a: (GMSegment) declaring class ---")
class GMSegment():
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMSegment) initializing class instance ---")
    def __init__(self,
            pinta: GMPoint = GMPoint(), pintb: GMPoint = GMPoint() ):
        self._pinta, self._pintb = pinta, pintb

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMSegment) string function for print() ---")
    def __str__(self) -> str:
        return ''
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMSegment ::\n'
            + '  pinta: GMPoint:' + self._pinta.__str__() + '\n'
            + '  pintb: GMPoint:' + self._pintb.__str__())

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMSegment) calculating segment ---")
    def copy(self) -> object:
        return copy.deepcopy(self)
    def vect_a2b(self) -> ndarray:
        return self._pinta.vect2pint(self._pintb)
    def vect_b2a(self) -> ndarray:
        return self._pintb.vect2pint(self._pinta)
    def leng(self) -> float:
        return self._pinta.dist2pint(self._pintb)
    def unitvect_a2b(self) -> ndarray:
        return self._pinta.unitvect2pint(self._pintb)
    def unitvect_b2a(self) -> ndarray:
        return self._pintb.unitvect2pint(self._pinta)
    def iprd(self) -> float:
        self._pinta.iprd(self._pintb)
    def oprd(self) -> ndarray:
        return self._pinta.oprd(self._pintb)
    def tprd(self) -> ndarray:
        return self._pinta.tprd(self._pintb)
    def prjx(self) -> float:
        pintaxx, pintayy = self._pinta.xxyy()
        pintbxx, pintbyy = self._pintb.xxyy()
        return (pintbxx - pintaxx) * (pintayy + pintbyy) / 2
    def prjy(self) -> float:
        pintaxx, pintayy = self._pinta.xxyy()
        pintbxx, pintbyy = self._pintb.xxyy()
        return (pintayy - pintbyy) * (pintbxx + pintaxx) / 2

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instances ---")
    pinta = GMPoint(xxyy=(1., 2.), unit=10.); pinta.prtcls('pinta -> ')
    pintb = GMPoint(xxyy=(2., 1.), unit=10.); pintb.prtcls('pintb -> ')
    segm = GMSegment(pinta=pinta, pintb=pintb); segm.prtcls('segm -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: calculating segment properties ---")
    print(f'{segm.vect_a2b() = }')
    print(f'{segm.vect_b2a() = }')
    print(f'{segm.leng() = }')
    print(f'{segm.unitvect_a2b() = }')
    print(f'{segm.unitvect_b2a() = }')

    # -----------------------------------------------------------------------------
    print("\n## --- section_mc: calculating triangle ---")
    pinta = GMPoint(xxyy=(1., 3.)); print('pinta: ', pinta)
    pintb = GMPoint(xxyy=(3., 1.)); print('pintb: ', pintb)
    pintc = GMPoint(xxyy=(1., 1.)); print('pintc: ', pintc)
    segma = GMSegment(pinta=pintb, pintb=pintc); segma.prtcls('segma -> ')
    segmb = GMSegment(pinta=pintc, pintb=pinta); segmb.prtcls('segmb -> ')
    segmc = GMSegment(pinta=pinta, pintb=pintb); segmc.prtcls('segmc -> ')
    print(f'{segma.iprd() = }, {segmb.iprd() = }, {segmc.iprd() = }')
    print(f'{segma.oprd() = }, {segmb.oprd() = }, {segmc.oprd() = }')
    print(f'{segma.tprd() = }, \n{segmb.tprd() = }, \n{segmc.tprd() = }')
    print(f'{segma.prjx() = }, {segmb.prjx() = }, {segmc.prjx() = }')
    print(f'{segma.prjy() = }, {segmb.prjy() = }, {segmc.prjy() = }')
    gravctr = (pinta.xxyy() + pintb.xxyy() + pintc.xxyy()) / 3
    print(f'{gravctr = }')

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
    ## --- section_a: (GMSegment) declaring class ---
    ## --- section_b: (GMSegment) initializing class instance ---
    ## --- section_c: (GMSegment) string function for print() ---
    ## --- section_d: (GMSegment) calculating segment ---
    ## --- section_ma: creating class instances ---
    pinta -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349) : unit = 10
    pintb -> :: GMPoint ::
      (super) GMVector : (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unit = 10
    segm -> :: GMSegment ::
      pinta: GMPoint:: (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349) : unit = 10
      pintb: GMPoint:: (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651) : unit = 10
    ## --- section_mb: calculating segment properties ---
    segm.vect_a2b() = array([ 1., -1.])
    segm.vect_b2a() = array([-1.,  1.])
    segm.leng() = 1.4142135623730951
    segm.unitvect_a2b() = array([ 0.70710678, -0.70710678])
    segm.unitvect_b2a() = array([-0.70710678,  0.70710678])
    ## --- section_mc: calculating triangle ---
    pinta:  : (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651) : unit = 1
    pintb:  : (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349) : unit = 1
    pintc:  : (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45) : unit = 1
    segma -> :: GMSegment ::
      pinta: GMPoint:: (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349) : unit = 1
      pintb: GMPoint:: (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45) : unit = 1
    segmb -> :: GMSegment ::
      pinta: GMPoint:: (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45) : unit = 1
      pintb: GMPoint:: (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651) : unit = 1
    segmc -> :: GMSegment ::
      pinta: GMPoint:: (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651) : unit = 1
      pintb: GMPoint:: (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349) : unit = 1
    segma.iprd() = None, segmb.iprd() = None, segmc.iprd() = None
    segma.oprd() = 2.0, segmb.oprd() = 2.0, segmc.oprd() = -8.0
    segma.tprd() = array([[3., 3.],
           [1., 1.]]), 
    segmb.tprd() = array([[1., 3.],
           [1., 3.]]), 
    segmc.tprd() = array([[3., 1.],
           [9., 3.]])
    segma.prjx() = -2.0, segmb.prjx() = 0.0, segmc.prjx() = 4.0
    segma.prjy() = 0.0, segmb.prjy() = -2.0, segmc.prjy() = 4.0
    gravctr = array([1.66666667, 1.66666667])
    '''
