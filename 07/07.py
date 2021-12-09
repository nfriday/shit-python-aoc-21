data = [int(i) for i in open("07/input.txt","r").read().split(",")]

# part 1

best = 0
for i in range(min(data),max(data)+1):
    fuel = sum([abs(x-i) for x in data])
    if fuel < best or best == 0: best = fuel

print(best)

# part 2

def tricost(n): return int((n * (n + 1))/2)

best = 0
for i in range(min(data),max(data)+1):
    fuel = sum([tricost(abs(x-i)) for x in data])
    if fuel < best or best == 0: best = fuel

print(best)