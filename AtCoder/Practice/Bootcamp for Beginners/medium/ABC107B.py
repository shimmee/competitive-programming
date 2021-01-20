# ABC107B - Grid Compression
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc107/tasks/abc107_b
# 日付: 2020/12/29

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 取り除く行と列をまず探して，インデックスを保存
# 空の配列に，キープしておく行だけブチ込む
# 行のキープの配列から，キープする列だけキープする

# ------------------- 解答 --------------------
#code:python
h, w = map(int, input().split())
a = [input() for _ in range(h)]

remove_r = []
for y in range(h):
    flag = True
    for x in range(w):
        if a[y][x] == '#':
            flag = False
    if flag:
        remove_r.append(y)

remove_c = []
for x in range(w):
    flag = True
    for y in range(h):
        if a[y][x] == '#':
            flag = False
    if flag:
        remove_c.append(x)

G = []
for y in range(h):
    if not y in remove_r:
        G.append(a[y])


for y in range(len(G)):
    s = ''
    for x in range(w):
        if not x in remove_c:
            s += G[y][x]
    print(s)


# ACしたけどコード長すぎ
# 解説: https://img.atcoder.jp/arc101/editorial.pdf
# まず，黒いマスが含まれる行および列をマークします．
# その後，マークされた行とマークされた列が交差する位置の ai,j のみを出力すればよいです．

h, w = map(int, input().split())
a = [input() for _ in range(h)]

flag_r = [False]*h
flag_c = [False]*w

for r in range(h):
    for c in range(w):
        if a[r][c] == '#':
            flag_r[r] = True
            flag_c[c] = True


for r in range(h):
    s = ''
    for c in range(w):
        if flag_r[r] and flag_c[c]:
            s += a[r][c]
    if s != '':
        print(s)


# ------------------ 入力例 -------------------
4 4
##.#
....
##.#
.#.#

4 5
.....
.....
..#..
.....

# ----------------- 解答時間 ------------------
# 11分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc101/editorial.pdf
# 最初の処理として取り除く行と列のインデックスを保存したが，そうではなく，キープする行列のインデックスを保存するべきだった
# これは教訓
# この差だけで5分くらい早く解けた気がする

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#medium復習