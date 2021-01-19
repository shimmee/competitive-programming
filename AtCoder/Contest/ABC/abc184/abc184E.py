# ABC184E - Third Avenue
# URL: https://atcoder.jp/contests/abc184/tasks/abc184_e
# 日付: 2020/11/22

# ---------- 思ったこと / 気づいたこと ----------
# 隣り合うマスdが.なら，distを埋めて，かつqueに入れる
# 隣り合うマスが'#'ならスキップ
# 隣り合うマスがアルファベットならdistを
# abcのdistが埋まってると困る
# 次行く所がabcだったら前とのminを取ればいい


# ------------------- 解答 --------------------
#code:python
from collections import deque
import sys
sys.setrecursionlimit(10**7)
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# アルファベットから数値
fun = lambda c: ord(c) - ord('a')

# 入力
h,w = map(int, input().split())
G = [input() for _ in range(h)]

#スタートとゴールを見つける
for y in range(h):
    for x in range(w):
        if G[y][x] == 'S':
            sx, sy = x, y
        if G[y][x] == 'G':
            gx, gy = x, y

# 同じ文字の座標を見つけてワープリストを作る
abc = [[] for _ in range(26)]
for y in range(h):
    for x in range(w):
        if 0 <= fun(G[y][x]) <= 26:
            abc[fun(G[y][x])].append([y, x])

# スタートからの各座標への距離の二次元リスト
inf = float('INF')
dist = [[inf for _ in range(w)] for _ in range(h)]
que = deque([])

dist[sy][sx] = 0
que.append([sy, sx])

# ワープを見たかどうかのリスト
abc_seen = [False]*26

while que:
    y, x = que.popleft()

    for dy, dx in d: # 上下左右の座標に移動
        Y = y + dy
        X = x + dx
        if 0 <= Y < h and 0 <= X < w:
            # もし訪れてなくて(distがinf)，かつ行ける場所(#でない)だったら，普通にいく
            if G[Y][X] != '#' and dist[Y][X] == inf:
                dist[Y][X] = dist[y][x] + 1
                que.append([Y, X])

    # 今の座標がアルファベットでかつワープしたことないアルファベットだったら
    if 0 <= fun(G[y][x]) <= 26:
        if not abc_seen[fun(G[y][x])]:
            abc_seen[fun(G[y][x])] = True # 見たことにする
            for Y, X in abc[fun(G[y][x])]:
                dist[Y][X] = min(dist[Y][X], dist[y][x] + 1) # すでに訪れてるかもしれないので，minをとる
                que.append([Y, X])

if dist[gy][gx] == inf:
    print(-1)
else:
    print(dist[gy][gx])


# ------------------ 入力例 -------------------
2 5
S.b.b
a.a.G

11 11
S##...#c...
...#d.#.#..
..........#
.#....#...#
#.....bc...
#.##......#
.......c..#
..#........
a..........
d..#...a...
.#........G


11 11
.#.#.e#a...
.b..##..#..
#....#.#..#
.#dd..#..#.
....#...#e.
c#.#a....#.
.....#..#.e
.#....#b.#.
.#...#..#..
......#c#G.
#..S...#...




# ----------------- 解答時間 ------------------
# 2時間くらい

# -------------- 解説 / 感想 / 反省 -------------
# ワープした場所の処理の方法が最後の最後まで思いつかなかった
# けんちょんさんのブログ: https://drken1215.hatenablog.com/entry/2020/11/23/071100
# 「実際に BFS をするときには、ある英小文字のマスに初めて到着したときに、それと同じ英小文字のマス全体に 1 ステップで行き渡らせることにする。」
# というヒントから，ワープで使ったアルファベットリストを作って，現在の座標がアルファベットで，まだワープを使ってないなら，
# 同じ文字の座標に1マスで飛べるようにした

# ----------------- カテゴリ ------------------
#AtCoder #abc
#幅優先探索 #



# ゴミ
# while que:
#     y, x = que.popleft()
#
#     for dy, dx in d: # とりあえず上下左右の座標を得る
#         Y = y + dy
#         X = x + dx
#         if 0 <= Y < h and 0 <= X < w:
#             # もし訪れてなくて(distが-1)，かつ行ける場所(Gか.)だったら，普通にいく
#             if (G[Y][X] == 'G' or G[Y][X] == '.') and dist[Y][X] == -1:
#                 dist[Y][X] = dist[y][x] + 1
#                 que.append([Y, X])
#
#             # 次の座標がアルファベットでかつ訪れてない場所だったら
#             elif 0 <= fun(G[Y][X]) <= 26 and abc_seen[fun(G[Y][X])] == False:
#                 dist[Y][X] = dist[y][x] + 1
#                 abc_seen[fun(G[Y][X])] = True
#                 que.append([Y, X])
#                 for Y_, X_ in abc[fun(G[Y][X])]:
#                     que.append([Y_, X_])
#                     dist[Y_][X_] = dist[y][x] + 2
#
#
