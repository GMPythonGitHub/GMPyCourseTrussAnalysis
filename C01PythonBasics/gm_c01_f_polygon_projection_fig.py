## gm_c01_f_polygon_projection_fig: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** calculation of polygon using projection: drawing figure ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing item from module ---')
from numpy import (sqrt)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting points ---')
points = ((2, 1), (3, 2), (2, 3), (1, 2))  # using 'tuple' of two dimension
print(f'Points: points = {points}')

# -----------------------------------------------------------------------------
print("\n## --- section_b: calculating sides using Pythagoras' theorem ---")
sides = []
for i in range(len(points)):
    side = sqrt((points[i][0]-points[i-1][0])**2 + (points[i][1]-points[i-1][1])**2)
    sides.append(side)
print(f'Side length: sides = {sides}')
print(f'Circumference: ss = {sum(sides):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_c: calculating total area enclosed: projection ---")
area, prj = 0, []
for i in range(len(points)):
    prj.append((points[i][1]+points[i-1][1]) * (points[i][0]-points[i-1][0]) / 2)
    area += prj[-1]
print(f'Area: area = {abs(area):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_d: calculating gravity center ---")
''' finding gravity center '''
point_gg_xx, point_gg_yy = 0, 0
for point in points:
    point_gg_xx += point[0];     point_gg_yy += point[1]
point_gg_xx /= len(points); point_gg_yy /= len(points)
print(f'Gravity center: (xx,yy) = ({point_gg_xx:g}, {point_gg_yy:g})')

# -----------------------------------------------------------------------------
print("\n## --- section_e: drawing polygon ---")
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 6.))
fig.suptitle('polygon and gravity center')
point_ss_xx, point_ss_yy = [], []
for ipoints in points:
    point_ss_xx.append(ipoints[0]); point_ss_yy.append(ipoints[1])

for i in range(len(points)):
    if prj[i] >= 0: clr = 'C1'
    else: clr = 'C2'
    xy = (
        (point_ss_xx[i-1],0), (point_ss_xx[i],0),
        (point_ss_xx[i],point_ss_yy[i]), (point_ss_xx[i-1],point_ss_yy[i-1]) )
    ptc = pat.Polygon(xy=xy, closed=True,
        linestyle='-', linewidth=1., edgecolor=clr, fill=True, facecolor=clr, alpha=0.2)
    ax.add_patch(ptc)

ax.scatter(point_ss_xx, point_ss_yy,
    marker='o', s=40, color='C0', edgecolor='C0')
point_ss_xx.append(points[0][0]); point_ss_yy.append(points[0][1])
ax.plot(tuple(point_ss_xx), tuple(point_ss_yy),
    linestyle='-', linewidth=2, color='C0')

ax.scatter(pointgx, pointgy,
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
Points: points = ((2, 1), (3, 2), (2, 3), (1, 2))

## --- section_b: calculating sides using Pythagoras' theorem ---
Side length: sides = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
Circumference: ss = 5.65685

## --- section_c: calculating total area enclosed: projection ---
Area: area = 2

## --- section_d: calculating gravity center ---
Gravity center: (xx,yy) = (2, 2)

## --- section_e: drawing polygon ---
'''

