# ABC129C-Typical Stairs
# URL: https://atcoder.jp/contests/abc129/tasks/abc129_c
# 日付: 2020/11/24

# ------------------- 方針 --------------------
# DPで解く

# ------------------- 解答 --------------------
code:python
    mod = 10**9+7
    n,m=map(int, input().split())
    a=[]
    for i in range(m):
        a.append(int(input()))
    a = set(a)
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(n):
        if i+1 in a:
            continue
        else:
            if i >= 1:
                dp[i+1] = (dp[i] + dp[i-1]) % mod
            else:
                dp[i+1] = dp[i] % mod
    print(dp[n] % mod)

# ------------------ 入力例 -------------------
6 1
3


10 2
4
5

100 5
1
23
45
67
89


# ----------------- 解答時間 ------------------
# 16分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc129/editorial.pdf
# 添字で手間取った
# 簡単なDPは書ける

# ----------------- カテゴリ ------------------
#AtCoder #abc
#動的計画法 #簡単なDP
