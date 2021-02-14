# ARC112A - B = C
# URL: https://atcoder.jp/contests/arc112/tasks/arc112_a
# Date: 2021/02/13

# ---------- Ideas ----------
# 各ケースに対してO(1)で解ける
# 考察用紙を見れば分かる

# ------------------- Answer --------------------
#code:python
T = int(input())
for _ in range(T):
    l, r = map(int, input().split())
    n = max(0, r-2*l+1)
    print(n*(n+1)//2)

# ------------------ Sample Input -------------------
5
2 6
0 0
1000000 1000000
12345 67890
0 1000000


# ----------------- Length of time ------------------
# 68分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc112/editorial
# とても時間がかかってしまった...
# これでdiff108はさすがにありえないですわ...
# 茶後半くらいのdiffは合っても良いと思う

# ----------------- Category ------------------
#AtCoder
#整数問題
#実験
#式展開