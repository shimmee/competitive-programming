# 典型90問064 - Uplift（★3）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bl
# Date: 2021/06/10

# ---------- Ideas ----------
# 差分は端っこの左右しか変化しないので，その部分だけクエリで変化させる

# ------------------- Answer --------------------
#code:python
n, q = map(int, input().split())
a = list(map(int, input().split()))
gap = [a[i]-a[i+1] for i in range(n-1)]
ans = sum([abs(gap[i]) for i in range(n-1)])

for _ in range(q):
    l ,r, v = map(int, input().split())
    l, r = l-1, r-1

    if l-1 >= 0: # lの1つ左側との差がどうなるか？
        ans += abs(gap[l - 1] - v) - abs(gap[l - 1])
        gap[l-1] -= v

    if r+1 < n: # rの1つ右側との差がどうなるか？
        ans += abs(gap[r] + v) - abs(gap[r])
        gap[r] += v

    print(ans)

# ------------------ Sample Input -------------------
6 1
1 3 2 1 4 2
2 5 1

3 3
1 2 3
2 3 1
1 2 -1
1 3 2

20 10
61 51 92 -100 -89 -65 -89 -64 -74 7 87 -2 51 -39 -50 63 -23 36 74 37
2 2 -45
6 19 82
2 9 36
7 13 71
16 20 90
18 20 -24
14 17 -78
10 11 -55
7 19 -26
20 20 -7
# ----------------- Length of time ------------------
# 30分くらい

# -------------- Editorial / my impression -------------
# クソバグる

# ----------------- Category ------------------
#AtCoder
#典型90問