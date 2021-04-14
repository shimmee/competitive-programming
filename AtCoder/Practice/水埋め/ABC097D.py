# ABC097D - Equals
# URL: https://atcoder.jp/contests/abc097/tasks/arc097_b
# Date: 2021/04/14

# ---------- Ideas ----------
# スワップの順番があるから，連結してるやつが色々ややこしい
# ペアをつなげることで一応木構造になりそう
# でもそもそも操作何回でもできるし，木の範囲内だったら自由に入れ替え可能なのではないか
# 連結成分の要素間のみでスワップ可能で，自由なところに配置できる
# ある連結成分に属するインデックスと，そのインデックスに書かれてる文字に被りがあれば，その数はpi=iとできる
# それを数える

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
P = list(map(int, input().split()))
P = [i - 1 for i in P]
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

ans = 0
for group in uf.all_group_members():
    p = []
    for i in group:
        p.append(P[i])
    ans += len(set(p) & set(group))
print(ans)



# ------------------ Sample Input -------------------
5 2
5 3 1 4 2
1 3
5 4


# ----------------- Length of time ------------------
# 18分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/arc097/editorial.pdf
# poypさんの水バチャで参加して18分で溶けた： 全完した
# 思いつけたのがとても嬉しい


# ----------------- Category ------------------
#AtCoder
#unionfind
#操作を何度でも可能
#グループ内なら自由に入れ替え可能
#グループ内なら自由に操作可能
#グラフに変換する問題
#木構造
#水色diff
#ABC-E