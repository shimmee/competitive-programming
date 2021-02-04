# ABC182E - Akari
# URL: https://atcoder.jp/contests/abc182/tasks/abc182_e
# Date: 2021/02/02

# ---------- Ideas ---------- 
# まずfieldを作る
# 4方向から進める
# ライトがあったら，flag=Trueにして，光ってることにする
# ブロックがあればflag=Falseにする
# 光ってれば，配列lampの該当箇所を1にする


# ------------------- Answer --------------------
#code:python
h, w, n, m = map(int, input().split())

# グリッドの配列を作る: ランプあるならL，壁なら#，なにもないなら. (最大1500*1500)
field = [['.' for _ in range(w)] for _ in range(h)]
for _ in range(n):
    a, b = map(int, input().split())
    field[a-1][b-1] = 'L' # ランプがあったらL
for _ in range(m):
    c, d = map(int, input().split())
    field[c-1][d-1] = '#' # ブロックがあれば#

# 4方向で見ていく
r = [[0 for _ in range(w)] for _ in range(h)]
l = [[0 for _ in range(w)] for _ in range(h)]
u = [[0 for _ in range(w)] for _ in range(h)]
d = [[0 for _ in range(w)] for _ in range(h)]

# 右から左に進む
for y in range(h):
    for x in range(w):
        if field[y][x] == '#':
            continue
        elif field[y][x] == 'L' or r[y][x-1] == 1:
            r[y][x] = 1

# 左から右に進む
for y in range(h):
    for x in reversed(range(w)):
        if field[y][x] == '#':
            continue
        elif field[y][x] == 'L' or (x+1 < w and l[y][x+1] == 1):
            l[y][x] = 1

# 上から下に進む
for x in range(w):
    for y in range(h):
        if field[y][x] == '#':
            continue
        elif field[y][x] == 'L' or u[y-1][x] == 1:
            u[y][x] = 1

# 上から下に進む
for x in range(w):
    for y in reversed(range(h)):
        if field[y][x] == '#':
            continue
        elif field[y][x] == 'L' or (y+1 < h and d[y+1][x] == 1):
            d[y][x] = 1

# 4つのテーブルいずれかが1であればOK
ans = 0
for y in range(h):
    for x in range(w):
        if r[y][x] == 1 or l[y][x] == 1 or u[y][x] == 1 or d[y][x] == 1:
            ans += 1
print(ans)


# ------------------ Sample Input -------------------
3 3 2 1
1 1
2 3
2 2


4 4 3 3
1 2
1 3
3 4
2 3
2 4
3 2


# ----------------- Length of time ------------------
# 想定解法は書けたけど，謎の挙動でTLEになった。
# かつっぱさんの解法で解説AC

# -------------- Editorial / my impression -------------
# 解説: https://atcoder.jp/contests/abc182/editorial
# 想定解法なのにTLEだしまくって辛かった
# ランプの定石は4方向から攻めるという方法だが，ツメが甘かった？

# ----------------- Category ------------------
#AtCoder  
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#ランプ問題
#ライト問題
#グリッド
#




# 一生TLEになったコード。ACしたコードよりこっちの方が断然キレイ
# 二重ループの中でif文を3つ使ってるが，2つだったら何故かTLEにならなくなる。
# わけがわからないが，もう放置する。
#
# h, w, n, m = map(int, input().split())
#
# # グリッドの配列を作る: ランプあるならL，壁なら#，なにもないなら. (最大1500*1500)
# field = [['.' for _ in range(w)] for _ in range(h)]
# for _ in range(n):
#     a, b = map(int, input().split())
#     field[a-1][b-1] = 'L' # ランプがあったらL
# for _ in range(m):
#     c, d = map(int, input().split())
#     field[c-1][d-1] = '#' # ブロックがあれば#
#
# # ランプが光るor届けば1を入れる配列: fieldと同じ大きさ
# lamp = [[0 for _ in range(w)] for _ in range(h)]
#
# # 右から左に進む
# for y in range(h):
#     flag = False
#     for x in range(w):
#         if field[y][x] == 'L':
#             flag = True
#         elif field[y][x] == '#':
#             flag = False
#         if flag:
#             lamp[y][x] = 1
#
# # 左から右に進む
# for y in range(h):
#     flag = False
#     for x in reversed(range(w)):
#         if field[y][x] == 'L':
#             flag = True
#         elif field[y][x] == '#':
#             flag = False
#         if flag:
#             lamp[y][x] = 1
#
# # 上から下に進む
# for x in range(w):
#     flag = False
#     for y in range(h):
#         if field[y][x] == 'L':
#             flag = True
#         elif field[y][x] == '#':
#             flag = False
#         if flag:
#             lamp[y][x] = 1
#
# # 下から上に進む
# for x in range(w):
#     flag = False
#     for y in reversed(range(h)):
#         if field[y][x] == 'L':
#             flag = True
#         elif field[y][x] == '#':
#             flag = False
#         if flag:
#             lamp[y][x] = 1
#
# print(sum([sum(i) for i in lamp]))




# フィールドを回転させる方法で書いてみてる
# TLEになった
#
# h, w, n, m = map(int, input().split())
# field = [['.' for _ in range(w)] for _ in range(h)]
# for _ in range(n):
#     a, b = map(int, input().split())
#     field[a-1][b-1] = 'L'
# for _ in range(m):
#     c, d = map(int, input().split())
#     field[c-1][d-1] = '#'
#
# # 回転する関数
# def rotate_clockwise2(matrix):
#     return list(map(list, zip(*matrix)))[::-1]
#
# def fun(field, lamp):
#     H = len(field)
#     W = len(field[0])
#     for y in range(H):
#         flag = False
#         for x in range(W):
#             if field[y][x] == 'L':
#                 flag = True
#             elif field[y][x] == '#':
#                 flag = False
#             if flag:
#                 lamp[y][x] = 1
#     return field, lamp
#
# lamp = [[0 for _ in range(w)] for _ in range(h)]
# # 1回目
# field, lamp = fun(field, lamp)
#
# # 2回目
# lamp = rotate_clockwise2(lamp)
# field = rotate_clockwise2(field)
# field, lamp = fun(field, lamp)
#
# # 3回目
# lamp = rotate_clockwise2(lamp)
# field = rotate_clockwise2(field)
# field, lamp = fun(field, lamp)
#
# # 4回目
# lamp = rotate_clockwise2(lamp)
# field = rotate_clockwise2(field)
# field, lamp = fun(field, lamp)
# print(sum([sum(i) for i in lamp]))
