import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]
count = int(input())
map_list = []
for i in range(height):
    raster = input()
    raster = list(raster)
    raster = [0 if i == '.' else 1 for i in raster]
    map_list.append(raster)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def make_tumbling(map_list, count):
    for _ in range(count):
        # Sort each list in the map to simulate the effect of gravity
        map_list = [sorted(i, reverse=True) for i in map_list]
        # Turn map_list counterclockwise by 90°
        map_list = [[map_list[j][i] for j in range(len(map_list))] for i in reversed(range(len(map_list[0])))]
        
    return map_list

map_list = make_tumbling(map_list, count)
map_list = [['.' if i == 0 else '#' for i in sublist] for sublist in map_list]
map_list = [''.join(i) for i in map_list]

for i in map_list:
    print(i)
