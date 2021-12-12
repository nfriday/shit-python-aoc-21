import re

cons = []
for i in open("12/input.txt","r").read().splitlines():
    con = i.split("-")
    cons.append(con)
    cons.append(con[::-1])
cons = [i for i in cons if i[1]!="start" and i[0]!="end"]

def adjacent(x):
    global cons
    return [i[1] for i in cons if i[0]==x]

def step(valid):    
    global paths

    new_paths = []
    progress = False

    for path in paths:
        if path[-1]=="end":
            new_paths.append(path)
        else:
            for next in adjacent(path[-1]):
                potential_path = path + [next]
                if valid(potential_path):
                    new_paths.append(potential_path)
                    progress = True

    paths = new_paths
    return progress

# part 1

def valid1(path):
    for i,val in enumerate(path[1:],1):
        if re.match("^[a-z]+$",val):
            for val2 in path[i+1:]:
                if val2==val:
                    return False
        else:
            next
    return True

paths = [["start"]]
while step(valid1): pass
print(len(paths))

# part 2

def valid2(path):
    small_cave_twice = False
    for i,val in enumerate(path[1:],1):
        if re.match("^[a-z]+$",val):
            for val2 in path[i+1:]:
                if val2==val:
                    if small_cave_twice:
                        return False
                    else:
                        small_cave_twice = True
        else:
            next
    return True

paths = [["start"]]
while step(valid2): pass
print(len(paths))