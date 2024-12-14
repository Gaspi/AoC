import re

robots = []
with open('./input.txt', 'r') as file:
    for line in file.read().splitlines():
        match = re.match("p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)$", line)
        robots.append({
            "p": [int(match[1]), int(match[2])],
            "v": (int(match[3]), int(match[4]))
            })

height = 103 # 7
width = 101 # 11

def final_pos(robot, n):
    return  ( robot["p"][0] + n*robot["v"][0]) % width, (robot["p"][1] + n*robot["v"][1]) % height



nbsteps = 100
quadrants = [0,0,0,0]

for robot in robots:
    final_x, final_y = final_pos(robot, nbsteps)
    if final_x < width // 2:
        if final_y < height // 2:
            quadrants[0]+=1
        elif final_y > height // 2:
            quadrants[1]+=1
    elif final_x > width // 2:
        if final_y < height // 2:
            quadrants[2]+=1
        elif final_y > height // 2:
            quadrants[3]+=1

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])

for i in range(10000):
    allpos = set([final_pos(r, i) for r in robots])
    if len(allpos) == 500:
        print(i)
        for i in range(height):
            print( ''.join(['.' if (i,j) in allpos else 'X' for j in range(width)]) )

