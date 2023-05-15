# gm_c05_b0_vector.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** (GMVector) class for vector ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: (GMVector) importing items from module ---')
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2,
    deg2rad as d2r, rad2deg as r2d, ndarray, array )

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVector) defining class ---')
class GMVector():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVector) initializing class instance ---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True):
        self.__xxyy = None
        self.set_vector(xxyy, rrth, cnv=cnv)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVector) setting and getting functions ---')
    ## setting functions
    def set_xxyy(self, xxyy: tuple) -> None:
        self.__xxyy = array(xxyy)
    def set_rrth(self, rrth: tuple, cnv: bool = True) -> None:
        rr, th = rrth
        if cnv: th = d2r(th)
        self.__xxyy = rr * array([cos(th), sin(th)])
    def set_vector(self, xxyy: tuple = None, rrth: tuple = None, cnv: bool = True) -> None:
        if rrth is not None:
            xxyy = None; self.set_rrth(rrth, cnv=cnv)
        if xxyy is not None: self.set_xxyy(xxyy)
    ## getting functions
    def xxyy(self) -> ndarray:
        return self.__xxyy
    def rrth(self, cnv: bool = True) -> ndarray:
        rr, th = sqrt(sum(square(self.__xxyy))), atan2(self.__xxyy[1], self.__xxyy[0])
        if cnv: th = r2d(th)
        return array([rr, th])

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMVector) string function for print() ---')
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(cnv=True)
        return f'GMVector:: (xx,yy) = ({xx:g}, {yy:g}), (rr,th) = ({rr:g}, {th:g})'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVector) operating vectors ---')
    def cnvvect(self, vect: object = None) -> ndarray:
        if type(vect) in (int, float, complex): return vect
        elif type(vect) in (list, tuple, ndarray): return array(vect)
        else: return vect.xxyy()
    def add(self, vect: object = None) -> ndarray:
        self.__xxyy += self.cnvvect(vect); return self.xxyy()
    def sub(self, vect: object = None) -> ndarray:
        self.__xxyy -= self.cnvvect(vect); return self.xxyy()
    def mul(self, vect: object = None) -> ndarray:
        self.__xxyy *= self.cnvvect(vect); return self.xxyy()
    def div(self, vect: object = None) -> ndarray:
        self.__xxyy /= self.cnvvect(vect); return self.xxyy()

    # -----------------------------------------------------------------------------
    print('## --- section_a5: (GMVector) overloading arithmetic operators ---')
    def __add__(self, vect): return GMVector(xxyy=self.__xxyy+self.cnvvect(vect))
    def __radd__(self, vect): return GMVector(xxyy=self.cnvvect(vect)+self.__xxyy)
    def __sub__(self, vect): return GMVector(xxyy=self.__xxyy-self.cnvvect(vect))
    def __rsub__(self, vect): return GMVector(xxyy=self.cnvvect(vect)-self.__xxyy)
    def __mul__(self, vect): return GMVector(xxyy=self.__xxyy*self.cnvvect(vect))
    def __rmul__(self, vect): return GMVector(xxyy=self.cnvvect(vect)*self.__xxyy)
    def __truediv__(self, vect): return GMVector(xxyy=self.__xxyy/self.cnvvect(vect))
    def __rtruediv__(self, vect): return GMVector(xxyy=self.cnvvect(vect)/self.__xxyy)

    def __iadd__(self, vect): self.__xxyy+=self.cnvvect(vect); return self
    def __isub__(self, vect): self.__xxyy-=self.cnvvect(vect); return self
    def __imul__(self, vect): self.__xxyy*=self.cnvvect(vect); return self
    def __itruediv__(self, vect): self.__xxyy/=self.cnvvect(vect); return self

    def __pos__(self):  self.__xxyy = + self.__xxyy; return self
    def __neg__(self):  self.__xxyy = - self.__xxyy; return self

    # -----------------------------------------------------------------------------
    print('## --- section_a6: (GMVector) calculating unit vector and products ---')
    def unitvect(self) -> ndarray:
        rr, _ = self.rrth()
        return self.__xxyy / rr if rr > 0. else None
    def dottprod(self, vect: object = None) -> float:
        xx, yy = self.__xxyy; vxx, vyy = vect.xxyy()
        return xx * vxx + yy * vyy
    def vectprod(self, vect: object = None) -> float:
        xx, yy = self.__xxyy; vxx, vyy = vect.xxyy()
        return xx * vyy - yy * vxx

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print('\n## --- section_b: creating class instances ---')
    vecta = GMVector(xxyy=(1., 1.)); print('vecta: ', vecta)
    vectb = GMVector(xxyy=(1., 2.)); print('vectb: ', vectb)

    # -----------------------------------------------------------------------------
    print('\n## --- section_c: operating vectors ---')
    vecta.set_vector(xxyy=(1., 1.))
    vecta.add(2); print('vecta.add(2): ', vecta)
    vecta.add([1, 2]); print('vecta.add([1,2]): ', vecta)
    vecta.add(vectb); print('vecta.add(vectb): ', vecta)
    vecta.set_vector(xxyy=(1., 1.)); vecta.sub(vectb); print('vecta.sub(vectb): ', vecta)
    vecta.set_vector(xxyy=(1., 1.)); vecta.mul(vectb); print('vecta.mul(vectb): ', vecta)
    vecta.set_vector(xxyy=(1., 1.)); vecta.div(vectb); print('vecta.div(vectb): ', vecta)

    # -----------------------------------------------------------------------------
    print('\n## --- section_d: operating vectors with operators ---')
    vecta.set_vector(xxyy=(1., 1.))
    print(f'vecta + 2: {vecta + 2}')
    print(f'vecta + [1,2]: {vecta + [1, 2]}')
    print(f'vecta + vectb: {vecta + vectb}')
    print(f'vecta - vectb: {vecta - vectb}')
    print(f'vecta * vectb: {vecta * vectb}')
    print(f'vecta / vectb: {vecta / vectb}')

    vecta.set_xxyy((1., 1.))
    vecta += 2; print('vecta += 2: ', vecta)
    vecta += [1,2]; print('vecta += [1,2]]: ', vecta)
    vecta += vectb; print('vecta += vectb: ', vecta)
    vecta.set_xxyy((1., 1.)); vecta -= vectb; print('vecta -= vectb: ', vecta)
    vecta.set_xxyy((1., 1.)); vecta *= vectb; print('vecta *= vectb: ', vecta)
    vecta.set_xxyy((1., 1.)); vecta /= vectb; print('vecta /= vectb: ', vecta)

    vecta.set_xxyy((1., 1.)); print('+ vecta: ', + vecta)
    vecta.set_xxyy((1., 1.)); print('- vecta: ', - vecta)

    # -----------------------------------------------------------------------------
    print('\n## --- section_e: calculating unit vectors and products ---')
    print(f'{vecta.unitvect() = }')
    print(f'{vectb.unitvect() = }')
    print(f'{vecta.dottprod(vectb) = }, {vecta.vectprod(vectb) = }')
    print(f'{vectb.dottprod(vecta) = }, {vectb.vectprod(vecta) = }')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
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
    
    ## --- section_b: creating class instances ---
    vecta:  GMVector:: (xx,yy) = (1, 1), (rr,th) = (1.41421, 45)
    vectb:  GMVector:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
    
    ## --- section_c: operating vectors ---
    vecta.add(2):  GMVector:: (xx,yy) = (3, 3), (rr,th) = (4.24264, 45)
    vecta.add([1,2]):  GMVector:: (xx,yy) = (4, 5), (rr,th) = (6.40312, 51.3402)
    vecta.add(vectb):  GMVector:: (xx,yy) = (5, 7), (rr,th) = (8.60233, 54.4623)
    vecta.sub(vectb):  GMVector:: (xx,yy) = (0, -1), (rr,th) = (1, -90)
    vecta.mul(vectb):  GMVector:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
    vecta.div(vectb):  GMVector:: (xx,yy) = (1, 0.5), (rr,th) = (1.11803, 26.5651)
    
    ## --- section_d: operating vectors with operators ---
    vecta + 2: GMVector:: (xx,yy) = (3, 3), (rr,th) = (4.24264, 45)
    vecta + [1,2]: GMVector:: (xx,yy) = (2, 3), (rr,th) = (3.60555, 56.3099)
    vecta + vectb: GMVector:: (xx,yy) = (2, 3), (rr,th) = (3.60555, 56.3099)
    vecta - vectb: GMVector:: (xx,yy) = (0, -1), (rr,th) = (1, -90)
    vecta * vectb: GMVector:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
    vecta / vectb: GMVector:: (xx,yy) = (1, 0.5), (rr,th) = (1.11803, 26.5651)
    vecta += 2:  GMVector:: (xx,yy) = (3, 3), (rr,th) = (4.24264, 45)
    vecta += [1,2]]:  GMVector:: (xx,yy) = (4, 5), (rr,th) = (6.40312, 51.3402)
    vecta += vectb:  GMVector:: (xx,yy) = (5, 7), (rr,th) = (8.60233, 54.4623)
    vecta -= vectb:  GMVector:: (xx,yy) = (0, -1), (rr,th) = (1, -90)
    vecta *= vectb:  GMVector:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
    vecta /= vectb:  GMVector:: (xx,yy) = (1, 0.5), (rr,th) = (1.11803, 26.5651)
    + vecta:  GMVector:: (xx,yy) = (1, 1), (rr,th) = (1.41421, 45)
    - vecta:  GMVector:: (xx,yy) = (-1, -1), (rr,th) = (1.41421, -135)
    
    ## --- section_e: calculating unit vectors and products ---
    vecta.unitvect() = array([-0.70710678, -0.70710678])
    vectb.unitvect() = array([0.4472136 , 0.89442719])
    vecta.dottprod(vectb) = -3.0, vecta.vectprod(vectb) = -1.0
    vectb.dottprod(vecta) = -3.0, vectb.vectprod(vecta) = 1.0
    '''
