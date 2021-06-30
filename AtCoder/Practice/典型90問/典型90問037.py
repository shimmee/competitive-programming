# 典型90問037 - Don't Leave the Spice
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ak
# Date: 2021/05/10

# ---------- Ideas ----------
# ナップサックDPか？
# dp[i][j]: i番目までの料理を選択可能で，香辛料がちょうどjとなるように作ったときの価値の最大値
# 愚直に書いたらO(N*W^2)になって間に合わない W <= 10^4, N <= 500
# セグ木でdpテーブルを用意して，in-place DPをやってみよう

# ------------------- Answer --------------------
#code:python
inf_neg = -float('INF')
W, n = map(int, input().split())
lrv = [[int(i) for i in input().split()] for _ in range(n)]

dp = [[inf_neg for _ in range(W+1)] for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    l, r, v = lrv[i]
    for j in range(W+1):

        # i番目の料理を作る時
        for w in range(l, r+1): # 使用する香辛料の量
            if j - w >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)
        # i番目の料理を作らない時
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

ans = dp[n][W]
print(ans if ans >= 0 else -1)

# O(N*W^2)TLEだぜ！！
# ABC179D - Leaping Takと同じように累積和でDP高速化するのでは？
# i番目の料理を作って香辛料のトータルをjにするときの価値は、i-1番目の列の香辛料がj-lからj-rまでの価値から推移してくるわけだけど、
# j-lからj-rの間の価値の最大値さえわかれば良さそうだから、dpテーブル自体をセグ木で管理するみたいなことができたらO(NW log)でいけるのかもしれない
# i番目とi+1番目の2本のdpテーブル (というか1次元配列)だけ用意して使い回す方法をin-place DPと呼ぶらしい
# セグ木でdpテーブルを用意して，in-place DPをやってみよう

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

inf_neg = -float('INF')
W, n = map(int, input().split())
lrv = [[int(i) for i in input().split()] for _ in range(n)]

dp2 = [0] + [inf_neg] * W # in-place DPの2本目のdpテーブル
for i in range(n):
    l, r, v2 = lrv[i]

    # 1本目のdpテーブルをセグ木で用意し，2本目のdpテーブルの値で初期化
    segtree = SegTree(dp2, operator=max, ide_ele=-float('INF'))
    dp1 = segtree.tree[segtree.k:(segtree.k+W+1)] # 1本目の配列を取り出しておく
    dp2 = [0] + [inf_neg] * W # 2本目を初期化

    for j in range(W+1):
        # i番目の料理を作る時
        if j - l >= 0:
            s = j - r if j - r >= 0 else 0
            v1 = segtree.get_query(s, j - l + 1) # i番目の価値の最大値
            if dp2[j] <= v1+v2:
                dp2[j] = v1+v2
        # i番目の料理を作らない時
        if dp2[j] <= dp1[j]:
            dp2[j] = dp1[j]

ans = dp2[W]
print(ans if ans >= 0 else -1)

# print('-------------------')
# print(dp1)
# print(dp2)
# TLE 4つが取れない！！！！！！！！！
# 最悪計算量は6000万回くらいなので，セグ木のライブラリがおかしいとしか思えない
# 定数倍の戦いだった: https://twitter.com/ryuusagi/status/1392286152955031553
# まず-infが遅いっぽい，あと，lとrの幅が狭いときにlogWでクエリ処理してたら損するので，dp1のテーブルを線形探索した方が速い
#





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

inf_neg = -10**15
W, n = map(int, input().split())
lrv = [[int(i) for i in input().split()] for _ in range(n)]

dp2 = [0] + [inf_neg] * W # in-place DPの2本目のdpテーブル
for i in range(n):
    l, r, v2 = lrv[i]

    # 1本目のdpテーブルをセグ木で用意し，2本目のdpテーブルの値で初期化
    segtree = SegTree(dp2, operator=max, ide_ele=-float('INF'))
    dp1 = segtree.tree[segtree.k:(segtree.k+W+1)] # 1本目の配列を取り出しておく
    dp2 = [0] + [inf_neg] * W # 2本目を初期化

    for j in range(W+1):
        # i番目の料理を作る時
        if j - l >= 0:
            if r - l <= 5:
                v1 = max([dp1[max(0, j - l - k)] for k in range(r - l + 1)])
                dp2[j] = max(dp2[j], v1 + v2)
            else:
                s = j - r if j - r >= 0 else 0
                v1 = segtree.get_query(s, j - l + 1) # i番目の価値の最大値
                if dp2[j] <= v1+v2:
                    dp2[j] = v1+v2
        # i番目の料理を作らない時
        if dp2[j] <= dp1[j]:
            dp2[j] = dp1[j]

ans = dp2[W]
print(ans if ans >= 0 else -1)

# ------------------ Sample Input -------------------
10000 20
4539 6002 485976
1819 5162 457795
1854 2246 487643
1023 4733 393530
1052 6274 289577
1874 2436 167747
1457 4248 452660
2103 4189 174955
3057 5061 319316
4898 4953 394627
1313 2880 154687
1274 1364 259598
3866 5844 233027
1163 5036 386223
1234 4630 155972
2845 4978 442858
3168 5368 171601
3708 4407 394899
3924 4122 428313
2112 4169 441976

5000 5
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000

100 4
13 15 31415
12 13 92653
29 33 58979
95 98 32384

100 4
30 40 120
30 40 30
30 40 1500
30 40 40

10 4
3 4 12
1 3 3
5 7 15
2 4 4

# ----------------- Length of time ------------------
# 2時間位...?

# -------------- Editorial / my impression -------------
# 解説 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/037.jpg
# 自力で解法を思いつけたのがとても嬉しい
# 初めての定数倍の戦いだった
# in-place DPとセグ木のDP高速化を学んだ
# 今回は定数倍との戦いだったので1本目のテーブルだけセグ木にしたが，本番の問題だとそんな制約が厳しくないだろうから，2本目もセグ木で大丈夫かも
# スライド最小値というテクニックを使えばO(NW)で解けたらしい

# ----------------- Category ------------------
#AtCoder
#ナップサックDP
#DP高速化
#動的最適化
#in-placeDP
#セグメント木
#segtree
#segment_tree
#DP
#典型90問
#RMQ