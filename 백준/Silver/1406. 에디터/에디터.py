import sys
from collections import deque
input = sys.stdin.readline

left_words = deque(input().rstrip())
right_words = deque()

command_number = int(input())

for i in range(command_number):
    command = input().rstrip()
    if command[0] == 'L' and left_words:
        right_words.appendleft(left_words.pop())
    elif command[0] == 'D' and right_words:
        left_words.append(right_words.popleft())
    elif command[0] == 'B' and left_words:
        left_words.pop()
    elif command[0] == 'P':
        command, word = command.split()
        left_words.append(word)

print(''.join(left_words)+''.join(right_words))