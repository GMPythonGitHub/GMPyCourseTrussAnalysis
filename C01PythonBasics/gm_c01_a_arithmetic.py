## gm_c01_a_arithmetic.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** arithmetic operations and Python basics ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- section_a: operating arithmetic operations ---')
aa, bb = 3, 2
sum, sub, mul, div = aa + bb, aa - bb, aa * bb, aa / bb  # four variables
print('sum, sub, mul, div = ', sum, sub, mul, div)
print('(sum - sub) / 2, (sum - sub) / 2 = ', (sum + sub) / 2, (sum - sub) / 2)
result = aa + bb, aa - bb, aa * bb, aa / bb  # variable as 'tuple'
print('result = ', result)
print('(result[0] + result[1]) / 2 = ', (result[0] + result[1]) / 2)
print('(result[0] - result[1]) / 2 = ', (result[0] - result[1]) / 2)

# -----------------------------------------------------------------------------
print("\n## --- section_b: using 'function' ---")
def func(nn):  # number, square and cubic
    square, cubic = nn * nn, nn * nn * nn  # calculating square and cubic
    return nn, square, cubic  # returning 'tuple' of three values
print('func(1) = ', func(1))
print('func(2) = ', func(2))
print('func(5) = ', func(5))

# -----------------------------------------------------------------------------
print("\n## --- section_c: using 'for-loop' ---")
accum = 0
for nn in range(5):  # counting up nn = 0 -> (5-1)
    accum += nn
    print('(nn, square, cubic) = ', func(nn), ', accum = ', accum)  # printing results

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
sum, sub, mul, div =  5 1 6 1.5
(sum - sub) / 2, (sum - sub) / 2 =  3.0 2.0
result =  (5, 1, 6, 1.5)
(result[0] + result[1]) / 2 =  3.0
(result[0] - result[1]) / 2 =  2.0

## --- section_b: using 'function' ---
func(1) =  (1, 1, 1)
func(2) =  (2, 4, 8)
func(5) =  (5, 25, 125)

## --- section_c: using 'for-loop' ---
(nn, square, cubic) =  (0, 0, 0) , accum =  0
(nn, square, cubic) =  (1, 1, 1) , accum =  1
(nn, square, cubic) =  (2, 4, 8) , accum =  3
(nn, square, cubic) =  (3, 9, 27) , accum =  6
(nn, square, cubic) =  (4, 16, 64) , accum =  10

## --- section_d: using 'if-structure' ---
aa, bb, cc =  1 4 5
cc >= aa + bb
'''
