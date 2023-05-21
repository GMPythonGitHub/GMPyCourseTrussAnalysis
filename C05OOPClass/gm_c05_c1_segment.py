# gm_c05_c1_segment.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print("\n*** (GMSegment) class for segment ***")
print("  *** class GMPoint is embedded as pinta and pintb ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMSegment) importing items from module ---")
from numpy import (
    ndarray, array, dot as dott, cross as cros, tensordot as tnsr )
from gm_c05_b1_point import GMPoint

# -----------------------------------------------------------------------------
print("## --- section_a: (GMSegment) declaring class ---")
class GMSegment():
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMSegment) initializing class instance ---")
    def __init__(self, pinta: GMPoint = GMPoint(), pintb: GMPoint = GMPoint()):
        self._pinta, self._pintb = pinta, pintb

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMSegment) string function for print() ---")
    def __str__(self) -> str:
        return ''
    def prtcls(self, idx: str = '') -> None:
        print(
            idx + ':: GMSegment ::\n'
            + '  pnta: GMPoint:' + self._pinta.__str__() + '\n'
            + '  pntb: GMPoint:' + self._pintb.__str__())

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMSegment) calculating segment ---")
    def leng(self) -> float:
        return self._pinta.dist_2pint(self._pintb)
    def unitvect_pa2pb(self) -> ndarray:
        return self._pinta.unitvect_2pint(self._pintb)
    def unitvect_pb2pa(self) -> ndarray:
        return self._pintb.unitvect_2pint(self._pinta)
    def dottprod_pa2pb(self) -> ndarray:
        return self._pinta.dottprod(self._pintb)
    def dottprod_pb2pa(self) -> ndarray:
        return self._pintb.dottprod(self._pintb)
    def crosprod_pa2pb(self) -> ndarray:
        return self._pinta.crosprod(self._pintb)
    def crosprod_pb2pa(self) -> ndarray:
        return self._pintb.crosprod(self._pinta)

    def projxx_pa2pb(self) -> float:
        pintaxx, pintayy = self._pinta.xxyy(); pintbxx, pintbyy = self._pintb.xxyy()
        return (pintbxx + pintaxx) * (pintbyy - pintayy) / 2
    def projxx_pb2pa(self) -> float:
        pintaxx, pintayy = self._pinta.xxyy(); pintbxx, pintbyy = self._pintb.xxyy()
        return (pintaxx + pintbxx) * (pintayy - pintbyy) / 2
    def projyy_pa2pb(self) -> float:
        pintaxx, pintayy = self._pinta.xxyy(); pintbxx, pintbyy = self._pintb.xxyy()
        return (pintbyy + pintayy) * (pintbxx - pintaxx) / 2
    def projyy_pb2pa(self) -> float:
        pintaxx, pintayy = self._pinta.xxyy(); pintbxx, pintbyy = self._pintb.xxyy()
        return (pintayy + pintbyy) * (pintaxx - pintbxx) / 2

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_b: creating class instances ---")
    pinta = GMPoint(xxyy=(1., 2.)); pinta.prtcls('pinta -> ')
    pintb = GMPoint(xxyy=(2., 1.)); pintb.prtcls('pintb -> ')
    segm = GMSegment(pinta=pinta, pintb=pintb); segm.prtcls('segm -> ')

    # -----------------------------------------------------------------------------
    print("\n## --- section_c: calculating segment properties ---")
    print(f'{segm.leng() = }')
    print(f'{segm.unitvect_pa2pb() = }, {segm.unitvect_pb2pa() = }')
    print(f'{segm.crosprod_pa2pb() = }, {segm.crosprod_pb2pa() = }')
    print(f'{segm.projxx_pa2pb() = }, {segm.projxx_pb2pa() = }')
    print(f'{segm.projyy_pa2pb() = }, {segm.projyy_pb2pa() = }')

    # -----------------------------------------------------------------------------
    print("\n## --- section_d: calculating triangle ---")
    pinta = GMPoint(xxyy=(1., 3.)); print('pinta: ', pinta)
    pintb = GMPoint(xxyy=(3., 1.)); print('pintb: ', pintb)
    pintc = GMPoint(xxyy=(0., 0.)); print('pintc: ', pintc)
    segma = GMSegment(pinta=pintb, pintb=pintc)
    segmb = GMSegment(pinta=pintc, pintb=pinta)
    segmc = GMSegment(pinta=pinta, pintb=pintb)
    gravctr = (pinta.xxyy() + pintb.xxyy() + pintc.xxyy()) / 3
    print(f'{gravctr = }')
    area = segma.crosprod_pa2pb() / 2. + segmb.crosprod_pa2pb() / 2. + segmc.crosprod_pa2pb() / 2.
    print(f'{abs(area) = }')

    # -----------------------------------------------------------------------------
    print("\n## --- section_e: calculating polygon ---")
    points = ((1,3),(4,4),(3,1),(0,0),)
    pints, segms = [], []
    for point in points:
        pint = GMPoint(xxyy=point); print(pint)
        pints.append(pint)
    for i in range(len(points)):
        segm = GMSegment(pinta=pints[i-1], pintb=pints[i])
        segms.append(segm)
    grav = 0.
    for pint in pints:
        grav += pint.xxyy()
    grav /= len(pints); print(f'{grav = }')
    area_prod, area_prjx, area_prjy = 0., 0., 0.
    for segm in segms:
        area_prod += segm.crosprod_pa2pb()
        area_prjx += segm.projxx_pa2pb()
        area_prjy += segm.projyy_pa2pb()
    area_prod /= 2; print(f'{abs(area_prod) = }')
    print(f'{abs(area_prjx) = }')
    print(f'{abs(area_prjy) = }')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMSegment) class for segment ***
      *** class GMPoint is embedded as pinta and pintb ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMSegment) importing items from module ---
    
    *** (GMPoint) class for point ***
      *** class GMVector is inherited ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMPoint) importing items from module ---
    
    *** (GMVector) class for vector ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMVector) importing items from module ---
    ## --- section_a: (GMVector) defining class ---
    ## --- section_a1: (GMVector) initializing class instance ---
    ## --- section_a2: (GMVector) setting and getting functions ---
    ## --- section_a3: (GMVector) string function for print() ---
    ## --- section_a4: (GMVector) operating vectors ---
    ## --- section_a5: (GMVector) overloading arithmetic operators ---
    ## --- section_a6: (GMVector) calculating unit vector and products ---
    ## --- section_a: (GMPoint) defining class ---
    ## --- section_a1: (GMPoint) initializing class instance ---
    ## --- section_a2: (GMPoint) string function for print() ---
    ## --- section_a3: (GMPoint) calculating relation with point ---
    ## --- section_a: (GMSegment) defining class ---
    ## --- section_a1: (GMSegment) initializing class instance ---
    ## --- section_a2: (GMSegment) string function for print() ---
    ## --- section_a3: (GMSegment) calculating segment properties ---
    
    ## --- section_b: creating class instances ---
    pinta -> :: GMPrint ::
      (sup) GMVector : (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
    pintb -> :: GMPrint ::
      (sup) GMVector : (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651)
    segm -> :: GMSegment ::
      pnta: GMPoint:: (xx,yy) = (1, 2) : (rr,th) = (2.23607, 63.4349)
      pntb: GMPoint:: (xx,yy) = (2, 1) : (rr,th) = (2.23607, 26.5651)
    
    ## --- section_c: calculating segment properties ---
    segm.leng() = 1.4142135623730951
    segm.unitvect_pa2pb() = array([ 0.70710678, -0.70710678]), segm.unitvect_pb2pa() = array([-0.70710678,  0.70710678])
    segm.crosprod_pa2pb() = array(-3.), segm.crosprod_pb2pa() = array(0.)
    segm.projxx_pa2pb() = 1.5, segm.projxx_pb2pa() = -1.5
    segm.projyy_pa2pb() = -1.5, segm.projyy_pb2pa() = 1.5
    
    ## --- section_d: calculating triangle ---
    pinta:  : (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651)
    pintb:  : (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349)
    pintc:  : (xx,yy) = (0, 0) : (rr,th) = (0, 0)
    gravctr = array([1.33333333, 1.33333333])
    abs(area) = 4.0
    
    ## --- section_e: calculating polygon ---
    : (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651)
    : (xx,yy) = (4, 4) : (rr,th) = (5.65685, 45)
    : (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349)
    : (xx,yy) = (0, 0) : (rr,th) = (0, 0)
    grav = array([2., 2.])
    abs(area_prod) = 8.0
    abs(area_prjx) = 8.0
    abs(area_prjy) = 8.0
    '''
