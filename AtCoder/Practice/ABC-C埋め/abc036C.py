# ABC036C - 座圧
# URL: https://atcoder.jp/contests/abc036/tasks/abc036_c
# 日付: 2020/12/18

# ---------- 思ったこと / 気づいたこと ----------
# 座標圧縮はscipyさんにおまかせ

# ------------------- 方針 --------------------
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rankdata.html
# 座標圧縮という名の「リストの要素の大きさにランキングをつけるだけ」

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = [int(input()) for _ in range(n)]
from scipy.stats import rankdata
rank = rankdata(a, method='dense') # 色々methodあるけどdense
for i in rank:
    print(i-1)

# ------------------ 入力例 -------------------
5
3
3
1
6
1


# ----------------- 解答時間 ------------------
# 3分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/abc/036/editorial.pdf
# 他の人はbisectやenumerate使って解いてる

# ----------------- カテゴリ ------------------
#AtCoder #abc
#座標圧縮
#scipy
