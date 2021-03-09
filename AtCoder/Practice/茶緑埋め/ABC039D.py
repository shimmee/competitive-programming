# ABC039D - 画像処理高橋君
# URL: https://atcoder.jp/contests/abc039/tasks/abc039_d
# Date: 2021/03/08

# ---------- Ideas ----------
# 白い自分の周りに1つでも黒があれば，自分を黒にする
# 対偶を取ると「操作後に自分が黒でないならば (白ならば)，操作前は自分の周りは全部白い」
# originという配列をすべて黒で初期化して，入力のfieldに白があれば，originにおけるそのマスとその周りを白にする
# 復元したoriginとfieldが矛盾しなければOpossible
# 操作後(field)に黒があるなら，自分を含めてその周りのoriginに黒がないとおかしい: ない場合は矛盾するのでimpossible


# ------------------- Answer --------------------
#code:python
DX = [-1, 0, 1, 1, 1, 0, -1, -1]
DY = [1, 1, 1, 0, -1, -1, -1, 0]

h, w = map(int, input().split())
field = []
for _ in range(h):
    l = [s for s in input()]
    field.append(l)

origin = [['#'] * w for _ in range(h)]

# 「操作後に自分が黒でないならば (白ならば)，操作前は自分の周りは全部白い」
for y in range(h):
    for x in range(w):
        if field[y][x] == '.':
            origin[y][x] = '.'
            for dx, dy in zip(DX, DY):
                X = x + dx
                Y = y + dy
                if 0 <= X < w and 0 <= Y < h:
                    origin[Y][X] = '.'

# 操作後(field)に黒があるなら，自分を含めてその周りのoriginに黒がないとおかしい: ない場合は矛盾するのでimpossible
possible = True
for y in range(h):
    for x in range(w):
        flag= False # 自分のoriginの周りに黒があるかどうか
        if field[y][x] == '#':
            if origin[y][x] == '#':
                flag = True
            for dx, dy in zip(DX, DY):
                X = x + dx
                Y = y + dy
                if 0 <= X < w and 0 <= Y < h and origin[Y][X] == '#':
                    flag = True
            if not flag:
                print('impossible')
                exit()
print('possible')
for l in origin:
    print(''.join(l))






# ------------------ Sample Input -------------------
4 4
###.
##.#
..##
..##


4 4
##..
##..
..##
..##

4 4
###.
##.#
..##
..##

# ----------------- Length of time ------------------
# 27分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/abc/039/editorial.pdf
# 対偶を取るのが肝だった
# 実装は結構たいへんだった

# ----------------- Category ------------------
#AtCoder
#グリッド
#grid
#周囲8方向
#対偶を取る