# gm_cta05_Class_b4_numbers.py: coded by Kinya MIURA 230418
# -----------------------------------------------------------------------------
print('\n*** class GMNumbers4 for operating numbers; ver. 4 ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
print('## --- section_a: (GMNumbers4) declaring class ---')
class GMNumbers4():
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMNumbers4) initializing class instance ---')
    def __init__(self, aa: int = 3, bb: int = 2) -> None:
        self.__aa, self.__bb = None, None  # declaring instance variables
        self.set_aabb(aa, bb)  # initializing instance variables

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMNumbers4) setting and getting functions ---')
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
    print('## --- section_a3: (GMNumbers4) string function for print() ---')
    def __str__(self) -> str:
        return f'aa = {self.__aa:g}, bb = {self.__bb:g}'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMNumbers4) functions for calculation ---')
    def add(self) -> float: return self.__aa + self.__bb
    def sub(self) -> float: return self.__aa - self.__bb
    def calc(self) -> tuple:
        return self.add(), self.sub()

# =============================================================================
# =============================================================================
print('\n## --- section_b: operating numbers using class object ---')
numbs = GMNumbers4()  # creating instance
print(numbs)  # printing instance variables
print(f'{numbs.add() = }, {numbs.sub() = }')   # printing calculation results
aa, bb = numbs.aa(), numbs.bb()  # getting instance variables
print(f'{aa * aa + bb * bb = }\n')  # printing calculations results

numbs.set_aabb(7, 3)  # setting instance variables
print(numbs)  # printing instance variables
add, sub = numbs.calc()  # getting calculation results
print(f'{add = }, {sub = }')  # printing calculation results
aa, bb = numbs.aa(), numbs.bb()  # getting instance variables
print(f'{aa * aa + bb * bb = }\n')  # printing calculation results

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbers4 for operating numbers; ver. 4 ***
# -----------------------------------------------------------------------------
## --- section_a: (GMNumbers4) declaring class ---
## --- section_a1: (GMNumbers4) initializing class instance ---
## --- section_a2: (GMNumbers4) setting and getting functions ---
## --- section_a3: (GMNumbers4) string function for print() ---
## --- section_a4: (GMNumbers4) functions for calculation ---

## --- section_b: operating numbers using class object ---
aa = 3, bb = 2
numbs.add() = 5, numbs.sub() = 1
aa * aa + bb * bb = 13

aa = 7, bb = 3
add = 10, sub = 4
aa * aa + bb * bb = 58
'''
