# ABC180E -  Traveling Salesman among Aerial Cities
# URL: https://atcoder.jp/contests/abc180/tasks/abc180_e
# 日付: 2020/12/27

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 全ての街同士の距離を隣接リストとして作成する

# ------------------- 解答 --------------------
#code:python
n = int(input())
xyz = [[int(i) for i in input().split()] for _ in range(n)]

G = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        a,b,c = xyz[i]
        p,q,r = xyz[j]
        cost = abs(p-a) + abs(q-b) + max(0, r-c)

        G[j].append([i, cost])

inf = float('INF')
dp = [[inf]*n for _ in range(2**n)]
dp[1][0] = 0 # S = 00001のとき，距離が0で初期化

for S in range(1 << n): # range(2**n)と同じ書き方。Sは0から2**n -1までの整数
    for v in range(n):
        if (S & (1 << v)) == 0: continue # vは必ずSに含まれてる必要がある

        # Sからvを除いた集合:推移式の{S-{v}}の部分
        sub = S ^ (1 << v)
        for k, w in G[v]: # 頂点kから頂点v，重さはw
            dp[S][v] = min(dp[S][v], dp[sub][k] + w)

# 最後に到着した頂点vから頂点0までの距離を加味して，最小のコストを出力する
ans = inf
for v, w in G[0]:
    ans = min(ans, dp[2**n-1][v] + w)
print(ans)

# ここまで9分!!

# ------------------ 入力例 -------------------
2
0 0 0
1 2 3

3
0 0 0
1 1 1
-1 -1 -1


17
14142 13562 373095
-17320 508075 68877
223606 -79774 9979
-24494 -89742 783178
26457 513110 -64591
-282842 7124 -74619
31622 -77660 -168379
-33166 -24790 -3554
346410 16151 37755
-36055 51275 463989
37416 -573867 73941
-3872 -983346 207417
412310 56256 -17661
-42426 40687 -119285
43588 -989435 -40674
-447213 -59549 -99579
45825 7569 45584

# ----------------- 解答時間 ------------------
# 9分!!

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/abc180/editorial/154
# AOJのtraveling salesman貼り付けたらいけた

# ----------------- カテゴリ ------------------
#AtCoder
#bitDP
#動的計画法
#復習したい