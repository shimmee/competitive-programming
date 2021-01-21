# AGC034B - ABC
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc034/tasks/agc034_b
# Date: 2021/01/19

# ---------- Ideas ----------
# ABC -> BCA
# AABC -> ABCA -> BCAA
# ABCABC -> ABCBCA -> BCABCA -> BCBCAA
# AがBCを追い抜ける回数を問われてる
# ACBC -> ダメ: AとBCの間に何か別の物が入ってるとダメ
# X=BCと置き換えて，AがXを追い越せる回数，入れ替えられる回数を数える
# ABCABC = AXAX -> AXXA -> XAXA -> XXAA

# ------------------- Solution --------------------
# BCをXに置き換える
# 空のリストlを用意し，Sで1文字ずつループを回す
# Aが出現したらlに0をappend
# Xが出現したら，今まで出現したAが全員そのXを追い抜けるので，とりあえずlの一番右の要素に+1
# その他の文字が出現したら，これまでのAはそれ以上進めないので，lを集計する
# lを右から累積和取ったものが，Aが乗り越えられる回数になるので，それをansにインクリメントする

# ------------------- Answer --------------------
#code:python
from itertools import accumulate
S = input()
S = S.replace('BC', 'X')
l = []
ans = 0
for i in range(len(S)):
    if S[i] == 'A':
        l.append(0)
    elif S[i] == 'X' and len(l) > 0:
        l[-1] += 1
    else:
        if len(l) > 0:
            ans += sum(accumulate(l[::-1]))
            l = []
ans += sum(accumulate(l[::-1]))
print(ans)
# AC!!!

# 累積和なんて使わなくても，Aが出てきた個数を数えてれば，Xが出現するたびにAの数だけインクリメントすればいい
# https://atcoder.jp/contests/agc034/submissions/19252010

S = input().replace('BC', 'X')

cnt = 0 # Aが出現した回数
ans = 0
for i in range(len(S)):
    if S[i] == 'A':
        cnt += 1
    elif S[i] == 'X':
        ans += cnt
    else:
        cnt = 0 # Aが出現した回数は初期化

print(ans)
# ------------------ Sample Input -------------------
ABCABC

C

ABCACCBABCBCAABCB


# ----------------- Length of time ------------------
# 20分くらい

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc034/editorial.pdf
# 初めて600点問題を解けた!
# 解説「これは転倒数なので、これまでに出てきた ’A’ の個数 などを持ちながら左から文字列を舐めることで線形で計算可能です。」
# 転倒数は、「数列を、隣り合う要素をswapすることで昇順にソートする時、必要なswap回数」という意味を持つ

# 類題: https://atcoder.jp/contests/agc029/tasks/agc029_a


# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#600点問題
#緑diff
#転倒数
#文字列操作
