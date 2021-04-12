# ARC017C - 無駄なものが嫌いな人
# URL: https://atcoder.jp/contests/arc017/tasks/arc017_3
# Date: 2021/04/09

# ---------- Ideas ----------
# 2^32は間に合わないので，半分に分けてみる: 半分全列挙してみる
# 半分にわけてそれぞれbit全探索で取りうる値を列挙する
# 半分ずつ列挙したものをCounterして，出現回数を出しておく
# 前半で出来た重さWの組み合わせを使うなら，後半からはX-Wの重さが必要なので探す
# もしあったら，出現回数の積が通り数なのでインクリメント

# ------------------- Answer --------------------
#code:python
import itertools
from collections import deque, Counter
n, x = map(int, input().split())
w = [int(input()) for _ in range(n)]

w1 = w[:(n//2)]
w2 = w[(n//2):]

n1 = len(w1)
n2 = len(w2)

l1 = []
all_pattern = itertools.product([0, 1], repeat=n1)
for pattern in all_pattern:
    cnt = 0
    for i in range(n1):
        if pattern[i] == 1:
            cnt += w1[i]
    l1.append(cnt)

l2 = []
all_pattern = itertools.product([0, 1], repeat=n2)
for pattern in all_pattern:
    cnt = 0
    for i in range(n2):
        if pattern[i] == 1:
            cnt += w2[i]
    l2.append(cnt)

counter1 = Counter(l1)
counter2 = Counter(l2)

ans = 0
for key, value in counter1.items():
    ans += value * counter2[x-key]
print(ans)



# ------------------ Sample Input -------------------
5 5
1
1
2
3
4


# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc017
# はじめての半分全列挙だった
# 半分全列挙を使うと知らないまま解いたけど思いつけた
# 簡単すぎてびっくりした
# もっと短くコード書けた気がするけど，満足

# ----------------- Category ------------------
#AtCoder
#半分全列挙
#全探索
#bit全探索