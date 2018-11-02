import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
top = [] # a list of start points
bottom = [] # a list of end points
legs = [] # a list of list where each sublist is a line of Ghost Legs diagram
for i in range(h):
    line = input()
    if i == 0:
        top.append(line)
        top = list(top[0].replace(' ',''))
    elif i == h-1:
        bottom.append(line)
        bottom = list(bottom[0].replace(' ', ''))
    else:
        # here we make an ugly trick to get the transition we want as '|--|  |' -> ['|--', '|', '|']
        line = line.replace('|--|', '|--  |') 
        line = line.split('  ')
        legs.append(line)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
result = [] # a list of connected pairs
for i in range(len(top)):
    pair = ''
    pair += top[i]
    end = i # assume that there is no connection and it goes straightly to the bottom
    for j in range(len(legs)):
        if len(legs[j][end]) == 3: # if there is connection between this leg and the one after it
            end = end + 1
        elif end != 0:
            if len(legs[j][end-1]) == 3: # if there is connection between this leg and the one before it
                end = end - 1
    pair += bottom[end]
    result.append(pair)
    
for r in result:
    print(r)
