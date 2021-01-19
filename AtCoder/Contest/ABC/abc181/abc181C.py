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

n = getN()
a,b = getXY(n)

def linear(x1, y1, x2, y2):
    def wrapper(x):
        if x2-x1 != 0:
            return  ((y2-y1)/(x2-x1))*(x-x1)+y1
        else:
            return 0
    return wrapper

for i in range(n):
    for j in range(i+1, n):
        if a[i] == a[j]:
            for k in range(n):
                if k != i and k != j:
                    if a[i] == a[k]:
                        print('Yes')
                        exit()
        elif b[i] == b[j]:
            for k in range(n):
                if k != i and k != j:
                    if b[i] == b[k]:
                        print('Yes')
                        exit()
        else:
            fun = linear(a[i], b[i], a[j], b[j])
            for k in range(n):
                if  k != i and k != j:
                    if b[k] == fun(a[k]):
                        print('Yes')
                        exit()
print('No')

9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1


14
5 5
0 1
2 5
8 0
2 1
0 0
3 6
8 6
5 9
7 9
3 4
9 2
9 8
7 2



4
0 1
0 2
0 3
1 1
