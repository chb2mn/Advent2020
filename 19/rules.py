import re

from pprint import pprint

rules = {}
phase = 0
cands = []
with open("input.txt", 'r') as fin:
    for line in fin:
        if line.strip() == '':
            phase += 1
        if phase == 0:
            parts = line.split(':')
            rule_num = parts[0]
            content = parts[1].strip()
            if content.startswith("\""):
                rules[rule_num] = content[1:-1]
            else:
                options = content.split('|')
                rules[rule_num] = []
                for opt in options:
                    rules[rule_num].append(opt.split())

        elif phase == 1:
            cands.append(line.strip())

#deref rule 0
def deref_rule(rule, index = None):
    global rules
    re_str = ""
    if isinstance(rule, str):
        return rule
    re_str += '('
    for i, subrule in enumerate(rule):
        if i != 0:
            re_str+="|"
        re_str+="("
        for item in subrule:
            re_str+=deref_rule(rules[item], index=item)
        re_str+=")"
    re_str += ')'

    return re_str

rules["8"] = [["42"],["42","8"]]
rules["11"] = [["42", "31"],["42","11","31"]]

pprint(rules)

re_42_str = deref_rule(rules["42"])
re_31_str = deref_rule(rules["31"])
print(re_42_str)
print(re_31_str)
re_42 = re.compile(re_42_str)
re_31 = re.compile(re_31_str)

#GOAL: 42_re+42_re{x}31_re{x} => 42_re{x}31_re{y} s.t. x>y>0

def find_succinct_matches(regex, line):
    n=0
    print(line)
    match = regex.match(line)
    while match is not None:
        n+=1
        line = line[match.end():]
        match = regex.match(line)
    if len(line) > 0:
        return n, line
    return n, ''

'''
my_re = deref_rule(rules["0"])
my_re = f"^{my_re}$"
print(my_re)
print("^a(((aa|bb)(ab|ba))|((ab|ba)(aa|bb)))b$")
re_0 = re.compile(my_re)
total = 0
for cand in cands:
    if re_0.match(cand):
        total+=1
print(total)
'''

#rule_0_re = re.compile(r"^a(((aa|bb)(ab|ba))|((ab|ba)(aa|bb)))b$")
#rule_0_re = re.compile(r"^a (( (aa|bb) (ab|ba) ) | ( (ab|ba) (aa|bb) )) b$")
total = 0
for cand in cands:
    x, remains=find_succinct_matches(re_42, cand)
    y, err=find_succinct_matches(re_31, remains)
    if len(err)>0:
        continue
    #print(rule_0_re.match(cand))
    if  y>0 and x>y:
        total +=1
print(total)
