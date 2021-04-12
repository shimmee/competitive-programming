# ARC045B - ドキドキデート大作戦高橋君
# URL: https://atcoder.jp/contests/arc045/tasks/arc045_b
# Date: 2021/04/10

# ---------- Ideas ----------
# 担当する区間におけるすべての教室で，2人以上掃除する人がいればサボることができる
# まずは各教室に何人掃除する人がいるのかimosで出す
# 次に，入力の各区間に属する教室の掃除する人の最小値を求めて，1より大きいならサボれるのでOK
# 区間の最小値なのでセグメント木を用いる

# ------------------- Answer --------------------
#code:python
class SegTree:

    """
    二項演算子と単位元の組み合わせのメモ: https://qiita.com/yukoba/items/fd7f6a9c7eab2def526d
    和: operator=sum, ide_ele=0
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
        self.tree = [ide_ele]*2*self.k

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

from itertools import accumulate
n, m = map(int, input().split())
st = [[int(i) for i in input().split()] for _ in range(m)]

imos = [0] * (n+2)
for s, t in st:
    imos[s] += 1
    imos[t+1] -= 1

cum = list(accumulate(imos))

segtree = SegTree(cum, operator=min, ide_ele=float('INF'))
ans = []
for i in range(m):
    s, t = st[i]
    if segtree.get_query(s, t+1) > 1:
        ans.append(i+1)

print(len(ans))
for i in ans:
    print(i)




# ------------------ Sample Input -------------------
10 5
1 4
5 5
6 8
9 10
5 6

# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc045
# わりとすぐに思いつけてとても嬉しかった
# 初めてセグメント木を初見の問題で使った
# imosのインデクスがバグってちょっとこまった

# ----------------- Category ------------------
#AtCoder
#水色diff
#imos
#いもす法
#セグメント木
#クエリ処理問題
#区間クエリ