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
