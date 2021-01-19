# ABC016C - 友達の友達
# URL: https://atcoder.jp/contests/abc016/tasks/abc016_3
# 日付: 2020/12/17

# ---------- 思ったこと / 気づいたこと ----------
# ただの全探索
# 自分と友達と友達の友達の3重ループを回す

# ------------------- 解答 --------------------
#code:python
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


for i in range(n): # 自分
    friends = G[i] # 自分の友達のリスト
    flag = [False]*n
    for j in friends: # 自分の友だちjさん
        for k in G[j]: # jさんの友達
            if i != k and not k in friends: # 友達の友達が自分でなく，かつ 友達の友達は友達ではない
                flag[k] = True
    print(sum(flag))

# ------------------ 入力例 -------------------
3 2
1 2
2 3

8 12
1 6
1 7
1 8
2 5
2 6
3 5
3 6
4 5
4 8
5 6
5 7
7 8

# ----------------- 解答時間 ------------------
# 10分

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc016
# 簡単。


# ----------------- カテゴリ ------------------
#AtCoder #abc
#グラフ #全探索