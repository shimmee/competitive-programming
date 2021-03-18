# ARC112B - -- - B
# URL: https://atcoder.jp/contests/arc112/tasks/arc112_b
# Date: 2021/03/14

# ---------- Ideas ----------
# B>0, B<0, B==0で場合分け
# 更に正の大きい，負の大きい，正の小さい，負の小さい，の4方向の増え方を求める

# ------------------- Answer --------------------
#code:python
B, C = map(int, input().split())

ans = 0
if B > 0:
    ans += max(0, (C-2)//2)
    ans += (C+1)//2
    ans += min(C//2 + (C-1)//2 + 1, 2*B)
elif B < 0:
    ans += (C-1)//2
    ans += (C+2)//2
    ans += min((C+1)//2 + max(0, (C-2)//2), -2*B)
elif B == 0:
    ans += (C-1)//2
    ans += (C+2)//2
print(ans)


# ------------------ Sample Input -------------------
1000000000000000000 1

11 2

0 4

112 20210213

-211 1000000000000000000

# ----------------- Length of time ------------------
# 77分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc112/editorial
# なんでこれがギリギリ緑diffなのかさっぱりわからん
# かなり難しかった

# ----------------- Category ------------------
#AtCoder
#場合分け
#条件分岐
#数え上げ問題