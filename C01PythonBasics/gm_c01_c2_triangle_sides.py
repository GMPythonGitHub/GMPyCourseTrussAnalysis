# gm_c01_c2_triangle_sides.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** calculation of triangle from side lengths ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- block__: importing items from module ---')
import sys
from numpy import (sqrt, arcsin, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- block_a: setting side lengths ---')
sdea, sdeb, sdec = 3, 4, 5
print(f'Side length: a, b, c = {sdea}, {sdeb}, {sdec}')
if (sdea >= sdeb + sdec) or (sdeb >= sdec + sdea) or (sdec >= sdea + sdeb):
    print('! the triangle cannot be formed !!!')
    sys.exit()  # exiting from the process

# -----------------------------------------------------------------------------
print("\n## --- block_b: calculating area ---")
''' finding area using Heron's formula '''
ss = (sdea + sdeb + sdec) / 2
area = sqrt(ss * (ss-sdea) * (ss-sdeb) * (ss-sdec))
print(f'Area: S = {area:g}')

# -----------------------------------------------------------------------------
print("\n## --- block_c: calculating angles ---")
''' finding angles using cosine formula '''
anga = arcsin(2 * area / sdeb / sdec)
angb = arcsin(2 * area / sdec / sdea)
angc = arcsin(2 * area / sdea / sdeb)
print(f'Angles: A, B, C = {r2d(anga):g}, {r2d(angb):g}, {r2d(angc):g} (deg)')

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# terminal log
'''
*** calculation of triangle from side lengths ***
# -----------------------------------------------------------------------------
## --- block__: importing items from module ---
## --- block_a: setting side lengths ---
Side length: a, b, c = 3, 4, 5
## --- block_b: calculating area ---
Area: S = 6
## --- block_c: calculating angles ---
Angles: A, B, C = 36.8699, 53.1301, 90 (deg)

'''
