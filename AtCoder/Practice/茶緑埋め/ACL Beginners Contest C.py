# ACL Beginners Contest C - Connect Cities
# URL: https://atcoder.jp/contests/abl/tasks/abl_c
# Date: 2021/02/02

# ---------- Ideas ---------- 
# 連結成分のグループ数を数えればいい。グループ数-1が答え
# Union-Find使う

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
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # 辺(a, b)の追加によってサイクルが形成されるときは追加しない
    # aとbが同じ親を持っていれば，サイクルが生まれることになる
    if uf.same(a, b): continue

    # 辺(a, b)を追加する
    uf.unite(a, b)

print(uf.group_count()-1)

# ------------------ Sample Input -------------------
3 1
1 2


# ----------------- Length of time ------------------
# 4分

# -------------- Editorial / my impression -------------
# 公式解説がない
# Union-Find貼り付けたらいけた！
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/09/27/080100
# BFSやDFSでも解けるよね。

# ----------------- Category ------------------
#AtCoder  
#Union-Find
#ABC-like
#ABC-C
#茶diff
#連結成分
