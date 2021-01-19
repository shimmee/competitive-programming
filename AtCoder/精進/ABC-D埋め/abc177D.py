# ABC177D - Friends
# URL: https://atcoder.jp/contests/abc177/tasks/abc177_d
# 日付: 2020/11/20

# ---------- 思ったこと / 気づいたこと ----------
# 最大派閥を探して，最大派閥の人数を出力すればいいやん

# ------------------- 方針 --------------------
# Union-findで友達の組をどんどんuniteする
# 最後に連結成分(グループに属する人数の数)の最大数を出力する

# ------------------- 解答 --------------------
# code:python
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
    uf.unite(a-1, b-1)
ans = 0
for g in uf.all_group_members():
    ans = max(ans, len(g))
print(ans)
# ------------------ 入力例 -------------------
5 3
1 2
3 4
5 1

4 10
1 2
2 1
1 2
2 1
1 2
1 3
1 4
2 3
2 4
3 4

10 4
3 1
4 1
5 9
2 6


# ----------------- 解答時間 ------------------
# 5分

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/abc177/editorial/90
# 一瞬で解けた！！！！嬉しい！！！！


# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#Union-Find
#連結成分の数