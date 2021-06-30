# 典型90問068 - Paired Information（★5）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bp
# Date: 2021/06/15

# ---------- Ideas ----------
# t=1のときxからyが導けるか？は，xとyが連結してるか？と同義なので，これはUnionFindで扱える
# 奇跡が起きて思いついた
# (v0, -v1, v2, -v3,...) みたいな感じの配列を考える。
# t=0のとき，この配列のx番目にvをいれるが，xが0-indexで偶数ならvを，奇数なら-vを入れる
# t=1のとき，この配列のxからyまでの累積和を取れば，未知数1つ(y)の1次方程式が立てられるので，その場で解いて出力する
# xとyの偶奇や大小で場合分けがトータル8個必要になる


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



def plus(a, b): return a + b  # 和の場合この関数を演算子として用いる
class SegTree:

    """
    二項演算子と単位元の組み合わせのメモ: https://qiita.com/yukoba/items/fd7f6a9c7eab2def526d
    和: operator=plus, ide_ele=0
    積: operator=prod, ide_ele=1
    最大値: operator=max, ide_ele=-float('INF')
    最小値: operator=min, ide_ele=float('INF')
    排他的論理和: operator=xor, ide_ele=False
    """

    def __init__(self, init_val, operator=min, ide_ele=float('INF')):
        """
        n: 元のデータ配列のサイズ
        init_val: 配列の初期値
        operator: 演算子(モノイド)。関数オブジェクト
        ide_ele: 演算子に対応する単位元
        k: n以上の最小の2のべき乗: 2**i >= nとなる最小のiとしたときの2**i=k
        tree: セグメント木(1-index)の配列: 初期値は単位元のide_ele: 配列の長さは1-indexで2*k
        """
        n = len(init_val)
        self.init_val = init_val
        self.operator = operator
        self.ide_ele = ide_ele

        # セグ木の構築の3つのステップ
        # ステップ1: k=2**i >= nを満たすようなkを求め，長さ2*kのセグ木配列treeを作る
        self.k = 1 << (n - 1).bit_length()
        self.tree = [self.ide_ele]*2*self.k

        # ステップ2: セグ木配列treeの最下段に，左詰めで，長さnの元の配列init_valを埋め込む
        for i in range(n):
            self.tree[self.k + i] = init_val[i]

        # ステップ3: 子供の方から親の方へ上りながら演算結果を埋めていく。ループのiが自分(親)とみなす。
        # 最下段はinit_valが埋まっているので，最下層の一段上の右端(i=k-1)から順にインデックス降順に埋めていく
        # 親(i)は自分の2人の子供(2*iと2*i+1)を演算したもの
        for i in reversed(range(1, self.k)):
            self.tree[i] = self.operator(self.tree[2 * i], self.tree[2 * i + 1])


    def update(self, i: int, x):
        """
        元の配列のi番目の値をxに更新する
        i: 元の配列の更新したいインデックス (0-index)
        x: 新しい数
        """
        i += self.k # self.kを足すことで，iが元の配列のインデックスから，セグ木配列のインデックスになる (最下段のインデックス)
        self.tree[i] = x # セグ木配列における最下段の値を更新する

        while i > 1: # 親がいる限り，構築と同じ手順で更新していく
            i //= 2 # 親のインデックス
            self.tree[i] = self.operator(self.tree[2 * i], self.tree[2 * i + 1])

    def get_query(self, l, r):
        """
        解説: https://www.creativ.xyz/segment-tree-entrance-999/
        元の配列において，半開区間[l, r)で演算したしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.k
        r += self.k
        while l < r:
            if l & 1:
                res = self.operator(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.operator(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


n = int(input())
q = int(input())

uf = UnionFind(n)
segtree = SegTree(init_val = [0]*(n-1), operator=plus, ide_ele=0)

for i in range(q):
    t, x, y, v = map(int, input().split())
    x, y = x-1, y-1

    if t == 0:
        # UnionFindの更新
        if uf.same(x, y): continue
        uf.unite(x, y)

        # segtreeの更新
        if x % 2 == 0:
            segtree.update(x, v)
        else:
            segtree.update(x, -v)

    elif t == 1:
        # xとyが同じならvを出力
        if x == y:
            print(v)
            continue

        # xとyが同じグループでなければ繋がってないのでambiguous
        if not uf.same(x, y):
            print('Ambiguous')
            continue

        cum = segtree.get_query(min(x,y), max(x,y))

        if x % 2 == y % 2 == 0: # x, yともに偶数のとき
            if x < y: print(v - cum)
            else: print(v + cum)
        elif x % 2 == y % 2 == 1: # x, yともに奇数のとき
            if x < y: print(v + cum)
            else: print(v - cum)
        elif x % 2 == 0 and y % 2 == 1: # xが偶数，yが奇数のとき
            if x < y: print(cum - v)
            else: print(-v - cum)
        elif x % 2 == 1 and y % 2 == 0: # xが奇数，yが偶数のとき
            if x < y: print(-v - cum)
            else: print(cum - v)






# ------------------ Sample Input -------------------
4
7
0 1 2 3
1 1 2 1
1 3 4 5
0 3 4 6
1 3 4 5
0 2 3 6
1 3 1 5

15
25
0 11 12 41
0 1 2 159
0 14 15 121
0 4 5 245
0 12 13 157
0 9 10 176
0 6 7 170
0 2 3 123
0 7 8 167
0 3 4 159
1 12 11 33
0 10 11 116
0 8 9 161
1 9 12 68
1 12 12 33
1 7 12 74
0 5 6 290
1 8 9 93
0 13 14 127
1 10 12 108
1 14 1 3
1 13 8 124
1 12 11 33
1 12 10 33
1 5 15 194


# ----------------- Length of time ------------------
# 1時間？

# -------------- Editorial / my impression -------------
# 今まで解けた問題で一番複雑だったかもしれない
# ダムの問題に似てたから，正負を交互にするのは思いつけた
# https://scrapbox.io/shinmeikeita-67718894/%23_ABC133D_-_Rain_Flows_into_Dams

# ----------------- Category ------------------
#AtCoder
#典型90問
#連立方程式
#芋づる式
#unionfind
#グラフ
#segtree
#セグメント木
#セグ木
