inst = lambda x,y: [x, int(y)]
data = [inst(*i.split(" ")) for i in open("02/input.txt","r").read().splitlines()]

# part 1

depth = 0
pos = 0
for instruction,value in data:
    if instruction == "forward": pos += value
    if instruction == "down": depth += value
    if instruction == "up": depth -= value

print(depth*pos)

# part 2
aim = 0
depth = 0
pos = 0
for instruction,value in data:
    if instruction == "forward":
            pos += value
            depth += aim * value
    if instruction == "down": aim += value
    if instruction == "up": aim -= value

print(depth*pos)