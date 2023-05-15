# gm_c05_b1_point.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** (GMPoint) class for point ***')
print('  *** class GMVector is inherited ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: (GMPoint) importing items from module ---')
from numpy import (ndarray)
from gm_c05_b0_vector import GMVector

# -----------------------------------------------------------------------------
print('## --- section_a: (GMPoint) defining class ---')
class GMPoint(GMVector):
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMPoint) initializing class instance ---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        super().__init__(xxyy, rrth, cnv=cnv)  # calling supper class initialization

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMPoint) string function for print() ---')
    def __str__(self) -> str:
        xx, yy = self.xxyy(); rr, th = self.rrth(cnv=True)
        return f'GMPoint:: (xx,yy) = ({xx:g}, {yy:g}), (rr,th) = ({rr:g}, {th:g})'
    def clsprint(self) -> None:
        print(self.__str__())

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMPoint) calculating relation with point ---')
    def dist_2pint(self, pint: object) -> float:
        rr, _ = (pint - self).rrth(); return rr
    def unitvect_2pint(self, pint: object) -> ndarray:
        return (pint - self).unitvect()

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print('\n## --- section_b: creating class instances ---')
    pinta = GMPoint(xxyy=(1., 1.)); print('pinta: ', pinta)
    pintb = GMPoint(xxyy=(1., 2.)); print('pintb: ', pintb)

    # -----------------------------------------------------------------------------
    print('\n## --- section_c: operating points ---')
    print(f'pinta + pintb: {pinta + pintb}')
    print(f'pinta - pintb: {pinta - pintb}')
    print(f'pinta * pintb: {pinta * pintb}')
    print(f'pinta / pintb: {pinta / pintb}')

    pinta.set_xxyy((1., 1.))
    pinta += 2; print('pinta += 2: ', pinta)
    pinta += [1, 2]; print('pinta += [1,2]: ', pinta)
    pinta += pintb; print('pinta += pintb: ', pinta)
    pinta.set_xxyy((1., 1.)); pinta -= pintb; print('pinta -= pintb: ', pinta)
    pinta.set_xxyy((1., 1.)); pinta -= pintb; print('pinta -= pintb: ', pinta)
    pinta.set_xxyy((1., 1.))
    pinta /= pintb
    print('pinta /= pintb: ', pinta)

    # -----------------------------------------------------------------------------
    print('\n## --- section_d: calculating unit vectors and products ---')
    pinta.set_xxyy((1., 2.))
    pintb.set_xxyy((2., 1.))
    print('pinta.uvect(): ', pinta.unitvect())
    print('pintb.uvect(): ', pintb.unitvect())
    print('dot product, vector product: ', pinta.dottprod(pintb), ',', pinta.vectprod(pintb))
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
    
    ## --- section_b: creating class instances ---
    pinta:  GMPoint:: (xx,yy) = (1, 1), (rr,th) = (1.41421, 45)
    pintb:  GMPoint:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
    
    ## --- section_c: operating points ---
    pinta + pintb: GMVector:: (xx,yy) = (2, 3), (rr,th) = (3.60555, 56.3099)
    pinta - pintb: GMVector:: (xx,yy) = (0, -1), (rr,th) = (1, -90)
    pinta * pintb: GMVector:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
    pinta / pintb: GMVector:: (xx,yy) = (1, 0.5), (rr,th) = (1.11803, 26.5651)
    pinta += 2:  GMPoint:: (xx,yy) = (3, 3), (rr,th) = (4.24264, 45)
    pinta += [1,2]:  GMPoint:: (xx,yy) = (4, 5), (rr,th) = (6.40312, 51.3402)
    pinta += pintb:  GMPoint:: (xx,yy) = (5, 7), (rr,th) = (8.60233, 54.4623)
    pinta -= pintb:  GMPoint:: (xx,yy) = (0, -1), (rr,th) = (1, -90)
    pinta -= pintb:  GMPoint:: (xx,yy) = (0, -1), (rr,th) = (1, -90)
    pinta /= pintb:  GMPoint:: (xx,yy) = (1, 0.5), (rr,th) = (1.11803, 26.5651)
    
    ## --- section_d: calculating unit vectors and products ---
    pinta.uvect():  [0.4472136  0.89442719]
    pintb.uvect():  [0.89442719 0.4472136 ]
    dot product, vector product:  4.0 , -3.0
    pinta.dist_2pint(pintb) = 1.4142135623730951
    pintb.dist_2pint(pinta) = 1.4142135623730951
    pinta.unitvect_2pint(pintb) = array([ 0.70710678, -0.70710678])
    pintb.unitvect_2pint(pinta) = array([-0.70710678,  0.70710678])
    '''
