# 典型90問004 - Cross Sum（★2）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_d
# Date: 2021/05/09

# ---------- Ideas ----------
# 行と列の和をそれぞれ事前計算でとっておく: sum_r, sum_c
# y行x列目の出力は，sum_rとsum_cの対応する部分の和からダブルカウントを引くために自分自身を引く
# = sum_r[y] + sum_c[x] - B[y][x]

# ------------------- Answer --------------------
#code:python
h, w = map(int, input().split())
B = [[int(i) for i in input().split()] for _ in range(h)]

sum_r = [sum(B[i]) for i in range(h)]
sum_c = [sum([B[i][j] for i in range(h)]) for j in range(w)]

for y in range(h):
    l = []
    for x in range(w):
        l.append(sum_r[y] + sum_c[x] - B[y][x])
    print(*l)


# ------------------ Sample Input -------------------
4 4
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# こういう問題こそnumpy使ったほうが速そう
# ランプ問題と同じ類
# 一応，包除原理らしい

# ----------------- Category ------------------
#AtCoder
#典型90問
#ダブルカウント
#ダブルカウントを引く
#包除原理
#ランプ問題
#Lamp問題
#ライト問題
#