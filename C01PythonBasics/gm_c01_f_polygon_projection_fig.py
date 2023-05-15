## gm_c01_f_polygon_projection_fig: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** calculation of polygon using projection: drawing figure ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing item from module ---')
from numpy import (sqrt)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting points ---')
pnts = ((2, 1), (3, 2), (2, 3), (1, 2))  # using 'tuple' of two dimension
print(f'Points: pnts = {pnts}')

# -----------------------------------------------------------------------------
print("\n## --- section_b: calculating sides using Pythagoras' theorem ---")
sdes = []
for i in range(len(pnts)):
    sde = sqrt((pnts[i][0]-pnts[i-1][0])**2 + (pnts[i][1]-pnts[i-1][1])**2)
    sdes.append(sde)
print(f'Side length: sdes = {sdes}')
print(f'Circumference: ss = {sum(sdes):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_c: calculating total area enclosed: projection ---")
area, prj = 0, []
for i in range(len(pnts)):
    prj.append((pnts[i][1]+pnts[i-1][1]) * (pnts[i][0]-pnts[i-1][0]) / 2)
    area += prj[-1]
print(f'Area: area = {abs(area):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_d: calculating gravity center ---")
''' finding gravity center '''
pntgx, pntgy = 0, 0
for (i, pnt) in enumerate(pnts):
    pntgx += pnt[0]; pntgy += pnt[1]
pntgx /= len(pnts); pntgy /= len(pnts)
print(f'Gravity center: (pgx,pgy) = ({pntgx:g}, {pntgy:g})')

# -----------------------------------------------------------------------------
print("\n## --- section_e: drawing polygon ---")
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 6.))
fig.suptitle('polygon and gravity center')
pntsx, pntsy = [], []
for ipnts in pnts:
    pntsx.append(ipnts[0]); pntsy.append(ipnts[1])

for i in range(len(pnts)):
    if prj[i] >= 0: clr = 'C1'
    else: clr = 'C2'
    xy = ((pntsx[i-1],0), (pntsx[i],0), (pntsx[i],pntsy[i]), (pntsx[i-1],pntsy[i-1]))
    ptc = pat.Polygon(xy=xy, closed=True,
        linestyle='-', linewidth=1., edgecolor=clr, fill=True, facecolor=clr, alpha=0.2)
    ax.add_patch(ptc)

ax.scatter(pntsx, pntsy,
    marker='o', s=40, color='C0', edgecolor='C0')
pntsx.append(pnts[0][0]); pntsy.append(pnts[0][1])
ax.plot(tuple(pntsx), tuple(pntsy),
    linestyle='-', linewidth=2, color='C0')

ax.scatter(pntgx, pntgy,
    marker='o', s=40, color='C1', edgecolor='C1', label='gravity center')

ax.set_aspect('equal')
ax.legend()
fig.savefig('gm_c01_f_polygon_projection.png')
plt.show()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of polygon using projection: drawing figure ***
# -----------------------------------------------------------------------------
## --- section__: importing item from module ---
## --- section_a: setting points ---
Points: pnts = ((2, 1), (3, 2), (2, 3), (1, 2))
## --- section_b: calculating sides using Pythagoras' theorem ---
Side length: sdes = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
Circumference: ss = 5.65685
## --- section_c: calculating total area enclosed: projection ---
Area: area = 2
## --- section_d: calculating gravity center ---
Gravity center: (pgx,pgy) = (2, 2)
## --- section_e: drawing polygon ---
'''

