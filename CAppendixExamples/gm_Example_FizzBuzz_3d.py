# gm_Example_FizzBuzz_3d: coded by Kinya MIURA 230414
# Fizz Buzz Problem: plan 3D **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan 3D ***')
print('# -----------------------------------------------------------------------------')

for i in range(1,31):
    if i%3 == 0:
        print(' Fizz', end='')
    else:
        print(f'{i:5d}', end='')
    if i % 10 == 0:
        print()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: Plan 3D ***
# -----------------------------------------------------------------------------
    1    2 Fizz    4    5 Fizz    7    8 Fizz   10
   11 Fizz   13   14 Fizz   16   17 Fizz   19   20
 Fizz   22   23 Fizz   25   26 Fizz   28   29 Fizz
'''
