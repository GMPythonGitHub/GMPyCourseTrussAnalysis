# gm_Example_prime_number_b: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** ------------ ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
number = 60
primes = []  # 'list' of prime numbers
for num in range(2,number+1):
    flg = False
    for i in primes:
        if num % i == 0:
            flg = True
            break
    if not flg:
        primes.append(num)

print(f'{number = }')
print(f'{primes = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
number = 60
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
'''