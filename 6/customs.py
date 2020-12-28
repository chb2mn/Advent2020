group_answers = []
with open('input.txt', 'r') as fin:
    group = set()
    debug_line = ''
    new_group=True
    for line in fin:
        if line.strip() == '':
            debug_line = ''
            print(group)
            group_answers.append(group)
            group = set()
            new_group=True
        elif new_group:
            group = set(line.strip())
            new_group=False
        else:
            print(group)
            group = group.intersection(set(line.strip()))
        print(line.strip())
        debug_line+=line
    print(debug_line)
    print(group)
    group_answers.append(set(group))

print(len(group_answers))
print([len(x) for x in group_answers])
print(sum([len(x) for x in group_answers]))
