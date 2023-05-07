# gm_c04_MatrixCalculation_A0_list: coded by Kinya MIURA 230505
# -----------------------------------------------------------------------------
print("\n*** POP for solving Truss Structure A0: enhanced by using 'list' ***")
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- block__: importing libraries ---')
import numpy as np  # import 'numpy' library

# -----------------------------------------------------------------------------
print('## --- block_a: setting truss structure ---')
nnode, nmemb = 4, 4  # number of nodes, number of members
dfrd = 2 * nnode  # degree of freedom
# -----------------------------------------------------------------------------
print('## --- block_a1: setting truss nodes ---')
ll = 1.  # (m) reference length for truss structure
ef = 100. * 1000.  # (kN) external force
posx = [0., ll, 0., ll]  # coordinate of position
posy = [0., 0., ll, ll]
fxcx = [True, True, False, False]  # fixity condition
fxcy = [True, True, False, False]
lcnx = [0, 2, 4, 6]  # location in global matrix
lcny = [1, 3, 5, 7]
dspx = [0., 0., 0., 0.]  # displacement
dspy = [0., 0., 0., 0.]
efcx = [0., 0., ef, 0.]  # external force
efcy = [0., 0., 0., 0.]
# -----------------------------------------------------------------------------
print('## --- block_a2: setting truss members ---')
ar  = 10. * 0.0001  # (cm^2) reference sectional area
yg = 205. * 1000000000.  # (kN/mm^2) common Young's modulus
nodea = [0, 1, 2, 0]  # node number of end node A
nodeb = [2, 3, 3, 3]  # node number of end node B
ara = [ar] * nmemb  # (m^2) sectional area
yng = [yg] * nmemb  # (N/m^2) Young's modulus
lng = [0.] * nmemb  # (m) length
tht = [0.] * nmemb  # (rad) direction angle, theta
dlt = [0.] * nmemb  # (m) strech, delta
eps = [0.] * nmemb  # ( ) tensile strain, epsilon 
sgm = [0.] * nmemb  # (N/m^2) tensile stress, sigma
afc = [0.] * nmemb  # (N) axial force
for i in range(nmemb):  # length and direction angle
    dxx = (posx[nodeb[i]]-posx[nodea[i]])
    dyy = (posy[nodeb[i]]-posy[nodea[i]])
    lng[i] = np.sqrt(np.square(dxx)+np.square(dyy))
    tht[i] = np.arctan2(dyy,dxx)

# -----------------------------------------------------------------------------
print('\n## --- block_b: building global matrix equation ---')
stf = [[0.]*dfrd for i in range(dfrd)]  # global stiffness matrix
dsp = [0.]*dfrd  # global displacement vector
efc = [0.]*dfrd  # global external force vector
fxc = [True]*dfrd  # global fixity condition vector
# -----------------------------------------------------------------------------
print('## --- block_b1: building global matrix ---')
for i in range(nmemb):
    co, sn = np.cos(tht[i]), np.sin(tht[i])
    cof = yng[i] * ara[i] / lng[i]
    ss = [  # local stiffness matrix
        [+co*co*cof, +co*sn*cof, -co*co*cof, -co*sn*cof],
        [+sn*co*cof, +sn*sn*cof, -sn*co*cof, -sn*sn*cof],
        [-co*co*cof, -co*sn*cof, +co*co*cof, +co*sn*cof],
        [-sn*co*cof, -sn*sn*cof, +sn*co*cof, +sn*sn*cof] ]
    lcnv = [  # location number vector in member
        lcnx[nodea[i]],lcny[nodea[i]],lcnx[nodeb[i]],lcny[nodeb[i]] ]
    for j in range(2*2):  # comprising global stiffness matrix
        for k in range(2*2):
            stf[lcnv[j]][lcnv[k]] += ss[j][k]
# -----------------------------------------------------------------------------
print('## --- block_b2: building global vector ---')
for i in range(nnode):
    dsp[lcnx[i]], dsp[lcny[i]] = dspx[i], dspy[i]  # displacement
    efc[lcnx[i]], efc[lcny[i]] = efcx[i], efcy[i]  # external force
    fxc[lcnx[i]], fxc[lcny[i]] = fxcx[i], fxcy[i]  # fixity condition

# -----------------------------------------------------------------------------
print('## --- block_c: solbing global matrix equation ---')
# -----------------------------------------------------------------------------
print('## --- block_c1: preparing working space ---')
wk = 0  # counting working space size
for i in range(dfrd):
    if not fxc[i]: wk += 1
aa = [[0.]*wk for i in range(wk)]  # matrix
bb, xx = [0.]*wk, [0.]*wk  # vectors
# -----------------------------------------------------------------------------
print('## --- block_c2: setting working matrix ---')
ii = 0
for i in range(dfrd):
    if not fxc[i]:
        jj = 0
        for j in range(dfrd):
            if not fxc[j]:
                aa[ii][jj] = stf[i][j]
                jj += 1
        ii += 1
# -----------------------------------------------------------------------------
print('## --- block_c3: setting working vectors ---')
ii = 0
for i in range(dfrd):
    if not fxc[i]:
        xx[ii], bb[ii] = dsp[i], efc[i]
        for j in range(dfrd):
            if fxc[j]: bb[ii] -= stf[i][j] * dsp[j]
        ii += 1
# -----------------------------------------------------------------------------
print('## --- block_c4: solving matrix equation ---')
xx = np.linalg.solve(aa,bb)
ii = 0
for i in range(dfrd):
    if not fxc[i]:
        dsp[i] = xx[ii]; ii += 1
for i in range(dfrd):
    efc[i] = 0.
    for j in range(dfrd):
        efc[i] += stf[i][j] * dsp[j]

# -----------------------------------------------------------------------------
print('\n## --- block_d: calculating truss structure ---')
# -----------------------------------------------------------------------------
print('## --- block_d1: calculating truss nodes ---')
for i in range(nnode):
    dspx[i], dspy[i] = dsp[lcnx[i]], dsp[lcny[i]]
    efcx[i], efcy[i] = efc[lcnx[i]], efc[lcny[i]]
# -----------------------------------------------------------------------------
print('## --- block_d2: calculating truss members ---')
for i in range(nmemb):
    co, sn = np.cos(tht[i]), np.sin(tht[i])
    dlt[i] = (
        -co*dspx[nodea[i]]-sn*dspy[nodea[i]]
        +co*dspx[nodeb[i]]+sn*dspy[nodeb[i]] )
    eps[i] = dlt[i] / lng[i]
    sgm[i] = yng[i] * eps[i]  
    afc[i] = ara[i] * sgm[i]

# -----------------------------------------------------------------------------
print('\n## --- block_e: printing truss structure ---')
# -----------------------------------------------------------------------------
print('## --- block_e1: converting units and printing truss nodes ---')
for i in range(nnode):
    dspx[i] /= 0.001  # (mm)
    dspy[i] /= 0.001  # (mm)
    efcx[i] /= 1000.  # (kN)
    efcy[i] /= 1000.  # (kN)
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
for i in range(nmemb):
    ara[i] /= 0.0001  # (cm^2)
    yng[i] /= 1000000000.  # (kN/mm^2)
    lng[i] /= 1.  # (m)
    tht[i] = np.rad2deg(tht[i])  # (deg)
    dlt[i] /= 0.001  # (mm)
    eps[i] /= 0.001  # (1/1000)
    sgm[i] /= 1000.  # (kN/m^2)  
    afc[i] /= 1000.  # (kN)
print('nodea =', nodea)
print('nodeb =', nodeb)
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
*** POP for solving Truss Structure A0: enhanced by using 'list' ***
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
