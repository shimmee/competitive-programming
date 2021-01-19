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

x1, y1, x2, y2 = mint()
y2 = -y2

if y1 == y2:
    print((x1+x2)/2)
else:
    x = (x1*(y2-y1)-y1*(x2-x1))/(y2-y1)
    print(x)
-9 99 -999 9999


1 1 7 2

1 1 3 2
