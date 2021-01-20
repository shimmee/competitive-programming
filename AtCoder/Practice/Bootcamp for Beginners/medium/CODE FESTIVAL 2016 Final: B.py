# CODE FESTIVAL 2016 Final: B - Exactly N points
# Bootcamp For Beginners - Medium
# URL:  https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b
# Date: 2021/01/08

# ---------- Ideas ----------
# O(N)でとく
# n以下の異なる数字を用いて和をnにする

# 含めるべき点数の最大値はN=1,2,3,4,5,6,...に対して，1,2,2,3,3,3,4,4,4,4みたいな感じ
# まずはこのリストを内包表記で作る
# 例えばN=8のとき，必要な最大値は4になる。4より小さい数字を貪欲にどんどん足していって，Nを作る


# ------------------- Answer --------------------
#code:python
n = int(input())
l = []
for i in range(5000):
    l += [i for _ in range(i)]
i_max = l[n-1]

flag = [False]*(i_max+1)
cnt = 0
for i in reversed(range(1, i_max+1)):
    if n < cnt + i: break
    cnt += i
    flag[i] = True

if cnt != n:
    print(n-cnt)
for i in range(len(flag)):
    if flag[i]: print(i)

# https://img.atcoder.jp/data/other/cf16-final/editorial.pdf
# 1+2+...+kが初めてnを超えるようなkを探す (線形探索)
n = int(input())
cnt = 0
for i_max in range(1, n+1):
    cnt += i_max
    if cnt >= n:
        break

cnt = 0
for i in reversed(range(1, i_max+1)):
    if n < cnt + i: break
    cnt += i
    print(i)
if cnt != n:
    print(n-cnt)


# ------------------ Sample Input -------------------
11

4

7

1

# ----------------- Length of time ------------------
# 30分くらい

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/other/cf16-final/editorial.pdf
# 最終的には解説と同じような解き方だけど，遠回りしてしまった
# 1からNまで各数字の最大値を求めてしまったが，線形探索で求められた。

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#線形探索