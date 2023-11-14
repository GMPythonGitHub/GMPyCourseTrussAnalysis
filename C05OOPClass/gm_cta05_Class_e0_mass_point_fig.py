# gm_cta05_Class_e0_mass_point_fig.py: coded by Kinya MIURA 230501
# -----------------------------------------------------------------------------
print('\n*** (GMMassPoint) class for position vector ***')
print('  *** class GMPoint is inherited; class GMVector is embedded as disp, velo, accl, efrc  ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- block__: (GMMassPoint) importing items from module ---')
from numpy import (array)
from _old.gm_c05_b0_vector import GMVector
from _old.gm_c05_b1_point import GMPoint

# -----------------------------------------------------------------------------
print('## --- block_a: (GMMassPoint) defining class ---')
class GMMassPoint(GMPoint):
    # -----------------------------------------------------------------------------
    print('## --- block_a1: (GMMassPoint) initializing class instance ---')
    def __init__(self,
            xxyy: tuple = (0., 0.), rrth: tuple = None, cnv: bool = True,
            mass: float = 1.,
            velo: GMVector = GMVector(), accl: GMVector = GMVector(),
            efrc: GMVector = GMVector() ):
        super().__init__(xxyy, rrth, cnv=cnv)
        self.__mass = None
        self._velo, self._accl, self._efrc = velo, accl, efrc
        self.set_coef(mass)

    # -----------------------------------------------------------------------------
    print('## --- block_a2: (GMMassPoint) setting and getting functions ---')
    def set_coef(self, mass: float = None, visc: float = None, sprg: float = None) -> None:
        if mass is not None: self.__mass = mass

    def mass(self) -> float: return self.__mass

    # -----------------------------------------------------------------------------
    print('## --- block_a3: (GMMassPoint) string function for print() ---')
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
    print('## --- block_a4: (GMPoint) calculating behavior of mass point ---')
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
    print('\n## --- block_b: creating class instances ---')
    mass = 1.
    velo, accl, efrc = (
        GMVector(xxyy=(1.,0.)), GMVector(xxyy=(0.,0.)), GMVector(xxyy=(0.,-1.)) )
    masspint = GMMassPoint(xxyy=(0.,0.), mass=mass, velo=velo, accl=accl, efrc=efrc)
    print('masspint: ', masspint)

    # -----------------------------------------------------------------------------
    print("\n## --- block_c: calculating mass point motion ---")
    dlt_time = 0.1
    print('masspint: ', masspint)
    elp_time, tim, dis, vel, acc = 0., [], [], [], []
    for i in range(21):
        elp_time = i * dlt_time
        if i == 0: ds, vl, ac = masspint.dataset()
        else: ds, vl, ac  = masspint.calc_motn(dlt_time)
        tim.append(elp_time)
        dis.append(ds); vel.append(vl); acc.append(ac)
    tim, dis, vel, acc = array(tim), array(dis), array(vel), array(acc)

    # -----------------------------------------------------------------------------
    print("\n## --- block_d: drawing polygon ---")
    from matplotlib import (pyplot as plt)

    fig, ax = plt.subplots(figsize=(6., 6.))
    fig.suptitle('mass point motion')
    ax.plot(dis[:,0], dis[:,1],
        linestyle='-', linewidth=2., color='C0',
        marker='o', markersize=2, markeredgewidth=2, markeredgecolor='C0', markerfacecolor='C0' )

    ax.set_aspect('equal')
    fig.savefig('gm_c05_d0_mass_point.png')
    plt.show()

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMMassPoint) class for position vector ***
      *** class GMPoint is inherited; class GMVector is embedded as disp, velo, accl, efrc  ***
    # -----------------------------------------------------------------------------
    ## --- block__: (GMMassPoint) importing items from module ---
    
    *** (GMVector) class for vector ***
    # -----------------------------------------------------------------------------
    ## --- block__: (GMVector) importing items from module ---
    ## --- block_a: (GMVector) defining class ---
    ## --- block_a1: (GMVector) initializing class instance ---
    ## --- block_a2: (GMVector) setting and getting functions ---
    ## --- block_a3: (GMVector) string function for print() ---
    ## --- block_a4: (GMVector) operating vectors ---
    ## --- block_a5: (GMVector) overloading arithmetic operators ---
    ## --- block_a6: (GMVector) calculating unit vector and products ---
    
    *** (GMPoint) class for point ***
      *** class GMVector is inherited ***
    # -----------------------------------------------------------------------------
    ## --- block__: (GMPoint) importing items from module ---
    ## --- block_a: (GMPoint) defining class ---
    ## --- block_a1: (GMPoint) initializing class instance ---
    ## --- block_a2: (GMPoint) string function for print() ---
    ## --- block_a3: (GMPoint) calculating relation with point ---
    ## --- block_a: (GMMassPoint) defining class ---
    ## --- block_a1: (GMMassPoint) initializing class instance ---
    ## --- block_a2: (GMMassPoint) setting getting functions ---
    ## --- block_a3: (GMMassPoint) string function for print() ---
    ## --- block_a4: (GMPoint) calculating behavior of mass point ---
    
    ## --- block_b: creating class instances ---
    masspint:  GMMassPoint:: 
        GMPoint:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        mass = 1 
        velo: GMVector:: (xx,yy) = (1, 0), (rr,th) = (1, 0)
        accl: GMVector:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        efrc: GMVector:: (xx,yy) = (0, -1), (rr,th) = (1, -90)
    
    ## --- block_c: calculating mass point motion ---
    masspint:  GMMassPoint:: 
        GMPoint:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        mass = 1 
        velo: GMVector:: (xx,yy) = (1, 0), (rr,th) = (1, 0)
        accl: GMVector:: (xx,yy) = (0, 0), (rr,th) = (0, 0)
        efrc: GMVector:: (xx,yy) = (0, -1), (rr,th) = (1, -90)
    
    ## --- block_d: drawing polygon ---
    '''
