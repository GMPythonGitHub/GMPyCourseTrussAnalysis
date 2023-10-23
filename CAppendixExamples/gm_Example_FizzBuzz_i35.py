# Fizz Buzz Problem: plan D **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan I ***')
print('# -----------------------------------------------------------------------------')

[print(('FizzBuzz' if i % 3 == 0 and i % 5 ==0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i)), ('\n' if i % 10 == 0 else ''), end='') for i in range(1, 31)]

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: Plan I ***
# -----------------------------------------------------------------------------
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 
11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz 
Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 
'''
