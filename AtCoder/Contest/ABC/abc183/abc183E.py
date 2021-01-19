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

h, w = mint()
S = [input() for i in range(h)]


dp = [[0]*(w+1) for _ in range(h+1)]
dp[0][0] = 1


for i in range(h):
    for j in range(w):
        if S[i][j] == '.':
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + dp[i][j]
print(dp)

3 3
...
.#.
...

4 4
...#
....
..#.
....
