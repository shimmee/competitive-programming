# ARC007C - 節約生活
# URL: https://atcoder.jp/contests/arc007/submissions/me
# Date: 2021/04/12

# ---------- Ideas ----------
# 入力の長さをnとすると，ずらすパターンもn個ある: n <= 10
# ずらすパターンをまず全部用意
# bit全探索で全部試してテレビが同時に見れる最小個数を更新

# ------------------- Answer --------------------
#code:python
import itertools
S = input()
n = len(S)

# ずらすパターンをまず全部用意
S = [S]
for i in range(n-1):
    S.append(S[-1][-1] + S[-1][:-1])

ans = 10**10
all_pattern = itertools.product([0, 1], repeat=n)
for pattern in all_pattern:
    flag = [False]*n # 各時間が見れるかどうかのflag
    for i in range(n):
        if pattern[i] == 1:
            s = S[i]
            for j in range(n):
                if s[j] == 'o':
                    flag[j] = True

    if all(i for i in flag): # 全部みれる条件
        ans = min(ans, sum(pattern))
print(ans)


# ------------------ Sample Input -------------------
oxxxxoooo

# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# 解説なかった
# 多分これが最善手
# 昔はbit全探索が水diffだったんだ

# ----------------- Category ------------------
#AtCoder
#bit全探索
#水diff