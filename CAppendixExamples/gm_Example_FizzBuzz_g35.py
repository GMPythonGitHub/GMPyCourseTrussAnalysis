# Fizz Buzz Problem: plan D **
# -----------------------------------------------------------------------------
print('\n*** Fizz Buzz problem: Plan G ***')
print('# -----------------------------------------------------------------------------')

for i in range(1,31):
    st = ''
    if i % 3 == 0:
        st += 'Fizz'
    if i % 5 == 0:
        st += 'Buzz'
    if st == '':
        st += str(i)
    st += ' '
    if i % 10 == 0:
        st = st + '\n'
    print(st, end='')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Fizz Buzz problem: Plan G ***
# -----------------------------------------------------------------------------
 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 
11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz 
Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 
'''
