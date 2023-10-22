## gm_c01_c2_triangle_sides.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** calculation of triangle from side lengths ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing items from module ---')
import sys
from numpy import (sqrt, arcsin, rad2deg as r2d)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting side lengths ---')
side_aa, side_bb, side_cc = 3, 4, 5
print(f'Side length: a, b, c = {side_aa}, {side_bb}, {side_cc}')
if (side_aa >= side_bb + side_cc) or (side_bb >= side_cc + side_aa) or (side_cc >= side_aa + side_bb):
    print('! the triangle cannot be formed !!!')
    sys.exit()  # exiting from the process

# -----------------------------------------------------------------------------
print("\n## --- section_b: calculating area using Heron's formula ---")
sss = (side_aa + side_bb + side_cc) / 2
area = sqrt(sss * (sss-side_aa) * (sss-side_bb) * (sss-side_cc))
print(f'Area = {area:g}')

# -----------------------------------------------------------------------------
print("\n## --- section_c: calculating angles using sine formula ---")
angle_aa = arcsin(2 * area / side_bb / side_cc)
angle_bb = arcsin(2 * area / side_cc / side_aa)
angle_cc = arcsin(2 * area / side_aa / side_bb)
print(f'Angle: A, B, C = {r2d(angle_aa):g}, {r2d(angle_bb):g}, {r2d(angle_cc):g} (deg)')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of triangle from side lengths ***
# -----------------------------------------------------------------------------
## --- section__: importing items from module ---
## --- section_a: setting side lengths ---
Side length: a, b, c = 3, 4, 5
## --- section_b: calculating area ---
Area: S = 6
## --- section_c: calculating angles using sine formula ---
Angles: A, B, C = 36.8699, 53.1301, 90 (deg)

'''
