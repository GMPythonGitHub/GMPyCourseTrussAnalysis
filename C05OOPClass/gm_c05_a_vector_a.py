# gm_c05_a_vector_a.py: coded by Kinya MIURA 230428
# -----------------------------------------------------------------------------
print('\n*** class GMVector for vector: ver. a ***')

print('# -----------------------------------------------------------------------------')
print('## --- section__: (GMVectorA) importing items from module ---')
from numpy import (sqrt, arctan2 as atan2)

# -----------------------------------------------------------------------------
print('## --- section_a: (GMVectorA) defining class ---')
class GMVectorA():  # defining class
    # -----------------------------------------------------------------------------
    print('## --- section_a1: (GMVectorA) initializing class instance ---')
    def __init__(self, xx: float = 1., yy: float = 1.):  # with default
        self.__xx, self.__yy = None, None  # declaring instance variables
        self.set_xxyy(xx, yy) 

    # -----------------------------------------------------------------------------
    print('## --- section_a2: (GMVectorA) setting and getting functions ---')
    ## setting functions
    def set_xxyy(self, xx: float = 1., yy: float = 1.) -> None:
        if xx is not None: self.__xx = xx
        if yy is not None: self.__yy = yy
    ## getting functions
    def xxyy(self) -> tuple: return self.__xx, self.__yy

    # -----------------------------------------------------------------------------
    print('## --- section_a3: (GMVectorA) string function for print() ---')
    def __str__(self) -> str:
        return f'xx = {self.__xx:g}, bb = {self.__yy:g}'

    # -----------------------------------------------------------------------------
    print('## --- section_a4: (GMVectorA) functions for calculation ---')
    def rrth(self) -> tuple:
        return sqrt(self.__xx**2 + self.__yy**2), atan2(self.__yy, self.__xx)
    def uvct(self) -> tuple:
        rr, _ = self.rrth()
        return self.__xx / rr, self.__yy / rr

# =============================================================================
print('\n## --- section_b: (GMVectorA) creating class instances ---')
vecta = GMVectorA(1., 1.); print('vecta = ', vecta)
vectb = GMVectorA(4., 3.); print('vectb = ', vectb)

# -----------------------------------------------------------------------------
print('\n## --- section_c: (GMVectorA) calculating properties of vectors ---')
print(f'{vecta.rrth() = }, \n{vecta.uvct() = }')
print(f'{vectb.rrth() = }, \n{vectb.uvct() = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVector for vector: ver. a ***
# -----------------------------------------------------------------------------
## --- section__: (GMVectorA) importing items from module ---
## --- section_a: (GMVectorA) defining class ---
## --- section_a1: (GMVectorA) initializing class instance ---
## --- section_a2: (GMVectorA) setting and getting functions ---
## --- section_a3: (GMVectorA) string function for print() ---
## --- section_a4: (GMVectorA) functions for calculation ---

## --- section_b: (GMVectorA) creating class instances ---
vecta =  xx = 1, bb = 1
vectb =  xx = 4, bb = 3

## --- section_c: (GMVectorA) calculating properties of vectors ---
vecta.rrth() = (1.4142135623730951, 0.7853981633974483), 
vecta.uvct() = (0.7071067811865475, 0.7071067811865475)
vectb.rrth() = (5.0, 0.6435011087932844), 
vectb.uvct() = (0.8, 0.6)
'''
