# ARC122B - Insurance
# URL: https://atcoder.jp/contests/arc122/tasks/arc122_b
# Date: 2021/06/12

# ---------- Ideas ----------
# 三分探索貼るだけ

# ------------------- Answer --------------------
#code:python
# 三分探索を行う
n = int(input())
A = list(map(int, input().split()))

def check(x):
    return sum([x + A[i] - min(A[i], 2*x) for i in range(n)]) / n

high = 10**9
low = 0

while high - low > 0.0000001:
    mid_left = (high+low*2)/3
    mid_right = (high*2+low)/3
    if check(mid_left) > check(mid_right):
        low = mid_left
    else:
        high = mid_right

print(check(low))

# ------------------ Sample Input -------------------
3
3 1 4

10
866111664 178537096 844917655 218662351 383133839 231371336 353498483 865935868 472381277 579910117


# ----------------- Length of time ------------------
# 30分

# -------------- Editorial / my impression -------------
# 下に凸の関数になるのか不安だったけど，サンプルが通ったので投げた

# ----------------- Category ------------------
#AtCoder
#ARC-B
#三分探索
#関数の最小化