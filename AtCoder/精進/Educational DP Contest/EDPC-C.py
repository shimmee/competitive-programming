# Educational DP Contest: C-Vacation
# URL: https://atcoder.jp/contests/dp/tasks/dp_c
# 日付: 2020/12/25

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# dp[i][j]: i日目に活動jをして，i日目までに得られる幸福度の総和の最大値

# ------------------- 解答 --------------------
#code:python
n = int(input())
abc = [[int(i) for i in input().split()] for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
dp[0] = abc[0]

for i in range(1, n):
    for j in range(3): # 今日の活動j
        choice1, choice2 = set([0,1,2]) - set([j]) # 昨日のj以外の2つの活動
        dp[i][j] = max(dp[i-1][choice1] + abc[i][j],
                       dp[i-1][choice2] + abc[i][j])
print(max(dp[n-1]))
# ------------------ 入力例 -------------------
3
10 40 70
20 50 80
30 60 90

1
100 10 1

7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1

# ----------------- 解答時間 ------------------
# 7分

# -------------- 解説 / 感想 / 反省 -------------
# 昨日と違う活動を選ぶ方法として，setを用いた

# ----------------- カテゴリ ------------------
#EDPC
#動的計画法
#DP