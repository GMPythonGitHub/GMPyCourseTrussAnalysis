## gm_c01_c1_triangle_sides.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** calculation of triangle from side lengths ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing items from module ---')
import sys
from numpy import (sqrt, arccos, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting side lengths ---')
sdea, sdeb, sdec = 3, 4, 5
print(f'Side length: a, b, c = {sdea}, {sdeb}, {sdec}')
if (sdea >= sdeb + sdec) or (sdeb >= sdec + sdea) or (sdec >= sdea + sdeb):
    print('! the triangle cannot be formed !!!')
    sys.exit()  # exiting from the process

# -----------------------------------------------------------------------------
print("\n## --- section_b: calculating angles using cosine formula ---")
anga = arccos((sdeb*sdeb + sdec*sdec - sdea*sdea) / (2*sdeb*sdec))
angb = arccos((sdec*sdec + sdea*sdea - sdeb*sdeb) / (2*sdec*sdea))
angc = arccos((sdea*sdea + sdeb*sdeb - sdec*sdec) / (2*sdea*sdeb))
print(f'Angles: A, B, C = {r2d(anga):g}, {r2d(angb):g}, {r2d(angc):g} (deg)')

# -----------------------------------------------------------------------------
print("\n## --- section_c: calculating area using Heron's formula ---")
ss = (sdea + sdeb + sdec) / 2
area = sqrt(ss * (ss-sdea) * (ss-sdeb) * (ss-sdec))
print(f'Area: S = {area:g}')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of triangle from side lengths ***
# -----------------------------------------------------------------------------
## --- section__: importing items from module ---
## --- section_a: setting side lengths ---
Side length: a, b, c = 3, 4, 5
## --- section_b: calculating angles ---
Angles: A, B, C = 36.8699, 53.1301, 90 (deg)
## --- section_c: calculating area ---
Area: S = 6
'''
