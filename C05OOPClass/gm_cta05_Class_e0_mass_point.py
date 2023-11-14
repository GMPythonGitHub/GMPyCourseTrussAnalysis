# gm_cta05_Class_e0_mass_point.py: coded by Kinya MIURA 230501
# -----------------------------------------------------------------------------
print('\n*** (GMMassPoint) class for position vector ***')
print('  *** class GMPoint is inherited; class GMVector is embedded as velo, accl, efrc  ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: (GMMassPoint) importing items from module ---')
from numpy import (array)
from _old.gm_c05_b0_vector import GMVector
from _old.gm_c05_b1_point import GMPoint

# -----------------------------------------------------------------------------
print('## --- section_a: (GMMassPoint) defining class ---')
class GMMassPoint(GMPoint):
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMMassPoint) initializing class instance ---')
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, cnv: bool = True,
            mass: float = 1.,
            velo: GMVector = GMVector(), accl: GMVector = GMVector(), efrc: GMVector = GMVector() ):
        super().__init__(xxyy, rrth, cnv=cnv)
        self.__mass = None
        self._velo, self._accl, self._efrc = velo, accl, efrc
        self.set_coef(mass)

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMMassPoint) setting and getting functions ---')
    def set_coef(self, mass: float = None, visc: float = None, sprg: float = None) -> None:
        if mass is not None: self.__mass = mass

    def mass(self) -> float: return self.__mass

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMMassPoint) string function for print() ---')
    def __str__(self) -> str:
        st  = (
            f'GMMassPoint:: \n'
            '\t' + super().__str__() + '\n'
            f'\tmass = {self.mass():g} \n'
            f'\tvelo: ' + self._velo.__str__() + '\n'
            f'\taccl: ' + self._accl.__str__() + '\n'
            f'\tefrc: ' + self._efrc.__str__() )
        return st
    def strprint(self) -> None:
        print(self.__str__())

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMPoint) calculating behavior of mass point ---')
    def calc_motn(self, dlt_time) -> tuple:  # calculating motion of mass point
        self._accl = self._efrc / self.__mass
        dlt_accl = 0.
        dlt_velo = self._accl * dlt_time + dlt_accl * dlt_time / 2.
        dlt_disp = self._velo * dlt_time + self._accl * dlt_time**2 / 2 + dlt_accl * dlt_time**2 / 6
        self.add(dlt_disp); self._velo += dlt_velo; self._accl += dlt_accl
        return self.dataset()
    def dataset(self) -> tuple:
        self._accl = self._efrc / self.__mass
        return tuple(self.xxyy()), tuple(self._velo.xxyy()), tuple(self._accl.xxyy())

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print('\n## --- section_b: creating class instances ---')
    mass = 1.
    velo, accl, efrc = (
        GMVector(xxyy=(1.,2.)), GMVector(xxyy=(0.,0.)), GMVector(xxyy=(0.,0.)) )
    masspint = GMMassPoint(xxyy=(0.,0.), mass=mass, velo=velo, accl=accl, efrc=efrc)
    print('masspint: ', masspint)

    # -----------------------------------------------------------------------------
    print('\n## --- section_c: calculating mass point motion ---')
    dlt_time = 0.1
    print('masspint: ', masspint)
    elp_time, tim, dis, vel, acc = 0., [], [], [], []
    for i in range(21):
        elp_time = i * dlt_time
        if i == 0: ds, vl, ac = masspint.dataset()
        else: ds, vl, ac  = masspint.calc_motn(dlt_time)
        tim.append(elp_time)
        dis.append(ds); vel.append(vl); acc.append(ac)
    print('masspint: ', masspint)
    print(array(tim))
    print(array(dis))
    print(array(vel))
    print(array(acc))

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMMassPoint) class for position vector ***
      *** class GMPoint is inherited; class GMVector is embedded as velo, accl, efrc  ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMMassPoint) importing items from module ---
    
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
    
    *** (GMPoint) class for point ***
      *** class GMVector is inherited ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMPoint) importing items from module ---
    ## --- section_a: (GMPoint) defining class ---
    ## --- section_a1: (GMPoint) initializing class instance ---
    ## --- section_a2: (GMPoint) string function for print() ---
    ## --- section_a3: (GMPoint) calculating relation with point ---
    ## --- section_a: (GMMassPoint) defining class ---
    ## --- section_a1: (GMMassPoint) initializing class instance ---
    ## --- section_a2: (GMMassPoint) setting getting functions ---
    ## --- section_a3: (GMMassPoint) string function for print() ---
    ## --- section_a4: (GMPoint) calculating behavior of mass point ---
    
    ## --- section_b: creating class instances ---
    masspint:  GMMassPoint:: 
        GMPoint:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        mass = 1 
        velo: GMVector:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
        accl: GMVector:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        efrc: GMVector:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
    
    ## --- section_c: calculating mass point motion ---
    masspint:  GMMassPoint:: 
        GMPoint:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        mass = 1 
        velo: GMVector:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
        accl: GMVector:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        efrc: GMVector:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
    masspint:  GMMassPoint:: 
        GMPoint:: (xx,yy) = (2, 4), (rr,th) = (4.47214, 63.4349)
        mass = 1 
        velo: GMVector:: (xx,yy) = (1, 2), (rr,th) = (2.23607, 63.4349)
        accl: GMVector:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        efrc: GMVector:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
	'''
