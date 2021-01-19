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

def getNest(n):
    nest = [[int(i) for i in input().split()] for _ in range(n)]
    return nest

n = intput()
a = lint()

L = [i for i in range(2, 1001)]

count = 0
best_l = 0
for l in L:
    cnt = 0
    for i in range(n):
        if a[i] % l == 0:
            cnt += 1
    if count < cnt:
        count = cnt
        best_l = l

print(best_l)


3
333 999 1000

9
1 2 3 4 5 6 7 8 9

5
8 9 18 90 72

5
1000 1000 1000 1000 1000

3
3 12 7


