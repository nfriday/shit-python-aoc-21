import functools as ft

data = open("10/input.txt","r").read().splitlines()

brackets = {
    "]": "[",
    ")": "(",
    "}": "{",
    ">": "<",
}

corrupted_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

# part 1

def get_corrupted_points(line):
    chars = list(line)
    openings = []

    for char in chars:
        if char in brackets.values():
            openings.append(char)
        else:
            if brackets[char]==openings[-1]:
                openings.pop()
            else:
                return corrupted_points[char]

    return 0

print(ft.reduce(lambda total,line: total+get_corrupted_points(line),data,0))

# part 2

incomplete_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

lookup = {val:key for key,val in brackets.items()}

def get_incomplete_points(line):
    chars = list(line)
    openings = []

    for char in chars:
        if char in brackets.values():
            openings.append(char)
        else:
            if brackets[char]==openings[-1]:
                openings.pop()
            else:
                return 0

    openings.reverse()
    closings = [lookup[i] for i in openings]
    
    return ft.reduce(lambda total,val: total*5+incomplete_points[val],closings,0)

incomplete_scores = [i for i in [get_incomplete_points(line) for line in data] if i>0]
incomplete_scores.sort()
print(incomplete_scores[int((len(incomplete_scores)-1)/2)])