# ABC159E - Dividing Chocolate
# URL: https://atcoder.jp/contests/abc159/tasks/abc159_e
# Date: 2021/04/09

# ---------- Ideas ----------
# おせんべいっぽい

# ------------------- Solution --------------------
# 横に切る回数をbit全探索で固定: 切られなかった行同士を足し合わせて，1行と見なす
# 列を左から貪欲に見ていきながら，各行のホワイトの累計がKを超えるまで貪欲に右に進んでいく
# 次に右に進んだときに，どこかの行がKを超えそうなのであれば，その時点で切る
# どこか1つでも行がKに達してれば時点でそこで切る

# ------------------- Answer --------------------
#code:python
from copy import deepcopy
h, w, k = map(int, input().split())
S = []
for _ in range(h):
    s = input()
    S.append([int(i) for i in s])

ans = 10**20
import itertools
all_pattern = itertools.product([0, 1], repeat=h-1) # 横にきるパターンを全列挙
for pattern in all_pattern:
    cut_cnt = sum(pattern) # 横に切る回数

    s = [deepcopy(S)[0]]
    for y in range(h-1): #
        if pattern[y] == 1: # 切る，見ている行をそのままsにappend
            s.append(deepcopy(S[y+1]))
        elif pattern[y] == 0: # 切らないので，上下の行を合体する
            for x in range(w):
                s[-1][x] += S[y+1][x]

    # この時点でsは横に切られてて，切られなかった行同士は上下で合体してる
    m = len(s) # 新しい合体チョコの行数
    cum = [0]*m

    flag = False
    for x in range(w):
        next_add = [s[y][x] for y in range(m)] # 次の列のチョコ
        # 次の列にk個以上のホワイトが含まれてるともうどうしようもないので，break
        if max(next_add) > k:
            flag = True
            break
        next_cnt = [cum[y] + next_add[y] for y in range(m)] # 次のチョコを累積和した状態

        if max(next_cnt) > k: # 次のチョコを足し合わせてkを超えるとダメなので，切っておく
            cut_cnt += 1
            cum = next_add
        else: # 次の列も切らなくていいなら, cumを更新して進む
            cum = next_cnt

    if flag:
        continue

    ans = min(ans, cut_cnt)
print(ans)




# ------------------ Sample Input -------------------

3 5 4
11100
10001
00111

4 10 4
1110010010
1000101110
0011101001
1101000111

# ----------------- Length of time ------------------
# 30分でほぼ解き終わったけど，参照渡ししてデータが壊れて7WA
# カンニングして参照渡しのバグを発見した

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc159/editorial.pdf
# おせんべいを解いたことあったおかげで簡単に思いつくことができた
# こういう頑張って思い実装で全探索する問題はとても好き
# appendでも参照渡しになるから，deepcopyが必要なことを学んだ
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/03/23/002300
# 縦横決めなきゃいけない問題は，どちらかを固定するのが常套手段

# ----------------- Category ------------------
#AtCoder
#参照渡しバグ
#ABC-E
#ある量を固定して考える
#ある量を決めるとGreedy
#Greedy
#貪欲
#bit全探索
#全探索
#グリッド
#0と1の問題
#水色diff