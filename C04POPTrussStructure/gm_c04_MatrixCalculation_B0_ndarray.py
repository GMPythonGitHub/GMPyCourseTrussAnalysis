# gm_c04_MatrixCalculation_B0_ndarray: coded by Kinya MIURA 230505
# -----------------------------------------------------------------------------
print("\n*** POP for solving Truss Structure B0: enhanced by using 'ndarray' ***")
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- block__: importing libraries ---')
from numpy import (
    sqrt as sr, square as sq, cos, sin, arctan2 as atan2,
    rad2deg as r2d, deg2rad as d2r,
    ndarray, array, append, ix_, zeros as zers, full,
    dot, tensordot as tdot, linalg )

# -----------------------------------------------------------------------------
print('## --- block_a: setting truss structure ---')
# -----------------------------------------------------------------------------
print('## --- block_a1: setting truss nodes ---')
ll = 1.  # (m) reference length for truss structure
ef = 100. * 1000.  # (kN) external force
posx, posy = array([0., ll, 0., ll]), array([0., 0., ll, ll])  # coordinate of position
fxcx, fxcy = [True, True, False, False], [True, True, False, False]  # fixity condition
lcnx, lcny = [0, 2, 4, 6], [1, 3, 5, 7]  # location in global matrix
dspx, dspy = array([0., 0., 0., 0.]), array([0., 0., 0., 0.])  # displacement
efcx, efcy = array([0., 0., ef, 0.]), array([0., 0., 0., 0.])  # external force
# -----------------------------------------------------------------------------
print('## --- block_a2: setting truss members ---')
ar  = 10. * 0.0001  # (cm^2) sectional area
yn = 205. * 1000000000.  # (kN/mm^2) Young's modulus
nodea, nodeb = array([0, 1, 2, 0]), array([2, 3, 3, 3])
    # node number of nodes A and B
ara, yng = full(len(nodea), ar), full(len(nodea), yn)
    # (cm^2) sectional area, (kN/mm^2) Young's modulus
dxx, dyy = posx[nodeb]-posx[nodea], posy[nodeb]-posy[nodea]
lng, tht = sr(sq(dxx)+sq(dyy)), atan2(dyy,dxx)
    # (m) length, (deg) direction angle

# -----------------------------------------------------------------------------
print('\n## --- block_b: building global matrix equation ---')
dfrd = posx.size + posy.size
stf = zers([dfrd,dfrd])  # global matrix 
dsp, efc = zers(dfrd), zers(dfrd)  # global vectors
fxc = full(dfrd, [True])  # global fixity condition vector
# -----------------------------------------------------------------------------
print('## --- block_b1: building global matrix ---')
vct = array([(cos(itht),sin(itht)) for itht in tht])  # unit vector
sf = array([  # local stiffness matrix
    icof * tdot(append(-ivct,ivct),append(-ivct,ivct),axes=0)
    for icof, ivct in zip(yng*ara/lng,vct)])
lcnv = [  # location number vector of member
    array([lcnx[inodea],lcny[inodea],lcnx[inodeb],lcny[inodeb]]) 
    for inodea, inodeb in zip(nodea,nodeb) ]
for ilcnv, isf in zip(lcnv,sf):
    stf[ix_(ilcnv,ilcnv)] += isf
# -----------------------------------------------------------------------------
print('## --- block_b2: building global vectors ---')
dsp[ix_(lcnx)], dsp[ix_(lcny)] = dspx, dspy  # displacement
efc[ix_(lcnx)], efc[ix_(lcny)] = efcx, efcy  # external force
fxc[ix_(lcnx)], fxc[ix_(lcny)] = fxcx, fxcy  # fixity condition

# -----------------------------------------------------------------------------
print('\n## --- block_c: solving global matrix equation ---')
# -----------------------------------------------------------------------------
print('## --- block_c1: preparing working space ---')
fix = [i for i, ifxc in enumerate(fxc) if ifxc ]
fre = [i for i, ifxc in enumerate(fxc) if not ifxc ]
# -----------------------------------------------------------------------------
print('## --- block_c2: setting working matrix and vectors ---')
aa, aa_co = stf[ix_(fre,fre)], stf[ix_(fre,fix)]
bb, xx_co = efc[ix_(fre)], dsp[ix_(fix)]
# -----------------------------------------------------------------------------
print('## --- block_c3: solving matrix equation ---')
bb -= dot(aa_co,xx_co)
xx = linalg.solve(aa, bb)  # solve partial matrix equation
dsp[ix_(fre)] = xx
efc = dot(stf, dsp)

# -----------------------------------------------------------------------------
print('\n## --- block_d: calculating truss structure ---')
# -----------------------------------------------------------------------------
print('## --- block_d1: calculating truss nodes ---')
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

# -----------------------------------------------------------------------------
print('\n## --- block_e: printing truss structure ---')
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

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** POP for solving Truss Structure B0: enhanced by using 'ndarray' ***
# -----------------------------------------------------------------------------
## --- block__: importing libraries ---
## --- block_a: setting truss structure ---
## --- block_a1: setting truss nodes ---
## --- block_a2: setting truss members ---

## --- block_b: building global matrix equation ---
## --- block_b1: building global matrix ---
## --- block_b2: building global vector ---

## --- block_c: solbing global matrix equation ---
## --- block_c1: preparing working space ---
## --- block_c2: setting working matrix ---
## --- block_c3: setting working vectors ---
## --- block_c4: solving matrix equation ---

## --- block_d: calculating truss structure ---
## --- block_d1: calculating truss nodes ---
## --- block_d2: calculating truss members ---

## --- block_e: printing truss structure ---
## --- block_e1: converting units and printing truss nodes ---
posx(m) = [0.0, 1.0, 0.0, 1.0]
posy(m) = [0.0, 0.0, 1.0, 1.0]
lcnx = [0, 2, 4, 6]
lcny = [1, 3, 5, 7]
dspx(mm) = [0.0, 0.0, 2.355330304754239, 1.867525426705459]
dspy(mm) = [0.0, 0.0, -1.4422238593260196e-16, -0.48780487804878087]
efcx(kN) = [-100.00000000000003, 6.123233995736769e-15, 99.99999999999994, 8.003553375601768e-14]
efcy(kN) = [-100.00000000000003, 100.00000000000004, 0.0, 0.0]
## --- block_e2: converting units and printing truss members ---
nodea = [0, 1, 2, 0]
nodeb = [2, 3, 3, 3]
ara(cm^2) = [10.0, 10.0, 10.0, 10.0]
yng(kN/mm^2) = [205.0, 205.0, 205.0, 205.0]
lng(m) = [1.0, 1.0, 1.0, 1.4142135623730951]
tht(deg) = [90.0, 90.0, 0.0, 45.0]
dlt(mm) = [0.0, -0.48780487804878075, -0.48780487804878025, 0.9756097560975612]
eps(1/1000) = [0.0, -0.48780487804878075, -0.48780487804878025, 0.6898602743283392]
sgm(kN/m^2) = [0.0, -100000.00000000006, -99999.99999999996, 141421.35623730952]
afc(kN) = [0.0, -100.00000000000006, -99.99999999999996, 141.4213562373095]
'''
