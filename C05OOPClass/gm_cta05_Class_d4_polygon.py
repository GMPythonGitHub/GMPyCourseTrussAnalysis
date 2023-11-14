# gm_cta05_Class_d4_polygon.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMPolygon) class for segment ***")
print("  *** class GMpoint and GMSegment are embedded as list pints and segms ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMPolygon) importing items from module ---")
from numpy import (ndarray, array)
from gm_cta05_Class_d1_point import (GMPoint)
from gm_cta05_Class_d3_segment import (GMSegment)

# -----------------------------------------------------------------------------
print("## --- section_a: (GMPolygon) declaring class ---")
class GMPolygon():
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMPolygon) initializing class instance ---")
    def __init__(self, points: tuple = ((1.,3.),(4.,4.),(3.,1.),(1.,1.),)):
        self.set_polygon(points)

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMPolygon) setting and getting functions ---")
    def set_polygon(self, points: tuple = ((1.,3.),(4,4),(3.,1.),(1.,1.),)):
        self._pints, self._segms = [], []
        for point in points:
            self._pints.append(GMPoint(point))
        for i, pint in enumerate(self._pints):
            self._segms.append(GMSegment(self._pints[i-1], pint))

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMPolygon) string function for print() ---")
    def __str__(self) -> str:
        return ''
    def prtcls(self, idx: str = '') -> None:
        st = idx + ':: GMPolygon ::\n'
        st += '  pints[]: GMPoint:\n'
        for i, pint in enumerate(self._pints):
            st += f'  [{i}]: ' + pint.__str__() + '\n'
        st += '  segms[]: GMSegment:\n'
        for i, segm in enumerate(self._segms):
            st += f'  [{i}] \t: pinta: GMPoint' + segm._pinta.__str__() + '\n'
            st +=  '    \t: pintb: GMPoint' + segm._pintb.__str__() + '\n'
        print(st)

    # -----------------------------------------------------------------------------
    print("## --- section_e: (GMPolygon) calculating polygon properties ---")
    def grav_ctr(self) -> ndarray:
        grav_ctr = array([0.,0.])
        for pint in self._pints:
            grav_ctr += pint.xxyy()
        return grav_ctr / len(self._pints)
    def leng(self) -> float:
        leng = 0.
        for segm in self._segms:
            leng += segm.leng()
        return leng
    def area_prd(self) -> float:  # area from cross product
        area = 0.
        for segm in self._segms:
            area += segm.oprd()
        return abs(area) / 2.
    def area_prjx(self) -> float:  # area from projection in x-dir.
        area = 0.
        for segm in self._segms:
            area += segm.prjx()
        return abs(area)
    def area_prjy(self) -> float:  # area from projection in y-dir.
        area = 0.
        for segm in self._segms:
            area += segm.prjy()
        return abs(area)

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: creating class instance ---")
    points = ((1,3),(4,4),(3,1),(0,0),)
    polg = GMPolygon(points); print(polg)
    polg.prtcls('polg -> ')

    # -----------------------------------------------------------------------------
    print("## --- section_mb: calculating polygon ---")
    print(f'{polg.grav_ctr() = }')
    print(f'{polg.leng() = }')
    print(f'{polg.area_prd() = }')
    print(f'{polg.area_prjx() = }')
    print(f'{polg.area_prjy() = }')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMPolygon) class for segment ***
      *** class GMpoint and GMSegment are embedded as list pints and segms ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMPolygon) importing items from module ---
    
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
    ## --- section_a: (GMVector) declaring class ---
    ## --- section_b: (GMVector) initializing class instance ---
    ## --- section_c: (GMVector) setting and getting functions ---
    ## --- section_d: (GMVector) string function for print() ---
    ## --- section_e: (GMVector) operating vectors ---
    ## --- section_f: (GMVector) overloading arithmetic operators ---
    ## --- section_g: (GMVector) calculating vector ---
    
    ## --- section_a: (GMPoint) declaring class ---
    ## --- section_b: (GMPoint) initializing class instance ---
    ## --- section_c: (GMPoint) string function for print() ---
    ## --- section_d: (GMPoint) calculating point ---
    
    ## --- section_a: (GMSegment) declaring class ---
    ## --- section_b: (GMSegment) initializing class instance ---
    ## --- section_c: (GMSegment) string function for print() ---
    ## --- section_d: (GMSegment) calculating segment ---
    
    ## --- section_a: (GMPolygon) declaring class ---
    ## --- section_b: (GMPolygon) initializing class instance ---
    ## --- section_c: (GMPolygon) setting and getting functions ---
    ## --- section_d: (GMPolygon) string function for print() ---
    ## --- section_e: (GMPolygon) calculating polygon properties ---
    
    ## --- section_ma: creating class instance ---
    polg -> :: GMSegment ::
      pints[]: GMPoint:
      [0]: : (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651)
      [1]: : (xx,yy) = (4, 4) : (rr,th) = (5.65685, 45)
      [2]: : (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349)
      [3]: : (xx,yy) = (0, 0) : (rr,th) = (0, 0)
      segms[]: GMSegment:
      [0] 	: pinta: GMPoint: (xx,yy) = (0, 0) : (rr,th) = (0, 0)
            : pintb: GMPoint: (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651)
      [1] 	: pinta: GMPoint: (xx,yy) = (1, 3) : (rr,th) = (3.16228, 71.5651)
            : pintb: GMPoint: (xx,yy) = (4, 4) : (rr,th) = (5.65685, 45)
      [2] 	: pinta: GMPoint: (xx,yy) = (4, 4) : (rr,th) = (5.65685, 45)
            : pintb: GMPoint: (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349)
      [3] 	: pinta: GMPoint: (xx,yy) = (3, 1) : (rr,th) = (3.16228, 18.4349)
            : pintb: GMPoint: (xx,yy) = (0, 0) : (rr,th) = (0, 0)
    
    ## --- section_mb: calculating polygon ---
    polg.grav_ctr() = array([2., 2.])
    polg.leng() = 12.649110640673518
    polg.area_prd() = 8.0
    polg.area_prjx() = 8.0
    polg.area_prjy() = 8.0
    '''
