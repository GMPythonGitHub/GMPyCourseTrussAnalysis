## gm_c01_a_arithmetic.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** arithmetic operations and Python basics ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section_a: operating arithmetic operations ---')
aa, bb = 3, 2
smm, sub, mul, div = aa + bb, aa - bb, aa * bb, aa / bb  # four variables
print('smm, sub, mul, div = ', smm, sub, mul, div)
print('(smm - sub) / 2, (smm - sub) / 2 = ', (smm + sub) / 2, (smm - sub) / 2)
result = aa + bb, aa - bb, aa * bb, aa / bb  # variable as 'tuple'
print('result = ', result)
print('(result[0] + result[1]) / 2 = ', (result[0] + result[1]) / 2)
print('(result[0] - result[1]) / 2 = ', (result[0] - result[1]) / 2)

# -----------------------------------------------------------------------------
print("\n## --- section_b: using 'function' ---")
def func(nn):  # number, square and cubic
    sqr, cub = nn * nn, nn * nn * nn  # calculating square and cube
    return nn, sqr, cub  # returning three numbers as 'tuple'
print('func(1) = ', func(1))
print('func(2) = ', func(2))
print('func(5) = ', func(5))

# -----------------------------------------------------------------------------
print("\n## --- section_c: using 'for-loop' ---")
sum = 0
for nn in range(5):  # counting up nn = 0 -> (5-1)
    sum += nn
    print('(nn, square, cubic) = ', func(nn), 'sum = ', sum)  # printing results

# -----------------------------------------------------------------------------
print("\n## --- section_d: using 'if-structure' ---")
aa, bb, cc = 1, 4, 5
print('aa, bb, cc = ', aa, bb, cc)
if aa >= bb + cc:
    print('aa >= bb + cc')
elif bb >= cc + aa:
    print('bb >= cc + aa')
elif cc >= aa + bb:
    print('cc >= aa + bb')
else:
    print('triangle is formable')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** arithmetic operations and Python basics ***
# -----------------------------------------------------------------------------
## --- section_a: operating arithmetic operations ---
smm, sub, mul, div =  5 1 6 1.5
(smm - sub) / 2, (smm - sub) / 2 =  3.0 2.0
result =  (5, 1, 6, 1.5)
(result[0] + result[1]) / 2 =  3.0
(result[0] - result[1]) / 2 =  2.0
## --- section_b: using 'function' ---
func(1) =  (1, 1, 1)
func(2) =  (2, 4, 8)
func(5) =  (5, 25, 125)
## --- section_c: using 'for-loop' ---
(nn, square, cubic) =  (0, 0, 0) sum =  0
(nn, square, cubic) =  (1, 1, 1) sum =  1
(nn, square, cubic) =  (2, 4, 8) sum =  3
(nn, square, cubic) =  (3, 9, 27) sum =  6
(nn, square, cubic) =  (4, 16, 64) sum =  10
## --- section_d: using 'if-structure' ---
aa, bb, cc =  1 4 5
cc >= aa + bb

'''
