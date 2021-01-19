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
    x, y, z= [list(i) for i in zip(*xy)]
    return x, y, z

def nest(n):
    nest = [[int(i) for i in input().split()] for _ in range(n)]
    return nest

# いもす法で解けるらしい
# ステップ1: 加算処理
# 区間[l, r]にvを加算したい時，l番目の値にvを加算する
# r+1番目の値に-v加算する
# ステップ2
# 最後に累積和すると最終結果を得られる


n, w = mint()
stp = nest(n)
stp = sorted(stp, key=lambda x: (x[0], x[1], x[2]))

d = [0]*(2*(10**5)+1)
for s, t, p in stp:
    d[s] += p
    d[t] -= p
cumsum = list(accumulate(d))
if max(cumsum) <= w:
    print('Yes')
else:
    print('No')

6 1000000000
0 200000 999999999
2 20 1
20 200 1
200 2000 1
2000 20000 1
20000 200000 1


4 10
1 3 5
2 4 4
3 10 6
2 3 1


4 10
1 3 5
2 4 4
3 10 6
2 4 1
