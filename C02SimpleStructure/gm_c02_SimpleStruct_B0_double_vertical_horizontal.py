# gm_c01_SimpleStruct_B0_double_vertical_horizontal: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** solving Simple Structure B0: double members vertical and horizontal ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: setting member a  ---')
lnga = 2.  # length (m)
print(f'lnga (m) = {lnga:g}')
araa = 10.  # sectional area (cm^2)
print(f'araa (cm^2) = {araa:g}'); araa *= 1e-4  # (cm^2 > m^2)  # multiple statement
ynga = 205.  # Young's modulus (kN/mm^2)
print(f'ynga (kN/mm^2) = {ynga:g}'); ynga *= 1e9  # (kN/mm^2 > N/m^2)

# -----------------------------------------------------------------------------
print('\n## --- section_b: setting member b  ---')
lngb = 1.  # length (m)
print(f'lngb (m) = {lngb:g}')
arab = 10.  # sectional area (cm^2)
print(f'arab (cm^2) = {arab:g}'); arab *= 1e-4  # (cm^2 > m^2)
yngb = 205.  # Young's modulus (kN/mm^2)
print(f'yngb (kN/mm^2) = {yngb:g}'); yngb *= 1e9  # (kN/mm^2 > N/m^2)

# -----------------------------------------------------------------------------
print('\n## --- section_c: setting external force on node B  ---')
frcx, frcy = 100., 50.  # force components (kN)
print(f'frcx, frcy (kN) = {frcx:g}, {frcy:g}')
frcx *= 1e3; frcy *= 1e3  # (kN > N) multiple statement

# -----------------------------------------------------------------------------
print('\n## --- section_d: calculating behavior  ---')
rfca, rfcc = -frcy, -frcx  # reaction forces (kN)
print(f'rfca, rfcb (kN) = {rfca/1e3:g}, {rfcc/1e3:g}')
afca, afcb = -rfca, -rfcc  # axial force (kN)
print(f'afca, afcb (kN) = {afca/1e3:g}, {afcb/1e3:g}')
sgma, sgmb = afca / araa, afcb / arab  # axial stress (kN/m^2)
print(f'sgma, sgmb (kN/m^2) = {sgma/1e3:g}, {sgmb/1e3:g}')
epsa, epsb = sgma / ynga, sgmb / yngb  # axial strain (1/0000)
print(f'epsa, epsb (micro) = {epsa/1e-3:g}, {epsb/1e-3:g}')
dspbx, dspby = dlta, dltb = epsa * lnga, epsb * lngb  # displacement (mm), stretch (mm)
print(f'dlta, dltb (mm) = {dlta/1e-3:g}, {dltb/1e-3:g}')
print(f'dspbx, dspby (mm) = {dspbx/1e-3:g}, {dspby/1e-3:g}')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** solving Simple Structure B0: double members vertical and horizontal ***
# -----------------------------------------------------------------------------
## --- section_a: setting member a  ---
lnga (m) = 2
araa (cm^2) = 10
ynga (kN/mm^2) = 205

## --- section_b: setting member b  ---
lngb (m) = 1
arab (cm^2) = 10
yngb (kN/mm^2) = 205

## --- section_c: setting external force on node B  ---
frcx, frcy (kN) = 100, 50

## --- section_d: calculating behavior  ---
rfca, rfcb (kN) = -50, -100
afca, afcb (kN) = 50, 100
sgma, sgmb (kN/m^2) = 50000, 100000
epsa, epsb (micro) = 0.243902, 0.487805
dlta, dltb (mm) = 0.487805, 0.487805
dspbx, dspby (mm) = 0.487805, 0.487805
'''
