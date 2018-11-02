import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

size = int(input())
angle = int(input())
block = []
for i in range(size):
    line = input()
    block.append(line.replace(' ',''))
    
def rotate_square_counter(block, count):
    """
    Return a square block after rotating counterclockwise 90° count times
    """
    for _ in range(count):
        block = [[block[j][i] for j in range(len(block))] for i in list(reversed(range(len(block))))]
        block = [''.join(i) for i in block]
    return block

def diag_line(matrix):
    """
    Return diagonal line of a list of list representation of a matrix
    """
    return [i[matrix.index(i)] for i in matrix]

def upper_triangle(matrix):
    """
    Return the upper triangle of a list of list representation of a square matrix
    """
    assert len(matrix) == len(matrix[0])
    return [i[matrix[:-1].index(i)+1:] for i in matrix[:-1]]
    
def lower_triangle(matrix):
    """
    Return the lower triangle of a list of list representation of a square matrix
    """
    assert len(matrix) == len(matrix[0])
    return [i[:matrix[1:].index(i)+1] for i in matrix[1:]]
    

def make_diamond(block):
    """
    Return a block after rotating counterclockwise 45° to form a diamond
    """

    result = []

    upper = upper_triangle(block)
    upper = [i.rjust(size-1) for i in upper]
    upper_form = []
    upper_length = len(upper)
    for i in range(upper_length):
        upper_form.append(diag_line(upper))
        upper = upper_triangle(upper)
        upper = [k.rjust(size-1-i-1) for k in upper]
    upper_form = [' '.join(i) for i in upper_form]
    upper_form = upper_form[::-1]

    diag = diag_line(block)
    diag = ' '.join(diag)

    lower = lower_triangle(block)
    lower = [i.ljust(size-1) for i in lower]
    lower_form = []
    lower_length = len(lower)
    for i in range(lower_length):
        lower_form.append(diag_line(lower))
        lower = lower_triangle(lower)
        lower = [k.ljust(size-1-i-1) for k in lower]
    lower_form = [' '.join(i) for i in lower_form]
    
    max_length = len(diag)
    upper_form = [i.center(max_length) for i in upper_form]
    lower_form = [i.center(max_length) for i in lower_form]

    result += upper_form
    result.append(diag)
    result += lower_form
    
    return result
    
count = int(angle/90) % 4 # number of times to rotate the block
block = rotate_square_counter(block, count)
result = make_diamond(block)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for line in result:
    print(line)
