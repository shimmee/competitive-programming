# CODE FESTIVAL 2016 qual A: C - 次のアルファベット
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_c
# Date: 2021/01/28

# ---------- Ideas ----------
# できれば皆aにしてあげたい
# Sの左の文字から順にaにしたい。貪欲に
# 左から1文字ずつ見ていって，aにするのにKで足りればaにして，aとの距離をKから引く
# 最後kが余ってたら，最後の文字を回す
# 文字がaの部分はスキップする

# ------------------- Answer --------------------
#code:python
S = input()
k = int(input())
alpha2num = lambda c: ord(c) - ord('a')
import string
alpha = list(string.ascii_lowercase)

t = ''
for s in S:
    dist = 26-alpha2num(s) # 文字sからaまでの距離
    if s == 'a':
        t += s
    elif dist <= k:
        t += 'a'
        k -= dist
    else:
        t += s
# 最後kが余ってたら，最後の文字を回す
print(t[:-1] + alpha[(alpha2num(t[-1])+k) % 26])


# ------------------ Sample Input -------------------
zzzzzzzzz
100

xyz
4

a
25

codefestival
100


# ----------------- Length of time ------------------
# 27分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/other/code-festival-2016-quala/editorial.pdf
# 解答の方針は一瞬で決まった: 左からどんどん貪欲に見るのは常套手段らしい
# 「先頭の要素から順に見ていき，今見ている要素をできるだけ小さくする，ということを貪欲に行う」
# aを見たらスキップという処理を忘れてWAした

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#辞書順
#貪欲
#greedy