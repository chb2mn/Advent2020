db = {}
valid =0
with open('db.txt', 'r') as fin:
    for line in fin:
        parts = line.split()
        req = parts[0].split('-')
        minn = int(req[0])
        maxn = int(req[1])
        key = parts[1][0]
        count = parts[2].count(key)
        if count <= maxn and count >= minn:
            valid +=1
            print(parts[2])
    print(valid)
