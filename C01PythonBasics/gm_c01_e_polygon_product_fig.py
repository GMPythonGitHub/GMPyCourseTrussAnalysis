## gm_c01_e_polygon_product_fig: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** calculation of polygon using outer product: drawing figure ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing item from module ---')
from numpy import (sqrt)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting points ---')
points = ((2,1), (3,2), (2,3), (1,2))  # using 'tuple' of two dimension
print(f'Points: points = {points}')

# -----------------------------------------------------------------------------
print("\n## --- section_b: calculating sides ---")
sides = []
for i in range(len(points)):
    side = sqrt((points[i][0]-points[i-1][0])**2 + (points[i][1]-points[i-1][1])**2)
    sides.append(side)
print(f'Side length: sides = {sides}')
print(f'Circumference: ss = {sum(sides):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_c: calculating area ---")
area, prd = 0, []
for i in range(len(points)):
    prd.append((points[i-1][0]*points[i][1] - points[i-1][1]*points[i][0]) / 2)
    area += prd[-1]
print(f'Area: area = {abs(area):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_d: calculating gravity center ---")
point_gg_xx, point_gg_yy = 0, 0
for (i, point) in enumerate(points):
    point_gg_xx += point[0]; point_gg_yy += point[1]
point_gg_xx /= len(points); point_gg_yy /= len(points)
print(f'Gravity center: (xx,yy) = ({point_gg_xx:g}, {point_gg_yy:g})')

# -----------------------------------------------------------------------------
print("\n## --- section_e: drawing polygon ---")
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 6.))
fig.suptitle('polygon and gravity center')
points_xx, points_yy = [], []
for ipoints in points:
    points_xx.append(ipoints[0]); points_yy.append(ipoints[1])

for i in range(len(points)):
    if prd[i] >= 0: clr = 'C1'
    else: clr = 'C2'
    xy = ((0,0),(points_xx[i],points_yy[i]),(points_xx[i-1],points_yy[i-1]))
    ptc = pat.Polygon(xy=xy, closed=True,
        linestyle='-', linewidth=1., edgecolor=clr, fill=True, facecolor=clr, alpha=0.2)
    ax.add_patch(ptc)

ax.scatter(tuple(points_xx), tuple(points_yy),
    marker='o', s=40, color='C0', edgecolor='C0')
points_xx.append(points[0][0]); points_yy.append(points[0][1])
ax.plot(tuple(points_xx), tuple(points_yy),
    linestyle='-', linewidth=2, color='C0')

ax.scatter(point_gg_xx, point_gg_yy,
    marker='o', s=40, color='C1', edgecolor='C1', label='gravity center')

ax.set_aspect('equal')
ax.legend()
fig.savefig('gm_c01_e_polygon_product.png')
plt.show()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of polygon using outer product: drawing figure ***
# -----------------------------------------------------------------------------
## --- section__: importing item from module ---
## --- section_a: setting points ---
Points: points = ((2, 1), (3, 2), (2, 3), (1, 2))
## --- section_b: calculating sides ---
Side length: sides = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
Circumference: ss = 5.65685
## --- section_c: calculating area ---
Area: area = 2
## --- section_d: calculating gravity center ---
Gravity center: (pgx,pgy) = (2, 2)
## --- section_e: drawing polygon ---
'''

