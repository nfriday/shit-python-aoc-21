data = open("03/input.txt","r").read().splitlines()

# part 1

gamma_str = ""

for i in range(len(data[0])):
    values = [y[i] for y in data]
    gamma_str += str(int(len([x for x in values if x=="1"]) > (len(values)/2)))
    epsilon_str = "".join([str(int(not bool(int(z)))) for z in gamma_str])

print(int(gamma_str,2) * int(epsilon_str,2))

# part 2

oxygen_values = data
for i in range(len(data[0])):
    values = [y[i] for y in oxygen_values]
    common_bit = str(int(len([x for x in values if x=="1"]) >= (len(values)/2)))
    oxygen_values = [z for z in oxygen_values if z[i]==common_bit]
    if len(oxygen_values)==1: break

co2_values = data
for i in range(len(data[0])):
    values = [y[i] for y in co2_values]
    non_common_bit = str(int(len([x for x in values if x=="1"]) < (len(values)/2)))
    co2_values = [z for z in co2_values if z[i]==non_common_bit]
    if len(co2_values)==1: break

print(int(oxygen_values[0],2) * int(co2_values[0],2))