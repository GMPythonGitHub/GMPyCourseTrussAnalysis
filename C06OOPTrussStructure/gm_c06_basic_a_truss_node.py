# gm_c06_basic_a_truss_node.py: coded by Kinya MIURA 230520
# -----------------------------------------------------------------------------
print("\n*** (GMTrussNodeBasic) class for truss node ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMTrussNodeBasic) importing items from module ---")
from numpy import (
    square, sqrt, sin, cos, arctan2 as atan2)

# -----------------------------------------------------------------------------
print("## --- section_a: (GMTrussNodeBasic) declaring class ---")
class GMTrussNodeBasic():
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMTrussNodeBasic) initializing class instance ---")
    def __init__(self,
            pos: tuple = (0., 0.), fxc: tuple = (False, False), lcn: tuple = (0, 1) ):
        self.pos, self.fxc, self.lcn = list(pos), list(fxc), list(lcn)
        # position (m), fixity condition (bool), location in matrix equation (int)
        self.dsp, self.efc = [0., 0.], [0., 0.]
        # displacement (m), external force (N)

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMTrussNodeBasic) string function for print() ---")
    def __str__(self):
        st = (
            f'pos(m) = {self.pos}, fxc = {self.fxc}, lcn = {self.lcn} \n'
            f'dsp(m) = {self.dsp}, efc(N) = {self.efc}' )
        return st

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMTrussNodeBasic) functions calculating nodes ---")
    def post_2node(self, node: object)-> list:  # position to node
        return [node.pos[0]-self.pos[0], node.pos[1]-self.pos[1]]
    def dist_2node(self, node: object) -> float:  # distance to node
        post = self.post_2node(node)
        return sqrt(square(post[0])+square(post[1]))
    def dirc_2node(self, node: object) -> float:  # direction to node
        post = self.post_2node(node)
        return atan2(post[1],post[0])
    def unitvect_2node(self, node: object) -> list:  # unit vector to node
        dirc = self.dirc_2node(node)
        return [cos(dirc), sin(dirc)]

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: (GMTrussNodeBasic) creating class instances ---")
    nodea = GMTrussNodeBasic(
        pos=(0., 0.), fxc=(False, False), lcn=(0, 1))
    nodea.dsp, nodea.efc = list((0., 1.*0.001)), list((10.*1000., 0.))
    nodeb = GMTrussNodeBasic(
        pos=(1., 1.), fxc=(False, False), lcn=(0, 1))
    nodeb.dsp, nodeb.efc = list((0., 2.*0.001)), list((20.*1000., 0.))
    print('nodea : \n', nodea)
    print('nodeb : \n', nodeb)

    # -----------------------------------------------------------------------------
    print("\n## --- section_mb: (GMTrussNodeBasic) calculating node to node ---")
    print(f'{nodea.post_2node(nodeb) = }')
    print(f'{nodeb.post_2node(nodea) = }')
    print(f'{nodea.dist_2node(nodeb) = }')
    print(f'{nodeb.dist_2node(nodea) = }')
    print(f'{nodea.dirc_2node(nodeb) = }')
    print(f'{nodeb.dirc_2node(nodea) = }')
    print(f'{nodea.unitvect_2node(nodeb) = }')
    print(f'{nodeb.unitvect_2node(nodea) = }')

    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    # terminal log
    '''
    *** (GMTrussNodeBasic) class for truss node ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMTrussNodeBasic) importing items from module ---
    ## --- section_a: (GMTrussNodeBasic) declaring class ---
    ## --- section_b: (GMTrussNodeBasic) initializing class instance ---
    ## --- section_c: (GMTrussNodeBasic) string function for print() ---
    ## --- section_d: (GMTrussNodeBasic) functions calculating nodes ---
    
    ## --- section_ma: (GMTrussNodeBasic) creating class instances ---
    nodea : 
     pos(m) = [0.0, 0.0], fxc = [False, False], lcn = [0, 1] 
    dsp(m) = [0.0, 0.001], efc(N) = [10000.0, 0.0]
    nodeb : 
     pos(m) = [1.0, 1.0], fxc = [False, False], lcn = [0, 1] 
    dsp(m) = [0.0, 0.002], efc(N) = [20000.0, 0.0]
    
    ## --- section_mb: (GMTrussNodeBasic) calculating node to node ---
    nodea.post_2node(nodeb) = [1.0, 1.0]
    nodeb.post_2node(nodea) = [-1.0, -1.0]
    nodea.dist_2node(nodeb) = 1.4142135623730951
    nodeb.dist_2node(nodea) = 1.4142135623730951
    nodea.dirc_2node(nodeb) = 0.7853981633974483
    nodeb.dirc_2node(nodea) = -2.356194490192345
    nodea.unitvect_2node(nodeb) = [0.7071067811865476, 0.7071067811865476]
    nodeb.unitvect_2node(nodea) = [-0.7071067811865475, -0.7071067811865476]
    '''
