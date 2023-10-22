## gm_c01_d_triangle_points.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** calculation of triangle from points: drawing figure ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing items from module ---')
from numpy import (sqrt, sin, arccos, rad2deg)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting three points ---')
point_aa, point_bb, point_cc = (0,0), (2,0), (1,2)  # using 'tuple'
print(f'Points: point_aa, point_bb, point_cc = {point_aa}, {point_bb}, {point_cc}')

# -----------------------------------------------------------------------------
print("\n## --- section_b: calculating sides using Pythagoras' theorem ---")
side_aa = sqrt((point_cc[0]-point_bb[0])**2 + (point_cc[1]-point_bb[1])**2)
side_bb = sqrt((point_aa[0]-point_cc[0])**2 + (point_aa[1]-point_cc[1])**2)
side_cc = sqrt((point_bb[0]-point_aa[0])**2 + (point_bb[1]-point_aa[1])**2)
print(f'Side length: a, b, c = {side_aa:g}, {side_bb:g}, {side_cc:g}')

# -----------------------------------------------------------------------------
print("\n## --- section_c: calculating angles using cosine formula ---")
angle_aa = arccos((side_bb**2 + side_cc**2 - side_aa**2) / (2*side_bb*side_cc))
angle_bb = arccos((side_cc**2 + side_aa**2 - side_bb**2) / (2*side_cc*side_aa))
angle_cc = arccos((side_aa**2 + side_bb**2 - side_cc**2) / (2*side_aa*side_bb))
print(f'Angle: A, B, C = {rad2deg(angle_aa):g}, {rad2deg(angle_bb):g}, {rad2deg(angle_cc):g} (deg)')

# -----------------------------------------------------------------------------
print("\n## --- section_d: calculating area using Heron's formula ---")
sss = (side_aa + side_bb + side_cc) / 2
area = sqrt(sss * (sss-side_aa) * (sss-side_bb) * (sss-side_cc))
print(f'Area = {area:g}')

# -----------------------------------------------------------------------------
print("\n## --- section_e: calculating gravity center ---")
point_gg = (
    (point_aa[0] + point_bb[0] + point_cc[0]) / 3,
    (point_aa[1] + point_bb[1] + point_cc[1]) / 3 )
print(f'gravity center: (xx,yy) = ({point_gg[0]:g}, {point_gg[1]:g})')

# -----------------------------------------------------------------------------
print("\n## --- section_f: calculating inscribed circle ---")
iii = (side_aa + side_bb + side_cc)
radius_ii = 2 * area / iii
point_ii = (
    (side_aa*point_aa[0] + side_bb*point_bb[0] + side_cc*point_cc[0]) / iii,
    (side_aa*point_aa[1] + side_bb*point_bb[1] + side_cc*point_cc[1]) / iii )
print(f'radius = {radius_ii:g},   Inner center: (xx,yy) = ({point_ii[0]:g}, {point_ii[1]:g})')

# -----------------------------------------------------------------------------
print("\n## --- section_g: calculating circumscribed circle ---")
ooo = sin(2*angle_aa) + sin(2*angle_bb) + sin(2*angle_cc)
radius_oo = side_aa / sin(angle_aa) / 2
point_oo = (
    (sin(2*angle_aa)*point_aa[0] + sin(2*angle_bb)*point_bb[0] + sin(2*angle_cc)*point_cc[0]) / ooo,
    (sin(2*angle_aa)*point_aa[1] + sin(2*angle_bb)*point_bb[1] + sin(2*angle_cc)*point_cc[1]) / ooo )
print(f'radius = {radius_oo:g},   Outer center: (xx,yy) = ({point_oo[0]:g}, {point_oo[1]:g})')

# -----------------------------------------------------------------------------
print("\n## --- section_h: drawing triangle and circles ---")
''' dwawing triangle and circles '''
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 6.))
fig.suptitle('triangle and circles')
ax.plot(
    (point_aa[0], point_bb[0], point_cc[0], point_aa[0]),
    (point_aa[1], point_bb[1], point_cc[1], point_aa[1]),
    linestyle='-', linewidth=2, color='C0')
ax.scatter(
    (point_aa[0], point_bb[0], point_cc[0]),
    (point_aa[1], point_bb[1], point_cc[1]),
    marker='o', s=40, color='C0', edgecolor='C0')

ax.scatter(point_gg[0], point_gg[1],
    marker='o', s=40, color='C1', edgecolor='C1',
    label='gravity center')

ptc = pat.Circle(xy=point_ii, radius=radius_ii,
    linestyle='--', linewidth=2., edgecolor='C2', fill=False)
ax.add_patch(ptc)
ax.scatter(point_ii[0], point_ii[1],
    marker='o', s=40, color='C2', edgecolor='C2',
    label='inscribed circle')

ptc = pat.Circle(xy=point_oo, radius=radius_oo,
    linestyle='--', linewidth=2., edgecolor='C3', fill=False)
ax.add_patch(ptc)
ax.scatter(point_oo[0], point_oo[1],
    marker='o', s=40, color='C3', edgecolor='C3',
    label='circumscribed circle')

ax.set_aspect('equal')
ax.legend()
fig.savefig('gm_c01_d_triangle_points.png')
plt.show()

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# terminal log
'''
*** calculation of triangle from points: drawing figure ***
# -----------------------------------------------------------------------------
## --- section__: importing items from module ---
## --- section_a: setting three points ---
Points: point_aa, point_bb, point_cc = (0, 0), (2, 0), (1, 2)
## --- section_b: calculating sides using Pythagoras' theorem ---
Side length: a, b, c = 2.23607, 2.23607, 2
## --- section_c: calculating angles using cosine formula ---
Angle: A, B, C = 63.4349, 63.4349, 53.1301 (deg)
## --- section_d: calculating area using Heron's formula ---
Area = 2
## --- section_e: calculating gravity center ---
gravity center: (xx,yy) = (1, 0.666667)
## --- section_f: calculating inscribed circle ---
radius = 0.618034,   Inner center: (xx,yy) = (1, 0.618034)
## --- section_g: calculating circumscribed circle ---
radius = 1.25,   Outer center: (xx,yy) = (1, 0.75)
## --- section_h: drawing triangle and circles ---
'''

