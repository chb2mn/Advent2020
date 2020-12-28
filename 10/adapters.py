
data = []

with open('input.txt', 'r') as fin:
    for line in fin:
        data.append(int(line.strip()))
data.append(0)
data.sort()
data.append(data[-1]+3)
print(data)
ojump = 0
tjump = 0
for i, x in enumerate(data):
    if i == 0:
        continue
    if x-data[i-1] == 1:
        ojump+=1
    elif x-data[i-1] == 3:
        tjump+=1

print(ojump)
print(tjump)
print(ojump*tjump)

cache_lookup = {}

def find_combos(x):
    global data
    if x in cache_lookup:
        return cache_lookup[x]
    if x == 0:
        return 1
    local_combos = 0
    if x-1 in data:
        local_combos += find_combos(x-1)
    if x-2 in data:
        local_combos += find_combos(x-2)
    if x-3 in data:
        local_combos += find_combos(x-3)
    cache_lookup[x] = local_combos
    return local_combos

print(find_combos(data[-1]))

'''
014
024
034
0124
0134
0234
01234
'''
'''

'''
