# ABC084C - Special Trains
# URL: https://atcoder.jp/contests/abc084/tasks/abc084_c
# 日付: 2020/11/28



# ------------------- 解答 --------------------
#code:python
n = int(input())
csf = [map(int, input().split()) for _ in range(n-1)]
c,s,f = [list(i) for i in zip(*csf)]

for train in range(n-1): # 電車の出発駅の位置 (0 ~ n-1)
    time = 1 # 時間
    while True:
        if train == n-1:
            break
        if s[train] <= time and time % f[train] == 0: # 出発できる条件
            time += c[train]
            train += 1 # 次の駅に行く
        else:
            time += 1
    print(time)
print(0)

# おそらくあってるけどTLE!!
# 1解のループで回す必要がある。

n = int(input())
csf = [map(int, input().split()) for _ in range(n-1)]
c,s,f = [list(i) for i in zip(*csf)]

time = 1 # 現在の時間
train = 0 # 電車の位置
duration = [0]*n # 各駅における到着時間
while True:
    if train == n-1:
        break
    if s[train] <= time and time % f[train] == 0: # 出発できる条件
        time += c[train] # 電車でかかる時間
        duration[train] = time
        train += 1 # 次の駅に行く
    else:
        time += 1
for i in duration:
    print(i)


# 解説: https://img.atcoder.jp/abc084/editorial.pdf
# 以下の3パターン
# t < Sj ならば開通式開始 Sj 秒後
# そうでなく、t ％ Fj = 0 ならば開通式開始 t 秒後
# そうでないなら、開通式開始 t + Fj − (t ％ Fj ) 秒後

# 誰かの解答: https://atcoder.jp/contests/abc084/submissions/1923040
n = int(input())
cur = [0] * n
for i in range(n - 1):
    c, s, f = map(int, input().split())
    for j in range(i + 1):
        cur[j] = max(s, (cur[j] + f - 1) // f * f) + c
print(*cur, sep='\n')

# よくわからんけどACしとこう
n = int(input())
time = [0] * n
for i in range(n - 1):
    c, s, f = map(int, input().split())
    for j in range(i + 1):
        time[j] = max(s, (time[j] + f - 1) // f * f) + c
for i in time:
    print(i)
# ------------------ 入力例 -------------------
3
6 5 1
1 10 1

4
12 24 6
52 16 4
99 2 2

4
12 13 1
44 17 17
66 4096 64


# ----------------- 解答時間 ------------------
# 1時間かかってよくわからんかった。

# -------------- 解説 / 感想 / 反省 -------------
# わからん。読解力が不足している

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解けなかった
#解説わからん
