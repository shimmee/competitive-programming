# dwangoプログラミングコンテスト: B - ニコニコ文字列
# URL: https://atcoder.jp/contests/dwango2015-prelims/tasks/dwango2015_prelims_2
# Date: 2021/02/13

# ---------- Ideas ----------
# 連続部分列
# 25を他の文字(X)にreplaceしてしゃくとり法
# groupbyのほうが簡単かも: m個連続でXが並んでるなら，連続部分列のスタートとゴールを決めるから
# そこから取れるのはm*(m+1)//2個

# ------------------- Answer --------------------
#code:python
from itertools import groupby
S = input()
S = S.replace('25', 'X')
n = len(S)

gr = groupby(S)
ans = 0
for key, group in gr:
    if key == 'X':
        m = len(list(group))
        ans += m*(m+1)//2
print(ans)

# ------------------ Sample Input -------------------
2525

1251251252525


# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/dwango2015-prelims/editorial.pdf
#groupbyとても使いやすい

# ----------------- Category ------------------
#AtCoder
#連続部分列
#groupby
#文字列操作