# ABC203
# URL:
# Date: 2021/05/30

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(n)]
ab = sorted(ab, key=lambda x: x[0])
a = [ab[i][0] for i in range(n)]
b = [ab[i][1] for i in range(n)]

money = k
pre = 0
for i in range(n):
    cost = a[i]
    gain = b[i]
    if money >= cost - pre:
        money -= (cost - pre)
        money += gain
        pre = cost
    else:
        print(pre + money)
        exit()
print(pre + money)



# ------------------ Sample Input -------------------
2 3
2 1
5 10


5 1000000000
1 1000000000
2 1000000000
3 1000000000
4 1000000000
5 1000000000

3 2
5 5
2 1
2 2

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい

