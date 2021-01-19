from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
from math import gcd, sin, cos, tan, asin, acos, atan, degrees, radians
from bisect import bisect_left, bisect_right, insort_left, insort_right
import numpy as np

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

h, w, n, m = mint()
a = [[int(i)-1 for i in input().split()] for _ in range(n)]
b = [[int(i)-1 for i in input().split()] for _ in range(m)]

lr = [[0 for i in range(w)] for j in range(h)]
ud = [[0 for i in range(w)] for j in range(h)]

for bx, by in b:
    lr[by][bx] = 2
    ud[by][bx] = 2

for x, y in a:
    if lr[y][x] == 0:
        lr[y][x] = 1
        l = x - 1
        r = x + 1

        while l >= 0 and (lr[y][l] == 0 or lr[y][l] == 1):
            lr[y][l] = 1
            l -= 1

        while r < w and (lr[y][r] == 0 or lr[y][r] == 1):
            lr[y][r] = 1
            r += 1

    if ud[y][x] == 0:
        ud[y][x] = 1
        u = y - 1
        d = y + 1

        while u >= 0 and (ud[u][x] == 0 or ud[u][x] == 1):
            ud[u][x] = 1
            u -= 1

        while d < h and (ud[d][x] == 0 or ud[d][x] == 1):
            ud[d][x] = 1
            d += 1

ans = 0
for i in range(h):
    for j in range(w):
        if lr[i][j] == 1 or ud[i][j] == 1:
            ans += 1
print(ans)


# なぜかRE!!!!!
