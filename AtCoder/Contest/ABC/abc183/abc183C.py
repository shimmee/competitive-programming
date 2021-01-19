from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
from math import gcd, sin, cos, tan, asin, acos, atan, degrees, radians
from bisect import bisect_left, bisect_right, insort_left, insort_right

import sys
sys.setrecursionlimit(1000000)
mod = 1000000007
inf = float('INF')

def intput(): return int(input())
def mint(): return map(int,input().split())
def lint(): return list(map(int,input().split()))
def getX(n): return [int(input()) for i in range(n)]
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

def nest(n):
    nest = [[int(i) for i in input().split()] for _ in range(n)]
    return nest

from itertools import permutations



n, k = mint()
T = nest(n)
pattern = list(permutations([i for i in range(1, n)]))

ans = 0
for p in pattern:
    p = [0] + list(p) + [0]

    dist = 0
    for i in range(n):
        # print(T[p[i]][p[i+1]])
        dist += T[p[i]][p[i+1]]
    if dist == k:
        ans += 1
print(ans)

5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0


4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0
