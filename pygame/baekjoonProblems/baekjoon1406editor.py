from collections import queue
import sys
words1=queue()
words1=sys.stdin.readline()
words2=queue()
m=int(input())
for i in range(m):
    cmd=input().split()
    if len(cmd) == 1:
        if cmd=='L':
            words2.appendleft(words1[len(words1)-1])
            words1.pop()
        elif cmd=='D':
            words1.append(words1[len(words1)-1])
            words2.popleft()