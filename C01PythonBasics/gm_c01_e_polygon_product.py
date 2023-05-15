## gm_c01_e1_polygon_product: coded by Kinya MIURA 230411
# -----------------------------------------------------------------------------
print('\n*** calculation of polygon using outer product ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section__: importing item from module ---')
from numpy import (sqrt)

# -----------------------------------------------------------------------------
print('\n## --- section_a: setting points ---')
pnts = ((2,1), (3,2), (2,3), (1,2))  # using 'tuple' of two dimension
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
print("\n## --- section_c: calculating total area enclosed: outer product ---")
area = 0
for i in range(len(pnts)):
    area += (pnts[i-1][0]*pnts[i][1] - pnts[i-1][1]*pnts[i][0]) / 2
print(f'Area: area = {abs(area):g}')

# -----------------------------------------------------------------------------
print("\n## --- section_d: calculating gravity center ---")
pntgx, pntgy = 0, 0
for (i, pnt) in enumerate(pnts):
    pntgx += pnt[0]; pntgy += pnt[1]
pntgx /= len(pnts); pntgy /= len(pnts)
print(f'Gravity center: (pgx,pgy) = ({pntgx:g}, {pntgy:g})')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** calculation of polygon using outer product ***
# -----------------------------------------------------------------------------
## --- section__: importing item from module ---
## --- section_a: setting points ---
Points: pnts = ((2, 1), (3, 2), (2, 3), (1, 2))
## --- section_b: calculating sides using Pythagoras' theorem ---
Side length: sdes = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
Circumference: ss = 5.65685
## --- section_c: calculating total area enclosed: outer product ---
Area: area = 2
## --- section_d: calculating gravity center ---
Gravity center: (pgx,pgy) = (2, 2)
'''

