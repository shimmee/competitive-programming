# ARC114B - Special Subsets
# URL: https://atcoder.jp/contests/arc114/tasks/arc114_b
# Date: 2021/03/14

# ---------- Ideas ----------
# union-findで閉じてるグループを作る
# 閉じてるグループを入れるか入れないかで2**k通り
# union-findじゃない！
# 有向グラフとして見なして，サイクルがあればそれは部分集合Tになる
# サイクルの数をnumとして，2**num-1が答え
# サイクルの数を数える方法: https://www.quora.com/How-do-I-count-the-number-of-cycles-in-a-directed-graph

# ------------------- Answer --------------------
#code:python
import sys
sys.setrecursionlimit(10000000)
from collections import defaultdict
class Solution:
    def countCycle(self, n, pairs):
        self.graph = defaultdict(list)
        self.visited = defaultdict(lambda: 0)
        self.count = 0
        for var1, var2 in pairs:
            self.addEdge(var1, var2)

        for i in range(n):
            self.depthFirstSearch(i)

        return self.count

    def addEdge(self, var1, var2):
        self.graph[var1].append(var2)

    def depthFirstSearch(self, var):
        # if cycle is detected
        if self.visited[var] == -1:
            self.count += 1
            return
        # if depth first search has been completed on this variable
        if self.visited[var] == 1:
            return

        self.visited[var] = -1

        for neighb in self.graph[var]:
            self.depthFirstSearch(neighb)

        # mark depth first search on this variable as completed
        self.visited[var] = 1

mod = 998244353
n = int(input())
F = list(map(int, input().split()))
pairs = []
for i in range(n):
    pairs.append([i, F[i]-1])

s = Solution()
num = s.countCycle(n, pairs)
print((2**num - 1) % mod)


# UnionFindでも解けるのか？
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

mod = 998244353
n = int(input())
F = list(map(int, input().split()))
uf = UnionFind(n)
for i in range(n):
    f = F[i] - 1
    # 辺(a, b)の追加によってサイクルが形成されるときは追加しない
    # aとbが同じ親を持っていれば，サイクルが生まれることになる
    if uf.same(i, f): continue

    # 辺(a, b)を追加する
    uf.unite(i, f)

cnt = uf.group_count()
print((2**cnt - 1) % mod)
# 解けた！

# ------------------ Sample Input -------------------
4
2 3 1 1

2
2 1

2
1 1

3
1 2 3


# ----------------- Length of time ------------------
# 50分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc114/editorial
# サイクルの数を数えればいいことに気付くのに時間がかかったけど，サイクルの数自体はググった方法ですぐ行けた
# 本番で解けた！

# ----------------- Category ------------------
#AtCoder
#有向グラフ
#サイクルのカウント
#グラフ
#cycle
#連結成分の個数
#UnionFind
