# CODE FESTIVAL 2015 あさぷろ Middle: A - ヘイホー君と最終試験
# URL: https://atcoder.jp/contests/code-festival-2015-morning-middle/tasks/cf_2015_morning_easy_c
# Date: 2021/02/13

# ---------- Ideas ----------
# 合計でK*R点必要
# 上位k個の合計がK*Rを上回っていればOK
# 下回っていれば上位K-1個とK*Rの差が必要
# 差が最高得点のmより小さければOK

# ------------------- Answer --------------------
#code:python
n, k, m, r = map(int, input().split())
S = [int(input()) for _ in range(n-1)]
S.sort(reverse=True)

goal = k*r
now = sum(S[:k])
if now >= goal:
    print(0)
else:
    rest = goal - sum(S[:k-1])
    print(rest if rest <= m else -1)

# ------------------ Sample Input -------------------
5 3 100 60
86
23
49
39


# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# https://smijake3.hatenablog.com/entry/2015/11/17/231745
# 公式の解説がないぜ
# ただの場合分けでした

# ----------------- Category ------------------
#AtCoder
#場合分け
#平均値
#緑diff