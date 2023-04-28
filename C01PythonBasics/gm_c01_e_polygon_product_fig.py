# gm_c01_e_polygon_product_fig: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** calculation of polygon using outer product: drawing figure ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- block__: importing item from module ---')
from numpy import (sqrt)

# -----------------------------------------------------------------------------
print('\n## --- block_a: setting points ---')
pnts = [[2,1], [3,2], [2,3], [1,2]]  # using 'list' of two dimension
print(f'Points: pnts = {pnts}')

# -----------------------------------------------------------------------------
print("\n## --- block_b: calculating sides ---")
sdes = []
for i in range(len(pnts)):
    sde = sqrt((pnts[i][0]-pnts[i-1][0])**2 + (pnts[i][1]-pnts[i-1][1])**2)
    sdes.append(sde)
print(f'Side length: sdes = {sdes}')
print(f'Circumference: ss = {sum(sdes):g}')

# -----------------------------------------------------------------------------
print("\n## --- block_c: calculating area ---")
area, prd = 0, []
for i in range(len(pnts)):
    prd.append((pnts[i-1][0]*pnts[i][1] - pnts[i-1][1]*pnts[i][0]) / 2)
    area += prd[-1]
print(f'Area: area = {abs(area):g}')

# -----------------------------------------------------------------------------
print("\n## --- block_d: calculating gravity center ---")
pntgx, pntgy = 0, 0
for (i, pnt) in enumerate(pnts):
    pntgx += pnt[0]
    pntgy += pnt[1]
pntgx /= len(pnts)
pntgy /= len(pnts)
print(f'Gravity center: (pgx,pgy) = [{pntgx:g}, {pntgy:g}]')

# -----------------------------------------------------------------------------
print("\n## --- block_e: drawing polygon ---")
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 6.))
fig.suptitle('polygon and gravity center')
pntsx, pntsy = [], []
for ipnts in pnts:
    pntsx.append(ipnts[0])
    pntsy.append(ipnts[1])

for i in range(len(pnts)):
    if prd[i] >= 0: clr = 'C1'
    else: clr = 'C2'
    xy = [[0,0],[pntsx[i],pntsy[i]],[pntsx[i-1],pntsy[i-1]]]
    ptc = pat.Polygon(xy=xy, closed=True,
        linestyle='-', linewidth=1., edgecolor=clr, fill=True, facecolor=clr, alpha=0.2)
    ax.add_patch(ptc)

ax.scatter(pntsx, pntsy,
    marker='o', s=40, color='C0', edgecolor='C0')
pntsx.append(pnts[0][0])
pntsy.append(pnts[0][1])
ax.plot(pntsx,pntsy,
    linestyle='-', linewidth=2, color='C0')

ax.scatter([pntgx], [pntgy],
    marker='o', s=40, color='C1', edgecolor='C1',
    label='gravity center')

ax.set_aspect('equal')
ax.legend()
fig.savefig('gm_c01_e_polygon_product.png')
plt.show()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of polygon using outer product: drawing figure ***
# -----------------------------------------------------------------------------
## --- block__: importing item from module ---
## --- block_a: setting points ---
Points: pnts = [[2, 1], [3, 2], [2, 3], [1, 2]]
## --- block_b: calculating sides ---
Side length: sdes = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
Circumference: ss = 5.65685
## --- block_c: calculating area ---
Area: area = 2
## --- block_d: calculating gravity center ---
Gravity center: (pgx,pgy) = [2, 2]
## --- block_e: drawing polygon ---
'''

