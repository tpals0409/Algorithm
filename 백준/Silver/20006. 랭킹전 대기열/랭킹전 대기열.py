player_num, start_num = map(int, input().split())
player_num = int(player_num)

room = list()
"""
key= [0, 20]
values = ['10 a', '15 b', ~]
"""


for _ in range(player_num):
    level, player = input().split()
    level = int(level)
    make_room = True
    for j in range(len(room)):
        min_level, max_level = room[j][0]
        if (min_level <= level <= max_level) and (len(room[j][1]) < start_num):
            room[j][1].append((level, player))
            make_room = False
            break
    if make_room:
        room.append([[level-10, level+10], [(level, player)]])

for answer in room:
    players = answer[1]
    if len(players) == start_num:
        print('Started!')
    else:
        print("Waiting!")
    players_sorted = sorted(players, key=lambda x: x[1])
    for level, player in players_sorted:
        print(level, player)
