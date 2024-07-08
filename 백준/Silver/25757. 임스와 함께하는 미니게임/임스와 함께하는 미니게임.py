import sys
input = sys.stdin.readline

N, game = input().rstrip().split()
N = int(N)

if game == 'Y':
    play = set()
    for i in range(N):
        who = input().rstrip()
        if who not in play:
            play.add(who)
    print(len(play))

elif game == 'F':
    play = set()
    for i in range(N):
        who = input().rstrip()
        if who not in play:
            play.add(who)
    print(len(play)//2)

elif game == 'O':
    play = set()
    for i in range(N):
        who = input().rstrip()
        if who not in play:
            play.add(who)
    print(len(play)//3)