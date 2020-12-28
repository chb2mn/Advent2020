mem = {}

turn = 0
last_number = -1
with open('input.txt', 'r') as fin:
    nums = fin.readline().split(',')
    for i, num in enumerate(nums):
        if last_number > -1:
            mem[last_number] = turn
        turn += 1
        last_number = int(num)
from pprint import pprint
pprint(mem)
while turn <30000000:
    turn_of_last_number = mem.get(last_number, 0)
    if turn_of_last_number != 0:
        diff = turn-turn_of_last_number
    else:
        diff = 0
    mem[last_number] = turn
    last_number=diff
    #pprint(mem)
    turn += 1
    
print(f"Turn {turn}:",last_number)

