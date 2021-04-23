# AGC024B - Backfront
# URL: https://atcoder.jp/contests/agc024/tasks/agc024_b
# Date: 2021/04/21

# ---------- Ideas ----------
# 最大の操作回数でも要素の数まで
# 右から左に進んで，順調に連続で数を数えられた回数をnから引いたらいいのでは？
# P = (1,3,2,4)なら，4,3までは順調だけど，その次の2が3の左側にないので，4-2=2

# ------------------- Answer --------------------
#code:python
n = int(input())
P = [int(input()) for _ in range(n)]

find_l = 1 # 左から
for i in range(n):
    if P[i] == find_l:
        find_l += 1
find_r = n # 右から
for i in reversed(range(n)):
    if P[i] == find_r:
        find_r -= 1

print(min(n-find_l+1, find_r))

# 15WA なので嘘解法かも
# でも結構自信がある解法なのに
# 解法見た: 1ずつ増加して昇順に並んでいる最長部分列を探す: https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2018/0520_agc024
# たしかに，1やnから始める必要はなくて，途中の数字からでも連続してればいいやん

n = int(input())
P = [int(input()) for _ in range(n)]
l = [0] * (n+1)
for i in range(n):
    l[P[i]] = l[P[i]-1] + 1
print(n - max(l))

# ------------------ Sample Input -------------------

8
6
3
1
2
7
4
8
5


# ----------------- Length of time ------------------
# 30分で解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc024/editorial.pdf
# この人の説明がわかりやすかった: https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2018/0520_agc024
# 1やnから始まってる部分列じゃないとダメだと思いこんでたけど，それが良くなかった

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#スワップ
#最長部分列
#DP
#動的最適化
#操作:最小回数
#操作:swap