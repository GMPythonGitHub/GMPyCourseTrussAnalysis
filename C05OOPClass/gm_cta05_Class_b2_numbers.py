# gm_cta05_Class_b2_numbers.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class GMNumbers2 for operating numbers; ver. 2 ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbers2) declaring class ---')
class GMNumbers2():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMNumbers2) initializing class instance ---')
    def __init__(self, aa: int, bb: int) -> None:
        self.aa, self.bb = aa, bb

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMNumbers2) functions for calculations ---')
    def add(self) -> float: return self.aa + self.bb
    def sub(self) -> float: return self.aa - self.bb
    def calc(self) -> tuple:
        return self.add(), self.sub()

# =============================================================================
# =============================================================================
print('\n## --- section_b: operating numbers using class object ---')
numbs = GMNumbers2(aa=3, bb=2)  # creating instance without initial values
print(f'{numbs.aa = }, {numbs.bb = }') # printing instance variables
print(f'{numbs.add() = }, {numbs.sub() = }\n')   # printing calculation results

numbs.aa, numbs.bb = 7, 3  # direct setting instance valuables
print(f'{numbs.aa = }, {numbs.bb = }') # printing instance variables
add, sub = numbs.calc()  # getting calculation results
print(f'{add = }, {sub = }\n')   # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbers2 for operating numbers; ver. 2 ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbers2) defining class ---
## --- section_a1: (GMNumbers2) initializing class instance ---
## --- section_a2: (GMNumbers2) functions for calculations ---

## --- section_b: operating numbers using class object ---
numbs.aa = 3, numbs.bb = 2
numbs.add() = 5, numbs.sub() = 1

numbs.aa = 7, numbs.bb = 3
add = 10, sub = 4
'''
