b = input()
b = int(b)
for i in range(b-len(str(b))*9, b):
    if i <= 0:
        continue
    elif i>0:
        if i+sum(list(map(int, str(i)))) == b:
            print(i)
            exit()
print(0)