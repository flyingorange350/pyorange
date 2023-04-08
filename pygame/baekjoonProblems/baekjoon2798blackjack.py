import sys

ans = 0
def play():
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                sum = cards[i]+cards[j]+cards[k]
                if sum <= m and sum > ans:
                    ans = sum
    print(ans)
    
n, m = sys.stdin.readline().split()
n = int(n)
m = int(m)
cards = list(map(int,sys.stdin.readline().split()))
cardNum = sorted(cards)
if cardNum[0] + cardNum[1] + cardNum[2] <= m:
    play()
