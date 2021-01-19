def getN(): return int(input())
def getLI(): return list(map(int,input().split()))
def getX(n): return [int(input()) for i in range(n)]
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

def getNest(n):
    xy = [[int(i) for i in input().split()] for _ in range(n)]
    return xy

def n_sum(n):
    return int(n*(n+1)/2)

n = getN()
a,b = getXY(n)
ans = 0
for i in range(n):
    ans += n_sum(b[i]) - n_sum(a[i]-1)
print(ans)

3
11 13
17 47
359 44683
