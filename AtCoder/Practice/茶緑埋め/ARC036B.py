# ARC036B - 山のデータ
# URL: https://atcoder.jp/contests/arc036/tasks/arc036_b
# Date: 2021/02/15

# ---------- Ideas ----------
# 連続する2つの極小値のインデックスの差が答え
# 全ての極小値のインデックスを保存して，最大の差を探す
# 左端と右端は極小値とみなしておく


# ------------------- Answer --------------------
#code:python
n = int(input())
h = [int(input()) for _ in range(n)]

# 極小値のインデックス: 左端と右端は必ず極小値とみなす
min_idx = [0, n-1]

# 真ん中の部分が極小かどうか
for i in range(1, n-1):
    if h[i-1] > h[i] and h[i] < h[i+1]: # 極小値の条件
        min_idx.append(i)

min_idx.sort()

# 連続する2つの極小値のインデックスの差が最大になるのがよい
ans = 0
for i in range(len(min_idx)-1):
    ans = max(ans, min_idx[i+1]-min_idx[i] + 1)
print(ans)


# ------------------ Sample Input -------------------
6
4
5
1
6
9
7


# ----------------- Length of time ------------------
# 13分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc036
# 解説通りだった。
# 極小値の差，に気づけたのがよかった
# CODE FESTIVAL 2014 決勝: E - 常ならずグラフににてる！

# ----------------- Category ------------------
#AtCoder
#極値
#極小値

