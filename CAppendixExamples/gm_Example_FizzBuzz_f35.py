# Fizz Buzz Problem: plan D **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan F ***')
print('# -----------------------------------------------------------------------------')

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz ', end='')
    elif i % 3 == 0:
        print('Fizz ', end='')
    elif i % 5 == 0:
        print('Buzz ', end='')
    else:
        print(i, end=' ')
    if i % 10 == 0:
        print()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: Plan F ***
# -----------------------------------------------------------------------------
 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 
11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz 
Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 
'''
