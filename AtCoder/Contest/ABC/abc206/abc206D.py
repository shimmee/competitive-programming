# ABC206D - KAIBUNsyo
# URL: https://atcoder.jp/contests/abc206/tasks/abc206_d
# Date: 2021/06/19

# ---------- Ideas ----------
# 前半分と反転した後ろ半分を各要素ずつ比較
# グラフとして見なして連結成分としてつなげる
# ある連結成分の要素数がk個なら，k-1回の操作でその連結成分内は全て同じ色にできる
# 各連結成分の要素数-1 の和が答え

# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))
A = [a-1 for a in A]
for_ = A[:n//2]
back_ = A[::-1][:n//2]

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)
    def unite(self, x, y):

        x, y = self.root(x), self.root(y)

        if x == y: return False


        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


    def all_group_members(self):
        from collections import defaultdict
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return list(group_members.values())



uf = UnionFind(max(A)+1)
for i in range(n//2):
    x = for_[i]
    y = back_[i]

    if x != y:
        if uf.same(x, y): continue
        uf.unite(x, y)
ans = 0
for group in uf.all_group_members():
    if len(group) >= 2:
        ans += len(group)-1
print(ans)

# ------------------ Sample Input -------------------


6
1 2 3 4 5 6

8
1 2 1 2 1 2 1 2

6
1 2 3 4 4 4

8
1 5 3 2 5 2 3 1

7
1 2 3 4 1 2 3

1
200000

7
1 2 3 4 5 6 2

# ----------------- Length of time ------------------
# 30分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc206/editorial
# bfsでもdfsでも連結成分は数えられるのでなんでもいい

# ----------------- Category ------------------
#AtCoder
#ABC206
#ABC-D
#unionfind
#連結成分

