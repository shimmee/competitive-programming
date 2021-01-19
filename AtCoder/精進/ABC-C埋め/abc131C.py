# ABC131C - Anti-Division
# URL: https://atcoder.jp/contests/abc131/tasks/abc131_c
# 日付: 2020/11/20

# ---------- 思ったこと / 気づいたこと ----------
# cとdで割れる = ((cで割れる)+(dで割れる)-(c*dの最小公倍数で割れる))

# ------------------- 方針 --------------------
# B以下で上の数を求めて，そこからA未満の上の数を引く

# ------------------- 解答 --------------------
#code:python

from math import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)

a,b,c,d=map(int, input().split())
a -= 1

A = (a//c + a//d - a//lcm(c, d))
B = (b//c + b//d - b//lcm(c, d))
print((b - a) - (B - A))


# ------------------ 入力例 -------------------
4 9 2 3
4 10 2 3
10 40 6 8
314159265358979323 846264338327950288 419716939 937510582


# ----------------- 解答時間 ------------------
# 30分くらい？

# -------------- 解説 / 感想 / 反省 -------------
# c*dではなく最大公約数で引く必要があることに気づくのに時間がかかった
# スニペットに入れました
# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#最大公約数 #lcm
