# ABC173-C: H and V
# URL:
# 日付: 2020年11月18日

# ---------- 思ったこと / 気づいたこと ----------
# h, w <= 6なので全探索出来そう
# 赤く塗る行列をそれぞれで選ぶbit全探索
# 2^12で行ける！
# こういうのはnumpy使ったほうが楽そう

# ------------------- 方針 --------------------
# 白を0，黒を1とする
# hとwの2重ループで赤くする行列を決める
# 赤くひっくり返す行or列を一気に0に変換
# 最後にsumを求めてkになるかどうか評価

# ------------------- 解答 --------------------
#code:python
import numpy as np
from copy import deepcopy
h, w, k = map(int, input().split())
C = [input() for _ in range(h)]

# 0, 1に直したい: #なら1
G = np.zeros((h, w), int)
for i in range(h):
    for j in range(w):
        if C[i][j] == '#':
            G[i][j] = 1

ans = 0
for hi in range(2**h):
    for wi in range(2**w):
        G_ = deepcopy(G)
        for hj in range(h): # 行を引っくり返す
            if (hi >> hj) & 1:
                G_[hj,:] = 0
        for wj in range(w): # 列をひっくり返す
            if (wi >> wj) & 1:
                G_[:, wj] = 0

        if G_.sum() == k:
            ans += 1
print(ans)


# ------------------ 入力例 -------------------
6 6 8
..##..
.#..#.
#....#
######
#....#
#....#

2 3 2
..#
###

# ----------------- 解答時間 ------------------
# 24分

# ---------------- 感想 / 反省 ----------------
# bitの部分を他のところからコピーしてきたから，空で書けるようになりたい。
# かといって実際のこと考えたら簡単なスニペットを用意しておいてもいいレベル

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#bit全探索 #numpy


