# Ghost Legs

## Problem

The original content is found on CodinGame website at [here](https://www.codingame.com/ide/puzzle/ghost-legs)

Ghost Legs is a kind of lottery game common in Asia. It starts with a number of vertical lines. Between the lines there are random horizontal connectors binding all lines into a connected diagram, like the one below.

```
A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3
```

To play the game, a player chooses a line in the top and follow the line downwards. When a horizontal connector is encountered, he must follow the connector to turn to another vertical line and continue downwards. Repeat this until reaching the bottom of the diagram.

In the example diagram, when you start from A, you will end up in 2. Starting from B will end up in 1. Starting from C will end up in 3. It is guaranteed that every top label will map to a unique bottom label.

Given a Ghost Legs diagram, find out which top label is connected with which bottom label. List all connected pairs.

**Input**: the Ghost Legs diagram as above

**Ouput**: List of all connected pairs, as in the example: ['A2', 'B1', 'C3']

## Solution

* [Python](https://github.com/nnguyen168/codingame-puzzle/blob/master/Easy/Ghost-Legs/solution.py)

  * First I create a list of top or start points, a list of bottom of end points, and a list of list where each sublist contains 
  a line of the Ghost Legs diagram.
```
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
```
Here, the line ```line = line.replace('|--|', '|--  |')``` is to extract better the connection between two legs in the diagram, so one line will be converted to a list as follow and we can keep track of the connection easily

```|  |  |``` -> ```['|', '|', '|']```

```|--|  |``` -> ```['|--', '|', '|']```

```|  |--|``` -> ```['|', '|--', '|']```

 * Now we will take every start point and traverse the Ghost Legs diagram to get its end point. the point will jump to its adjencent legs depend on whether there is a connection between those two legs.
```
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
```
