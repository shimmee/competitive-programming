# Tenka1 Programmer Beginner Contest 2019 C - Stones
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_c
# Date: 2021/01/17

# ---------- Ideas ----------
# 超頻出っぽい問題
# [#.]がダメ: ##か..にしたい
# 連続する黒(＃)の次に連続する白(.)を数えて，少ない方を全てひっくり返すのが良い?
# でも黒にしちゃって，次また白が出てきたら，ひっくり返すべき黒が多くなって損かも
# [#####...###........]だったら，最初の...を###にすると
# 後ろから見るべきかも?
# 後ろから見ていって，...が続いて#がでてきたら，連続を数えて，少ない方を選ぶ
# [##.....]なら[.......]


# ------------------- Solution -------------------- 
# 最終的な解法
# アイデア: [....####]の形になればいい。[.....]でも[#####]でもOK
# あるインデックス以前を全て白(.)に，インデックス以降を全て黒(#)にすればいい。
# あるインデックスまでの黒の数，以降の白の数を数える
# 黒と白それぞれの個数を累積和で持っておく

# ------------------- Answer --------------------
#code:python
n = int(input())
S = input()

import itertools
gr = itertools.groupby(S)
l = []
for key, group in gr:
    l.append(len(list(group)))

if key == '#':
    l = l[:-1]

if len(l) == 0 or len(l) == 1:
    print(0)
else:
    ans = 0
    for i in range(len(l)-1, 0, -2):
        if l[i-1] < l[i]:
            ans += l[i-1]
        else:
            ans += l[i]
    print(ans)

# これは嘘解法である！！！！
# [####...|####.....] -> まず[####...|.........]になって，[#######|.........]となる。
# 結局どっちかに塗り切る必要がある?

# 最終的に[.......######]となれば，右の####は塗らなくてもOK。
# [....] or [####] or [....####]の形のみOK

n = int(input())
S = input()

from itertools import groupby, accumulate
gr = groupby(S)
l = []
for key, group in gr:
    l.append(len(list(group)))

if S[-1] == '#': # 右端の#は無視できる
    l = l[:-1]
if S[0] == '.': # 左端の.は無視できる
    l = l[1:]
if len(l) == 0 or len(l) == 1:
    print(0)
else:
    # この時点でlは[#の数，.の数，#の数，.の数,]と並んでる。lの長さは必ず偶数である。
    # [....####]は，あるインデックスまで全て#を.に変えて，そのインデクス以降は全て.を#に変える
    # つまり，インデックスまでの#の個数，インデックス以降の.を数える
    # インデックスが0の時，[######]になって，nのとき[......]になる

    black_cum = [0] + list(accumulate(l[::2]))
    white_cum = [0] + list(accumulate(l[1::2]))

    m = len(l)//2
    ans = n
    for i in range(m+1):
        cnt_black = black_cum[i]
        cnt_white = white_cum[-1] - white_cum[i]
        ans = min(ans, cnt_black+cnt_white)
    print(ans)

# 解説みた: https://babcs2035.hateblo.jp/entry/2019/04/20/224051
# 別にgroupbyしなくても，各インデックスまでの累積和を持っておけばOK

n = int(input())
S = input()

black = [0]*(n+1)
white = [0]*(n+1)

for i in range(n):
    if S[i] == '#':
        black[i+1] += black[i] + 1
        white[i+1] = white[i]
    else:
        white[i + 1] += white[i] + 1
        black[i + 1] = black[i]

ans = n
for i in range(n+1):
    ans = min(ans, black[i] + white[-1] - white[i])
print(ans)


# ------------------ Sample Input -------------------
15
###....######..

68
####....##......#.....###..############......................####..#

22
#.######......###....#

13
.#.#.#.#.##.#

38
...###....#####......#######........#

3
#.#

5
#.##.

9
.........

# ----------------- Length of time ------------------
# 60分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/tenka1-2019/editorial.pdf
# 最終的なあるべき姿を想像せず，「後ろから見る」という貪欲法に走ってしまったのが最悪だった。嘘貪欲だった。
# 嘘貪欲のせいでitertools.groupbyとか使ってしまった
# 最終的にあるべき石のならびは[.....#####]みたいな感じなので，これさえ最初に思いついておけば，
# もう少し早めに累積和に辿り着いたと思う

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#wanna_review #hard復習 #復習したい
#累積和
#緑diff
#並べた石の反転
#隣り合わないようにする
