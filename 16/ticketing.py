from pprint import pprint
rules ={}
my_ticket=None
tickets=[]

with open('input.txt', 'r') as fin:
    line = 'null'
    while True:
        line = fin.readline()
        line = line.strip()
        if len(line) == 0:
            break
        parts = line.split(': ')
        ranges = parts[1].split(' or ')
        range_values = [x.split('-') for x in ranges]
        rules[parts[0]] = [[int(y) for y in x] for x in range_values]
    pprint(rules)
    fin.readline()
    my_ticket = [int(x) for x in fin.readline().split(',')]
    print(f"my ticket: {my_ticket}")
    fin.readline()
    fin.readline()
    for line in fin:
        tickets.append([int(x) for x in line.split(',')])
    print("others:")

def is_possible_value(rulebook, value):
    for v in rulebook.values():
        for rng in v:
            if value >= rng[0] and value <= rng[1]:
                return True
    return False

def get_validity(rulebook, value):
    validity = []
    for v in rulebook.values():
        if value >= v[0][0] and value <= v[0][1] or value >= v[1][0] and value <= v[1][1]:
            validity.append(True)
        else:
            validity.append(False)
    return validity


#Ticketing error rate
error_rate =0
ticket_index_to_delete = []
for i, ticket in enumerate(tickets):
    for value in ticket:
        if not is_possible_value(rules, value):
            #error_rate+=value
            ticket_index_to_delete.append(i)
#print(error_rate)
print(len(tickets))
for i in reversed(ticket_index_to_delete):
    tickets.pop(i)
print(len(tickets))
tickets.append(my_ticket)

possibilities = [[x for x in rules.keys()] for i in range(len(my_ticket))]
for ticket in tickets:
    for i, value in enumerate(ticket):
        validity = get_validity(rules, value)
        for j, v in enumerate(validity):
            if not v:
                possibilities[i][j] = ''

for i in range(len(possibilities)):
    possibilities[i] = [x for x in possibilities[i] if x != '']

mapping = {}

while True:
    if all([len(x) ==0 for x in possibilities]):
        break
    gottem = []
    for i in range(len(possibilities)):
        if len(possibilities[i]) == 1:
            print(i, possibilities[i])
            mapping[possibilities[i][0]] = i
            if possibilities[i][0] not in gottem:
                gottem.append(possibilities[i][0])
            else:
                print("error logic duality")
    for hit in gottem:
        for row in possibilities:
            if hit in row:
                row.remove(hit)
pprint(mapping)
ans = 1
for k,v in mapping.items():
    if k.startswith('departure'):
        ans*=my_ticket[v]
print(ans)
'''
field_ranges = []
for i in range(len(my_ticket)):
    field_ranges.append([])
for ticket in tickets:
    for i, value in enumerate(ticket):
        try:
            field_ranges[i][1] = max(value, field_ranges[i][1])
            field_ranges[i][0] = min(value, field_ranges[i][0])
        except IndexError:
            field_ranges[i].append(value)
            field_ranges[i].sort()
print(field_ranges)
'''
