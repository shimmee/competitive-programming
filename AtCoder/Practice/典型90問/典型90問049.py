# 典型90問049 - Flip Digits 2
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_aw
# Date: 2021/05/25

# ---------- Ideas ----------
# 解説AC
# 最小全域木らしい

# ------------------- Answer --------------------
#code:python
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



n, m = map(int, input().split())
G = []
for i in range(m):
    c, l, r = map(int, input().split())
    G.append([c, l, r])

# Gの各辺を重みが小さい順にソートする
G.sort()
uf = UnionFind(n+1)
ans = 0

for i in range(m):
    w, a, b = G[i]

    # 辺(a, b)の追加によってサイクルが形成されるときは追加しない
    # aとbが同じ親を持っていれば，サイクルが生まれることになる
    if uf.same(a-1, b): continue

    # 辺(a, b)を追加する
    ans += w
    uf.unite(a-1, b)

if uf.group_count() != 1:
    print(-1)
else:
    print(ans)

# ------------------ Sample Input -------------------
2 3
1 1 1
1 2 2
10 1 2

4 5
3 1 2
5 2 4
9 3 4
4 1 4
8 2 4

# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/049.jpg
# 結構注意深く読んだけど全く思いつかなかった

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#最小全域木