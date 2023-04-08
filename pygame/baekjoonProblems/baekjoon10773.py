k=int(input())
num = []
for i in range(k):
    call=int(input())
    if call>0:
        num.append(call)
    elif call == 0:
        num.pop()
print(sum(num))