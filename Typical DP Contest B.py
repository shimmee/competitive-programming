# Typical DP Contest B - ゲーム
# URL: https://atcoder.jp/contests/tdpc/tasks/tdpc_game
# Date: 2021/05/15

# ---------- Ideas ----------
# 2人が順番に最善手を選んで，それぞれスコアを最大にしたいゲーム
# 2人の得点の差をdp値として，最終局面から遡っていくミニマックス法
# dp[i][j]: Aの山にi個，Bの山がj個残っている時の先手-後手の点差の最適値
# 先手はdp値を最大化したくて，後手は最小化したい
# 貰うDPを書く

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
a = list(map(int, input().split()))[::-1]
b = list(map(int, input().split()))[::-1]

dp = [[-1]*(m+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(m+1):
        if i == j == 0: continue

        if (n + m) % 2 == 1: # 最後の手番が後手
            if (i+j) % 2 == 1: # 先手の手番でdp値を最大化したい
                if i == 0: # Aの山がないのでBから取るしかない
                    dp[i][j] = dp[i][j-1] + b[j-1]
                elif j == 0: # Bの山がないのでAから取る
                    dp[i][j] = dp[i-1][j] + a[i-1]
                else: # どっちからでも取れる時
                    dp[i][j] = max(dp[i-1][j] + a[i-1], # Aから取る
                                   dp[i][j-1] + b[j-1]) # Bから取る
            else:
                if i == 0: # Aの山がないのでBから取るしかない
                    dp[i][j] = dp[i][j-1] - b[j-1]
                elif j == 0: # Bの山がないのでAから取る
                    dp[i][j] = dp[i-1][j] - a[i-1]
                else: # どっちからでも取れる時
                    dp[i][j] = min(dp[i-1][j] - a[i-1], # Aから取る
                                   dp[i][j-1] - b[j-1]) # Bから取る
        else: # 最後の手番が先手
            if (i+j) % 2 == 0: # 先手の手番でdp値を最大化したい
                if i == 0: # Aの山がないのでBから取るしかない
                    dp[i][j] = dp[i][j-1] + b[j-1]
                elif j == 0: # Bの山がないのでAから取る
                    dp[i][j] = dp[i-1][j] + a[i-1]
                else: # どっちからでも取れる時
                    dp[i][j] = max(dp[i-1][j] + a[i-1], # Aから取る
                                   dp[i][j-1] + b[j-1]) # Bから取る
            else:
                if i == 0: # Aの山がないのでBから取るしかない
                    dp[i][j] = dp[i][j-1] - b[j-1]
                elif j == 0: # Bの山がないのでAから取る
                    dp[i][j] = dp[i-1][j] - a[i-1]
                else: # どっちからでも取れる時
                    dp[i][j] = min(dp[i-1][j] - a[i-1], # Aから取る
                                   dp[i][j-1] - b[j-1]) # Bから取る

total = sum(a) + sum(b)
print((dp[n][m]+total)//2)

# ------------------ Sample Input -------------------
1 2
1
2 10

# ----------------- Length of time ------------------
# 50分

# -------------- Editorial / my impression -------------
# ABC201Dが解けなくて悔しくて同じような問題探して解きました。
# 2人ゲームではdpテーブルの作り方が一番大事。これさえ定義できれば推移は自然に考えられる。
# dpテーブル: ある状態における先手と後手の点数の差

# ----------------- Category ------------------
#AtCoder
##ミニマックス法
#DP
#動的最適化
#ゲーム
#2人ゲーム
#点差を最適化するゲーム
#Typical-DP