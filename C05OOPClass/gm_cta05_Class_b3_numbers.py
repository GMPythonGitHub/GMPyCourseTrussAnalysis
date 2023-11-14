# gm_c05_Class_b3_numbers.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class GMNumbers3 for operating numbers; ver. 3 ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbers3) declaring class ---')
class GMNumbers3():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMNumbers3) initializing class instance ---')
    def __init__(self, aa: int = 3, bb: int = 2) -> None:
        self.aa, self.bb = aa, bb  # initializing instance variables

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMNumbers3) string function for print() ---')
    def __str__(self) -> str:
        return f'aa = {self.aa:g}, bb = {self.bb:g}'

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMNumbers3) functions for calculation ---')
    def add(self) -> float: return self.aa + self.bb
    def sub(self) -> float: return self.aa - self.bb
    def calc(self) -> tuple:
        return self.add(), self.sub()

# =============================================================================
# =============================================================================
print('\n## --- section_b: operating numbers using class object ---')
numbs = GMNumbers3()  # creating instance
print(numbs)  # printing instance variables
print(f'{numbs.add() = }, {numbs.sub() = }\n')   # printing calculation results

numbs.aa, numbs.bb = 7, 3  # direct setting instance valuables
print(numbs)  # printing instance variables
add, sub = numbs.calc()  # getting calculation results
print(f'{add = }, {sub = }\n')  # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbers3 for operating numbers; ver. 3 ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbers3) declaring class ---
## --- section_a1: (GMNumbers3) initializing class instance ---
## --- section_a2: (GMNumbers3) string function for print() ---
## --- section_a3: (GMNumbers3) functions for calculation ---

## --- section_b: operating numbers using class object ---
aa = 3, bb = 2
numbs.add() = 5, numbs.sub() = 1

aa = 7, bb = 3
add = 10, sub = 4
'''
