arr = [int(line) for line in open("01/input.txt","r").read().splitlines()]

# part 1
count = 0
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]: count+=1

print(count)

# part 2
count = 0
arr2 = [arr[i]+arr[i+1]+arr[i+2] for i in range(0,len(arr)-2)]
for i in range(1,len(arr2)):
    if arr2[i]>arr2[i-1]: count+=1

print(count)