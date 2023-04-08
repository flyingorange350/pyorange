
output = []
outcomes = ['모','도','개','걸','윷']

for i in range(3):
    yut = list(map(int,input().split()))
    cnt = 0
    for j in range(4):
        if yut[j] == 0:
            cnt += 1
    output.append(outcomes[cnt])

for k in range(len.output):
    print(output[k])