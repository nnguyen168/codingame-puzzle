import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class RoyalPeople(object):
    def __init__(self, name, parent, birth, death, religion, gender):
        self.name = name
        self.parent = parent
        self.birth = birth
        self.death = death
        self.religion = religion
        self.gender = gender
        self.children = []
        
    def make_children(self):
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
        self.children.append(child)
        
    def __repr__(self):
        return 'Royal name: %s, Parent name: %s, Birth year: %d, Religion: %s, Gender: %s' % (self.name, self.parent if isinstance(self.parent, str) else self.parent.name, self.birth, self.religion, self.gender)

n = int(input())
people_dict = {}
anscetor = ''
for i in range(n):
    name, parent, birth, death, religion, gender = input().split()
    if i == 0: anscetor = name
    birth = int(birth)
    if parent != "-":
        parent = people_dict[parent]
    person = RoyalPeople(name, parent, birth, death, religion, gender)   
    people_dict[name] = person

people_dict = {k: v.make_children() for k, v in people_dict.items()}
    
def order_of_succession(people_dict, person):
    result = []
    if person.death == '-' and person.religion != "Catholic":
        result.append(person.name)
    for child in person.get_children():
        result += order_of_succession(people_dict, child)
    return result
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
anscetor = people_dict[anscetor]
result = order_of_succession(people_dict, anscetor)
for name in result:
    print(name)
