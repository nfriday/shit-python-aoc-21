import re

data = [[int(j) for j in re.search("(\d+),(\d+) -> (\d+),(\d+)",i).groups()] for i in open("05/input.txt","r").read().splitlines()]

grid_size = 1000

def points(line,diagonal):
    startx,starty,endx,endy = line
    if startx == endx:
        if starty > endy: starty, endy = endy, starty
        return [[startx,y] for y in range(starty,endy+1)]
    elif starty == endy:
        if startx > endx: startx, endx = endx, startx
        return [[x,starty] for x in range(startx,endx+1)]
    elif diagonal:
        return_points = []
        xstep = 1 if endx > startx else -1
        ystep = 1 if endy > starty else -1
        xs = range(startx,endx+xstep,xstep)
        ys = range(starty,endy+ystep,ystep)
        for i in range(len(xs)): return_points.append([xs[i],ys[i]])
        return return_points
    else:
        return []

# part 1
grid = [[0] * grid_size for _ in range(grid_size)]

for line in data:
    for point in points(line,False):
        grid[point[0]][point[1]] += 1

count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y]>=2: count+=1

print(count)

# part 2
grid = [[0] * grid_size for _ in range(grid_size)]

for line in data:
    for point in points(line,True):
        grid[point[0]][point[1]] += 1

count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y]>=2: count+=1

print(count)

#print board
# for x in range(grid_size):
#     line = ""
#     for y in range(10):
#         val = grid[x][y]
#         if val==0:
#             line+="."
#         else:
#             line+=str(grid[x][y])
#     print(line)