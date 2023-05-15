# gm_c05__ex_numbers_c.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class example (GMNumbers) for operating numbers; ver. c ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbersC) defining class ---')
class GMNumbersC():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: initializing class instance ---')
    def __init__(self, aa: int = 3, bb: int = 2) -> None:
        self.aa, self.bb = aa, bb  # initializing instance variables

    # -----------------------------------------------------------------------------
    print('## --- section_a2: string function for print() ---')
    def __str__(self) -> str:
        return f'aa = {self.aa:g}, bb = {self.bb:g}'

    # -----------------------------------------------------------------------------
    print('## --- section_a3: functions for calculation ---')
    def add(self) -> float: return self.aa + self.bb
    def sub(self) -> float: return self.aa - self.bb
    def calc(self) -> tuple:
        return self.add(), self.sub()

# =============================================================================
print('\n## --- section_b: operating numbers using class object ---')
numbers = GMNumbersC()  # creating instance
print(numbers)  # printing instance variables
add, sub = numbers.add(), numbers.sub()  # getting calculation results
print(f'{add = }, {sub = }\n')  # printing calculation results

numbers.aa, numbers.bb = 7, 3  # direct setting instance valuables
print(numbers)  # printing instance variables
add, sub = numbers.calc()  # getting calculation results
print(f'{add = }, {sub = }\n')  # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class example (GMNumbers) for operating numbers; ver. c ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbersC) defining class ---
## --- section_a1: initializing class instance ---
## --- section_a2: string function for print() ---
## --- section_a3: functions for calculation ---

## --- section_b: operating numbers using class object ---
aa = 3, bb = 2
add = 5, sub = 1

aa = 7, bb = 3
add = 10, sub = 4
'''
