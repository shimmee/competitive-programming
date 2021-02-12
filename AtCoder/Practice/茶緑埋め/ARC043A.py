# ARC043A - 点数変換
# URL: https://atcoder.jp/contests/arc043/tasks/arc043_a
# Date: 2021/02/11

# ---------- Ideas ----------
# 調整前の平均をXとすると
# A = PX+Q
# B = P(max(S) - min(S))
# まずPを求めてから，Qを求める
# 全員の点数が同じ時，min=maxのとき，max-minで割り算できないので，解なし

# ------------------- Answer --------------------
#code:python
n, A, B = map(int, input().split())
S = [int(input()) for _ in range(n)]
X = sum(S) / n
m1 = max(S)
m2 = min(S)

if m1 == m2:
    print(-1); exit()

P = B / (m1-m2)
Q = A - P*X

print(P, Q)

# ------------------ Sample Input -------------------
5 2 4
2
4
6
8
10


# ----------------- Length of time ------------------
# 11分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc043
# ただの連立方程式だった。平均の定義知らない人は解けなさそう
#

# ----------------- Category ------------------
#AtCoder
#平均値
#式変形
#点数調整