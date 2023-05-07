# gm_c04_MatrixCalculation_B0_ndarray: coded by Kinya MIURA 230505
# -----------------------------------------------------------------------------
print("\n*** POP for solving Truss Structure C0: enhanced by using 'function' ***")
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- block__: importing libraries ---')
from numpy import (  # 'numpy' library
    sqrt as sr, square as sq, cos, sin, arctan2 as atan2,
    rad2deg as r2d, deg2rad as d2r,
    ndarray, array, append, ix_, zeros as zers, full,
    dot, tensordot as tdot, linalg ) 

# -----------------------------------------------------------------------------
print('## --- block_a: setting truss structure ---')
def set_truss() -> tuple:
    # -----------------------------------------------------------------------------
    print('## --- block_a1: setting truss nodes ---')
    ll = 1.  # (m) reference size of struss structure
    ef = 100. * 1000.  # (kN) external force
    # 'ndarray' structure *
    posx, posy = (  # coordinate for position
        array([0., ll, 0., ll]), array([0., 0., ll, ll]) )
    lcnx, lcny = (  # location in global matrix
        [0, 2, 4, 6], [1, 3, 5, 7] )
    fxcx, fxcy = (  # fixity condition
        [True, True, False, False], [True, True, False, False] )
    dspx, dspy = (  # displacement
        array([0., 0., 0., 0.]), array([0., 0., 0., 0.]) )
    efcx, efcy = (  # external force
        array([0., 0., ef, 0.]), array([0., 0., 0., 0.]) )
    # -----------------------------------------------------------------------------
    print('## --- block_a2: setting truss members ---')
    ar  = 10. * 0.0001  # (cm^2) sectional area
    yn = 205. * 1000000000.  # (kN/mm^2) Young's modulus
    nodea, nodeb = (  # node number for end nodes a and b
        array([0, 1, 2, 0]), array([2, 3, 3, 3]) )
    ara, yng = full(len(nodea), ar), full(len(nodea), yn)
        # (cm^2) sectional area, (kN/mm^2) Young's modulus
    dxx, dyy = posx[nodeb]-posx[nodea], posy[nodeb]-posy[nodea]
    lng, tht = sr(sq(dxx)+sq(dyy)), atan2(dyy,dxx)
        # (m) length, (deg) direction angle
    # dlt (mm); strech, eps (0.001); tensile strain
    # sgm (kN/m^2); tensile stress, afc (kN); axial force
    return ( 
        posx,posy,lcnx,lcny,
        fxcx,fxcy,dspx,dspy,efcx,efcy,
        nodea,nodeb, ara,yng,lng,tht )

# -----------------------------------------------------------------------------
print('\n## --- block_b: building global matrix equation ---')
def buld_mtxeq() -> array:
    dfrd = posx.size + posy.size
    stf = zers([dfrd,dfrd])  # global matrix 
    dsp, efc = zers(dfrd), zers(dfrd)  # global vectors
    fxc = full(dfrd, [True])  # global fixity condition vector
    # -----------------------------------------------------------------------------
    print('## --- block_b1: building global matrix ---')
    vct = array([(cos(itht),sin(itht)) for itht in tht])
    sf = array([  # local stiffness matrix
        icof * tdot(append(-ivct,ivct),append(-ivct,ivct),axes=0)
        for icof, ivct in zip(yng*ara/lng,vct)])
    lcnv = [  # location number vector of member
        array([lcnx[inodea],lcny[inodea],lcnx[inodeb],lcny[inodeb]]) 
        for inodea, inodeb in zip(nodea,nodeb) ]
    for ilcnv, isf in zip(lcnv,sf):
        stf[ix_(ilcnv,ilcnv)] += isf
    # -----------------------------------------------------------------------------
    print('## --- block_b1: building global vectors ---')
    dsp[ix_(lcnx)], dsp[ix_(lcny)] = dspx, dspy  # displacement
    efc[ix_(lcnx)], efc[ix_(lcny)] = efcx, efcy  # external force
    fxc[ix_(lcnx)], fxc[ix_(lcny)] = fxcx, fxcy  # fixity condition
    return (vct,stf, dsp,efc,fxc)

# -----------------------------------------------------------------------------
print('\n## --- block_c: solving global matrix equation ---')
def solv_mtxeq(dsp,efc,fxc) -> tuple:
    # -----------------------------------------------------------------------------
    print('## --- block_c1: preparing working space ---')
    fix = [i for i, ifxc in enumerate(fxc) if ifxc ]
    fre = [i for i, ifxc in enumerate(fxc) if not ifxc ]
    # -----------------------------------------------------------------------------
    print('## --- block_c2: setting working matrix and vectors ---')
    aa, aa_co = stf[ix_(fre, fre)], stf[ix_(fre, fix)]
    bb, xx_co = efc[ix_(fre)], dsp[ix_(fix)]
    # -----------------------------------------------------------------------------
    print('## --- block_c3: solving matrix equation ---')
    bb -= dot(aa_co,xx_co)
    xx = linalg.solve(aa,bb)  # solve partial matrix equation
    dsp[ix_(fre)] = xx
    efc = dot(stf,dsp)
    return (dsp,efc)

# -----------------------------------------------------------------------------
print('\n## --- block_d: calculating truss structure ---')
def calc_truss(dsp,efc) -> tuple:
    # -----------------------------------------------------------------------------
    print('## --- block_d1: calculating truss nodes ---')
    print('block Da: calculating behavior of truss nodes :')
    dspx, dspy = dsp[ix_(lcnx)], dsp[ix_(lcny)]
    efcx, efcy = efc[ix_(lcnx)], efc[ix_(lcny)]
    # -----------------------------------------------------------------------------
    print('## --- block_d2: calculating truss members ---')
    dlt = array([
        dot(append(-ivct,ivct),
            array([dspx[inodea],dspy[inodea],dspx[inodeb],dspy[inodeb]]) ) 
        for (inodea,inodeb,ivct) in zip(nodea,nodeb,vct) ])
    eps = dlt / lng
    sgm = yng * eps  
    afc = ara * sgm
    return (dspx,dspy,efcx,efcy, dlt,eps,sgm,afc)

# -----------------------------------------------------------------------------
print('\n## --- block_e: printing truss structure ---')
def prnt_truss(
        posx,posy,lcnx,lcny, dspx,dspy,efcx,efcy, 
        nodea,nodeb, ara,yng,lng,tht,dlt,eps,sgm,afc) -> None:
    # -----------------------------------------------------------------------------
    print('## --- block_e1: converting units and printing truss nodes ---')
    dspx /= 0.001  # (mm)
    dspy /= 0.001  # (mm)
    efcx /= 1000.  # (kN)
    efcy /= 1000.  # (kN)
    print('posx(m) =', posx)
    print('posy(m) =', posy)
    print('lcnx =', lcnx)
    print('lcny =', lcny)
    print('dspx(mm) =', dspx)
    print('dspy(mm) =', dspy)
    print('efcx(kN) =', efcx)
    print('efcy(kN) =', efcy)
    # -----------------------------------------------------------------------------
    print('## --- block_e2: converting units and printing truss members ---')
    ara /= 0.0001  # (cm^2)
    yng /= 1000000000.  # (kN/mm^2)
    lng /= 1.  # (m)
    tht = r2d(tht)  # (deg)
    dlt /= 0.001  # (mm)
    eps /= 0.001  # (1/1000)
    sgm /= 1000.  # (kN/m^2)  
    afc /= 1000.  # (kN)
    print(f'{nodea = }, {nodeb = }')
    print('ara(cm^2) =', ara)
    print('yng(kN/mm^2) =', yng)
    print('lng(m) =', lng)
    print('tht(deg) =', tht)
    print('dlt(mm) =', dlt)
    print('eps(1/1000) =', eps)
    print('sgm(kN/m^2) =', sgm)
    print('afc(kN) =', afc)

# calling block A
(posx,posy,lcnx,lcny,
 fxcx,fxcy,dspx,dspy,efcx,efcy,
 nodea,nodeb, ara,yng,lng,tht) = set_truss()
# calling block B 
(vct,stf, dsp,efc,fxc) = buld_mtxeq()
# calling block C
(dsp,efc) = solv_mtxeq(dsp,efc,fxc)
# calling block D
(dspx,dspy,efcx,efcy, dlt,eps,sgm,afc) = calc_truss(dsp,efc)
# calling block E
prnt_truss(
    posx,posy,lcnx,lcny, dspx,dspy,efcx,efcy, 
    nodea,nodeb, ara,yng,lng,tht,dlt,eps,sgm,afc)


# =============================================================================
# terminal log / terminal log / terminal log /
'''
C:\Users\Kinya_MIURA\GMPyC03MatrixCalculationMethod\Scripts\python.exe C:\Users\Kinya_MIURA\PycharmProjects\GMPythonCourse\GMPyC03MatrixCalculationMethod\gm_c04_MatrixCalculation_C0_func.py 

*** POP for solving Truss Structure C0: enhanced by using 'function' ***
# -----------------------------------------------------------------------------
## --- block__: importing libraries ---
## --- block_a: setting truss structure ---

## --- block_b: building global matrix equation ---

## --- block_c: solving global matrix equation ---

## --- block_d: calculating truss structure ---

## --- block_e: printing truss structure ---
## --- block_a1: setting truss nodes ---
## --- block_a2: setting truss members ---
## --- block_b1: building global matrix ---
## --- block_b1: building global vectors ---
## --- block_c1: preparing working space ---
block Ca: setting working space : 
## --- block_c2: setting working matrix and vectors ---
## --- block_c3: solving matrix equation ---
## --- block_d1: calculating truss nodes ---
block Da: calculating behavior of truss nodes :
## --- block_d2: calculating truss members ---
## --- block_e1: converting units and printing truss nodes ---
posx(m) = [0. 1. 0. 1.]
posy(m) = [0. 0. 1. 1.]
lcnx = [0, 2, 4, 6]
lcny = [1, 3, 5, 7]
dspx(mm) = [0.         0.         2.3553303  1.86752543]
dspy(mm) = [ 0.00000000e+00  0.00000000e+00 -1.44222386e-16 -4.87804878e-01]
efcx(kN) = [-1.00000000e+02  6.12323400e-15  1.00000000e+02  8.00355338e-14]
efcy(kN) = [-100.  100.    0.    0.]
## --- block_e2: converting units and printing truss members ---
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
