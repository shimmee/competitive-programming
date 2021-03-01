# ARC041B - アメーバ
# URL: https://atcoder.jp/contests/arc041/tasks/arc041_b
# Date: 2021/02/27

# ---------- Ideas ----------
# 周りの4マスのminかな

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
inf = float('INF')
n, m = map(int, input().split())
B = [input() for _ in range(n)]
A = [[str(inf)]*m for _ in range(n)]

Ys = deque([y for y in range(1, n-1)])
Xs = deque([x for x in range(1, m-1)])

Y_que = []
X_que = []
while Ys:
    y = Ys.popleft()
    Y_que.append(y)
    if Ys:
        y = Ys.pop()
        Y_que.append(y)

while Xs:
    x = Xs.popleft()
    X_que.append(x)
    if Xs:
        x = Xs.pop()
        X_que.append(x)

# なんかこんなの書いてたけど1時間考えても無理なので解説AC
# 解説AC
# 最初の解法が惜しかった: 周り4マスのminが自分になる
# 実際は，周り4マスのminが自分になるんだけど，B自体の周りの4マスをminで引いて更新しておく必要がある

inf = float('INF')
n, m = map(int, input().split())
B = [input() for _ in range(n)]
B = [[int(j) for j in B[i]] for i in range(n)]
A = [[0] * m for _ in range(n)]

for y in range(1, n - 1):
    for x in range(1, m - 1):
        min_b = int(min([B[y - 1][x], B[y][x - 1], B[y + 1][x], B[y][x + 1]]))
        A[y][x] = min_b
        B[y - 1][x] -= min_b
        B[y][x - 1] -= min_b
        B[y + 1][x] -= min_b
        B[y][x + 1] -= min_b

for a in A:
    print(''.join([str(i) for i in a]))

# ------------------ Sample Input -------------------
5 5
02310
26551
36962
24733
02130


5 3
010
121
242
323
030

3 4
0230
2323
0230

5 5
00100
03040
20903
05060
00300


# ----------------- Length of time ------------------
# 1.5h考えて解説AC

# -------------- Editorial / my impression -------------
# 難しかった
# 最初，自分の周りのminを取った値が自分の値になるという惜しい解法でWA
# 次に，周りの外枠から順に書けばいいかと思ってdequeなどを持ち出すが，断念

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#アメーバ
#グリッド
#grid






for y in range(n):
    for x in range(m):
        if [y, x] == [0, 0] or [y, x] == [0, m - 1] or [y, x] == [n - 1, 0] or [y, x] == [n - 1, m - 1]:
            continue
        if y == 0: # 一番上の行
            A[y][x] = min([B[y][x - 1], B[y + 1][x], B[y][x + 1]])
        elif y == n-1: # 一番下の行
            A[y][x] = min([B[y - 1][x], B[y][x - 1], B[y][x + 1]])
        elif x == 0: # 一番左の列
            A[y][x] = min([B[y-1][x], B[y+1][x], B[y][x+1]])
        elif x == m-1: # 一番右の列
            A[y][x] = min([B[y-1][x], B[y][x-1], B[y+1][x]])
        else:
            A[y][x] = min([B[y-1][x], B[y][x-1], B[y+1][x], B[y][x+1]])

for a in A:
    print(''.join(a))

