
with open('input.txt', 'r') as fin:
    dump = fin.readline()
    bus_times = fin.readline().split(',')

a = []
n = []
for i, bus in enumerate(bus_times):
    if bus != 'x':
        a.append(int(bus)-i)
        n.append(int(bus))
print(a)
print(n)
big_n=1
for i in n:
    big_n *= i
print(f"big_n: {big_n}")
Ni = [int(big_n/x) for x in n]

xi = []
#now we find inverses
#we want to find where Ni*xi = 1 (mod n)
for i, ni in enumerate(Ni):
    x_i =0
    while (x_i*ni) % n[i] != 1:
        x_i+=1
    print(f"{x_i}*{ni} % {n[i]} == 1")
    xi.append(x_i)
print(f"a: {a}")
print(f"Ni: {Ni}")
print(f"xi: {xi}")

bnx = [a[i]*Ni[i]*xi[i] for i in range(len(n))]
print(f"bnx: {bnx}")
bigX = sum(bnx) 
print(f"bigX: {bigX}")
answer= bigX%big_n
print(f"answer: {answer}")

'''
#first progression
i = 0
x = n[0]
while True:
    if x%n[1] == a[1]:
        print(x)
        break
    x+=n[0]
#second progression
while True:
    if x%n[2] == a[2]:
        print(x)
        break
    x+=n[0]*n[1]
'''
