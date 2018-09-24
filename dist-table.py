
"""
Coen Valk HW 1-2

Crypto 1 Fall 2018

This program takes in an S box and creates the entire
differential distribution table.
"""

import numpy as np

def get_row_num(val):
    if len(bin(val)) == 3:
        new_val_row = bin(val)[2]
    else:
        new_val_row = bin(val)[2] + bin(val)[-1]

    # print "row:", bin(val), new_val_row
    new_val_row = int(new_val_row, 2)
        
    return new_val_row

def get_col_num(val):
    if bin(val)[3:-1] == '':
        new_val_col = 0
    else:
        new_val_col = int(bin(val)[3:-1], 2)
    # print "col:", bin(val), bin(new_val_col)
        
    return new_val_col
        
def differential(S, output_space):
    diff = np.zeros((np.prod(S.shape), output_space))
    tmp = 0
    for row_idx1, row1 in enumerate(S):
        for col_idx1, col1 in enumerate(row1):
            for row_idx2, row2 in enumerate(S):
                for col_idx2, row2 in enumerate(row2):
                    tmp += 1
                    in_val1 = row_idx1 * S.shape[1] + col_idx1 # x
                    in_val2 = row_idx2 * S.shape[1] + col_idx2 # x*
                    in_new_val = in_val1 ^ in_val2 # x'

                    val1_row = get_row_num(in_val1)
                    val1_col = get_col_num(in_val1)

                    val2_row = get_row_num(in_val2)
                    val2_col = get_col_num(in_val2)

                    print in_val1, in_val2, in_new_val
                    
                    place1 = S[val1_row][val1_col] # y
                    place2 = S[val2_row][val2_col] # y*

                    place = place1 ^ place2 # y'
                    
                    diff[in_new_val][place] += 1
    return diff

def find_in_pairs(XOR_in, XOR_out, S, possible):
    ret = []
    for x1 in range(possible):
        for x2 in range(x1, possible):
            if x1 ^ x2 == XOR_in:
                x1_row = get_row_num(x1)
                x1_col = get_col_num(x1)

                x2_row = get_row_num(x2)
                x2_col = get_col_num(x2)

                s1 = S[x1_row][x1_col]
                s2 = S[x2_row][x2_col]

                if s1 ^ s2 == XOR_out:
                    print x1, x2
                    ret.append((x1, x2))
    return ret

def s_lookup(x, S):
    row = get_row_num(x)
    col = get_col_num(x)

    return S[row][col]

S = np.array(
    [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]
)

"""
S = np.array(
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]
)
"""


XOR_in = 1
XOR_out = 3

np.set_printoptions(threshold=np.nan)
print find_in_pairs(XOR_in, XOR_out, S, 16)
print s_lookup(1, S)
#D = differential(S, 16)
#print D
#print D.shape
