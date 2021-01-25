# ARC081D - Coloring Dominoes
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/arc081/tasks/arc081_b
# Date: 2021/01/24

# ---------- Ideas ----------
# 左からどんどん塗っていく
# 前回のパターンと今回のパターンで場合分け

# ------------------- Solution --------------------
# if文で場合分けしまくる
# ans=1としてどんどんかけていく

# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n = int(input())
s1 = input()
s2 = input()

ans = 1
if s1[0] == s2[0]: # 最初のドミノを縦置き
    pre_tate = True
    ans *= 3
    i = 1
else: # 最初のドミノを横置き
    pre_tate = False
    ans *= 6
    i = 2

while i < n:
    if s1[i] == s2[i]: # 次のドミノを縦置き
        if pre_tate: # 一つ前が縦置き
            ans *= 2
        else: # 一つ前が横置き
            ans *= 1
        pre_tate = True
        i += 1
    else: # 次のドミノを横置き
        if pre_tate: # 一つ前が縦置き
            ans *= 2
        else: # 一つ前が横置き
            ans *= 3
        pre_tate = False
        i += 2

print(ans % mod)
# ------------------ Sample Input -------------------
3
aab
ccb

1
Z
Z

52
RvvttdWIyyPPQFFZZssffEEkkaSSDKqcibbeYrhAljCCGGJppHHn
RLLwwdWIxxNNQUUXXVVMMooBBaggDKqcimmeYrhAljOOTTJuuzzn


# ----------------- Length of time ------------------
# 15分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/arc081/editorial.pdf
# 他の人も全く同じ解き方してる: https://www.google.com/search?q=atcoder+Coloring+Dominoes&oq=atcoder+Coloring+Dominoes&aqs=chrome..69i57j69i64j69i60.3162j1j7&sourceid=chrome&ie=UTF-8

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#場合の数
#隣り合うドミノの塗り方
#条件分岐
