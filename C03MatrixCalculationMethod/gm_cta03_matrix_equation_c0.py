# gm_cta03_matrix_equation_c0: coded by Kinya MIURA 231104
# -----------------------------------------------------------------------------
print('\n*** Matrix Equation C0: aa * xx = bb; find xx and bb with fixity ***')
print('# -----------------------------------------------------------------------------')
import copy

# -----------------------------------------------------------------------------
aa1 = [
    [1., 1., 1., 1., 1., 1.],
    [1., 2., 1., 1., 1., 1.],
    [1., 1., 3., 1., 1., 1.],
    [1., 1., 1., 4., 1., 1.],
    [1., 1., 1., 1., 5., 1.],
    [1., 1., 1., 1., 1., 6.] ]
bb1 = [0., 23., 27., 0., 0., 51.]
xx1 = [1., 0., 0., 4., 5., 6.]
fix_bb1 = (False, True, True, False, False, True)
fix_xx1 = (True, False, False, True, True, False)

aa2 = [
    [1., 1., 1., 1., 1., 1.],
    [1., 1., 1., 1., 2., 1.],
    [1., 1., 1., 3., 1., 1.],
    [1., 1., 4., 1., 1., 1.],
    [1., 5., 1., 1., 1., 1.],
    [6., 1., 1., 1., 1., 1.] ]
bb2 = [0., 26., 29., 0., 0., 26.]
xx2 = [0., 2., 3., 0., 0., 6.]
fix_bb2 = (False, True, True, False, False, True)
fix_xx2 = (False, True, True, False, False, True)

aa, bb, xx = aa1, bb1, xx1
fix_bb, fix_xx = fix_bb1, fix_xx1
rank = len(bb)
aa_wk, bb_wk = [], []
for i in range(rank):
    if fix_bb[i]:
        aai = []
        for j in range(rank):
            if not fix_xx[j]:
                aai.append(aa[i][j])
        aa_wk.append(aai)
        bbi = bb[i]
        for j in range(rank):
            if fix_xx[j]:
                bbi -= aa[i][j] * xx[j]
        bb_wk.append(bbi)

rank_wk = len(bb_wk)
# forward elimination
for i in range(rank_wk):
    for j in range(i+1,rank_wk):  # pivotting partial
        if abs(aa_wk[i][i]) < abs(aa_wk[j][i]):
            for k in range(i,rank_wk):
                aa_wk[i][k], aa_wk[j][k] = aa_wk[j][k], aa_wk[i][k]
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank_wk):
        ratio = aa_wk[j][i] / aa_wk[i][i]
        for k in range(i,rank_wk):
            aa_wk[j][k] -= aa_wk[i][k] * ratio
        bb_wk[j] -= bb_wk[i] * ratio

# backward substitution
for i in range(rank_wk-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa_wk[j][i] / aa_wk[i][i]
        for k in range(i,rank_wk):
            aa_wk[j][k] -= aa_wk[i][k] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# normalization
xx_wk = []
for i in range(rank_wk):
    xx_wk.append(bb_wk[i] / aa_wk[i][i])
# calculation vectors
jj = 0
for j in range(rank):
    if not fix_xx[j]:
        xx[j] = xx_wk[jj]
        jj += 1
for i in range(rank):
    bb[i] = 0
    for j in range(rank):
        bb[i] += aa[i][j] * xx[j]

print(f'{aa = }')
print(f'{bb = }')
print(f'{xx = }')
print(f'{fix_bb = }')
print(f'{fix_xx = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation C0: aa * xx = bb; find xx and bb with fixity ***
# -----------------------------------------------------------------------------
aa = [
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 2.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 3.0, 1.0, 1.0, 1.0], 
    [1.0, 1.0, 1.0, 4.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 5.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 6.0] ]
bb = [21.0, 23.0, 27.0, 33.0, 41.0, 50.99999999999999]
xx = [1.0, 2.0000000000000004, 3.0, 4.0, 5.0, 5.999999999999999]
fix_bb = (False, True, True, False, False, True)
fix_xx = (True, False, False, True, True, False)

*** Matrix Equation C0: aa * xx = bb; find xx and bb with fixity ***
# -----------------------------------------------------------------------------
aa = [
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 2.0, 1.0], [1.0, 1.0, 1.0, 3.0, 1.0, 1.0], 
    [1.0, 1.0, 4.0, 1.0, 1.0, 1.0], [1.0, 5.0, 1.0, 1.0, 1.0, 1.0], [6.0, 1.0, 1.0, 1.0, 1.0, 1.0] ]
bb = [21.0, 26.0, 29.0, 30.0, 29.0, 26.0]
xx = [1.0000000000000002, 2.0, 3.0, 3.9999999999999996, 5.0, 6.0]
fix_bb = (False, True, True, False, False, True)
fix_xx = (False, True, True, False, False, True)
'''