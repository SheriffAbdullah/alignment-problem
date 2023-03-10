
'''
1) Randomized Sequence s1 & s2
* ONLY Recursive function calls *

2) 

3) 1st 

Computational Complexity & Time Complexity

Outputs:
-> Alignment Matrix
-> Traceback for 4 Matches + Alignment (with gaps)
-> 

'''

#%%

import random

random.seed(10)

# Recursive Function
def generateSequence(chars):
    if chars:
        c = chars[random.randint(0, len(chars)-1)]
        chars.remove(c)
        return c + generateSequence(chars)
    else:
        return ""
    
# Helper Function
def generateChars(setchar):
    chars = [x for pair in zip(charset,charset) for x in pair]
    chars = [x for pair in zip(chars,chars) for x in pair]

    return chars

# 1) Randomize S1, S2
charset = ['A', 'C', 'G', 'T']

chars = generateChars(charset)
s1 = generateSequence(chars)

chars = generateChars(charset)
s2 = generateSequence(chars)

print(f"s1: {s1} \ns2: {s2}")

#%%

# ALIGNMENT MATRIX

l1 = 16
l2 = 16

match_score = 5
mismatch_score = -4

alignment_matrix = [[0 for i in range(l1+1)] for i in range(l2+1)]

def printAlignmentMatrix(alignment_matrix):
    for i in alignment_matrix:
        for j in i:
            print(j, end='\t')
        print()

printAlignmentMatrix(alignment_matrix)


#%%

def dp(s1, s2, alignment_matrix, i, j):
    if j > len(s2):
        print(alignment_matrix)
        return alignment_matrix
    else:
        if i > len(s1):
            dp(s1, s2, alignment_matrix, 1, j+1)
            return alignment_matrix
        else:
            # MATCH
            if s1[j-1] == s2[i-1]:
                alignment_matrix[i][j] = alignment_matrix[i-1][j-1] + match_score;
            # MISMATCH
            else:
                alignment_matrix[i][j] = max(alignment_matrix[i-1][j], alignment_matrix[i][j-1]) + mismatch_score;
            dp(s1, s2, alignment_matrix, i+1, j)
    
print()
printAlignmentMatrix(alignment_matrix)

#dp(s1, s2, alignment_matrix, 1, 1)



