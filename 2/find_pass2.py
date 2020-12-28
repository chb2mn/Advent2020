db = {}
x=0
valid =0
at_least = 0
with open('db.txt', 'r') as fin:
    for line in fin:
        parts = line.split()
        req = parts[0].split('-')
        minn = int(req[0])
        maxn = int(req[1])
        key = parts[1][0]
        #count = parts[2].count(key)
        if bool(parts[2][minn-1] == key) != bool(parts[2][maxn-1] == key):
            x +=1
        
        if parts[2][minn-1] == key or parts[2][maxn-1] == key:
            at_least +=1
            if not (parts[2][minn-1] == key and parts[2][maxn-1] == key):
                valid+=1
    print(at_least)
    print(valid)
    print(x)
