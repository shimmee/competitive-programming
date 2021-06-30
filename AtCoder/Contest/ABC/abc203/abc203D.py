# ABC203
# URL:
# Date: 2021/05/30

# ---------- Ideas ----------
# 事前計算が必要?
# 中央値がpになるようなマスのとり方はありますか？
# マスの要素がp以上の個数がちょうど k**2/2 + 1 個ありますか?
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(n)]

# 右がOKの二分探索
ok = 10**9+1 # 絶対okの範囲
ng = -1 # 絶対にngの範囲
while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    B = [[0]*(n+1) for _ in range(n+1)]
    for y in range(n):
        for x in range(n):
            if A[y][x] > mid:
                B[y+1][x+1] = 1
            else:
                B[y+1][x+1] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            B[i][j] = B[i][j] + B[i][j - 1] + B[i - 1][j] - B[i - 1][j - 1]

    flag = False
    l = set()
    for y1 in range(1, n-k+2): # 区画の左上座標
        for x1 in range(1, n-k+2):
            y2 = y1 + k - 1
            x2 = x1 + k - 1

            cum = B[y2][x2] - B[y1-1][x2] - B[y2][x1-1] + B[y1-1][x1-1]
            if cum <  k**2//2 + 1:
                flag = True

    if flag: # 条件
        ok = mid
    else:
        ng = mid
print(ok)



# ------------------ Sample Input -------------------
3 2
1 7 0
5 8 11
10 4 2

3 2
3 3 3
3 3 3
3 3 3

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい

