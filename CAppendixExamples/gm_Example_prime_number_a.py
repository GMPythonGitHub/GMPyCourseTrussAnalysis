# gm_Example_prime_number_a: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** ------------ ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
num = 29
flg = False
for i in range(2, num):
    if num % i == 0:
        flg = True
        break
if flg:
    print(f'{num} is not a prime number!')
else:
    print(f'{num} is a prime number!')

# =============================================================================
# terminal log / terminal log / terminal log /
'''

'''
