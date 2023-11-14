# gm_cta05_Class_c0_vector.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** class GMVector for vector: ver. 1 ***')
print('  *** introducing modified setting and getting functions ***')

print('# -----------------------------------------------------------------------------')
print('## --- section__: (GMVector1) importing items from module ---')
from numpy import (sqrt, arctan2 as atan2)

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVector1) defining class ---')
class GMVector1():  # declaring class
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVector1) initializing class instance ---')
    def __init__(self, xx: float = 1., yy: float = 1.):  # with default
        self.__xx, self.__yy = None, None  # declaring instance variables
        self.set_xxyy(xx, yy) 

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVector1) setting and getting functions ---')
    ## setting functions
    def set_xxyy(self, xx: float = 1., yy: float = 1.) -> None:
        if xx is not None: self.__xx = xx
        if yy is not None: self.__yy = yy
    ## getting functions
    def xxyy(self) -> tuple: return self.__xx, self.__yy

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMVector1) string function for print() ---')
    def __str__(self) -> str:
        return f'xx = {self.__xx:g}, bb = {self.__yy:g}'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVector1) functions for calculation ---')
    def rrth(self) -> tuple:
        return sqrt(self.__xx**2 + self.__yy**2), atan2(self.__yy, self.__xx)
    def uvct(self) -> tuple:
        rr, _ = self.rrth()
        return self.__xx / rr, self.__yy / rr

# =============================================================================
# =============================================================================
print('\n## --- section_b: creating class instances ---')
vecta = GMVector1(1., 1.); print('vecta = ', vecta)
vectb = GMVector1(4., 3.); print('vectb = ', vectb)

# -----------------------------------------------------------------------------
print('\n## --- section_c: calculating properties of vectors ---')
print(f'{vecta.rrth() = }, \n{vecta.uvct() = }')
print(f'{vectb.rrth() = }, \n{vectb.uvct() = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVector for vector: ver. 1 ***
  *** introducing modified setting and getting functions ***
# -----------------------------------------------------------------------------
## --- section__: (GMVector1) importing items from module ---
## --- section_a: (GMVector1) defining class ---
## --- section_a1: (GMVector1) initializing class instance ---
## --- section_a2: (GMVector1) setting and getting functions ---
## --- section_a3: (GMVector1) string function for print() ---
## --- section_a4: (GMVector1) functions for calculation ---

## --- section_b: creating class instances ---
vecta =  xx = 1, bb = 1
vectb =  xx = 4, bb = 3

## --- section_c: calculating properties of vectors ---
vecta.rrth() = (1.4142135623730951, 0.7853981633974483), 
vecta.uvct() = (0.7071067811865475, 0.7071067811865475)
vectb.rrth() = (5.0, 0.6435011087932844), 
vectb.uvct() = (0.8, 0.6)
'''
