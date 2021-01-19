# ABC085D - Katana Thrower
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc085/tasks/abc085_d
# Date: 2021/01/16

# ---------- Ideas ----------
# 貪欲でいけそう
# a <= bなので，基本的にbは使い切ったほうがいい
# bの合計で足りるなら，それだけでいい
# 最終的にはbを全部投げつけた方が良いんだから，それまではAの一番強いのを投げればいいのかな？
# 注意! 一番強いaより弱いbでは攻撃しないほうがいい
# 弱いbは一番強いaで置き換えればいい！


# ------------------- Answer --------------------
#code:python
from math import ceil
n, h = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(n)]
a = sorted([i[0] for i in ab], reverse=True)
max_a = max(a)

# 弱いbを一番強いaで置き換える
b = []
for i in range(n):
    b.append(max(max_a, ab[i][1]))
b.sort(reverse=True)

if sum(b) >= h: # bだけで足りるとき
    cnt = 0
    for i in range(n): # hを超えるまでインクリメント
        cnt += b[i]
        if cnt >= h:
            print(i+1)
            exit()
else: # bだけで足りないときは，一番つよいaで攻撃し続ける
    rest_h = h - sum(b)
    ans = ceil(rest_h / max(a)) # aの攻撃回数
    ans += n # bを全て投げつける
    print(ans)


# ------------------ Sample Input -------------------
1 10
3 5

2 10
3 5
2 6

4 1000000000
1 1
1 10000000
1 30000000
1 99999999

5 500
35 44
28 83
46 62
31 79
40 43

# ----------------- Length of time ------------------
# 14分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc085/editorial.pdf
# 解説通りに溶けた
# 「すでに投げてしまった刀も振ることができるというルールに変更しても問題の答えは変わりません」と解釈できるらしい
# たしかに自分の解き方でもそうしてるわ?

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#貪欲
#greedy
#ABC-D
#400点問題
#緑diff
