# gm_cta05_Class_b0_numbers.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class GMNumbers1 for operating numbers; ver. 0 ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbers0) declaring class ---')
class GMNumbers0():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMNumbers1) initializing class instance ---')
    def __init__(self) -> None:
        self.aa, self.bb = 3, 2

# =============================================================================
# =============================================================================
print('\n## --- section_b: operating numbers using class object ---')
numbs = GMNumbers0()  # creating instance without initial values
print(f'{numbs.aa = }, {numbs.bb = }')  # printing instance variables
add, sub = (  # calculating arithmetics using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }\n')  # printing calculation results

numbs.aa, numbs.bb = 7, 3  # setting directly instance valuables
print(f'{numbs.aa = }, {numbs.bb = }')  # printing instance variables
add, sub = (  # calculating arithmetics using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }\n')  # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbers0 for operating numbers; ver. 0 ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbers0) defining class ---
## --- section_a1: (GMNumbers0) initializing class instance ---

## --- section_b: operating numbers using class object ---
numbs.aa = 3, numbs.bb = 2
add = 5, sub = 1

numbs.aa = 7, numbs.bb = 3
add = 10, sub = 4
'''
