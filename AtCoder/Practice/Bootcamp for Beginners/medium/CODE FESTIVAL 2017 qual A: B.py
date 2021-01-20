# CODE FESTIVAL 2017 qual A: B - fLIP
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_b
# Date: 2021/01/08

# ---------- Ideas ----------
# ひっくり返す行数，列数が決まれば黒マスの個数は順番にかかわらず一定になる，
# 行数，列数の総当りで1000*1000の計算量

# ------------------- Solution --------------------
# ひっくり返す行数，列数でそれぞれループを回す
# まず行をひっくり返して

# ------------------- Answer --------------------
#code:python
n, m, k = map(int, input().split())

for r in range(n+1): # n行のうちr行を反転
    for c in range(m+1): # m列のうちc列を反転
        black = m*r # r行を全て黒にする
        black -= c*r # ひっくり返す列のうち黒になってる行を白にする
        black += (n-r)*c # ひっくり返す列のうち，黒にする分を加える

        if black == k:
            print('Yes'); exit(); break
print('No')




# ------------------ Sample Input -------------------
2 2 2

2 2 1

3 5 8

7 9 20


# ----------------- Length of time ------------------
# 20分AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/code-festival-2017-quala/editorial.pdf
# 解説通り！
# こういうのは「何度でも反転できる」と書いてるけど，行，列それぞれ一度ずつひっくりかえせばOK

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#反転
#ひっくり返す