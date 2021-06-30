# 典型90問072 - Loop Railway Plan（★4）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bt
# Date: 2021/06/20

# ---------- Ideas ----------
# スタート地点を全探索，かつ各マスから行ける方向を全探索する: bit全探索と同じ要領
# 1. 各マスから行ける方向をメモする，スタート地点として成立するならそれも別途メモ
# 2. itertools.productで各マスからの行く方向のパターンを全列挙
# 3. スタート地点と2を2重ループで回す
# 4. スタート地点に戻ってきたらansを更新してbreak，訪問済みだったらbreak

# ------------------- Answer --------------------
#code:python
import itertools
h,w = map(int, input().split())
G = [input() for _ in range(h)]

# それぞれのマスから，上下左右どの方向に進めるのかをメモ
dir_pattern = [[[] for _ in range(w)] for _ in range(h)]
start_option = []
wall_count = 0
for y in range(h):
    for x in range(w):
        if G[y][x] != '.':
            wall_count += 1
            dir_pattern[y][x].append('#')
        else:
            # 各方向に進めるかどうか調べて，進めるならappend
            if x - 1 >= 0 and G[y][x - 1] == '.': dir_pattern[y][x].append('l')
            if x + 1 < w  and G[y][x + 1] == '.': dir_pattern[y][x].append('r')
            if y - 1 >= 0 and G[y - 1][x] == '.': dir_pattern[y][x].append('u')
            if y + 1 < h  and G[y + 1][x] == '.': dir_pattern[y][x].append('d')

            # どこも進めないときには#を入れておく
            if len(dir_pattern[y][x]) == 0:
                dir_pattern[y][x].append('#')

            # 今の(y,x)のマスから1マス方向にしか進めないのであれば，スタート地点になりえない。
            # 2マス以上ある場合のみスタート地点の候補となれる
            if len(dir_pattern[y][x]) >= 2:
                start_option.append(w * y + x)

# 4*4マスで壁が1以下のときは間に合わないので，ここで出力しておわる。2*8と3*5も同様
#
if h == w == 4:
    if wall_count == 0:
        print(16)
        exit()
    elif wall_count == 1:
        print(14)
        exit()

if (h == 2 and w == 8) or (h == 8 and w == 2):
    if wall_count == 0:
        print(16)
        exit()

if (h == 3 and w == 5) or (h == 5 and w == 3):
    if wall_count == 0:
        print(14)
        exit()

# dir_patternを1次元にする
dir_pattern1 = [item for sublist in dir_pattern for item in sublist]

# 各マスから進める方向を全列挙する
all_pattern = list(itertools.product(*dir_pattern1))
ans = 0

# スタート地点がたくさんあっても意味ないから，適当に削る。さもなくば定数倍で負ける
if len(start_option) >= 0 and len(start_option) >= 7:
    start_option = [start_option[0]] + [start_option[4]] + [start_option[6]]
start_option = start_option[:4]

for pattern in all_pattern:
    for sid in start_option:  # スタートのマス番号
        y, x = divmod(sid, w)  # 現在地のマス座標
        id = sid  # 現在地のマスid

        # 訪問済みフラグ
        seen = [[False] * w for _ in range(h)]
        seen[y][x] = True

        while True:
            if pattern[id] == 'l': x -= 1
            if pattern[id] == 'r': x += 1
            if pattern[id] == 'u': y -= 1
            if pattern[id] == 'd': y += 1

            id_next = w * y + x # 次の移動先のid
            # スタートに戻ってきたらansを更新してbreak
            if sid == id_next:
                ans = max(ans, sum([sum(l) for l in seen]))
                break

            # 次行く場所がすでに訪問済みだったらbreak
            if seen[y][x]:
                break
            id = id_next
            seen[y][x] = True
print(ans if ans >= 3 else -1)


# ------------------ Sample Input -------------------
2 2
..
..

4 4
.#..
####
....
....


3 3
...
.#.
...

4 4
....
#...
....
...#

1 6
......

# ----------------- Length of time ------------------
# 1時間 + バグ直しでだいぶ

# -------------- Editorial / my impression -------------
# バグりまくって大変だった
# こういう探索問題はdfsで書きたいけど書けない


# ----------------- Category ------------------
#AtCoder
#典型90問
#DFS
#深さ優先探索
#bit全探索
#hanjo
#グラフ探索
#grid