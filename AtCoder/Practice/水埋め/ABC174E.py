# ABC174E - Logs
# URL: https://atcoder.jp/contests/abc174/tasks/abc174_e
# Date: 2021/04/10

# ---------- Ideas ----------
# わからなすぎて解説の1行目からヒントもらって思いついた
# 答えがXだとしたら，全てのlogsをK回以内のカットでX以下にする必要がある
# それぞれの木aiがX以内に納まるためのカット回数をO(N)で求めて，合計を出す。この合計がK以内かどうか調べる
# 右がOKの二分探索でこのXを探す

# ------------------- Answer --------------------
#code:python
from math import ceil
n, k = map(int, input().split())
A = list(map(int, input().split()))

ok = max(A)+1
ng = 0
while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    total = sum([ceil(a/mid) - 1 for a in A])
    if total <= k:
        ok = mid
    else:
        ng = mid
print(ok)

# ------------------ Sample Input -------------------
"""
2 3
7 9

10 10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202
"""
# ----------------- Length of time ------------------
# 40分くらい考えた

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc174/editorial.pdf
# ヘンリーにめぐる式二分探索のokとngがweirdって言われた
# pycharmのデバッグ教えてもらった
# 最小を求めるって言われたときに二分探索をすぐに思いつくべきだった
# 射撃王に似てる

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#二分探索
#決め打ち二分探索
