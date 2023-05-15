# gm_c01_SimpleStruct_C1_double_vertical_indeterminate: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** solving Simple Structure C1: double members vertical indeterminate structure ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: setting member a  ---')
lnga, araa, ynga = 2., 10., 205.
# length (m), sectional area (cm^2), Young's modulus (kN/mm^2)
lnga, araa, ynga = lnga, araa * 1e-4, ynga * 1e9  # converting unit: (m), (m^2), (N/m^2)

# -----------------------------------------------------------------------------
print('## --- section_b: setting member b  ---')
lngb, arab, yngb = 1., 10., 205.
# length (m), sectional area (cm^2), Young's modulus (kN/mm^2)
lngb, arab, yngb = lngb, arab * 1e-4, yngb * 1e9  # converting unit: (m), (m^2), (N/m^2)

# -----------------------------------------------------------------------------
print('## --- section_c: setting external force on nodes B and C --- *')
frcb = 100.  # external forces (kN)
frcb = frcb * 1e3  # converting unit: (N)

# -----------------------------------------------------------------------------
print('## --- section_d: calculating behavior  --- *')
rfcc = (
    - frcb * (lnga/ynga/araa)
    / (lnga/ynga/araa + lngb/yngb/arab) )
rfca = - (frcb + rfcc)
afca, afcb = -rfca, rfcc
sgma, sgmb = afca / araa, afcb / arab
epsa, epsb = sgma / ynga, sgmb / yngb
dlta, dltb = epsa * lnga, epsb * lngb
dspb = dlta

# -----------------------------------------------------------------------------
print('## --- section_e: printing calculation results  ---')
print(
    ':: member a : \n'
    f'\tlnga (m) = {lnga:5g}, araa (cm^2) = {araa/1e-4:5g}, ynga (kN/mm^2) = {ynga/1e9:5g}, \n'
    f'\tafca (kN) = {afca/1e3:5g}, sgma (kN/m^2) = {sgma/1e3:5g}, \n'
    f'\tepsa (1/1000) = {epsa/1e-3:5g}, dlta (mm) = {dlta/1e-3:5g}' )
print(
    ':: member b : \n'
    f'\tlngb (m) = {lngb:5g}, arab (cm^2) = {arab/1e-4:5g}, yngb (kN/mm^2) = {yngb/1e9:5g}, \n'
    f'\tafcb (kN) = {afcb/1e3:5g}, sgmb (kN/m^2) = {sgmb/1e3:5g}, \n'
    f'\tepsb (1/1000) = {epsb/1e-3:5g}, dltb (mm) = {dltb/1e-3:5g}' )
print(
    ':: node A : \n'
    f'\trfca (kN) = {rfca/1e3:5g}' )
print(
    ':: node B : \n'
    f'\tfrcb (kN) = {frcb/1e3:5g}, dspb (mm) = {dspb/1e-3:5g}' )
print(
    ':: node C : \n'
    f'\trfcc (kN) = {rfcc/1e3:5g}' )

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** solving Simple Structure C1: double members vertical indeterminate structure ***
# -----------------------------------------------------------------------------
## --- section_a: setting member a  ---
## --- section_b: setting member b  ---
## --- section_c: setting external force on nodes B and C --- *
## --- section_d: calculating behavior  --- *
## --- section_e: printing calculation results  ---
:: member a : 
	lnga (m) =     2, araa (cm^2) =    10, ynga (kN/mm^2) =   205, 
	afca (kN) = 33.3333, sgma (kN/m^2) = 33333.3, 
	epsa (1/1000) = 0.162602, dlta (mm) = 0.325203
:: member b : 
	lngb (m) =     1, arab (cm^2) =    10, yngb (kN/mm^2) =   205, 
	afcb (kN) = -66.6667, sgmb (kN/m^2) = -66666.7, 
	epsb (1/1000) = -0.325203, dltb (mm) = -0.325203
:: node A : 
	rfca (kN) = -33.3333
:: node B : 
	frcb (kN) =   100, dspb (mm) = 0.325203
:: node C : 
	rfcc (kN) = -66.6667
'''
