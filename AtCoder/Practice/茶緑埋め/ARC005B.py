# ARC005B - P-CASカードと高橋君
# URL: https://atcoder.jp/contests/arc005/tasks/arc005_2
# Date: 2021/03/04

# ---------- Ideas ----------
# Wによってmove_xとmove_yを定義
# 次に動く場所が範囲外なら，問題文の通りにmoveの方向を変更する

# ------------------- Answer --------------------
#code:python
x, y, W = input().split()
x = int(x) -1
y = int(y) -1
field = [input() for _ in range(9)]

move_x = 1 if 'R' in W else -1 if 'L' in W else 0
move_y = 1 if 'D' in W else -1 if 'U' in W else 0

ans = field[y][x]
for _ in range(3):
    next_x = x + move_x
    next_y = y + move_y

    if W in ['R', 'L', 'U', 'D']:
        if next_x < 0 or 8 < next_x or next_y < 0 or 8 < next_y:
            move_x *= -1
            move_y *= -1
    else:
        if next_x < 0 or 8 < next_x:
            move_x *= -1
        if next_y < 0 or 8 < next_y:
            move_y *= -1

    x = x + move_x
    y = y + move_y
    ans += field[y][x]
print(ans)


# ACしたけど
# もう少しきれいに描けそう
# dx, dyを使う
# if文を削る

x, y, W = input().split()
x = int(x) -1
y = int(y) -1
field = [input() for _ in range(9)]

dx = 1 if 'R' in W else -1 if 'L' in W else 0
dy = 1 if 'D' in W else -1 if 'U' in W else 0

ans = field[y][x]
for _ in range(3):
    if x + dx < 0 or 8 < x + dx: dx *= -1
    if y + dy < 0 or 8 < y + dy: dy *= -1

    x += dx
    y += dy
    ans += field[y][x]
print(ans)




# ------------------ Sample Input -------------------

2 2 LU
729142134
509607882
640003027
215270061
214055727
745319402
777708131
018697986
277156993

# ----------------- Length of time ------------------
# 24分

# -------------- Editorial / my impression -------------
# move_x, move_yをdx, dyと書いたほうがかっこよかった
# 解答はない模様
# この人の解答が綺麗: https://kusano-prog.hatenablog.com/entry/20120701/1341153128

# ----------------- Category ------------------
#AtCoder
#グリッドの移動

