## gm_c01_f_polygon_projection: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** calculation of polygon using projection ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing item from module ---')
from numpy import (sqrt)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting points ---')
points = ((2, 1), (3, 2), (2, 3), (1, 2))  # using 'tuple' of two dimension
print(f'Points: points = {points}')

# -----------------------------------------------------------------------------
print("\n## --- section_b: calculating sides ---")
''' finding side length using Pythagoras' theorem '''
sides = []
for i in range(len(points)):
    side = sqrt((points[i][0]-points[i-1][0])**2 + (points[i][1]-points[i-1][1])**2)
    sides.append(side)
print(f'Side length: sides = {sides}')
print(f'Circumference: ss = {sum(sides):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_c: calculating area ---")
''' finding total area enclosed: projection '''
area = 0
for i in range(len(points)):
    area += (points[i][1]+points[i-1][1]) * (points[i][0]-points[i-1][0]) / 2
print(f'Area: area = {abs(area):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_d: calculating gravity center ---")
''' finding gravity center '''
point_gg_xx, point_gg_yy = 0, 0
for point in points:
    point_gg_xx += point[0];     point_gg_yy += point[1]
point_gg_xx /= len(points); point_gg_yy /= len(points)
print(f'Gravity center: (xx,yy) = ({point_gg_xx:g}, {point_gg_yy:g})')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of polygon using projection ***
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
Gravity center: (xx,yy) = (2, 2)
'''

