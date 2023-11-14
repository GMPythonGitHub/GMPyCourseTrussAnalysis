# gm_cta05_Class_b1_numbers.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class GMNumbers1 for operating numbers; ver. 1 ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbers1) declaring class ---')
class GMNumbers1():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMNumbers1) initializing class instance ---')
    def __init__(self, aa: int = 3, bb: int = 2) -> None:
        self.aa, self.bb = aa, bb

# =============================================================================
# =============================================================================
print('\n## --- section_b: operating numbers using class object ---')
numbs = GMNumbers1(3, 2)  # creating instance without initial values
print(f'{numbs.aa = }, {numbs.bb = }')  # printing instance variables
add, sub = (  # calculating some using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }\n')  # printing calculation results

numbs.aa, numbs.bb = 7, 3  # setting directly instance valuables
print(f'{numbs.aa = }, {numbs.bb = }')  # printing instance variables
add, sub = (  # calculating some using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }\n')  # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbers1 for operating numbers; ver. 1 ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbers1) defining class ---
## --- section_a1: (GMNumbers1) initializing class instance ---

## --- section_b: operating numbers using class object ---
numbs.aa = 3, numbs.bb = 2
add = 5, sub = 1

numbs.aa = 7, numbs.bb = 3
add = 10, sub = 4
'''
