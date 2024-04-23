# gm_c01_SimpleStruct_Ex_simple_structure: coded by Kinya MIURA 240423
# -----------------------------------------------------------------------------
print('\n*** solving Simple Structure Ex: truss structure ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print("## --- section__: importing items from 'numpy' ---")
from numpy import (pi, sqrt, cos, sin, tan, arctan, rad2deg, deg2rad)

# -----------------------------------------------------------------------------
print('## --- section_a: setting member ---')
ll = 1.
lngax, lngay, lngbx, lngby = ll, ll, 0, ll  # Ex_A
# lngax, lngay, lngbx, lngby = 0, ll, -ll, ll  # Ex_B
# lngax, lngay, lngbx, lngby = ll, ll, -ll, ll  # Ex_C
# horizontal and vertical lengths (m)
lnga, thta = sqrt(lngax**2 + lngay**2), arctan(lngay/lngax)  # Ex_A
lngb, thtb = sqrt(lngbx**2 + lngby**2), pi / 2.
# lnga, thta = sqrt(lngax**2 + lngay**2), pi / 2.  # Ex_A
# lngb, thtb = sqrt(lngbx**2 + lngby**2), arctan(lngby/lngbx)
# lnga, thta = sqrt(lngax**2 + lngay**2), arctan(lngay/lngax)  # Ex_A
# lngb, thtb = sqrt(lngbx**2 + lngby**2), arctan(lngby/lngbx)
# length (m) and direction angle (rad)
ara, yng = 10., 205.
# sectional area (cm^2), Young's modulus (kN/mm^2)
araa = arab = ara * 1e-4  # converting unit: (m^2)
ynga = yngb = yng * 1e9  # converting unit: (N/m^2)

# -----------------------------------------------------------------------------
print('## --- section_b: setting external force on node B ---')
frc = 100.  # external forces on node b (kN)
frcbx = frc * 1e3  # converting unit: (N)
frcby = 0.

# -----------------------------------------------------------------------------
print('## --- section_d: calculating behavior ---')
# afca * cos(thta) + afcb * cos(thtb) = frcbx
# afca * sin(thta) + afcb * sin(thtb) = frcby
afca =  (+ sin(thtb) * frcbx  - cos(thtb) * frcby) / (cos(thta) * sin(thtb) - sin(thta) * cos(thtb))
afcb =  (- sin(thta) * frcbx  + cos(thta) * frcby) / (cos(thta) * sin(thtb) - sin(thta) * cos(thtb))

rfcax, rfcay = - afca * cos(thta), - afca * sin(thta)
rfccx, rfccy = - afcb * cos(thtb), - afcb * sin(thtb)

sgma = afca / araa; sgmb = afcb / arab
epsa = sgma / ynga; epsb = sgmb / yngb
dlta = epsa * lnga; dltb = epsb * lngb

# dlta = dspbx * cos(thta) + dspby * sin(thta)
# dltb = dspbx * cos(thtb) + dspby * sin(thtb)
dspbx = (+ sin(thtb) * dlta - sin(thta) * dltb) / (cos(thta) * sin(thtb) - cos(thtb) * sin(thta))
dspby = (- cos(thtb) * dlta + cos(thta) * dltb) / (cos(thta) * sin(thtb) - cos(thtb) * sin(thta))

# -----------------------------------------------------------------------------
print('## --- section_e: printing calculated behavior ---')
print(
    ':: member_a : \n'
    f'\tlngh (m) = {lngax:5g}, lngv (m) = {lngay:5g}, '
    f'lng (m) = {lnga:5g}, tht (deg) = {rad2deg(thta):5g}, \n'
    f'\tara (cm^2) = {araa/1e-4:5g}, yng (kN/mm^2) = {ynga/1e9:5g}, \n'
    f'\tafc (kN) = {afca/1e3:5g}, sgm (kN/m^2) = {sgma/1e3:5g}, \n'
    f'\teps (1/1000) = {epsa/1e-3:5g}, dlt (mm) = {dlta/1e-3:5g}' )
print(
    ':: member_b : \n'
    f'\tlngh (m) = {lngbx:5g}, lngv (m) = {lngby:5g}, '
    f'lng (m) = {lngb:5g}, tht (deg) = {rad2deg(thtb):5g}, \n'
    f'\tara (cm^2) = {arab/1e-4:5g}, yng (kN/mm^2) = {yngb/1e9:5g}, \n'
    f'\tafc (kN) = {afcb/1e3:5g}, sgm (kN/m^2) = {sgmb/1e3:5g}, \n'
    f'\teps (1/1000) = {epsb/1e-3:5g}, dlt (mm) = {dltb/1e-3:5g}' )
print(
    ':: node A : \n'
    f'\trfcax (kN) = {rfcax/1e3:5g}, rfcay (kN) = {rfcay/1e3:5g}' )
print(
    ':: node B : \n'
    f'\tfrcbx (kN) = {frcbx/1e3:5g}, frcby (kN) = {frcby/1e3:5g}, '
    f'dspbx (mm) = {dspbx/1e-3:5g}, dspby (mm) = {dspby/1e-3:5g}' )
print(
    ':: node C : \n'
    f'\trfccx (kN) = {rfccx/1e3:5g}, rfccy (kN) = {rfccy/1e3:5g}' )

# =============================================================================
# terminal log / terminal log / terminal log /
'''

'''
