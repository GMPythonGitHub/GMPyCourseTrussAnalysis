# gm_c01_a_arithmetic.py: coded by Kinya MIURA 230410
# -----------------------------------------------------------------------------
print('\n*** arithmetic operations and some basics ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('\n## --- block_a: operating arithmetic operations ---')
a, b = 3, 2
smm, sub, mul, div = a+b, a-b, a*b, a/b  # four variables
print('smm, sub, mul, div = ', smm, sub, mul, div)
print('(smm-sub)/2, (smm-sub)/2 = ', (smm+sub) / 2, (smm-sub) / 2)
result = a+b, a-b, a*b, a/b  # variable as 'tuple'
print('result = ', result)
print('(result[0]+result[1])/2 = ', (result[0]+result[1])/2)
print('(result[0]-result[1])/2 = ', (result[0]-result[1])/2)

# -----------------------------------------------------------------------------
print("\n## --- block_b: using 'function' ---")
def func(n):  # number, square and cubic
    sqr, cub = n*n, n*n*n  # calculating square and cube
    return n, sqr, cub  # returning three numbers as 'tuple'
print('func(1) = ', func(1))
print('func(2) = ', func(2))
print('func(3) = ', func(3))

# -----------------------------------------------------------------------------
print("\n## --- block_c: using 'for-loop' ---")
ss = 0
for n in range(5):  # counting up n = 0 -> (5-1)
    ss += n
    print('(n, n*n, n*n*n, ss) = ', func(n), ss)  # printing results

# -----------------------------------------------------------------------------
print("\n## --- block_d: using 'if-structure' ---")
a, b, c = 1, 4, 5
print('a, b, c = ', a, b, c)
if a >= b + c:
    print('a >= b + c')
elif b >= c + a:
    print('b >= c + a')
elif c >= a + b:
    print('c >= a + b')
else:
    print('triangle is formable')

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# terminal log
'''
*** arithmetic operations and some basics ***
# -----------------------------------------------------------------------------

## --- block_a: operating arithmetic operations ---
smm, sub, mul, div =  5 1 6 1.5
(smm-sub)/2, (smm-sub)/2 =  3.0 2.0
result =  (5, 1, 6, 1.5)
(result[0]+result[1])/2 =  3.0
(result[0]-result[1])/2 =  2.0

## --- block_b: using 'function' ---
func(1) =  (1, 1, 1)
func(2) =  (2, 4, 8)
func(3) =  (3, 9, 27)

## --- block_c: using 'for-loop' ---
(n, n*n, n*n*n, ss) =  (0, 0, 0) 0
(n, n*n, n*n*n, ss) =  (1, 1, 1) 1
(n, n*n, n*n*n, ss) =  (2, 4, 8) 3
(n, n*n, n*n*n, ss) =  (3, 9, 27) 6
(n, n*n, n*n*n, ss) =  (4, 16, 64) 10

## --- block_d: using 'if-structure' ---
a, b, c =  1 4 5
c >= a + b
'''
