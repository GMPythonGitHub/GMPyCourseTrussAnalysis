# gm_cta05_Class_d4_polygon_fig.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMPolygon) class for segment ***")
print("  *** class GMpoint and GMSegment are embedded as list pints and segms ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMPolygon) importing items from module ---")
from gm_cta05_Class_d4_polygon import GMPolygon

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

    # -----------------------------------------------------------------------------
    print("\n## --- section_mc: drawing polygon ---")
    from matplotlib import (pyplot as plt, patches as pat)

    fig, ax = plt.subplots(figsize=(6., 6.))
    fig.suptitle('polygon and gravity center')
    for segm in polg._segms:
        idx = ('outer product', 'projection to x-axis', 'projection to y-axis')[2]
        if idx == 'outer product':
            prd = segm.oprd()
            if prd>= 0:
                clr = 'C1'
            else:
                clr = 'C2'
            pinta, pintb = segm._pinta, segm._pintb
            xy = ((0, 0), tuple(pinta.xxyy()), tuple(pintb.xxyy()))
        elif idx == 'projection to x-axis':
            prj = segm.prjx()
            if prj >= 0:
                clr = 'C1'
            else:
                clr = 'C2'
            pintaxx, pintayy = segm._pinta.xxyy()
            pintbxx, pintbyy = segm._pintb.xxyy()
            xy = ((pintaxx, 0), (pintbxx, 0), (pintbxx, pintbyy), (pintaxx, pintayy))
        elif idx == 'projection to y-axis':
            prj = segm.prjy()
            if prj >= 0:
                clr = 'C1'
            else:
                clr = 'C2'
            pintaxx, pintayy = segm._pinta.xxyy()
            pintbxx, pintbyy = segm._pintb.xxyy()
            xy = ((0, pintayy), (0, pintbyy), (pintbxx, pintbyy), (pintaxx, pintayy))
        ptc = pat.Polygon(xy=xy, closed=True,
            linestyle='-', linewidth=1., edgecolor=clr, fill=True, facecolor=clr,
            alpha=0.2)
        ax.add_patch(ptc)

    pintsxxyy = []
    for pint in polg._pints:
        xx, yy = xxyy = list(pint.xxyy())
        pintsxxyy.append(xxyy)
        ax.scatter([xx], [yy],
            marker='o', s=40, color='C3', edgecolor='C3')
    ptc = pat.Polygon(xy=pintsxxyy, closed=True,
        linestyle='-', linewidth=2., edgecolor='C3', fill=False)
    ax.add_patch(ptc)

    pintgxx, pintgyy = polg.grav_ctr()
    ax.scatter((pintgxx,), (pintgyy,),
        marker='o', s=40, color='C3', edgecolor='C3', label='gravity center')

    ax.set_aspect('equal')
    ax.legend()
    fig.savefig('gm_cta05_Class_d4_polygon_fig.png')
    plt.show()

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
    polg.pint_grav() = array([2., 2.])
    polg.leng_segms() = 12.649110640673518
    polg.area_prod() = 8.0
    polg.area_projxx() = 8.0
    polg.area_projyy() = 8.0
    
    ## --- section_c: drawing polygon ---
    '''
