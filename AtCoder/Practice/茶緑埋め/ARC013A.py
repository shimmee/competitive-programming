# ARC013A - 梱包できるかな？
# URL: https://atcoder.jp/contests/arc013/tasks/arc013_1
# Date: 2021/02/18

# ---------- Ideas ----------
# 荷物の向きを決める: 3パターン
# ダンボールの向きは固定で，荷物の向きを変える

# ------------------- Answer --------------------
#code:python
n,m,l = map(int, input().split())
p,q,r = map(int, input().split())

if max([n,m,l]) < max([p,q,r]):
    print(0); exit()

cnt1 = (l//r)*max((n//p)*(m//q), (n//q)*(m//p)) # rを高さにする
cnt2 = (l//q)*max((n//p)*(m//r), (n//r)*(m//p)) # qを高さにする
cnt3 = (l//p)*max((n//q)*(m//r), (n//r)*(m//q)) # pを高さにする

print(max(cnt1, cnt2, cnt3))

# ------------------ Sample Input -------------------
7 7 1
3 3 1

5 5 5
2 2 2

5 10 3
2 5 3


# ----------------- Length of time ------------------
# 17分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/hamayanhamayan/at-coder-regular-contest-013
# 思ったより時間がかかった
# ダンボール問題は辺を固定して全探索?

# ----------------- Category ------------------
#AtCoder
#荷詰め
#ダンボール
#場合分け