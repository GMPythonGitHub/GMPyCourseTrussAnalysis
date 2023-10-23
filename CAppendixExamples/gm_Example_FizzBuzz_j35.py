# Fizz Buzz Problem: plan D **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan J ***')
print('# -----------------------------------------------------------------------------')

st = 'FizzBuzz'
for i in range(1, 31):
    st = 'FizzBuzz'[4 if i%3 else 0:4 if i%5 else 8]
    if len(st) == 0:
        print(str(i) + ' ', end='')
    else:
        print(st + ' ', end='')
    if i % 10 == 0:
        print()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: Plan J ***
# -----------------------------------------------------------------------------
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 
11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz 
Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 
'''
