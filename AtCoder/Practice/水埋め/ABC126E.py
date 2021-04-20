# ABC126E - 1 or 2
# URL: https://atcoder.jp/contests/abc126/tasks/abc126_e
# Date: 2021/04/19

# ---------- Ideas ----------
# 未知数の個数を数えればいい？
# x1+x2=z, x2+x3=p, x3+x4=?
# みたいな式があれば，x1さえわかれば芋づる式に他の変数もわかりそう
# 何かの変数を介してつながってれば，1つだけ当てればよさそう
# 連結成分のグループ数を数えればいい -> UnionFind

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
uf = UnionFind(n)
unseen = [True]*n
for i in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    unseen[x] = False
    unseen[y] = False

    # 辺(a, b)の追加によってサイクルが形成されるときは追加しない
    # aとbが同じ親を持っていれば，サイクルが生まれることになる
    if uf.same(x, y): continue

    # 辺(a, b)を追加する
    uf.unite(x, y)

print(uf.group_count())

# ------------------ Sample Input -------------------
3 1
1 2 1

6 5
1 2 1
2 3 2
1 3 3
4 5 4
5 6 5

100000 1
1 100000 100

# ----------------- Length of time ------------------
# 3分 速い！

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc126/editorial.pdf
# けんちょんさん: https://drken1215.hatenablog.com/entry/2019/05/19/224500_1
# Z使わないんかーいってなった
# ABC097 D - Equalsにとても似てた

# ----------------- Category ------------------
#AtCoder
#連結成分の個数
#ABC-E
#パリティ
#Union-Find
#データ構造
#連結成分
#方程式
#差分制約系
#水色diff
#式変形
#競技数学色強め
#グラフに見立てて連結成分数える