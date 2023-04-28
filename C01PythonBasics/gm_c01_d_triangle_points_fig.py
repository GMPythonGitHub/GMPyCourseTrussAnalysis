# gm_c01_d_triangle_points.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** calculation of triangle from points: drawing figure ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- block__: importing items from module ---')
from numpy import (sqrt, sin, arccos, rad2deg)

# -----------------------------------------------------------------------------
print('\n## --- block_a: setting three points ---')
pnta, pntb, pntc = [0,0], [2,0], [0,2]  # using 'list'
print(f'Points: pnta, pntb, pntc = {pnta}, {pntb}, {pntc}')

# -----------------------------------------------------------------------------
print("\n## --- block_b: calculating sides ---")
''' finding sides using Pythagoras' theorem '''
sdea = sqrt((pntc[0]-pntb[0])**2 + (pntc[1]-pntb[1])**2)
sdeb = sqrt((pnta[0]-pntc[0])**2 + (pnta[1]-pntc[1])**2)
sdec = sqrt((pntb[0]-pnta[0])**2 + (pntb[1]-pnta[1])**2)
print(f'Side length: a, b, c = {sdea:g}, {sdeb:g}, {sdec:g}')

# -----------------------------------------------------------------------------
print("\n## --- block_c: calculating angles ---")
''' finding angles using cosine formula '''
anga = arccos((sdeb*sdeb + sdec*sdec - sdea*sdea) / (2*sdeb*sdec))
angb = arccos((sdec*sdec + sdea*sdea - sdeb*sdeb) / (2*sdec*sdea))
angc = arccos((sdea*sdea + sdeb*sdeb - sdec*sdec) / (2*sdea*sdeb))
print(f'Angles: A, B, C = {rad2deg(anga):g}, {rad2deg(angb):g}, {rad2deg(angc):g} (deg)')

# -----------------------------------------------------------------------------
print("\n## --- block_d: calculating area ---")
''' finding area using Heron's formula '''
ss = (sdea + sdeb + sdec) / 2
area = sqrt(ss * (ss-sdea) * (ss-sdeb) * (ss-sdec))
print(f'Area: S = {area:g}')

# -----------------------------------------------------------------------------
print("\n## --- block_e: calculating gravity center ---")
''' finding gravity center '''
pntg = [
    (pnta[0] + pntb[0] + pntc[0]) / 3,
    (pnta[1] + pntb[1] + pntc[1]) / 3 ]
print(f'gravity center: (pgx,pgy) = [{pntg[0]:g}, {pntg[1]:g}]')

# -----------------------------------------------------------------------------
print("\n## --- block_f: calculating inscribed circle ---")
''' finding center and radius '''
ii = (sdea + sdeb + sdec)
rri = 2 * area / ii
pnti = [
    (sdea*pnta[0] + sdeb*pntb[0] + sdec*pntc[0]) / ii,
    (sdea*pnta[1] + sdeb*pntb[1] + sdec*pntc[1]) / ii ]
print(f'Radius: ri = {rri:g},   Inner center: (pix,piy) = [{pnti[0]:g}, {pnti[1]:g}]')

# -----------------------------------------------------------------------------
print("\n## --- block_g: calculating circumscribed circle ---")
''' finding center and radius '''
oo = sin(2*anga) + sin(2*angb) + sin(2*angc)
rro = sdea / sin(anga) / 2
pnto = [
    (sin(2*anga)*pnta[0] + sin(2*angb)*pntb[0] + sin(2*angc)*pntc[0]) / oo,
    (sin(2*anga)*pnta[1] + sin(2*angb)*pntb[1] + sin(2*angc)*pntc[1]) / oo ]
print(f'Radius: ro = {rro:g},   Outer center: (pox,poy) = [{pnto[0]:g}, {pnto[1]:g}]')

# -----------------------------------------------------------------------------
print("\n## --- block_h: drawing triangle and circles ---")
''' dwawing triangle and circles '''
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 6.))
fig.suptitle('triangle and circles')
ax.plot([pnta[0],pntb[0],pntc[0],pnta[0]], [pnta[1],pntb[1],pntc[1],pnta[1]],
    linestyle='-', linewidth=2, color='C0')
ax.scatter([pnta[0],pntb[0],pntc[0]], [pnta[1],pntb[1],pntc[1]],
    marker='o', s=40, color='C0', edgecolor='C0')

ax.scatter([pntg[0]], [pntg[1]],
    marker='o', s=40, color='C1', edgecolor='C1',
    label='gravity center')

ptc = pat.Circle(xy=pnti, radius=rri,
    linestyle='--', linewidth=2., edgecolor='C2', fill=False)
ax.scatter([pnti[0]], [pnti[1]],
    marker='o', s=40, color='C2', edgecolor='C2',
    label='inscribed circle')
ax.add_patch(ptc)

ptc = pat.Circle(xy=pnto, radius=rro,
    linestyle='--', linewidth=2., edgecolor='C3', fill=False)
ax.scatter([pnto[0]], [pnto[1]],
    marker='o', s=40, color='C3', edgecolor='C3',
    label='circumscribed circle')
ax.add_patch(ptc)

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
## --- block__: importing items from module ---
## --- block_a: setting three points ---
Points: pnta, pntb, pntc = [0, 0], [2, 0], [0, 2]
## --- block_b: calculating sides ---
Side length: a, b, c = 2.82843, 2, 2
## --- block_c: calculating angles ---
Angles: A, B, C = 90, 45, 45 (deg)
## --- block_d: calculating area ---
Area: S = 2
## --- block_e: calculating gravity center ---
gravity center: (pgx,pgy) = [0.666667, 0.666667]
## --- block_f: calculating inscribed circle ---
Radius: ri = 0.585786,   Inner center: (pix,piy) = [0.585786, 0.585786]
## --- block_g: calculating circumscribed circle ---
Radius: ro = 1.41421,   Outer center: (pox,poy) = [1, 1]
'''

