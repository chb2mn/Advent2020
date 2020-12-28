state = [[[[]]]]

zero = 0

def print_state():
    global state
    global zero
    for j, w in enumerate(state):
        for i, z in enumerate(w):
            print(f"z={zero+i}, w={j}")
            for row in z:
                print(row)
    print('-=-=-=-')


with open('input.txt', 'r') as fin:
    for i, line in enumerate(fin):
        line=line.strip()
        if len(state[0][zero]) <= zero+i:
            state[0][zero].append([])
        for j, c in enumerate(line):
            if c == "#":
                state[0][zero][zero+i].append(1)
            else:
                state[0][zero][zero+i].append(0)

print_state()
from copy import deepcopy

def get_value(x,y,z, w):
    global state
    if x < 0 or y < 0 or z < 0 or w<0:
        return 0
    cube_len = len(state[0][0])
    if x >= len(state[0][0][0]) or y >=len(state[0][0]) or z >= len(state[0]) or w>=len(state):
        return 0
    try:
        return state[w][z][y][x]
    except IndexError:
        print("error")
        print(state[w][z])
        print(state[w][z][y])
        print(w,z,y,x)
        quit()

def check_adjacent(x,y,z,w):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i==0 and j ==0 and k == 0 and l == 0:
                        continue
                    #if get_value(x+i, y+j, z+k, w+l) > 0:
                    #    print("val at ({} {} {} {}) == {}".format(x+i, y+j, z+k, w+l, get_value(x+i, y+j, z+k, w+l)))
                    count += get_value(x+i, y+j, z+k, w+l)
    #print(f"count at {x}, {y}, {z}, {w}: {count}")
    return count

def expand_state():
    global state
    global zero
    #first, add the new dead space...
    #first build the new z plane
    for cube in state:
        new_unexpanded_plane = []
        for i in range(len(cube[0])):
            new_unexpanded_plane.append([])
            for j in range(len(cube[0][0])):
                new_unexpanded_plane[i].append(0)
        cube.append(deepcopy(new_unexpanded_plane))
        cube.insert(0, deepcopy(new_unexpanded_plane))
        #add the new column and row for each z plane
        for i in range(len(cube)):
            row_len = len(cube[i])
            #add a new row
            cube[i].append([0]*row_len)
            cube[i].insert(0, [0]*row_len)
            for j in range(len(cube[i])):
                #add columns
                cube[i][j].append(0)
                cube[i][j].insert(0, 0)
    #now copy this cube with zero'd values
    empty_row = [0]*len(state[0][0][0])
    empty_plane = [deepcopy(empty_row) for i in range(len(state[0][0]))]
    new_unexpanded_cube = [deepcopy(empty_plane) for i in range(len(state[0]))]
    state.append(deepcopy(new_unexpanded_cube))
    state.insert(0,deepcopy(new_unexpanded_cube))
    #print_state()

    #now trigger the power
    new_state = deepcopy(state)
    for l, w in enumerate(state):
        for k, z in enumerate(w):
            for j, y in enumerate(z):
                for i, x in enumerate(y):
                    avail_power = check_adjacent(i,j,k,l)
                    #if l==0:
                    #    print(f"{i}, {j}, {k}, {l}, {avail_power}")
                    if state[l][k][j][i] == 0 and avail_power == 3:
                        #print(f"{i}, {j}, {k}, {l}, {avail_power}")
                        new_state[l][k][j][i] = 1
                    elif state[l][k][j][i] == 1 and (avail_power < 2 or avail_power >3):
                        new_state[l][k][j][i] = 0
    state = new_state
    
    #print_state()
for i in range(6):
    expand_state()

total_count = 0
for w in state:
    for z in w:
        for y in z:
            for x in y:
                total_count += x

print(total_count)

