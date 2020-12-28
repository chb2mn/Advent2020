#def calc_line(line, paren = True):
#    line=line.strip()
#    paren_count = 0
#    start_i = None
#    running_total = 0
#    operator = '+'
#    for i, c in enumerate(line):
#        if c.strip() == '':
#            continue
#        if c == '(':
#            if paren_count == 0:
#                start_i = i
#            paren_count+=1
#        elif c == ')':
#            paren_count-=1
#            if paren_count == 0:
#                if operator == '*':
#                    running_total *= calc_line(line[start_i+1:i])
#                elif operator == '+':
#                    running_total += calc_line(line[start_i+1:i])
#        elif paren_count == 0:
#            if c == '+' or c == '*':
#                operator = c
#            else:
#                if operator == "*":
#                    new_addend = calc_line(line[i:], paren =False)
#                    running_total *= new_addend 
#                else:
#                    running_total += int(c)
#    print(f"{line}: {running_total}")
#    return running_total

#NOTE: could work; too hard
#def build_tree(entries):
#    op_tree = {}
#    paren_count = 0
#    start_i = None
#    if len(entries) == 1:
#        return int(entries[0])
#    for i,c in enumerate(entries):
#        if paren_count > 0:
#            if c == ')':
#                paren_count-=1
#                if paren_count == 0:
#                    return build_tree(entries[start_i+1:i])
#        elif c == '*':
#            op_tree['*'] = [build_tree(entries[:i]), build_tree(entries[i+1:])]
#            return op_tree
#        elif c == '+':
#            op_tree['+'] = [build_tree(entries[:i]), build_tree(entries[i+1:])]
#            return op_tree
#        if c == '(':
#            if paren_count == 0: start_i = i
#            paren_count += 1
#
#def execute_tree(op_tree):
#    if isinstance(op_tree, dict):
#        for k in op_tree.keys():
#            if k == '*':
#                return execute_tree(op_tree[k][0]) * execute_tree(op_tree[k][1])
#            if k == '+':
#                return execute_tree(op_tree[k][0]) + execute_tree(op_tree[k][1])
#    else:
#        return op_tree

def easy_exec(entries):
    start_i = None
    paren_count = 0
    #execute parens
    no_paren_entries = []
    parens = False
    for i, c in enumerate(entries):
        if c == '(':
            parens=True
            if paren_count == 0 : start_i = i
            paren_count += 1
        elif c == ')':
            paren_count -= 1
            if paren_count == 0:
                no_paren_entries.append(easy_exec(entries[start_i+1:i]))
        elif paren_count == 0:
            no_paren_entries.append(c)
    i = 0
    while i < len(no_paren_entries):
        c=no_paren_entries[i]
        if c == '+':
            op_1 = int(no_paren_entries.pop(i-1))
            #shed the operand
            no_paren_entries.pop(i-1)
            op_2 = int(no_paren_entries.pop(i-1))
            no_paren_entries.insert(i-1, op_1+op_2)
            continue
        #if c == '*':
        #    if i == 1:
        #        post_plus.append(int(no_paren_entries[i-1]))
        #    post_plus.append('*')
        #    if i == len(no_paren_entries)-2:
        #        post_plus.append(int(no_paren_entries[i+1]))
        i+=1
    i = 0
    while i < len(no_paren_entries):
        c = no_paren_entries[i]
        if c == '*':
            op_1 = int(no_paren_entries.pop(i-1))
            #shed the operand
            no_paren_entries.pop(i-1)
            op_2 = int(no_paren_entries.pop(i-1))
            no_paren_entries.insert(i-1, op_1 * op_2)
            continue
        i+=1
    return no_paren_entries[0]
    



from pprint import pprint
with open('input.txt', 'r') as fin:
    total = 0
    for line in fin:
        entries = [x for x in line.strip() if x!=' ']
        print(line.strip())
        subtotal = easy_exec(entries)
        #tree  = build_tree(entries)
        #pprint(tree)
        #subtotal = execute_tree(tree)
        print(f"subtotal: {subtotal}")
        total+=subtotal
    print('-=-=-=-')
    print(total)
