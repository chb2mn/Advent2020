


data = {}
reverse_data = {}
with open('input.txt', 'r') as fin:
    for line in fin:
        parts = line.strip().split()
        subject = "{} {}".format(parts[0], parts[1])
        for i in range(4, len(parts[4:])+1, 4):
            num = int(parts[i])
            obj = "{} {}".format(parts[i+1], parts[i+2])
            try:
                data[subject].append((obj, num))
            except KeyError:
                data[subject] = [(obj, num)]
            try:
                reverse_data[obj].append((subject, num))
            except KeyError:
                reverse_data[obj] = [(subject,num)]

from pprint import pprint
count = []
def count_children(start_node):
    global count
    count.extend([x[0] for x in reverse_data[start_node]])
    for v in reverse_data[start_node]:
        if v[0] in reverse_data:
            count_children(v[0])

count_children('shiny gold')
print(len(set(count)))

downcount = 0
def count_children_again(start_node, multiplier=1):
    global downcount
    for v in data[start_node]:
        downcount += multiplier*v[1]
        if v[0] in data:
            count_children_again(v[0], multiplier=multiplier*v[1])


count_children_again('shiny gold')
print(downcount)
