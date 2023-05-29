# gm_c06_OOP_TrussStructure_Basic_C_truss_structure.py: coded by Kinya MIURA 230518
# -----------------------------------------------------------------------------
print("\n*** (GMTrussStructureAdvanced) class for segment ***")
print("  *** class GMTrussNodeAdvanced, GMTrussMemberAdvanced are embedded as nodes and membsb ***")
print("# -----------------------------------------------------------------------------")

# -----------------------------------------------------------------------------
print("## --- section__: (GMTrussStructureAdvanced) importing items from module ---")
from numpy import (
    ndarray, array, append, zeros as zers, full, ix_,
    dot as dott, linalg)
from gm_c06_OOP_TrussStructure_Advanced_B_truss_member import (GMTrussNodeAdvanced, GMTrussMemberAdvanced)

# -----------------------------------------------------------------------------
print("## --- section_a: (GMTrussStructureAdvanced) declaring class ---")
class GMTrussStructureAdvanced():
    # -----------------------------------------------------------------------------
    print("## --- section_b: (GMTrussStructureAdvanced) initializing class instance ---")
    def __init__(self, nodes: list, membs: list):
        self._nodes, self._membs = [], []
        self.__numnode, self.__nummemb, self.__dfrd = 0, 0, 0
        self._disp, self._exfc = array([]), array([])
        self._stif = array([[]])
        self.set_truss_structure(nodes, membs)

    # -----------------------------------------------------------------------------
    print("## --- section_c: (GMTrussStructureAdvanced) setting and getting functions ---")
    ## setting functions
    def set_truss_structure(self, nodes: list, membs: list) -> None:
        self._nodes, self._membs = nodes, membs
        self.__nnode, self.__nmemb = len(self._nodes), len(self._membs)
        self.__dfrd = self.__nnode * len(self._nodes[0].xxyy())
        self._fixc = full((self.__dfrd,), False)
        self._disp, self._exfc = zers((self.__dfrd,)), zers((self.__dfrd,))
        self._stif = zers((self.__dfrd, self.__dfrd,))
        #  mtxeq = GMMtxEq(nrow=self.__dfrd, ncol=self.__dfrd)

    ## getting functions
    def nnode(self) -> int: return self.__nnode
    def nmemb(self) -> int: return self.__nmemb
    def dfrd(self) -> int: 
        return self.__dfrd

    # -----------------------------------------------------------------------------
    print("## --- section_d: (GMTrussStructureAdvanced) string function ---")
    def __str__(self):
        st  = (
            f'nnode = {self.nnode():d}, nmemb = {self.nmemb():d}, dfrd = {self.dfrd():d} ' )
        return st
    def prtcls(self, idx: str = '') -> None:
        print(idx + ':: GMTrussStructureAdvanced ::')
        print(self.__str__())
        for i, node in enumerate(self._nodes):
            print(f'GMTrussNodeAdvanced[{i:02d}]: ---------- '); node.prtcls()
        for i, memb in enumerate(self._membs):
            print(f'GMTrussMemberAdvanced[{i:02d}]: ---------- '); memb.prtcls()
 
    # -----------------------------------------------------------------------------
    print("## --- section_e: (GMTrussStructureAdvanced) calculating truss structure ---")
    def buld_mtxeq(self) -> None:  # building matrix equation
        # building matrix
        for memb in self._membs:
            stif = memb.buld_stif()
            locn = memb.locn()
            for i, ilocn in enumerate(locn):
                for j, jlocn in enumerate(locn):
                    self._stif[ilocn,jlocn] += stif[i,j]
        # building vectors
        for node in self._nodes:
            for (fixc,locn,disp,exfc) in zip(
                    node.fixc(),node.locn(),node._disp.xxyy(False),node._exfc.xxyy(False)):
                self._fixc[locn] = fixc
                self._disp[locn] = disp
                self._exfc[locn] = exfc

    def solv_mtxeq(self) -> None:  # solving matrix equation
        # setting work space
        fixs = [i for i, fixc in enumerate(self._fixc) if fixc ]
        fres = [i for i, fixc in enumerate(self._fixc) if not fixc ]
        # setting working matrix and vectors
        aa, aa_co = self._stif[ix_(fres, fres)], self._stif[ix_(fres, fixs)]
        bb, xx_co = self._exfc[ix_(fres)], self._disp[ix_(fixs)]
        bb -= dott(aa_co,xx_co)
        # solving matrix equation
        xx = linalg.solve(aa,bb)
        for i, fre in enumerate(fres):
            self._disp[fre] = xx[i]
        self._exfc = dott(self._stif,self._disp)
        # modifying nodes
        for i, node in enumerate(self._nodes):
            xxyy = []
            for locn in node.locn():
                xxyy.append(self._disp[locn])
            self._nodes[i]._disp.set_xxyy(xxyy, cnv=False)
        for memb in self._membs:
            memb.calc_strt()


    # -----------------------------------------------------------------------------
    print("## --- section_f: (GMTrussStructureAdvanced) drawing figure ---")
    def graph(self,
            scl_dfm: float = 0.05, scl_frc: float = 0.005,
            xlim: tuple =(-1, 2.), ylim: tuple = (-1.0, 2.0) ) -> None:
        import matplotlib.pyplot as plt

        # -----------------------------------------------------------------------------
        print('## --- section_f1: setting figure ---')
        plt.rcdefaults()  # initializing drawing environment
        fig, ax = plt.subplots(figsize=(8., 6.))
        fig.suptitle('Truss Deformation Behavior with Forces')
        ax.set_aspect('equal')
        leng = 1.
        ax.set_xlim(xlim); ax.set_ylim(ylim)
        ax.hlines(0., -0.5, +1.5, linestyle='-', color='black', linewidth=2.)

        # -----------------------------------------------------------------------------
        print('## --- section_f2: drawing reference truss frame ---')
        ## truss members
        for memb in membs:
            xx, yy = append(
                memb._nodea.xxyy().reshape(2,1),
                memb._nodeb.xxyy().reshape(2,1), axis=1)
            ax.plot( xx, yy,
                color='0.7', linewidth=3., linestyle='-', zorder=1 )
        ## truss nodes
        for node in nodes:
            xx, yy = node.xxyy(False)
            ax.scatter( xx, yy,
                marker='o', s=120., color='1.0', linewidth=2., edgecolor='0.7',
                zorder=2 )

        # -----------------------------------------------------------------------------
        print('## --- section_f3: drawing deformed truss frame ---')
        ## truss members
        for memb in membs:
            xx, yy = append(
                (memb._nodea.xxyy() + memb._nodea._disp.xxyy() * scl_dfm).reshape(2,1),
                (memb._nodeb.xxyy() + memb._nodeb._disp.xxyy() * scl_dfm ).reshape(2,1), axis=1)
            ax.plot( xx, yy,
                color='0.0', linewidth=3., linestyle='-', zorder=3 )
        ## truss nodes and external forces
        for node in nodes:
            xx, yy = node.xxyy() + node._disp.xxyy() * scl_dfm
            ax.scatter( xx, yy,
                marker='o', s=120., color='1.0', linewidth=2.0, edgecolor='0.0', zorder=4)
            dxx, dyy = node._rafc.xxyy() * scl_frc
            if abs(dxx) > leng / 100. or abs(dyy) > leng / 100.:
                ax.arrow( xx-dxx, yy - dyy, dxx, dyy,
                    width=0.02, length_includes_head=True, color='red', zorder=5)

        # -----------------------------------------------------------------------------
        print('## --- section_f5: saving and showing figure ---')
        fig.savefig('gm_c06_OOP_TruessStructure_Advanced.png')
        plt.show()

#
# ////////////////////////////////////////////////////////////////////////////
#
if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    print("\n## --- section_ma: (GMTrussStructureAdvanced) setting nodes, membs, and strc ---")
    ## setting nodes
    nodes = list(range(4))
    leng, exfc = 1., 100.  # (m), (kN)
    nodes[0] = GMTrussNodeAdvanced(
        xxyy=(leng*0, leng*0), fixc=(True, True), locn=(0, 1) )
    nodes[1] = GMTrussNodeAdvanced(
        xxyy=(leng*1, leng*0), fixc=(True, True), locn=(2, 3) )
    nodes[2] = GMTrussNodeAdvanced(
        xxyy=(leng*0, leng*1), fixc=(False, False), locn=(4, 5) )
    nodes[2]._exfc.set_vector(xxyy=(exfc, 0.))
    nodes[3] = GMTrussNodeAdvanced(
        xxyy=(leng*1, leng*1), fixc=(False, False), locn=(6, 7) )
    ## setting membs
    area, yong = 10., 205.  # (cm^2), (kN/mm^2
    membs = list(range(4))
    membs[0] = GMTrussMemberAdvanced(
        nodea=nodes[0], nodeb=nodes[2], area=area, yong=yong)
    membs[1] = GMTrussMemberAdvanced(
        nodea=nodes[1], nodeb=nodes[3], area=area, yong=yong)
    membs[2] = GMTrussMemberAdvanced(
        nodea=nodes[2], nodeb=nodes[3], area=area, yong=yong)
    membs[3] = GMTrussMemberAdvanced(
        nodea=nodes[0], nodeb=nodes[3], area=area, yong=yong)

    strc = GMTrussStructureAdvanced(nodes=nodes, membs=membs)

    # -----------------------------------------------------------------------------
    print("## --- section_mb: (GMTrussStructureAdvanced) setting nodes, membs, and strc ---")
    strc.buld_mtxeq()
    print(f'{strc._stif = }')
    print(f'{strc._fixc = }')
    print(f'{strc._disp = }')
    print(f'{strc._exfc = }')

    strc.solv_mtxeq()
    strc.prtcls('strc -> ')

    # -----------------------------------------------------------------------------
    print("## --- section_mc: (GMTrussStructureAdvanced) drawing figure ---")
    strc.graph(scl_dfm=0.05, scl_frc=0.005, xlim=(-1,2.), ylim=(-1.0, 2.0))

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMTrussStructureAdvanced) class for segment ***
      *** class GMTrussNodeAdvanced, GMTrussMemberAdvanced are embedded as nodes and membsb ***
    # -----------------------------------------------------------------------------
    ## --- section__: (GMTrussStructureAdvanced) importing items from module ---
    
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
    ## --- section_a: (GMTrussStructureAdvanced) declaring class ---
    ## --- section_b: (GMTrussStructureAdvanced) initializing class instance ---
    ## --- section_c: (GMTrussStructureAdvanced) setting and getting functions ---
    ## --- section_d: (GMTrussStructureAdvanced) string function ---
    ## --- section_e: (GMTrussStructureAdvanced) calculating truss structure ---
    ## --- section_f: (GMTrussStructureAdvanced) drawing figure ---
    
    ## --- section_ma: (GMTrussStructureAdvanced) setting nodes, membs, and strc ---
    ## --- section_mb: (GMTrussStructureAdvanced) setting nodes, membs, and strc ---
    strc -> :: GMTrussStructureAdvanced ::
    nnode = 4, nmemb = 4, dfrd = 8 
    GMTrussNodeAdvanced[00]: ---------- 
    :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1
      fixc: ndarray:[ True  True] 
      locn: ndarray:[0 1]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (-100, -100) : (rr,th) = (141.421, -135) : unt = 1000
    GMTrussNodeAdvanced[01]: ---------- 
    :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unt = 1
      fixc: ndarray:[ True  True] 
      locn: ndarray:[2 3]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 100) : (rr,th) = (100, 90) : unt = 1000
    GMTrussNodeAdvanced[02]: ---------- 
    :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[4 5]
      disp: GMVector:: (xx,yy) = (2.35533, 0) : (rr,th) = (2.35533, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (100, 0) : (rr,th) = (100, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (100, 0) : (rr,th) = (100, 0) : unt = 1000
    GMTrussNodeAdvanced[03]: ---------- 
    :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[6 7]
      disp: GMVector:: (xx,yy) = (1.86753, -0.487805) : (rr,th) = (1.93018, -14.6388) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    GMTrussMemberAdvanced[00]: ---------- 
    :: GMTrussMemberAdvanced ::
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = 0, epsl (1/1000) = 0, sigm (kN/m^2) = 0, axfc(kN) = 0 
    nodea -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1
      fixc: ndarray:[ True  True] 
      locn: ndarray:[0 1]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (-100, -100) : (rr,th) = (141.421, -135) : unt = 1000
    nodeb -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[4 5]
      disp: GMVector:: (xx,yy) = (2.35533, 0) : (rr,th) = (2.35533, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (100, 0) : (rr,th) = (100, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (100, 0) : (rr,th) = (100, 0) : unt = 1000
    GMTrussMemberAdvanced[01]: ---------- 
    :: GMTrussMemberAdvanced ::
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = -0.487805, epsl (1/1000) = -0.487805, sigm (kN/m^2) = -100000, axfc(kN) = -100 
    nodea -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (1, 0) : (rr,th) = (1, 0) : unt = 1
      fixc: ndarray:[ True  True] 
      locn: ndarray:[2 3]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 100) : (rr,th) = (100, 90) : unt = 1000
    nodeb -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[6 7]
      disp: GMVector:: (xx,yy) = (1.86753, -0.487805) : (rr,th) = (1.93018, -14.6388) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    GMTrussMemberAdvanced[02]: ---------- 
    :: GMTrussMemberAdvanced ::
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = -0.487805, epsl (1/1000) = -0.487805, sigm (kN/m^2) = -100000, axfc(kN) = -100 
    nodea -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 1) : (rr,th) = (1, 90) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[4 5]
      disp: GMVector:: (xx,yy) = (2.35533, 0) : (rr,th) = (2.35533, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (100, 0) : (rr,th) = (100, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (100, 0) : (rr,th) = (100, 0) : unt = 1000
    nodeb -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[6 7]
      disp: GMVector:: (xx,yy) = (1.86753, -0.487805) : (rr,th) = (1.93018, -14.6388) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    GMTrussMemberAdvanced[03]: ---------- 
    :: GMTrussMemberAdvanced ::
    area (cm^2) = 10, yong (kN/mm^2) = 205 
    delt (mm) = 0.97561, epsl (1/1000) = 0.68986, sigm (kN/m^2) = 141421, axfc(kN) = 141.421 
    nodea -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1
      fixc: ndarray:[ True  True] 
      locn: ndarray:[0 1]
      disp: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (-100, -100) : (rr,th) = (141.421, -135) : unt = 1000
    nodeb -> :: GMTrussNodeAdvanced ::
      (super) GMPoint:: (xx,yy) = (1, 1) : (rr,th) = (1.41421, 45) : unt = 1
      fixc: ndarray:[False False] 
      locn: ndarray:[6 7]
      disp: GMVector:: (xx,yy) = (1.86753, -0.487805) : (rr,th) = (1.93018, -14.6388) : unt = 0.001
      exfc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
      rafc: GMVector:: (xx,yy) = (0, 0) : (rr,th) = (0, 0) : unt = 1000
    ## --- section_mc: (GMTrussStructureAdvanced) drawing figure ---
    ## --- section_f1: setting figure ---
    ## --- section_f2: drawing reference truss frame ---
    ## --- section_f3: drawing deformed truss frame ---
    ## --- section_f5: saving and showing figure ---
    '''
