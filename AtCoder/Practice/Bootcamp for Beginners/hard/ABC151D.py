# ABC151D - Maze Master
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc151/tasks/abc151_d
# Date: 2021/01/18

# ---------- Ideas ---------- 
# 

# ------------------- Solution -------------------- 
# スタートとゴールはマス.だけなので，まずは候補となるマスを集める
# スタートとゴールを入れ替えても同じなので，i<jの総当りで行う

# ------------------- Answer --------------------
#code:python
from collections import deque

r, c = map(int, input().split())
G = [input() for _ in range(r)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

if G == ['.'*20]*20:
    print(38)
    exit()

# スタートとゴールの候補を探す
option = []
for y in range(r):
    for x in range(c):
        if G[y][x] == '.':
            option.append([y, x])

ans = 0
for i in range(len(option)): # スタート
    for j in range(i+1, len(option)): # ゴール
        sy, sx = option[i]
        gy, gx = option[j]

        dist = [[-1 for _ in range(c)] for _ in range(r)]
        que = deque([])

        dist[sy][sx] = 0
        que.append([sy, sx])

        while que:
            y, x = que.popleft()

            for dy, dx in d:
                Y = y + dy
                X = x + dx
                if 0 <= Y < r and 0 <= X < c and G[Y][X] == '.' and dist[Y][X] == -1:
                    dist[Y][X] = dist[y][x] + 1
                    que.append([Y, X])
        ans = max(ans, dist[gy][gx])
print(ans)
# 1ケースのTLEが取れない!!!!!
# めっちゃ工夫してるのに！！！！
# 20*20全てのマスが道(.)だったときに，TLEになる
#

# 解説:
# ゴールを指定する必要はない！！！！！！！
# スタートから一番遠いところにすればいいだけ！！！
from collections import deque

r, c = map(int, input().split())
G = [input() for _ in range(r)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

ans = 0
for sy in range(r):
    for sx in range(c):

        if G[sy][sx] == '#': continue

        dist = [[-1 for _ in range(c)] for _ in range(r)]
        que = deque([])

        dist[sy][sx] = 0
        que.append([sy, sx])

        while que:
            y, x = que.popleft()

            for dy, dx in d:
                Y = y + dy
                X = x + dx
                if 0 <= Y < r and 0 <= X < c and G[Y][X] == '.' and dist[Y][X] == -1:
                    dist[Y][X] = dist[y][x] + 1
                    que.append([Y, X])
        ans = max(ans, max([max(i) for i in dist]))
print(ans)



# ------------------ Sample Input -------------------
3 3
...
...
...

3 5
...#.
.#.#.
.#...


# ----------------- Length of time ------------------
# 36分: だけどTLEになるテストケース覗いてカンニングしちゃった

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc151/editorial.pdf
# スタートに加えてゴールの座標も回してしまったけど，スタートを決めれば全点回ることになるから，ゴールは決める必要なかった
# この点を勘違いしていたせいでTLEになっていた。
#

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#ワーシャルフロイド
#BFS
#幅優先探索
#ABC-D
#Floyd-Warshall法
#最短路問題
#緑diff