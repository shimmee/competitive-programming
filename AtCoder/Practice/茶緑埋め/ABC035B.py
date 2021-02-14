# ABC035B - ドローン
# URL: https://atcoder.jp/contests/abc035/tasks/abc035_b
# Date: 2021/02/12

# ---------- Ideas ----------
# ポインタを持って足したり引いたりするやつ
# ？はあとで考えて，とりあえずLRUDで進むとする

# ------------------- Solution --------------------
# Sを走査して，?の数をカウントし，かつLで-1,Rで+1するカウンタ，Uで+1, Dで-1するカウンタを用意
# ？を無視すれば，RLとUDの2つのカウンタで表される座標にいると考えられる
# 最大値であれば，?の個数分だけ更に進める
# 最小値であれば原点に近づきたいので，できるだけ近づく。もし行き過ぎる場合，偶数なら原点行けて，奇数なら1歩余るので最終的な距離は1

# ------------------- Answer --------------------
#code:python
S = input()
T = int(input())

cnt_lr, cnt_ud, cnt_free = 0, 0, 0
for s in S:
    if s == '?':
        cnt_free += 1
    elif s == 'L':
        cnt_lr -= 1
    elif s == 'R':
        cnt_lr += 1
    elif s == 'U':
        cnt_ud += 1
    elif s == 'D':
        cnt_ud -= 1

dist = abs(cnt_lr)+abs(cnt_ud)

if T == 1: # 最大値を出力
    print(dist + cnt_free)
else: # 最小値を出力
    rest = dist - cnt_free # ?の分減点に近づく
    if rest >= 0: # 原点にたどり着けなければ，原点からそこまでの距離
        print(rest)
    else: # 原点にたどり着ければ，残りが偶数なら原点行けるし，奇数なら1歩余る
        if rest % 2 == 0:
            print(0)
        else:
            print(1)

# counter使えばもう少し綺麗にかけたかも
S = input()
T = int(input())
from collections import deque, Counter
counter = Counter(S)
cnt_lr = counter['R'] - counter['L']
cnt_ud = counter['U'] - counter['D']
cnt_free = counter['?']
dist = abs(cnt_lr)+abs(cnt_ud)

if T == 1: # 最大値を出力
    print(dist + cnt_free)
else: # 最小値を出力
    rest = dist - cnt_free # ?の分減点に近づく
    if rest >= 0: # 原点にたどり着けなければ，原点からそこまでの距離
        print(rest)
    else: # 原点にたどり着ければ，残りが偶数なら原点行けるし，奇数なら1歩余る
        if rest % 2 == 0:
            print(0)
        else:
            print(1)

# ------------------ Sample Input -------------------
UUUU?DDR?LLLL
1

UD?
1

# ----------------- Length of time ------------------
# 11分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/abc035
# こういう座標の移動系は偶奇が大事になる事が多い
# 結構好きな問題

# ----------------- Category ------------------
#AtCoder
#Counter
#偶奇に注目
#座標の移動
#マンハッタン距離