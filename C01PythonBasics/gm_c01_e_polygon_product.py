## gm_c01_e1_polygon_product: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** calculation of polygon using outer product ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing item from module ---')
from numpy import (sqrt)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting points ---')
points = ((2,1), (3,2), (2,3), (1,2))  # using 'tuple' of two dimension
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
print("\n## --- section_c: calculating total area enclosed: outer product ---")
area = 0
for i in range(len(points)):
    area += (points[i-1][0]*points[i][1] - points[i-1][1]*points[i][0]) / 2
print(f'Area: area = {abs(area):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_d: calculating gravity center ---")
point_gg_xx, point_gg_yy = 0, 0
for (i, point) in enumerate(points):
    point_gg_xx += point[0]; point_gg_yy += point[1]
point_gg_xx /= len(points); point_gg_yy /= len(points)
print(f'Gravity center: (xx,yy) = ({point_gg_xx:g}, {point_gg_yy:g})')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of polygon using outer product ***
# -----------------------------------------------------------------------------
## --- section__: importing item from module ---
## --- section_a: setting points ---
Points: points = ((2, 1), (3, 2), (2, 3), (1, 2))
## --- section_b: calculating sides using Pythagoras' theorem ---
Side length: sides = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
Circumference: ss = 5.65685
## --- section_c: calculating total area enclosed: outer product ---
Area: area = 2
## --- section_d: calculating gravity center ---
Gravity center: (pgx,pgy) = (2, 2)
'''

