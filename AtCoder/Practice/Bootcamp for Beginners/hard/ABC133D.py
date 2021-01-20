# ABC133D - Rain Flows into Dams
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc133/tasks/abc133_d
# Date: 2021/01/16

# ---------- Ideas ----------
# 時計問題は超不得意?
# 数学だ！
# 連立方程式を建てる: x1が求まると，芋づる式に求まる
# a1-a2+a3-a4+a5-...=x1となる
# x1を求めたら，a1=(x1+x2)/2 よりx2が求まり，続けてa2=(x2+x3)/2よりx3が求まっていく

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

x1 = 0
for i in range(n):
    if i % 2 == 0:
        x1 += a[i]
    else:
        x1 -= a[i]

ans = [x1]
for i in range(n-1):
    x = 2*a[i]-ans[-1]
    ans.append(x)
for i in ans:
    print(i, end = ' ')



# ------------------ Sample Input -------------------
3
2 2 4

5
3 8 7 5 5

3
1000000000 1000000000 0

# ----------------- Length of time ------------------
# 16分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc133/editorial.pdf
# 紙で色々書いてよかった
# 考察うまかったおかげで，コードは一瞬でかけた

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#方程式
#緑diff
#ABC-D
#芋づる式
#連立方程式