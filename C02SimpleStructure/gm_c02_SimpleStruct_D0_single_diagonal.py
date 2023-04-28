# gm_c01_SimpleStruct_D0_single_diagonal: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** solving Simple Structure D0: single member diagonal ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print("## --- block__: importing items from 'numpy'  ---")
from numpy import (cos, sin, tan, arctan, rad2deg, deg2rad, sqrt)

# -----------------------------------------------------------------------------
print('## --- block_a: setting member  ---')
lngh, lngv = 1., 0.75
# horizontal and vertical lengths (m)
lng, tht = sqrt(lngh**2 + lngv**2), arctan(lngv/lngh)
# length (m) and direction angle (rad)
ara, yng = 10., 205.
# sectional area (cm^2), Young's modulus (kN/mm^2)
ara, yng = ara * 1e-4, yng * 1e9  # converting unit: (m^2), (N/m^2)

# -----------------------------------------------------------------------------
print('## --- block_b: setting external force on node B ---')
frcb = 100.  # external forces on node b (kN)
frcb = frcb * 1e3  # converting unit: (N)

# -----------------------------------------------------------------------------
print('## --- block_d: calculating behavior  ---')
rfcbx = frcb * tan(tht)
rfcax, rfcay = - rfcbx, - frcb
afc = - rfcax * sin(tht) - rfcay * cos(tht)
sgm = afc / ara
eps = sgm / yng
dlt = eps * lng
dspby = dlt / sin(tht)

# -----------------------------------------------------------------------------
print('## --- block_e: printing calculation results  ---')
print(
    ':: member : \n'
    f'\tlngh (m) = {lngh:5g}, lngv (m) = {lngv:5g}, '
    f'lng (m) = {lng:5g}, tht (deg) = {rad2deg(tht):5g}, \n'
    f'\tara (cm^2) = {ara/1e-4:5g}, yng (kN/mm^2) = {yng/1e9:5g}, \n'
    f'\tafc (kN) = {afc/1e3:5g}, sgm (kN/m^2) = {sgm/1e3:5g}, \n'
    f'\teps (1/1000) = {eps/1e-3:5g}, dlt (mm) = {dlt/1e-3:5g}' )
print(
    ':: node A : \n'
    f'\trfcax (kN) = {rfcax/1e3:5g}, rfcay (kN) = {rfcay/1e3:5g}' )
print(
    ':: node B : \n'
    f'\tfrcb (kN) = {frcb/1e3:5g}, rfcbx (kN) = {rfcbx/1e3:5g}, '
    f'dspby (mm) = {dspby/1e-3:5g}' )

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** solving Simple Structure D0: single member diagonal ***
# -----------------------------------------------------------------------------
## --- block__: importing items from 'numpy'  ---
## --- block_a: setting member  ---
## --- block_b: setting external force on node B ---
## --- block_d: calculating behavior  ---
## --- block_e: printing calculation results  ---
:: member : 
	lngh (m) =     1, lngv (m) =  0.75, lng (m) =  1.25, tht (deg) = 36.8699, 
	ara (cm^2) =    10, yng (kN/mm^2) =   205, 
	afc (kN) =   125, sgm (kN/m^2) = 125000, 
	eps (1/1000) = 0.609756, dlt (mm) = 0.762195
:: node A : 
	rfcax (kN) =   -75, rfcay (kN) =  -100
:: node B : 
	frcb (kN) =   100, rfcbx (kN) =    75, dspby (mm) = 1.27033
'''
