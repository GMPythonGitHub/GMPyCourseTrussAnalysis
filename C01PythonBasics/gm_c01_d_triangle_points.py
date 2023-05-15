## gm_c01_d_triangle_points.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** calculation of triangle from points ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing items from module ---')
from numpy import (sqrt, sin, arccos, rad2deg)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting three points ---')
pnta, pntb, pntc = (0,0), (2,0), (1,2)  # using 'tuple'
print(f'Points: pnta, pntb, pntc = {pnta}, {pntb}, {pntc}')

# -----------------------------------------------------------------------------
print("\n## --- section_b: calculating sides using Pythagoras' theorem ---")
sdea = sqrt((pntc[0]-pntb[0])**2 + (pntc[1]-pntb[1])**2)
sdeb = sqrt((pnta[0]-pntc[0])**2 + (pnta[1]-pntc[1])**2)
sdec = sqrt((pntb[0]-pnta[0])**2 + (pntb[1]-pnta[1])**2)
print(f'Side length: a, b, c = {sdea:g}, {sdeb:g}, {sdec:g}')

# -----------------------------------------------------------------------------
print("\n## --- section_c: calculating angles using cosine formula ---")
anga = arccos((sdeb*sdeb + sdec*sdec - sdea*sdea) / (2*sdeb*sdec))
angb = arccos((sdec*sdec + sdea*sdea - sdeb*sdeb) / (2*sdec*sdea))
angc = arccos((sdea*sdea + sdeb*sdeb - sdec*sdec) / (2*sdea*sdeb))
print(f'Angles: A, B, C = {rad2deg(anga):g}, {rad2deg(angb):g}, {rad2deg(angc):g} (deg)')

# -----------------------------------------------------------------------------
print("\n## --- section_d: calculating area using Heron's formula ---")
ss = (sdea + sdeb + sdec) / 2
area = sqrt(ss * (ss-sdea) * (ss-sdeb) * (ss-sdec))
print(f'Area: S = {area:g}')

# -----------------------------------------------------------------------------
print("\n## --- section_e: calculating gravity center ---")
pntg = (
    (pnta[0] + pntb[0] + pntc[0]) / 3,
    (pnta[1] + pntb[1] + pntc[1]) / 3 )
print(f'gravity center: (pgx,pgy) = ({pntg[0]:g}, {pntg[1]:g})')

# -----------------------------------------------------------------------------
print("\n## --- section_f: calculating inscribed circle ---")
ii = (sdea + sdeb + sdec)
rri = 2 * area / ii
pnti = (
    (sdea*pnta[0] + sdeb*pntb[0] + sdec*pntc[0]) / ii,
    (sdea*pnta[1] + sdeb*pntb[1] + sdec*pntc[1]) / ii )
print(f'Radius: ri = {rri:g},   Inner center: (pix,piy) = ({pnti[0]:g}, {pnti[1]:g})')

# -----------------------------------------------------------------------------
print("\n## --- section_g: calculating circumscribed circle ---")
oo = sin(2*anga) + sin(2*angb) + sin(2*angc)
rro = sdea / sin(anga) / 2
pnto = (
    (sin(2*anga)*pnta[0] + sin(2*angb)*pntb[0] + sin(2*angc)*pntc[0]) / oo,
    (sin(2*anga)*pnta[1] + sin(2*angb)*pntb[1] + sin(2*angc)*pntc[1]) / oo )
print(f'Radius: ro = {rro:g},   Outer center: (pox,poy) = ({pnto[0]:g}, {pnto[1]:g})')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of triangle from points ***
# -----------------------------------------------------------------------------
## --- section__: importing items from module ---
## --- section_a: setting three points ---
Points: pnta, pntb, pntc = (0, 0), (2, 0), (1, 2)
## --- section_b: calculating sides using Pythagoras' theorem ---
Side length: a, b, c = 2.23607, 2.23607, 2
## --- section_c: calculating angles using cosine formula ---
Angles: A, B, C = 63.4349, 63.4349, 53.1301 (deg)
## --- section_d: calculating area using Heron's formula ---
Area: S = 2
## --- section_e: calculating gravity center ---
gravity center: (pgx,pgy) = (1, 0.666667)
## --- section_f: calculating inscribed circle ---
Radius: ri = 0.618034,   Inner center: (pix,piy) = (1, 0.618034)
## --- section_g: calculating circumscribed circle ---
Radius: ro = 1.25,   Outer center: (pox,poy) = (1, 0.75)
'''

