
facing = 0
waypointx = 10
waypointy = 1
shipx = 0
shipy = 0
with open('input.txt', 'r') as fin:
    for line in fin:
        action = line[0]
        magnitude = int(line[1:])
        if action == 'F':
            shipx += waypointx * magnitude
            shipy += waypointy * magnitude
        if action == 'E':
            waypointx += magnitude
        elif action == 'W':
            waypointx -= magnitude
        elif action == 'N':
            waypointy += magnitude
        elif action == 'S':
            waypointy -= magnitude
        elif action == 'R':
            for i in range(magnitude/90):
                waypointy += waypointx
                waypointx = waypointy-waypointx
                waypointy = -1*(waypointy-waypointx)
        elif action == 'L':
            for i in range(magnitude/90):
                waypointy += waypointx
                waypointx = -1*(waypointy-waypointx)
                waypointy = waypointy+waypointx
print(shipx)
print(shipy)
print(abs(shipx)+abs(shipy))

