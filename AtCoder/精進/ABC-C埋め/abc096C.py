# ABC096C - Grid Repainting 2
# URL: https://atcoder.jp/contests/abc096/tasks/abc096_c
# 日付: 2020/11/28

# ------------------- 方針 --------------------
# 全マス探索して，自分自身が黒の時に，左右上下に黒がいればOK
# 左右上下はdで扱う
# 居なかったらダメ

# ------------------- 解答 --------------------
#code:python
h, w = map(int, input().split())
s = [input() for _ in range(h)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

flag = True
for y in range(h):
    for x in range(w):
        if s[y][x] == '#':
            flag2 = False # 自分が'#'のとき，周りの4方向に'#'があるかどうか
            for dx, dy in d:
                Y = y + dy
                X = x + dx
                if 0 <= Y < h and 0 <= X < w: # 枠ないならOK
                    if s[Y][X] == '#':
                        flag2 = True
            if flag2:
                continue
            else:
                flag = False
                break
if flag:
    print('Yes')
else:
    print('No')


# ------------------ 入力例 -------------------
3 3
.#.
###
.#.


5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#

11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##.


# ----------------- 解答時間 ------------------
# 7分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc096/editorial.pdf
# 結構早く解けて嬉しい！

# ----------------- カテゴリ ------------------
#AtCoder #abc
#グリッド
#全探索