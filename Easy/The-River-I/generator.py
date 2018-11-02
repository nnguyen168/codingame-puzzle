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
    
def digital_river(start_point):
    """
    Return a generator of the digital river given its start point
    """
    k = start_point
    while True:
        yield k
        k = k + sum_digit(k)
        
def find_meeting_point(river_1, river_2):
    """
    Find the first meeting point of two rivers
    """
    meeting_points = []
    while not meeting_points:
        points_1 = []
        points_2 = []
        for _ in range(10000):
            points_1.append(next(river_1))
            points_2.append(next(river_2))
        meeting_points = [i for i in points_1 if i in points_2]
    return meeting_points[0]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
river_1 = digital_river(r_1)
river_2 = digital_river(r_2)
print(find_meeting_point(river_1, river_2))
