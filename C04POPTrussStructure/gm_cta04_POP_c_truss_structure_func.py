# gm_cta04_POP_c_truss_structure_func: coded by Kinya MIURA 230505
# -----------------------------------------------------------------------------
print("\n*** POP for solving Truss Structure ver. c: enhanced by using 'function' ***")
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section__: importing libraries ---')
from numpy import (  # importing module 'numpy'
    sqrt as sr, square as sq, cos, sin, arctan2 as atan2,
    rad2deg as r2d, deg2rad as d2r,
    ndarray, array, append, ix_, zeros as zers, full,
    dot as iprd, tensordot as tprd, logical_not as loginot, linalg )

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting truss structure ---')
def set_truss():
    global posx, posy, lcnx, lcny
    global fxcx, fxcy, dspx, dspy, efcx, efcy
    global nodea, nodeb,  ara, yng, lng, tht
    # -----------------------------------------------------------------------------
    print('## --- section_a1: setting truss nodes ---')
    ll = 1.  # 1(m) reference length
    ef = 100. * 1e3  # 100(kN) external force
    posx, posy = array([0., ll, 0., ll]), array([0., 0., ll, ll])  # (m) position coordinate
    fxcx, fxcy = [True, True, False, False], [True, True, False, False]  # fixity condition
    lcnx, lcny = [0, 2, 4, 6], [1, 3, 5, 7]  # location in global matrix equation
    dspx, dspy = array([0., 0., 0., 0.]), array([0., 0., 0., 0.])  # (m) displacement
    efcx, efcy = array([0., 0., ef, 0.]), array([0., 0., 0., 0.])  # (N) external force
    # -----------------------------------------------------------------------------
    print('## --- section_a2: setting truss members ---')
    ar = 10. * 1e-4  # 10(cm^2) sectional area
    yn = 205. * 1e9  # 205(kN/mm^2) Young's modulus
    nodea, nodeb = array([0, 1, 2, 0]), array([2, 3, 3, 3])
    # node number of nodes A and B
    ara, yng = full(len(nodea), ar), full(len(nodea), yn)
    # (m^2) sectional area, (N/m^2) Young's modulus
    dxx, dyy = posx[nodeb] - posx[nodea], posy[nodeb] - posy[nodea]
    lng, tht = sr(sq(dxx) + sq(dyy)), atan2(dyy, dxx)
    # (m) length, (rad) theta; direction angle

# -----------------------------------------------------------------------------
print('\n## --- section_b: building global matrix equation ---')
def buld_mtxeq():
    global vct, stf, lcn
    global stf_glb, dsp_glb, efc_glb, fxc_glb
    dfrd = posx.size + posy.size
    stf_glb = zers([dfrd, dfrd])  # global matrix
    dsp_glb, efc_glb = zers(dfrd), zers(dfrd)  # global vectors
    fxc_glb = full(dfrd, [True])  # global fixity condition vector
    # -----------------------------------------------------------------------------
    print('## --- section_b1: building global matrix ---')
    vct = array([(cos(itht), sin(itht)) for itht in tht])  # unit vector
    stf = array([  # local stiffness matrix
        icof * tprd(append(-ivct, ivct), append(-ivct, ivct), axes=0)
        for icof, ivct in zip(yng * ara / lng, vct)])
    lcn = [  # location number vector of member
        array([lcnx[inodea], lcny[inodea], lcnx[inodeb], lcny[inodeb]])
        for inodea, inodeb in zip(nodea, nodeb)]
    for (ilcn, istf) in zip(lcn, stf):
        stf_glb[ix_(ilcn, ilcn)] += istf
    # -----------------------------------------------------------------------------
    print('## --- section_b2: building global vectors ---')
    dsp_glb[ix_(lcnx)], dsp_glb[ix_(lcny)] = dspx, dspy  # displacement
    efc_glb[ix_(lcnx)], efc_glb[ix_(lcny)] = efcx, efcy  # external force
    fxc_glb[ix_(lcnx)], fxc_glb[ix_(lcny)] = fxcx, fxcy  # fixity condition

# -----------------------------------------------------------------------------
print('\n## --- section_c: solving global matrix equation ---')
def solv_mtxeq():
    global dsp_gbl, efc_glb
    # -----------------------------------------------------------------------------
    print('## --- section_c1: setting working matrix and vectors ---')
    aa = stf_glb[ix_(loginot(fxc_glb), loginot(fxc_glb))]
    bb = efc_glb[ix_(loginot(fxc_glb))] - iprd(stf_glb[ix_(fxc_glb)], dsp_glb)
    # -----------------------------------------------------------------------------
    print('## --- section_c2: solving working matrix equation ---')
    xx = linalg.solve(aa, bb)  # solve partial matrix equation
    dsp_glb[ix_(loginot(fxc_glb))] = xx
    efc_glb = iprd(stf_glb, dsp_glb)

# -----------------------------------------------------------------------------
print('\n## --- section_d: calculating truss structure ---')
def calc_truss():
    global dspx, dspy, efcx, efcy
    global dlt, eps, sgm, afc
    # -----------------------------------------------------------------------------
    print('## --- section_d1: calculating truss nodes ---')
    dspx, dspy = dsp_glb[ix_(lcnx)], dsp_glb[ix_(lcny)]
    efcx, efcy = efc_glb[ix_(lcnx)], efc_glb[ix_(lcny)]
    # -----------------------------------------------------------------------------
    print('## --- section_d2: calculating truss members ---')
    dlt = array([
        iprd(append(-ivct, ivct),
             array([dspx[inodea], dspy[inodea], dspx[inodeb], dspy[inodeb]]))
        for (inodea, inodeb, ivct) in zip(nodea, nodeb, vct)])
    eps = dlt / lng
    sgm = yng * eps
    afc = ara * sgm

# -----------------------------------------------------------------------------
print('\n## --- section_e: printing truss structure ---')
def prnt_truss():
    global posx, posy, lcnx, lcny
    global fxcx, fxcy, dspx, dspy, efcx, efcy
    global nodea, nodeb, ara, yng, lng, tht
    global dlt, eps, sgm, afc
    # -----------------------------------------------------------------------------
    print('## --- section_e1: converting units and printing truss nodes ---')
    dspx /= 1e-3; dspy /= 1e-3  # (mm)
    efcx /= 1e3; efcy /= 1e3  # (kN)
    print('posx(m) =', posx); print('posy(m) =', posy)
    print('lcnx =', lcnx); print('lcny =', lcny)
    print('dspx(mm) =', dspx); print('dspy(mm) =', dspy)
    print('efcx(kN) =', efcx); print('efcy(kN) =', efcy)
    # -----------------------------------------------------------------------------
    print('## --- section_e2: converting units and printing truss members ---')
    ara /= 1e-4  # (cm^2)
    yng /= 1e9  # (kN/mm^2)
    lng /= 1.  # (m)
    tht = r2d(tht)  # (deg)
    dlt /= 1e-3  # (mm)
    eps /= 1e-3  # (1/1000)
    sgm /= 1e3  # (kN/m^2)
    afc /= 1e3  # (kN)
    print(f'{nodea = }, {nodeb = }')
    print('ara(cm^2) =', ara); print('yng(kN/mm^2) =', yng)
    print('lng(m) =', lng); print('tht(deg) =', tht)
    print('dlt(mm) =', dlt); print('eps(1/1000) =', eps)
    print('sgm(kN/m^2) =', sgm); print('afc(kN) =', afc)

print('\n  --- calling functions ---')
set_truss()  # calling section A
buld_mtxeq()  # calling section B
solv_mtxeq()  # calling section C
calc_truss()  # calling section D
prnt_truss()  # calling section E

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** POP for solving Truss Structure ver. c: enhanced by using 'function' ***
# -----------------------------------------------------------------------------
## --- section__: importing libraries ---

## --- section_a: setting truss structure ---

## --- section_b: building global matrix equation ---

## --- section_c: solving global matrix equation ---

## --- section_d: calculating truss structure ---

## --- section_e: printing truss structure ---

  --- calling functions ---
## --- section_a1: setting truss nodes ---
## --- section_a2: setting truss members ---
## --- section_b1: building global matrix ---
## --- section_b2: building global vectors ---
## --- section_c1: setting working matrix and vectors ---
## --- section_c2: solving working matrix equation ---
## --- section_d1: calculating truss nodes ---
## --- section_d2: calculating truss members ---
## --- section_e1: converting units and printing truss nodes ---
posx(m) = [0. 1. 0. 1.]
posy(m) = [0. 0. 1. 1.]
lcnx = [0, 2, 4, 6]
lcny = [1, 3, 5, 7]
dspx(mm) = [0.         0.         2.3553303  1.86752543]
dspy(mm) = [ 0.00000000e+00  0.00000000e+00 -1.44222386e-16 -4.87804878e-01]
efcx(kN) = [-1.00000000e+02  6.12323400e-15  1.00000000e+02  8.00355338e-14]
efcy(kN) = [-100.  100.    0.    0.]
## --- section_e2: converting units and printing truss members ---
nodea = array([0, 1, 2, 0]), nodeb = array([2, 3, 3, 3])
ara(cm^2) = [10. 10. 10. 10.]
yng(kN/mm^2) = [205. 205. 205. 205.]
lng(m) = [1.         1.         1.         1.41421356]
tht(deg) = [90. 90.  0. 45.]
dlt(mm) = [ 0.         -0.48780488 -0.48780488  0.97560976]
eps(1/1000) = [ 0.         -0.48780488 -0.48780488  0.68986027]
sgm(kN/m^2) = [      0.         -100000.         -100000.          141421.35623731]
afc(kN) = [   0.         -100.         -100.          141.42135624]
'''
