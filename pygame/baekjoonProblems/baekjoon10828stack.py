import sys

def push(x):
    stack.append(x)
def pop():
    if len(stack)>0:
        print(stack[len(stack)-1])
        stack.pop()
    elif len(stack)==0:
        print(-1)
def size():
    print(len(stack))
def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
def top():
    if len(stack)>0:
        print(stack[len(stack)-1])
    else:
        print(-1)

stack = []
n=int(sys.stdin.readline())
for i in range(n):
    cmd=sys.stdin.readline().split()
    if len(cmd) > 1:
        if cmd[0]=='push':
            push(cmd[1])
    elif len(cmd) == 1:
        if cmd[0]=='pop':
            pop()
        elif cmd[0]=='size':
            size()
        elif cmd[0]=='empty':
            empty()
        elif cmd[0]=='top':
            top()