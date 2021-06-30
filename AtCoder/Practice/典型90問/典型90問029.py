# 典型90問029 - Long Bricks
# URL: https://github.com/E869120/kyopro_educational_90/blob/main/problem/029.jpg
# Date: 2021/05/10

# ---------- Ideas ----------
# 各区間における最大値を保存して，O(1)くらいでアクセスできるようにする
# セグ木で書けそう
# 普通のセグ木は更新が1点しかできないから，区間を更新できる遅延セグメント木が必要だった
# ここから拝借した: https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e

# ------------------- Answer --------------------
#code:python

class LazySegTree:
    # 区間の更新が可能な遅延セグメント木: https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e
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
        self.lazy = [None] * 2 * self.k

        # ステップ2: セグ木配列treeの最下段に，左詰めで，長さnの元の配列init_valを埋め込む
        for i in range(n):
            self.tree[self.k + i] = init_val[i]

        # ステップ3: 子供の方から親の方へ上りながら演算結果を埋めていく。ループのiが自分(親)とみなす。
        # 最下段はinit_valが埋まっているので，最下層の一段上の右端(i=k-1)から順にインデックス降順に埋めていく
        # 親(i)は自分の2人の子供(2*iと2*i+1)を演算したもの
        for i in reversed(range(1, self.k)):
            self.tree[i] = self.operator(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, l, r):
        """
        伝搬する対象の区間を求める
        lm: 伝搬する必要のある最大の左閉区間
        rm: 伝搬する必要のある最大の右開区間
        """
        l += self.k
        r += self.k
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()

        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1


    def propagates(self, *ids):
        """
        遅延伝搬処理
        ids: 伝搬する対象の区間
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.tree[2 * i] = v
            self.tree[2 * i + 1] = v
            self.lazy[i] = None

    def update_interval(self, l, r, x):
        """
        区間[l, r)の値をxに更新
        l, r: index(0-index)
        x: update value
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.k
        r += self.k
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.tree[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.operator(self.tree[2 * i], self.tree[2 * i + 1])

    def get_query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

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

w, n = map(int, input().split())
lazysegtree = LazySegTree([0]*w, operator=max, ide_ele=-float('INF'))
for _ in range(n):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    max_val = lazysegtree.get_query(l, r+1)
    lazysegtree.update_interval(l, r+1, max_val+1)

    print(max_val + 1)

# ------------------ Sample Input -------------------
100 4
27 100
8 39
83 97
24 75

3 5
1 2
2 2
2 3
3 3
1 2

# ----------------- Length of time ------------------
# 40分
#

# -------------- Editorial / my impression -------------
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/029-02.jpg
# 初めて遅延セグメント使った。中身はよくわかってないけど便利

# ----------------- Category ------------------
#AtCoder
#区間最大値
#セグメント木
#segtree
#segment_tree
#セグ木
#遅延セグメント木
#遅延評価セグメント木