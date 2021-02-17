# ARC106B - Values
# URL: https://atcoder.jp/contests/arc106/tasks/arc106_b
# Date: 2021/02/15

# ---------- Ideas ----------
# 連携成分内のaとbの合計値が一致してたらいけるんじゃない？
# UnionFindでグループ作って，グループを走査して，aとbの合計が一致するか見る
# 全てのグループで一致すればOK

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
A = list(map(int, input().split()))
B = list(map(int, input().split()))

uf = UnionFind(n)
for i in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    # 辺(c, d)の追加によってサイクルが形成されるときは追加しない
    # cとdが同じ親を持っていれば，サイクルが生まれることになる
    if uf.same(c, d): continue

    # 辺(c, d)を追加する
    uf.unite(c, d)

uf.all_group_members()
flag = True
for group in uf.all_group_members():
    total_A = 0
    total_B = 0
    for i in group:
        total_A += A[i]
        total_B += B[i]
    if total_A != total_B:
        flag = False

print('Yes' if flag else 'No')



# ------------------ Sample Input -------------------

3 2
1 2 3
2 2 2
1 2
2 3


# ----------------- Length of time ------------------
# 8分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc106/editorial
# 操作して結局全部できまーす，みたいなこういう問題結構ある。
# 今までもいくつかあったから，すぐに気付けた


# ----------------- Category ------------------
#AtCoder
#グラフ
#UnionFind
#連結成分
#ARC-B
#茶diff
#操作:SをTにすることが目的の操作の問題
#操作を好きな回数だけ行える
#総和の一致
#全部できる
#基本できる