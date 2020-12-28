data = []
with open('input.txt', 'r') as fin:
    for line in fin:
        data.append(line.strip())
instructions_executed = []
i = 0
accumulator = 0
while True:
    if i in instructions_executed:
        print("loop detected; exiting")
        print("duplicated instruction: {} ({})".format(i, data[i]))
        print("loop caused by {} ({})".format(instructions_executed[-1], data[instructions_executed[-1]]))
        break
    if i < 0:
        print("error out of range")
        break
    if i >= len(data):
        print("executing gracefully...")
        print(accumulator)
        break
    instructions_executed.append(i)
    
    code = data[i].split()
    if code[0] == 'acc':
        if code[1][0] == '+':
            accumulator += int(code[1][1:])
        elif code[1][0] == '-':
            accumulator -= int(code[1][1:])
    elif code[0] == 'jmp':
        if code[1][0] == '-':
            i -= int(code[1][1:])
        elif code[1][0] == '+':
            i += int(code[1][1:])
    if code[0] != 'jmp':
        i+=1
