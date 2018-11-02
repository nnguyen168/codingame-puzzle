import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
r_2 = int(input())

def sum_digit(number):
    """
    Calculate the sum of a number's digits
    """
    assert type(number) == int
    number_str = str(number)
    number_list = [int(i) for i in list(number_str)]
    return sum(number_list)
        
def find_meeting_point(river_1, river_2):
    """
    Find the first meeting point of two rivers
    """
    while river_1 != river_2:
        if river_1 < river_2:
            river_1 = river_1 + sum_digit(river_1)
        else:
            river_2 = river_2 + sum_digit(river_2)
    return river_1
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(find_meeting_point(r_1, r_2))
