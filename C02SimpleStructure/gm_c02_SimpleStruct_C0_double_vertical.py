# gm_c01_SimpleStruct_C0_double_vertical: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** solving Simple Structure C0: double members vertical ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- block_a: setting member a  ---')
lnga, araa, ynga = 2., 10., 205.
# length (m), sectional area (cm^2), Young's modulus (kN/mm^2)
lnga, araa, ynga = lnga, araa * 1e-4, ynga * 1e9  # converting unit: (m), (m^2), (N/m^2)

# -----------------------------------------------------------------------------
print('## --- block_b: setting member b  ---')
lngb, arab, yngb = 1., 10., 205.
# length (m), sectional area (cm^2), Young's modulus (kN/mm^2)
lngb, arab, yngb = lngb, arab * 1e-4, yngb * 1e9  # converting unit: (m), (m^2), (N/m^2)

# -----------------------------------------------------------------------------
print('## --- block_c: setting external force on nodes B and C ---')
frcb, frcc = 100., 50.  # external forces (kN)
frcb, frcc = frcb * 1e3, frcc * 1e3  # converting unit: (N)

# -----------------------------------------------------------------------------
print('## --- block_d: calculating behavior  ---')
rfca = - (frcb + frcc)
afca, afcb = -rfca, frcc
sgma, sgmb = afca / araa, afcb / arab
epsa, epsb = sgma / ynga, sgmb / yngb
dlta, dltb = epsa * lnga, epsb * lngb
dspb, dspc = dlta, dlta + dltb

# -----------------------------------------------------------------------------
print('## --- block_e: printing calculation results  ---')
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
    f'\tfrcc (kN) = {frcc/1e3:5g}, dspc (mm) = {dspc/1e-3:5g}' )

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** solving Simple Structure C0: double members vertical ***
# -----------------------------------------------------------------------------
## --- block_a: setting member a  ---
## --- block_b: setting member b  ---
## --- block_c: setting external force on nodes B and C ---
## --- block_d: calculating behavior  ---
## --- block_e: printing calculation results  ---
:: member a : 
	lnga (m) =     2, araa (cm^2) =    10, ynga (kN/mm^2) =   205, 
	afca (kN) =   150, sgma (kN/m^2) = 150000, 
	epsa (1/1000) = 0.731707, dlta (mm) = 1.46341
:: member b : 
	lngb (m) =     1, arab (cm^2) =    10, yngb (kN/mm^2) =   205, 
	afcb (kN) =    50, sgmb (kN/m^2) = 50000, 
	epsb (1/1000) = 0.243902, dltb (mm) = 0.243902
:: node A : 
	rfca (kN) =  -150
:: node B : 
	frcb (kN) =   100, dspb (mm) = 1.46341
:: node C : 
	frcc (kN) =    50, dspc (mm) = 1.70732
'''
