# ABC075B - Minesweeper
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc075/tasks/abc075_b
# 日付: 2020/12/28


# ------------------- 方針 --------------------
# 愚直にやる
# 周りの8マスを配列で処理

# ------------------- 解答 --------------------
#code:python
h, w = map(int, input().split())
S = [input() for _ in range(h)]
G = [[0]*w for _ in range(h)] # これに保存していく

x_move = [-1, 0, 1, 1, 1, 0, -1, -1]
y_move = [1, 1, 1, 0, -1, -1, -1, 0]

for y in range(h):
    for x in range(w):
        if S[y][x] == '#':
            G[y][x] = '#'
            continue
        for dx, dy in zip(x_move, y_move):  # vに隣接する頂点wを1つずつ巡る
            X = x + dx
            Y = y + dy
            if 0 <= Y < h and 0 <= X < w:
                if S[Y][X] == '#':
                    G[y][x] += 1

for l in G:
    p = ''
    for s in l:
        p += str(s)
    print(p)
# ------------------ 入力例 -------------------
3 5
.....
.#.#.
.....

6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#...

# ----------------- 解答時間 ------------------
# 9分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc075/editorial.pdf
# これが灰色だと？
# 結構面倒やん

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#グリッド
#ABC-B