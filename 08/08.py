import re
import functools as ft

data = open("08/input.txt","r").read().splitlines()

# part 1

outputs = [i.split(" | ")[1].split(" ") for i in data]
print(ft.reduce(lambda total, val: total + len([i for i in val if len(i) in [2,4,3,7]]),outputs,0))

# part 2

def matching_segments(a,b):
    a = list(a)
    b = list(b)
    return len([i for i in a if i in b])

def sorted_string(x):
    x = list(x)
    x.sort()
    return "".join(x)

def solve(line):
    inputs = re.split("[^a-z]+",line)
    segments = {}
    segments[1] = sorted_string([i for i in inputs if len(i)==2][0]) # find the ones, with 2 segments
    segments[4] = sorted_string([i for i in inputs if len(i)==4][0]) # find the fours, with 4 segments
    segments[7] = sorted_string([i for i in inputs if len(i)==3][0]) # find the sevens, with 3 segments
    segments[8] = sorted_string([i for i in inputs if len(i)==7][0]) # find the eights, with 7 segments
    segments[3] = sorted_string([i for i in inputs if len(i)==5 and matching_segments(i,segments[1])==2][0]) # find the threes, which have 5 segments and 2 matching segment with ones
    segments[2] = sorted_string([i for i in inputs if len(i)==5 and matching_segments(i,segments[4])==2][0]) # find the twos, which have 5 segments and 2 matching segments with fours
    segments[5] = sorted_string([i for i in inputs if len(i)==5 and not sorted_string(i) in [segments[2],segments[3]]][0]) # find the fives, which have 5 segments but aren't twos or threes
    segments[6] = sorted_string([i for i in inputs if len(i)==6 and matching_segments(i,segments[1])==1][0]) # find the sixes, which have 6 segments and 1 matching segments with ones
    segments[9] = sorted_string([i for i in inputs if len(i)==6 and matching_segments(i,segments[4])==4][0]) # find the nines, which have 6 segments and 4 matching segments with fours
    segments[0] = sorted_string([i for i in inputs if len(i)==6 and not sorted_string(i) in [segments[6],segments[9]]][0]) # find the zeroes, which have 6 segments but aren't sixes or nines
    segment_lookup = {value: str(key) for key,value in segments.items()}
    answer = int("".join([segment_lookup[sorted_string(i)] for i in line.split(" | ")[1].split(" ")]))
    return answer

print(ft.reduce(lambda total, line: total + solve(line), data, 0))