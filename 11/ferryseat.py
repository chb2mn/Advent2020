grid = []
with open('input.txt', 'r') as fin:
    for line in fin:
        grid.append(line.strip())

def get_adjacents(grid, i, j):
    adjacent_seats = []
    for u in range(i-1, i+2):
        for w in range(j-1, j+2):
            if u < 0 or w < 0:
                continue
            try:
                if u == i and w == j:
                    continue
                adjacent_seats.append(grid[u][w])
            except IndexError:
                continue
    return adjacent_seats

def get_adjacent_vision(grid, i, j):
    adjacent_seats = []
    target=False
    #target = bool(i ==0 and j == 2)
    for u in range(-1, 2):
        for w in range(-1, 2):
            try:
                if u == 0 and w == 0:
                    continue
                distance = 1
                while grid[i+u*distance][j+w*distance] == '.' and i+u*distance >=0 and j+w*distance >=0:
                    distance +=1
                if i+u*distance <0 or j+w*distance < 0:
                    continue
                adjacent_seats.append(grid[i+u*distance][j+w*distance])
            except IndexError:
                continue
    if target:
        print(adjacent_seats)
    return adjacent_seats

def check_sitting(grid, i, j):
    if grid[i][j] == '.':
        return False
    adjacent_seats = get_adjacent_vision(grid, i ,j)
    if grid[i][j] == "L":
        #check if someone sits
        if adjacent_seats.count('#') == 0:
            return True
    elif grid[i][j] == "#":
        #check if the person leaves
        if adjacent_seats.count('#') >=5:
            return True
    else:
        return False

from copy import deepcopy
from pprint import pprint

new_grid = []
changed = False
while True:
    changed=False
    for i in range(len(grid)):
        new_grid.append("")
        for j in range(len(grid[i])):
            if check_sitting(grid, i, j):
                if grid[i][j] == 'L':
                    new_grid[i]+='#'
                else:
                    new_grid[i]+='L'
                changed=True
            else:
                new_grid[i]+=grid[i][j]
    grid = deepcopy(new_grid)
    new_grid = []
    '''
    p = input('continue?')
    if len(p) > 0:
        break
    '''
    if not changed:
        break
pprint(grid)
print(sum([x.count('#') for x in grid]))
    
