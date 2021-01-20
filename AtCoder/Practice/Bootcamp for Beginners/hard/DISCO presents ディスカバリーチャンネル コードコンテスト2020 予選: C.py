# DISCO presents ディスカバリーチャンネル コードコンテスト2020 予選: C - Strawberry Cakes
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_c
# Date: 2021/01/18

# ---------- Ideas ----------
# h,w,k<=300なのでO(hwk)で解くんだろう
# 基本1行で切ればOK?
# [...#...#..#] みたいなのは [...#...|#..|#]こう切る: 次の#が出てくるまで切る
# 上から勧めていって，次の行にいちごがなかったらこまる: 前の行と同じものをいれる
# 最初の行にいちごがなかったら困る: 最初に出てくるいちごの行とスイッチする

# ------------------- Solution --------------------
# いちごの存在する行のリストをまず作る
# 最初の行にいちごがなければ，初めていちごが出てくる行と入れ替える
# いちご存在行リストも更新する: 0を加えて，最初の番号を消す
# いちご番号をnow=1として初期化，ansとしてh*w配列を用意
# ループで行，列を回す:
# 行にいちごがなかったら，一つ上の行と同じものにする
# 行で最初にでてきたいちごは無視して，nowをansに代入
# 行で1番目ではないいちごがあれば，nowをインクリメントしてansに代入
# いちごじゃないときはnowを代入
# 行の終わり(x==w-1)のときには，nowをインクリメント

# ------------------- Answer --------------------
#code:python
h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

ichigo_h = []
for y in range(h):
    if '#' in s[y]:
        ichigo_h.append(y)

# 最初の行にいちごがなかったら，最初に出てくるいちごの行と同じにする
# ヒントもろた: https://c-taquna.hatenablog.com/entry/2019/11/24/232937
if not 0 in ichigo_h:
    s[0], s[ichigo_h[0]] = s[ichigo_h[0]], s[0]
    ichigo_h.pop(0)
    ichigo_h = [0]+ichigo_h
ichigo_h = set(ichigo_h)

ans = [[-1 for _ in range(w)] for _ in range(h)]
now = 1
for y in range(h):
    first_ichigo = True
    if not y in ichigo_h: # もし行にいちごがなければ，前の行をそのまま追加
        ans[y] = ans[y-1]
    else:
        for x in range(w):
            if s[y][x] == '#':
                if first_ichigo:
                    ans[y][x] = now
                    first_ichigo = False
                else:
                    now += 1
                    ans[y][x] = now
            else:
                ans[y][x] = now

            if x == w-1: # 次の行は新しい番号から始める
                now += 1
for y in ans:
    print(*y) # この書き方凄い!!!!!
# ------------------ Sample Input -------------------
3 10 2
..........
..........
..#..#....

3 5 14
#####
##.##
#####


2 2 4
##
##

3 3 5
#.#
.#.
#.#

3 7 7
#...#.#
..#...#
.#..#..

6 7 7
.......
#...#.#
.......
..#...#
.#..#..
.......
# ----------------- Length of time ------------------
# 54分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/ddcc2020-qual/editorial.pdf
# 最初の行にいちごがない場合の処理の方法として，とりあえず上から埋めて，
# もし埋まってない行があれば，上と同じ切り方にする，という方法をとってみたら，4ケースWAになったので，
# ここ(https://c-taquna.hatenablog.com/entry/2019/11/24/232937)からヒントをもらって
# 最初にいちごが出てくる行と0行目をスイッチすることにした
# 最後の出力の仕方が勉強になった

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#ヒントAC
#wanna_review #hard復習 #復習したい
#ケーキの切り分け
#複数行の出力
#複数行出力

