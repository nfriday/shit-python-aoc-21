def print_grid(grid):
    for line in [[str(i) for i in line] for line in grid]: print("-".join(line).replace("0","\033[92m0\033[00m"))
    print("---")

def step(grid):

    global step_flashes
    step_flashes = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1

    def adjacent(x,y):
        coords = [
            (x-1,y-1),  (x-1,y),   (x-1,y+1),
            (x,y-1),    (x,y),     (x,y+1),
            (x+1,y-1),  (x+1,y),   (x+1,y+1)
        ]
        return [(x,y) for x,y in coords if x>=0 and x<len(grid) and y>=0 and y<len(grid[0])]

    def flash(x,y):

        global flashes
        global step_flashes

        if grid[x][y]>0: grid[x][y] = 0; flashes += 1; step_flashes += 1
        
        for xa,ya in adjacent(x,y):
            if grid[xa][ya]>0: grid[xa][ya] += 1
            if grid[xa][ya]>9: flash(xa,ya)

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y]>9: flash(x,y)

# part 1
grid = [[int(j) for j in list(i)] for i in open("11/input.txt","r").read().splitlines()]

flashes = 0

for _ in range(100): step(grid)
#print_grid(grid)
print(flashes)

# part 2
grid = [[int(j) for j in list(i)] for i in open("11/input.txt","r").read().splitlines()]

flashes = 0
step_flashes = 0

i = 0
while step_flashes < len(grid)*len(grid[0]):
    i += 1
    step(grid)

#print_grid(grid)
print(i)