import functools as ft

data = [[int(j) for j in list(i)] for i in open("09/input.txt","r").read().splitlines()]

# part 1

def adjacent_vals(x,y):
    coords = [i for i in [[x,y+1],[x,y-1],[x+1,y],[x-1,y]] if -1 not in i and i[0]<len(data) and i[1]<len(data[0])]
    return [data[i][j] for i,j in coords]

def lowpoints(input):
    points = []
    for x in range(len(input)):
        for y in range(len(input[0])):
            if data[x][y] < min(adjacent_vals(x,y)): points.append([x,y])
    return points

answer = ft.reduce(lambda total,val: total+data[val[0]][val[1]]+1, lowpoints(data), 0)

print(answer)

# part 2

def adjacent_coords(x,y):
    coords = [i for i in [[x,y+1],[x,y-1],[x+1,y],[x-1,y]] if -1 not in i and i[0]<len(data) and i[1]<len(data[0])]
    return coords

def basin(x,y):
    coords = [i for i in adjacent_coords(x,y) if data[i[0]][i[1]]>data[x][y] and data[i[0]][i[1]]<9]
    return coords

def size_basin(x,y):
    flows = [[x,y]]
    list = [[x,y]]
    while flows:
        new_flows = []
        for i in flows:
            for j in basin(i[0],i[1]):
                if len([z for z in flows+list if z[0]==j[0] and z[1]==j[1]])==0:
                    new_flows.append(j)
                    list.append(j)
        flows = new_flows
    return len(list)

sizes = [size_basin(x,y) for x,y in lowpoints(data)]
sizes.sort()

print(ft.reduce(lambda total,val: total*val,sizes[-3:]))