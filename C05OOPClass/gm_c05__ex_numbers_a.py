# gm_c05__ex_numbers_a.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class example (GMNumbers) for operating numbers; ver. a ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbersA) defining class ---')
class GMNumbersA():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: initializing class instance ---')
    def __init__(self, aa: int = 3, bb: int = 2) -> None:
        self.aa, self.bb = aa, bb

# =============================================================================
print('\n## --- section_b: operating numbers using class object ---')
numbers = GMNumbersA()  # creating instance without initial values
print(f'{numbers.aa = }, {numbers.bb = }')  # printing instance variables
add, sub = (  # calculating some using instance variables
    numbers.aa + numbers.bb, numbers.aa - numbers.bb )
print(f'{add = }, {sub = }\n')  # printing calculation results

numbers.aa, numbers.bb = 7, 3  # direct setting instance valuables
print(f'{numbers.aa = }, {numbers.bb = }')  # printing instance variables
add, sub = (  # calculating some using instance variables
    numbers.aa + numbers.bb, numbers.aa - numbers.bb )
print(f'{add = }, {sub = }\n')  # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class example (GMNumbers) for operating numbers; ver. a ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbersA) defining class ---
## --- section_a1: initializing class instance ---

## --- section_b: operating numbers using class object ---
numbers.aa = 3, numbers.bb = 2
add = 5, sub = 1

numbers.aa = 7, numbers.bb = 3
add = 10, sub = 4
'''
