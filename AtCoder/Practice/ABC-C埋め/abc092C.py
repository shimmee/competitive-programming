# ABC093C - Traveling Plan
# URL: https://atcoder.jp/contests/arc093/tasks/arc093_a
# 日付: 2020/12/06

# ---------- 思ったこと / 気づいたこと ----------
# 累積和はいらない

# ------------------- 方針 --------------------
# 座標のリスト頭とケツに0を加える
# dist = 各座標a[i]とa[i+1]の距離
# dist2 = 各座標a[i]とa[i+2]の距離: 一つ飛ばしの距離
# distとdist2から訪れない地点iを飛ばして計算する

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

a = [0] + a + [0]
dist = []
for i in range(len(a)-1):
    dist.append(abs(a[i]-a[i+1]))

dist2 = []
for i in range(len(a)-2):
    dist2.append(abs(a[i]-a[i+2]))

total = sum(dist)
for i in range(n):
    print(total - dist[i] - dist[i+1] + dist2[i])

# ------------------ 入力例 -------------------
3
3 5 -1

5
1 1 1 2 0

6
-679 -2409 -3258 3095 -3291 -4462

# ----------------- 解答時間 ------------------
# 19分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc093/editorial.pdf
# 最初累積和かと思ったけどただの距離求めるだけだった
# 添字がバグりそうな問題だけど頑張った

# ----------------- カテゴリ ------------------
#AtCoder #abc

