# gm_c01_SimpleStruct_C2_double_vertical_thermal: coded by Kinya MIURA 230412
# -----------------------------------------------------------------------------
print('\n*** solving Simple Structure C2: double members vertical thermal expansion ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- block_a: setting member a  --- *')
lnga, araa, ynga = 2., 10., 205.
# length (m), sectional area (cm^2), Young's modulus (kN/mm^2)
lnga, araa, ynga = lnga, araa * 1e-4, ynga * 1e9  # converting unit: (m), (m^2), (N/m^2)
alpa, tmpa = 11.7, 10.
# coefficient of thermal expansion (10^-6/K), temperature difference (K)
alpa, tmpa = alpa * 1e-6, tmpa

# -----------------------------------------------------------------------------
print('## --- block_b: setting member b  --- *')
lngb, arab, yngb = 1., 10., 205.
# length (m), sectional area (cm^2), Young's modulus (kN/mm^2)
lngb, arab, yngb = lngb, arab * 1e-4, yngb * 1e9  # converting unit: (m), (m^2), (N/m^2)
alpb, tmpb = 11.7, 10.
# coefficient of thermal expansion (10^-6/K), temperature difference (K)
alpb, tmpb = alpb * 1e-6, tmpb

# -----------------------------------------------------------------------------
print('## --- block_c: setting external force on nodes B and C --- *')
frcb = 100.  # external forces (kN)
frcb = frcb * 1e3  # converting unit: (N)

# -----------------------------------------------------------------------------
print('## --- block_d: calculating behavior  --- *')
rfcc = (
    - (frcb * (lnga/ynga/araa) + alpa*tmpa*lnga + alpb*tmpb*lngb)
    / (lnga/ynga/araa + lngb/yngb/arab) )
rfca = - (frcb + rfcc)
afca, afcb = -rfca, rfcc
sgma, sgmb = afca / araa, afcb / arab
epsa, epsb = sgma / ynga + alpa * tmpa, sgmb / yngb + alpb * tmpb
dlta, dltb = epsa * lnga, epsb * lngb
dspb = dlta

# -----------------------------------------------------------------------------
print('## --- block_e: printing calculation results  ---')
print(
    ':: member a : \n'
    f'\tlnga (m) = {lnga:5g}, araa (cm^2) = {araa/1e-4:5g}, ynga (kN/mm^2) = {ynga/1e9:5g}, \n'
    f'\talpa (10^-6/K) = {alpa/1e-6:5g}, tmpa (K) = {tmpa:5g}, \n'
    f'\tafca (kN) = {afca/1e3:5g}, sgma (kN/m^2) = {sgma/1e3:5g}, \n'
    f'\tepsa (1/1000) = {epsa/1e-3:5g}, dlta (mm) = {dlta/1e-3:5g}' )
print(
    ':: member b : \n'
    f'\tlngb (m) = {lngb:5g}, arab (cm^2) = {arab/1e-4:5g}, yngb (kN/mm^2) = {yngb/1e9:5g}, \n'
    f'\talpb (10^-6/K) = {alpb/1e-6:5g}, tmpb (K) = {tmpb:5g}, \n'
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
*** solving Simple Structure C2: double members vertical thermal expansion ***
# -----------------------------------------------------------------------------
## --- block_a: setting member a  --- *
## --- block_b: setting member b  --- *
## --- block_c: setting external force on nodes B and C --- *
## --- block_d: calculating behavior  --- *
## --- block_e: printing calculation results  ---
:: member a : 
	lnga (m) =     2, araa (cm^2) =    10, ynga (kN/mm^2) =   205, 
	alpa (10^-6/K) =  11.7, tmpa (K) =    10, 
	afca (kN) = 9.34833, sgma (kN/m^2) = 9348.33, 
	epsa (1/1000) = 0.162602, dlta (mm) = 0.325203
:: member b : 
	lngb (m) =     1, arab (cm^2) =    10, yngb (kN/mm^2) =   205, 
	alpb (10^-6/K) =  11.7, tmpb (K) =    10, 
	afcb (kN) = -90.6517, sgmb (kN/m^2) = -90651.7, 
	epsb (1/1000) = -0.325203, dltb (mm) = -0.325203
:: node A : 
	rfca (kN) = -9.34833
:: node B : 
	frcb (kN) =   100, dspb (mm) = 0.325203
:: node C : 
	rfcc (kN) = -90.6517
'''
