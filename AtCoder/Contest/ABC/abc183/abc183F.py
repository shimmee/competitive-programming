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

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n # 自分が根の場合，根を-1と表記: 初期状態ではみんなバラバラなのでみんな-1

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # xとyが同じグループに属するかどうか (根が一致するかどうか)
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループとを併合する
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)

        # すでに同じグループのときは何もしない
        if x == y: return False

        # union by size (y側のサイズが小さくなるようにする: xとyをスワップする: xをyの親にしたい)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    # xを含むグループのサイズ
    def size(self, x):
        return self.siz[self.root(x)]

    # グループ数を返す
    def group_count(self):
        parents = [i for i, x in enumerate(self.par) if x == -1]
        return len(parents)

    # 各グループに属する要素をリストで返す
    def all_group_members(self):
        from collections import defaultdict
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return list(group_members.values())


n, q = mint()
c = lint()
uf = UnionFind(n)
for i in range(q):
    Q = lint()
    if Q[0] == 1:
        a, b = Q[1]-1, Q[2]-1
        uf.unite(a, b)
    if Q[0] == 2:
        x, y = Q[1] - 1, Q[2]

query = nest(q)



5 5
1 2 3 2 1
1 1 2
1 2 5
2 1 1
1 3 4
2 3 4
