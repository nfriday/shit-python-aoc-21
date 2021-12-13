import functools as ft

data,folds = open("13/input.txt","r").read().split("\n\n")
folds = [(a[-1],int(b)) for a,b in [i.split("=") for i in folds.split("\n")]]

def printgrid(grid,onchar,offchar):
    for i in range(len(grid[0])):
        line = [onchar if bool(j[i]) else offchar for j in grid]
        print("".join(line))
    print("\n")

# initialise grid
init_coords = [(int(x),int(y)) for x,y in [i.split(",") for i in data.split("\n")]]
grid = [[0] * (max([y for x,y in init_coords])+1) for _ in range(max([x for x,y in init_coords])+1)]
for x,y in init_coords: grid[x][y]=1

def yfold(fold,grid):

    new_grid = [[0] * max([fold,len(grid[0])-fold-1]) for _ in range(len(grid))]
    
    y = 1
    while (fold-y)>=0 or (fold+y)<len(grid[0]):
        above_line = [i[fold-y] for i in grid] if (fold-y)>=0 else [0] * len(grid)   
        below_line = [i[fold+y] for i in grid] if (fold+y)<len(grid[0]) else [0] * len(grid)
        new_line = [above_line[i] | below_line[i] for i in range(len(grid))]
        
        for i,val in enumerate(new_line):
            new_grid[i][len(new_grid[0])-y] = val

        y += 1

    return new_grid

def xfold(fold,grid):

    new_grid = [[0] * len(grid[0]) for _ in range(max([fold,len(grid)-fold-1]))]

    x=1
    while (fold-x)>=0 or (fold+x)<len(grid):
        left_line = grid[fold-x] if (fold-x)>=0 else [0] * len(grid[0])
        right_line = grid[fold+x] if (fold+x)<len(grid) else [0] * len(grid[0])
        new_line = [left_line[i] | right_line[i] for i in range(len(grid[0]))]
        
        new_grid[len(new_grid)-x] = new_line        

        x += 1

    return new_grid

# part 1
inst = folds[0]
grid = xfold(inst[1],grid) if inst[0]=="x" else yfold(inst[1],grid)
print(ft.reduce(lambda total,line: total+sum(line), grid, 0))

# part 2
for inst in folds[1:]:
    grid = xfold(inst[1],grid) if inst[0]=="x" else yfold(inst[1],grid)
printgrid(grid,"#",".")