# ARC040C - Z塗り
# URL: https://atcoder.jp/contests/arc040/tasks/arc040_c
# Date: 2021/03/15

# ---------- Ideas ----------
# 操作回数は最高でも100回: (1, 1)から(100, 1)までやる
# ある2行に渡ってZで塗りきれることがある場合のみ，1回省略できる
# 当然だけどoだけの列は飛ばしていい
# r行目にzがあった場合は，r+1行はそのまま塗れるので，次探索するのはr+2行目から
# きれいなZは当然塗れる
# ...oooo
# oo.....

# 綺麗じゃなくても条件を満たせば1回で塗れる:
# ....oooo
# oooooo..

# Zを描いてみて，それが連続2行に渡って一致してたらOK


# ------------------- Answer --------------------
#code:python
from itertools import groupby
n = int(input())
S = [input() for _ in range(n)]

z_cnt = 0
y = 0
ans = n
while y < n:
    s1 = S[y]

    if s1 == 'o'*n:
        ans -= 1
        y += 1
        continue
    elif y == n-1:
        break
    s2 = S[y+1]
    gr1 = list(groupby(s1))
    gr2 = list(groupby(s2))

    # その行は
    # ....oo と ooo...oo と ooo.... だけOKで， ..ooo.. とか o..o..とかはダメ
    if not(len(gr1) == 2 or (len(gr1) == 3 and gr1[0][0] == 'o')):
        y += 1
        continue

    # 次の行も同じ
    if not(len(gr1) == 2 or (len(gr1) == 3 and gr1[0][0] == 'o')):
        y += 2
        continue

    # もし 今の行と次の行が，....oo と ooo...oo と ooo....  だったら
    for x in range(n):
        if (s1[x] == '.' and (x == n-1 or s1[x+1] == 'o')):
            break
    else:
        y += 1
        continue

    # 今の行はxまでoが続いてるから，次の行のxより前に.があったり，xの真下に.がなかったりしたらダメ
    flag = True
    for i in range(n):
        if i < x and s2[i] == '.': flag = False
        elif i == x and s2[i] != '.': flag = False

    if flag:
        ans -= 1
        y += 2

print(ans)

# WAです。Zの探し方がアホみたいです。
# Zを描いてそれと一致するかどうかを見れば良さそう

n = int(input())
S = [input() for _ in range(n)]

y = 0
ans = n
while y < n:
    s1 = S[y]

    if s1 == 'o'*n:
        ans -= 1
        y += 1
        continue
    elif y == n-1:
        break
    s2 = S[y+1]

    flag = False
    for x in range(n):
        if s1[x+1:] == 'o'*(n-x-1) and s2[:x] == 'o' * x:
            flag = True
            break
    if flag:
        ans -= 1
        y += 2
    else:
        y += 1

print(ans)

# 11時16分，半分WA
# この解法だと，「Zで2行一気に濡れなかった場合」の処理で，1行目と2行目を適当にをZに塗ればいいものを，1行目しか塗ってないことになってた
# 解説見た: 各行の塗ってないマスの一番右に注目して，ここを堺にZを描いて，貪欲にシミュレーションする

n = int(input())
S = []
for _ in range(n):
    S.append([s for s in input()])

ans = 0
for y in range(n):
    for x in reversed(range(n)):
        if S[y][x] == '.':
            ans += 1

            # 塗り直す
            S[y][:x+1] = ['o']*(x+1)
            if y < n-1:
                S[y+1][x:] = ['o']*(n-x)
print(ans)




# ------------------ Sample Input -------------------
6
oooooo
....oo
......
.o..o.
...o..
.o....

5
o.o.o
ooo.o
.oo.o
oooo.
.....


4
.oo.
..oo
o..o
oo..

5
ooo..
oooo

3
ooo
ooo
ooo

7
...oooo
oo.....
ooooooo
ooooooo
.....oo
oooo...
ooooooo


# ----------------- Length of time ------------------
# 2時間かかって解説AC

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc040
# Zで1回で塗れる場所が見つからなかったら，その行だけ塗ったことにしてた。
# 何かしらZで塗れば次の行も塗れるのに，それをせずに探索を進めていたので，嘘解法だった。
# 実際に塗って行かなきゃ探索が正しく行われないことに気づかなかった: ここが一番の反省点
# Zに塗れる場所の探し方自体のアイデアは綺麗に思い浮かんでいたが，このアイデア自体が必要ではなかった。


# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#シミュレーション
#貪欲
#greedy
#grid
#塗り絵