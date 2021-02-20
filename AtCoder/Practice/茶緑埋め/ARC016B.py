# ARC016B - 音楽ゲーム
# URL: https://atcoder.jp/contests/arc016/tasks/arc016_2
# Date: 2021/02/18

# ---------- Ideas ----------
# 90度回転させてgroupbyする
# key=='x'であれば連続する長さをインクリメント
# key == 'o'であれば+1インクリメント

# ------------------- Answer --------------------
#code:python
from itertools import groupby
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

n = int(input())
a = [input() for _ in range(n)]
a = rotated(a)

ans = 0
for l in a:
    gr = groupby(l)
    for key, group in gr:
        if key == 'x':
            ans += len(list(group))
        elif key == 'o':
            ans += 1
print(ans)

# ACしたけど解説が違う解き方してた！
# 列数と同じ長さの配列を用意して，直前(上)がoだったらTrueにして，カウントしない
n = int(input())
X = [input() for _ in range(n)]
flag = [False]*9
ans = 0
for i in range(n):
    for j in range(9):
        s = X[i][j]
        if s == 'o':
            if not flag[j]:
                ans += 1
            flag[j] = True
        else:
            flag[j] = False
            if s == 'x': ans += 1
print(ans)

# もっと簡単にかける。直前(上)がoかどうかを毎回調べればいい
n = int(input())
S = ['.'*9] + [input() for _ in range(n)]
ans = 0
for y in range(1, n+1):
    for x in range(9):
        if S[y][x] == 'x':
            ans += 1
        elif S[y][x] == 'o' and S[y-1][x] != 'o':
            ans += 1
print(ans)


# ------------------ Sample Input -------------------
6
..o..x.o.
..o..x.o.
..x..o.o.
..o..o.o.
..o..x.o.
..o..x.o.


15
.........
.x.......
.........
...x.....
.........
.......o.
.......o.
.......o.
.........
..x.....o
........o
........o
....x...o
.x......o
........o


# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/atcoder-regular-contest-016
# 解説にある方法2つとも試してみた。
# 結局普通に全探索するのが一番早い

# ----------------- Category ------------------
#AtCoder
#全探索
#ARC-B