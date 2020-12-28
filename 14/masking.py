from itertools import permutations
from copy import deepcopy

memory = {}
mask = "X"*36
def apply_mask(mask, value):
    total = ''
    print(mask)
    value = '0'*(38-len(value)) + value[2:]
    print(value, len(value))
     
    for i,x in enumerate(mask):
        if x == 'X':
            total += 'X'
        elif x=='1':
            total += '1'
        elif x=='0':
            total += value[i]
    print(total)
    all_combos=[]
    for i in range(2**total.count('X')):
        combo = str(bin(i))[2:]
        combo = "0"*(total.count('X')-len(combo))+combo
        all_combos.append(combo)
    ret = []
    for combo in all_combos:
        t = deepcopy(total)
        for i in range(len(combo)):
            t=t.replace('X', combo[i], 1)
        ret.append(t)
    return ret

with open("input.txt", 'r') as fin:
    for line in fin:
        parts = line.strip().split(' = ')
        operator = parts[0]
        operand = parts[1]
        if operator == 'mask':
            mask = operand
        else:
            address = int(operator.split('[')[1][:-1])
            for add in apply_mask(mask, str(bin(address))):
                memory[add] = int(operand)
            '''
            print("-=-=-=-")
            memory[address] = apply_mask(mask, str(bin(int(operand))))
            '''

print(sum(memory.values()))
