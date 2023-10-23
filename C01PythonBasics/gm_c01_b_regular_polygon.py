## gm_c01_b_regular_polygon.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** area of regular polygon ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section_a: triangle and square --- ##')
side = 2  # side length
area = side * (side*3**.5/2) / 2, side * side  # equilateral triangle and a square
print('side = ', side, ', area = ', area)

# -----------------------------------------------------------------------------
print("\n## --- section_b: importing items from standard module math ---")
from math import (pi, cos, sin)  # importing items from standard module 'math'
print('pi = ', pi, ', sin(pi/2) = ', sin(pi/2), ', cos(pi) = ', cos(pi))

# -----------------------------------------------------------------------------
print('\n## --- section_c: area of n-th regular polygon ---')
radius = 2  # radius of circumscribed circle
nn = 3  # number of sides
theta_nn = 2 * pi / nn  # top angle
area_tri = (1 /2) * (2 * radius * sin(theta_nn/2)) * (radius * cos(theta_nn/2))  # area of triangle
area = nn * area_tri  # area of polygon
print('nn = ', nn, ', \tradius = ', radius, ', \tarea = ', area)

# -----------------------------------------------------------------------------
print('\n## --- section_d: calculating a series of polygon areas ---')
for nn in range(3,8):
    theta_nn = 2 * pi / nn
    area_tri = radius * sin(theta_nn/2) * radius * cos(theta_nn/2)
    area = area_tri * nn
    print('nn = ', nn, ', \tradius = ', radius, ', \tarea = ', area)
print('circle: area = ', pi * radius * radius)

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** area of regular polygon ***
# -----------------------------------------------------------------------------
## --- section_a: triangle and square --- ##
side =  2 , area =  (1.7320508075688772, 4)

## --- section_b: importing items from standard module math ---
pi =  3.141592653589793 , sin(pi/2) =  1.0 , cos(pi) =  -1.0

## --- section_c: area of n-th regular polygon ---
radius =  2 , 	nn =  3 , 	area =  5.196152422706633

## --- section_d: calculating a series of polygon areas ---
nn =  3 , 	radius =  2 , 	area =  5.196152422706633
nn =  4 , 	radius =  2 , 	area =  8.000000000000002
nn =  5 , 	radius =  2 , 	area =  9.510565162951536
nn =  6 , 	radius =  2 , 	area =  10.392304845413264
nn =  7 , 	radius =  2 , 	area =  10.945640754552418
circle: area =  12.566370614359172
'''
