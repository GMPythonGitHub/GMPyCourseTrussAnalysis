# gm_c01_b_regular_polygon.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** area of regular polygon ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- block_a: triangle and square --- ##')
aa = 2  # side length
ss = aa * (aa*3**.5/2) / 2, aa * aa  # equilateral triangle and a square
print('aa = ', aa, ', ss = ', ss)

# -----------------------------------------------------------------------------
print("\n## --- block_b: importing item from standard module math ---")
from math import (pi, cos, sin)  # importing items from standard module 'math'
print('pi = ', pi, ', sin(pi/2) = ', sin(pi/2), ', cos(pi) = ', cos(pi))

# -----------------------------------------------------------------------------
print('\n## --- block_c: area of n-th regular polygon ---')
rr = 2  # radius of circumscribed circle
nn = 3  # number of sides
th = 2 * pi / nn  # top angle
ss_tri = (1 /2) * (2 * rr * sin(th/2)) * (rr * cos(th/2))  # area of triangle
ss = nn * ss_tri  # area of polygon
print('rr = ', rr, 'nn = ', nn, 'ss = ', ss)

# -----------------------------------------------------------------------------
print('\n## --- block_d: calculating a series of polygon areas ---')
for nn in range(3,8):
    th = 2 * pi / nn
    ss_tri = rr * sin(th/2) * rr * cos(th/2)
    ss = ss_tri * nn
    print('nn = ', nn, ',\trr = ', rr, ',\tss = ', ss)
print('circle: ss = ', pi * rr * rr)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# terminal log
'''
*** area of regular polygon ***
# -----------------------------------------------------------------------------

## --- block_a: triangle and square --- ##
aa =  2 , ss =  (1.7320508075688772, 4)

## --- block_b: importing items from standard module 'math' ---
pi =  3.141592653589793 , sin(pi/2) =  1.0 , cos(pi) =  -1.0

## --- block_c: area of n-th regular polygon ---
rr =  2 nn =  3 ss =  5.196152422706633

## --- block_d: calculating a series of polygon areas ---
nn =  3 ,	rr =  2 ,	ss =  5.196152422706633
nn =  4 ,	rr =  2 ,	ss =  8.000000000000002
nn =  5 ,	rr =  2 ,	ss =  9.510565162951536
nn =  6 ,	rr =  2 ,	ss =  10.392304845413264
nn =  7 ,	rr =  2 ,	ss =  10.945640754552418
circle: ss =  12.566370614359172
'''
