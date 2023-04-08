m=0
index=0
for i in range(9):
    a=int(input())
    if a>m:
        m=a
        index=i
print(m)
print(index)