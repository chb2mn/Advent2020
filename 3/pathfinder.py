data = []
with open('input.txt', 'r') as fin:
    for line in fin:
        data.append(line.strip())

#varying slopes
def find_collisions(m):
    collisions = 0
    j=0
    for line in data:
        if line[j] == '#':
            collisions += 1
        j+=m
        j = j % len(line)

    return collisions

a=find_collisions(1)
b=find_collisions(3)
c=find_collisions(5)
d=find_collisions(7)

collisions = 0
i = 0
j=0
while i < len(data):
    if data[i][j] == "#":
        collisions += 1
    j += 1
    j = j % len(data[i])
    i += 2

e=collisions

print(a,b,c,d,e)
print(a*b*c*d*e)
