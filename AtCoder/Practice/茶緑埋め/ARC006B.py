# ARC006B - あみだくじ
# URL: https://atcoder.jp/contests/arc006/tasks/arc006_2
# Date: 2021/02/20

# ---------- Ideas ----------
# 今なんの列にいるのかnowで管理しながら，左右に'-'があれば移動する，という感じで上から下に走査する

# ------------------- Answer --------------------
#code:python
N, L = map(int, input().split())
field = [input() for _ in range(L)]
goal = input()
idx = goal.index('o') // 2

for now in range(N):
    i = now
    for y in range(L):
        if (now*2 + 1 < len(field[0])) and (field[y][now*2 + 1] == '-'):
            now += 1
        elif (now*2 - 1 > 0) and field[y][now*2 - 1] == '-':
            now -= 1
    if now == idx:
        print(i + 1)
        exit()

# ACしたけど
# nowを0-Nではなく，そもそも籤のあるインデックスで管理してみたほうが楽なのではないか
N, L = map(int, input().split())
field = [input() for _ in range(L)]
goal = input().index('o')

for now in range(0, (N-1)*2+1, 2):
    i = now
    for y in range(L):
        if (now + 1 < len(field[0])) and (field[y][now + 1] == '-'):
            now += 2
        elif (now - 1 > 0) and field[y][now - 1] == '-':
            now -= 2
    if now == goal:
        print(i//2+1)
        exit()


# ------------------ Sample Input -------------------
10 2
| |-| |-| |-| |-| |
|-| |-| |-| |-| |-|
            o

3 2
| |-|
|-| |
o

4 2
| | | |
| | | |
      o

9 8
| | | | | | | | |
|-| | |-| | |-| |
| | |-| | |-| | |
| |-| | | | | |-|
| | | |-| | | |-|
| | |-| |-| | | |
|-| | |-| | |-| |
| | | | | |-| | |
            o

# ----------------- Length of time ------------------
# 24分AC

# -------------- Editorial / my impression -------------
# 最後の当たり行がローカル環境だとinput()で上手く読み込めなくて，テストできなくて困った。
# 効率の悪い方法でといてしまった気がする。

# ----------------- Category ------------------
#AtCoder
#あみだくじ
#変な入力
