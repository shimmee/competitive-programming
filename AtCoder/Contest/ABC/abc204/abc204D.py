# ABC204D - Cooking
# URL: https://atcoder.jp/contests/abc204/tasks/abc204_d
# Date: 2021/06/06

# ------------------- Solution --------------------
# ググって出てきたのを貼ってACしました
# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
# 部分和問題として考える
# TのトータルをSとしたとき，最終的な答えは「T1からTnまでの和で作れるS/2以上の整数の最小値は？」になる
# なので，Sまでの部分和問題を2次元DPでやる

# ------------------- Answer --------------------
#code:python
import sys
def findMin(a, n):
    su = 0

    # Calculate sum of all elements
    su = sum(a)

    # Create an 2d list to store
    # results of subproblems
    dp = [[0 for i in range(su + 1)]
          for j in range(n + 1)]

    # Initialize first column as true.
    # 0 sum is possible
    # with all elements.
    for i in range(n + 1):
        dp[i][0] = True

    # Initialize top row, except dp[0][0],
    # as false. With 0 elements, no other
    # sum except 0 is possible
    for j in range(1, su + 1):
        dp[0][j] = False

    # Fill the partition table in
    # bottom up manner
    for i in range(1, n + 1):
        for j in range(1, su + 1):

            # If i'th element is excluded
            dp[i][j] = dp[i - 1][j]

            # If i'th element is included
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]

    # Initialize difference
    # of two sums.
    diff = sys.maxsize

    # Find the largest j such that dp[n][j]
    # is true where j loops from sum/2 t0 0
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break

    return diff


n = int(input())
T = list(map(int, input().split()))
m = findMin(T)
s = sum(T)
a = (m+s)//2
b = (s-m)//2
print(max(a,b))

# ------------------ Sample Input -------------------
9
3 14 15 9 26 5 35 89 79


# ----------------- Length of time ------------------
# ググって10分

# -------------- Editorial / my impression -------------
# editorialが賢い

# ----------------- Category ------------------
#AtCoder
#動的最適化
#DP
#部分和問題
#ABC-D