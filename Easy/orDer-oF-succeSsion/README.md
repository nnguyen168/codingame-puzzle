# orDer oF succeSsion

## Problem

The original content could be found on CodinGame website at [here](https://www.codingame.com/ide/puzzle/order-of-succession)

The goal is to generate the order of succession to the British throne given a list of people. The order is as follow:
From a descendant A, the next in the order is A’s first child B.
Then, the next one is B’s first child C if any and so on.
If C has no child, then the next one is B’s second child D.
Then D’s children if any. Then B’s third child E… then A’s second child F…

__Ordering rules__
* in order of generation
* in order of gender
* in order of age (year of birth)

__Outputting rules__
* exclude dead people
* exclude people who are catholic

For example

**Input**: a list of people with the following information: their parent, their year of birth, their year of death, their religion, and their gender
**Output**: a list of succession

## Solution
* [Python](https://github.com/nnguyen168/codingame-puzzle/blob/master/Easy/orDer-oF-succeSsion/object-modelling.py)
  * First, a class representation of royal people is built using object modeling in Python
```
class RoyalPeople(object):
    def __init__(self, name, parent, birth, death, religion, gender):
        """
        Initiates a royal people along with their information
        """
        self.name = name
        self.parent = parent
        self.birth = birth
        self.death = death
        self.religion = religion
        self.gender = gender
        self.children = []
        
    def make_children(self):
        """
        This method acknowledge the parent of the presence of the child itself
        """
        if self.parent != "-":
            self.parent.set_children(self)
        return self
        
    def get_children(self):
        # Sort the children in order of gender and year of birth
        males = [child for child in self.children if child.gender == "M"]
        females = [child for child in self.children if child.gender == "F"]
        males.sort(key=lambda x: x.birth)
        females.sort(key=lambda x: x.birth)
        return males + females
        
    def set_children(self, child):
        # Fill the list of children of a person
        self.children.append(child)
        
    def __repr__(self):
        return 'Royal name: %s, Parent name: %s, Birth year: %d, Religion: %s, Gender: %s' % (self.name, self.parent if isinstance(self.parent, str) else self.parent.name, self.birth, self.religion, self.gender)

```
  * Next, let's prepare all the information about the royal family by reading from the standard input
```
n = int(input())
people_dict = {} # create a dictionary of people, the key is their name and the value is their object corresponding to their information
anscetor = ''
for i in range(n):
    name, parent, birth, death, religion, gender = input().split()
    if i == 0: anscetor = name
    birth = int(birth)
    if parent != "-":
        parent = people_dict[parent]
    person = RoyalPeople(name, parent, birth, death, religion, gender)   
    people_dict[name] = person

people_dict = {k: v.make_children() for k, v in people_dict.items()} # fill the information about the children and parent
```
  * Here a recursive method is used to find all the heirs starting from the ancestor
```
def order_of_succession(people_dict, person):
    result = []
    if person.death == '-' and person.religion != "Catholic":
        # exclude people who are death or catholic
        result.append(person.name)
    for child in person.get_children():
        # get the order of children by recursion
        result += order_of_succession(people_dict, child)
    return result
```
  * Hint: orDer oF succeSsion = DFS


