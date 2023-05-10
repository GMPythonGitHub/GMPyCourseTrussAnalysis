# gm_c04_MatrixCalculation_B0_ndarray_fig: coded by Kinya MIURA 230505
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

# -----------------------------------------------------------------------------
print('\n## --- block_f: drawing truss structure ---')
# -----------------------------------------------------------------------------
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
print('## --- block_f1: setting figure ---')
scl_dfm, scl_frc = 0.05, 0.005  # setting scale
xlim, ylim = (-1, 2.), (-1.0, 2.0)  # setting drawing range
plt.rcdefaults()  # initializing drawing environment
fig, ax = plt.subplots(figsize=(8., 6.))
fig.suptitle('Truss Deformation Behavior')
ax.set_aspect('equal')
ax.set_xlim(xlim); ax.set_ylim(ylim)
ax.hlines(0., -0.5, +1.5, linestyle='-', color='black', linewidth=2.)

# -----------------------------------------------------------------------------
print('## --- block_f2: drawing reference truss frame ---')
## truss members
for inodea, inodeb in zip(nodea, nodeb):
    ax.plot(  # segment
        (posx[inodea], posx[inodeb]), (posy[inodea], posy[inodeb]),
        color='0.7', linewidth=3., linestyle='-', zorder=1)
## truss nodes
for iposx, iposy in zip(posx, posy):
    ax.scatter(  # point
        iposx, iposy,
        marker='o', s=120., color='1.0', linewidth=2., edgecolor='0.7',
        zorder=2)

# -----------------------------------------------------------------------------
print('## --- block_f3: drawing deformed truss frame ---')
## truss members
for inodea, inodeb in zip(nodea, nodeb):
    ax.plot(  # segment
        (posx[inodea] + dspx[inodea] * scl_dfm, posx[inodeb] + dspx[inodeb] * scl_dfm),
        (posy[inodea] + dspy[inodea] * scl_dfm, posy[inodeb] + dspy[inodeb] * scl_dfm),
        color='0.0', linewidth=3., linestyle='-', zorder=3)
## truss nodes and external forces
for iposx, iposy, idspx, idspy, iefcx, iefcy in zip(posx, posy, dspx, dspy, efcx, efcy):
    xx, yy = iposx + idspx * scl_dfm, iposy + idspy * scl_dfm,
    ax.scatter(  # point
        xx, yy,
        marker='o', s=120., color='1.0', linewidth=2.0, edgecolor='0.0', zorder=4)
    dxx, dyy = iefcx * scl_frc, iefcy * scl_frc
    if abs(dxx) > ll/100. or abs(dyy) > ll/100.:
        ax.arrow(  # arrow
            xx - dxx, yy - dyy, dxx, dyy,
            width=0.02, length_includes_head=True, color='red', zorder=5)

# -----------------------------------------------------------------------------
print('## --- block_f4: saving and showing figure ---')
fig.savefig('gm_c04_MatrixCalculation_B0_ndarray.png')
plt.show()

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
