# gm_c01_SimpleStruct_A0_single_vertical: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** solving Simple Structure A0: single member vertical ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- block_a: setting member ---')
lng = 1.  # length (m)
print('lng(m) = ', lng)
ara = 10. * 1e-4  # sectional area (cm^2 > m^2)
print('ara(m^2) = ', ara)
yng = 205. * 1e9  # Young's modulus (kN/mm^2 > N/m^2)
print('yng(N/m^2) = ', yng)
frc = 100. * 1e3 # force vertical (kN > N)
print('frc(N) = ', frc)

# -----------------------------------------------------------------------------
print('\n## --- block_b: calculating behavior ---')
rfc = -frc  # reaction force (N)
print('rfc(N) = ', rfc)
afc = -rfc  # axial force (N)
print('afc(N) = ', afc)
sgm = afc / ara  # axial stress (N\m^2)
print('sgm(N/m^2) = ', sgm)
eps = sgm / yng  # axial strain ( )
print('eps( ) = ', eps)
dlt = eps * lng  # stretch (m)
print('dlt(m) = ', dlt)
dsp = dlt  # displacement (m)
print('dsp(m) = ', dsp)

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** solving Simple Structure A0: single member vertical ***
# -----------------------------------------------------------------------------
## --- block_a: setting member ---
lng(m) =  1.0
ara(m^2) =  0.001
yng(N/m^2) =  205000000000.0
frc(N) =  100000.0

## --- block_b: calculating behavior ---
rfc(N) =  -100000.0
afc(N) =  100000.0
sgm(N/m^2) =  100000000.0
eps( ) =  0.0004878048780487805
dlt(m) =  0.0004878048780487805
dsp(m) =  0.0004878048780487805
'''