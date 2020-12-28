data = []
def check_height(s):
    try:
        if s[2:4] == 'in':
            i = int(s[0:2]) 
            if i >= 59 and i <= 76:
                return True
        elif s[3:5] == 'cm':
            i = int(s[0:3])
            if i >=150 and i <= 193:
                return True
    except IndexError:
        pass
    return False

def check_eyes(s):
    if s[0] == "#":
        for i in range(1,7):
            try:
                int(s[i], 16)
            except:
                return False
        else:
            return True
    return False

def check_pid(s):
    if len(s) == 9:
        try:
            int(s)
        except TypeError:
            return False
        return True
    return False

fields = {
        'byr':lambda x: bool(int(x)>=1920 and int(x)<=2002) ,
        'iyr':lambda x: bool(int(x)>=2010 and int(x)<=2020),
        'eyr':lambda x: bool(int(x)>=2020 and int(x)<=2030),
        'hgt':check_height,
        'hcl':check_eyes,
        'ecl':lambda x: bool(x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
        'pid':check_pid,
        'cid':lambda x: True,
        }
with open('input.txt', 'r') as fin:
    item = {}
    for line in fin:
        if line.strip() == '':
            data.append(item)
            item = {}
        for item_pair in line.split():
            kv = item_pair.split(":")
            item[kv[0]] = kv[1]

from pprint import pprint
#pprint(data)

def check_passport(item):
    score = 8
    for field in item:
        if field in fields:
            if fields[field](item[field]):
                score -=1
    if score == 0:
        return True
    elif score == 1:
        if 'cid' in item:
            return False
        return True
    return False

count = 0
total = 0
for item in data:
    total += 1
    if check_passport(item):
        count +=1

print(count)
print(total)
