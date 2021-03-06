# ABC035C - オセロ
# URL: https://atcoder.jp/contests/abc035/tasks/abc035_c
# 日付: 2020/12/22

# ---------- 思ったこと / 気づいたこと ----------
# 各オセロの駒がトータルで何回ひっくり返るのかはimos法で得られる
# imosの結果，ひっくり返す数が偶数だったら黒(0)で，奇数なら白(1)になる

# ------------------- 方針 --------------------
# 区間[l, r]にaを追加したいとき，配列imosを用意して
# ステップ1: imos[l] += a
# ステップ2: imos[r+1] -= a
# ステップ3: imosの累積和を取る (ここまでimos法)
# ステップ4: 累積和のmaxを取る

# ------------------- 解答 --------------------
#code:python
n, q = map(int, input().split())
imos = [0]*(n+10)
for _ in range(q):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r+1] -= 1

from itertools import accumulate
cum = list(accumulate(imos))

ans = []
for i in range(1, n+1):
    ans.append(str(cum[i] % 2))
print(''.join(ans))

# ------------------ 入力例 -------------------
5 4
1 4
2 5
3 3
1 5

20 8
1 8
4 13
8 8
3 18
5 20
19 20
2 7
4 9

# ----------------- 解答時間 ------------------
# 13分: 6分くらいで解けてたけど文字列操作みすってTLEになってた

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc035
# 最後のans='01010100100'みたいな文字列を作る時に，ans=''としてインクリメントしていくとO(N^2)かかってTLEになった
# ここはリストにしてappendでO(1)，ループのトータルでO(N)で計算して，最後にリストを文字列にする必要があった
# 長さ20万くらいの文字列を作る時はこの点に注意!!

# ----------------- カテゴリ ------------------
#AtCoder #abc
#いもす法
#imos
