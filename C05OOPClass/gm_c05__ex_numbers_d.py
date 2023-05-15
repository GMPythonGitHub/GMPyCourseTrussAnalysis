# gm_c05__ex_numbers_d.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class example (GMNumbers) for operating numbers; ver. d ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbersD) defining class ---')
class GMNumbersD():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: initializing class instance ---')
    def __init__(self, aa: int = 3, bb: int = 2) -> None:
        self__aa, self.__bb = None, None  # declaring instance variables
        self.set_aabb(aa, bb)  # initializing instance variables

    # -----------------------------------------------------------------------------
    print('## --- section_a2: setting and getting functions ---')
    ## setting functions
    def set_aabb(self, aa: float = None, bb: float = None) -> None:
        if aa is not None: self.__aa = aa
        if bb is not None: self.__bb = bb
    ## getting functions
    def aa(self) -> float: return self.__aa
    def bb(self) -> float: return self.__bb
    def aabb(self) -> tuple:
        return self.__aa, self.__bb

    # -----------------------------------------------------------------------------
    print('## --- section_a3: string function for print() ---')
    def __str__(self) -> str:
        return f'aa = {self.__aa:g}, bb = {self.__bb:g}'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: functions for calculation ---')
    def add(self) -> float: return self.__aa + self.__bb
    def sub(self) -> float: return self.__aa - self.__bb
    def calc(self) -> tuple:
        return self.add(), self.sub()

# =============================================================================
print('## --- section_b: operating numbers using class object ---')
numbers = GMNumbersD()  # creating instance
print(numbers)  # printing instance variables
add, sub = numbers.calc()  # getting calculation results
print(f'{add = }, {sub = }')  # printing calculation results
aa, bb = numbers.aa(), numbers.bb()  # getting instance variables
print(f'{aa * aa - bb * bb = }\n')  # printing calculations results

numbers.set_aabb(7, 3)  # setting instance variables
print(numbers)  # printing instance variables
add, sub = numbers.calc()  # getting calculation results
print(f'{add = }, {sub = }')  # printing calculation results
aa, bb = numbers.aa(), numbers.bb()  # getting instance variables
print(f'{aa * aa - bb * bb = }\n')  # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class example (GMNumbers) for operating numbers; ver. d ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbersD) defining class ---
## --- section_a1: initializing class instance ---
## --- section_a2: setting and getting functions ---
## --- section_a3: string function for print() ---
## --- section_a4: functions for calculation ---
## --- section_b: operating numbers using class object ---
aa = 3, bb = 2
add = 5, sub = 1
aa * aa - bb * bb = 5

aa = 7, bb = 3
add = 10, sub = 4
aa * aa - bb * bb = 40
'''
