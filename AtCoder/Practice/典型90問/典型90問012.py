# 典型90問 12日目
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_l
# Date: 2021/04/11

# ---------- Ideas ----------
# 緑diffなので解けそう
# O(Q)でクエリ処理しなきゃいけない
# グリッドのセルをグラフの頂点と見なして，union-findで隣接するセルをunionしてグループ化すればよさそう
# セルにidを振る必要がある: 1-indexedで id = w*(y-1) + x と表せる
# 0-indexならid = w*y+x
# 隣接マスが訪問済みなら同じグループに入れられる

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

dydx = [[0, 1], [1, 0], [0, -1], [-1, 0]]
h, w = map(int, input().split())
Q = int(input())
uf = UnionFind(h*w)
seen = [False]*(h*w)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1: # クエリをufに追加
        y, x = q[1] - 1, q[2] - 1
        id = w*y + x
        seen[id] = True

        # 隣接マスが訪問済みなら同じグループに入れられる
        for dy, dx in dydx:
            Y = y + dy
            X = x + dx
            if 0 <= Y < h and 0 <= X < w:
                id_adj = w * Y + X
                if seen[id_adj]:
                    if uf.same(id, id_adj): continue
                    uf.unite(id, id_adj)
    else: # 陸続きの判定クエリ
        sy, sx, gy, gx = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
        sid = w * sy + sx # スタート地点のid
        gid = w * gy + gx # ゴール地点のid
        if seen[sid] and seen[gid] and uf.same(sid, gid):
            print('Yes')
        else:
            print('No')



# ------------------ Sample Input -------------------
3 3
10
1 2 2
1 1 1
2 1 1 2 2
1 3 2
2 1 1 2 2
2 2 2 3 2
1 2 3
1 2 1
2 1 1 2 2
2 1 1 3 3


1 1
3
2 1 1 1 1
1 1 1
2 1 1 1 1

# ----------------- Length of time ------------------
# 20分くらい

# -------------- Editorial / my impression -------------
# グリッドのunion-findは初めてかも
# 実装が結構重かった
# 1-indexedで書くとバグったので0-indexedで書き直した

# ----------------- Category ------------------
#AtCoder
#グリッドに番号を振る
#グリッドのグラフ化
#Union-find
#grid
#陸続きの判定
#グリッド上のunionfind