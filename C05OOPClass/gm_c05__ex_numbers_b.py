# gm_c05__ex_numbers_b.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class example (GMNumbers) for operating numbers; ver. b ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbersB) defining class ---')
class GMNumbersB():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: initializing class instance ---')
    def __init__(self, aa: int = 3, bb: int = 2) -> None:
        self.aa, self.bb = aa, bb

    # -----------------------------------------------------------------------------
    print('## --- section_a2: functions for calculations ---')
    def add(self) -> float: return self.aa + self.bb
    def sub(self) -> float: return self.aa - self.bb
    def calc(self) -> tuple:
        return self.add(), self.sub()

# =============================================================================
print('\n## --- section_b: operating numbers using class object ---')
numbers = GMNumbersB()  # creating instance without initial values
print(f'{numbers.aa = }, {numbers.bb = }') # printing instance variables
add, sub = numbers.calc()  # getting calculation results
print(f'{add = }, {sub = }\n')   # printing calculation results

numbers.aa, numbers.bb = 7, 3  # direct setting instance valuables
print(f'{numbers.aa = }, {numbers.bb = }') # printing instance variables
add, sub = numbers.calc()  # getting calculation results
print(f'{add = }, {sub = }\n')   # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class example (GMNumbers) for operating numbers; ver. b ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbersB) defining class ---
## --- section_a1: initializing class instance ---
## --- section_a2: functions for calculations ---

## --- section_b: operating numbers using class object ---
numbers.aa = 3, numbers.bb = 2
add = 5, sub = 1

numbers.aa = 7, numbers.bb = 3
add = 10, sub = 4
'''
