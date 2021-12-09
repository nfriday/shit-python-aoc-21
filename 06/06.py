data = open("06/input.txt","r").read().split(",")

def solve(max_days):
    fish = []
    for i in range(9): fish.append(len([j for j in data if j==str(i)]))

    for i in range(max_days):
        new_fish = fish[0]
        fish = fish[1:] + [new_fish]
        fish[6] += new_fish

    sum = 0
    for i in fish: sum += i

    return sum

print(solve(80))
print(solve(256))