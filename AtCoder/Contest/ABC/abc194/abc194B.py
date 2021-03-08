# ABC194B - Job Assignment
# URL: https://atcoder.jp/contests/abc194/tasks/abc194_b
# Date: 2021/03/06

# ---------- Ideas ----------
# 頭がこんがらがる
# 2重ループで間に合う

# ------------------- Answer --------------------
#code:python
n = int(input())
a_min = 10**10
b_min = 10**10
ans = 10**10

for _ in range(n):
    a,b = map(int, input().split())
    ans = min(ans, a+b)
    if a <= b:
        a_min = min(a_min, a)
    else:
        b_min = min(b_min, b)

print(min(ans, max(a_min, b_min)))

# これでWAだしてもうた
# 2重ループで解いてみる

n = int(input())
ab = [[int(i) for i in input().split()] for _ in range(n)]

ans = 10**20
for i in range(n):
    for j in range(n):
        ai, bi = ab[i]
        aj, bj = ab[j]
        if i == j:
            ans = min(ans, ai + bi)
        else:
            ans = min([ans, max(ai, bj), max(aj, bi)])
print(ans)


# ------------------ Sample Input -------------------
1
2 1

3
8 5
4 4
7 9

# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
