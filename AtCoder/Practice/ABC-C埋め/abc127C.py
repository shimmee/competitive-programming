# ABC127C- Prison
# URL: https://atcoder.jp/contests/abc127/tasks/abc127_c
# 日付: 2020/11/26

# ---------- 思ったこと / 気づいたこと ----------
# いもす法使えそう

# ------------------- 方針 --------------------
# 各区間の情報でいもす法する
# これで得た数は，「各ゲートを通せるカードの枚数」
# これがゲートの数と一致する個数を出力する

# 区間[l, r]にaを追加したいとき，配列imosを用意して
# ステップ1: imos[l] += a
# ステップ2: imos[r+1] -= a
# ステップ3: imosの累積和を取る (ここまでimos法)
# ステップ4: 累積和のmaxを取る

# ------------------- 解答 --------------------
#code:python
from itertools import accumulate
n,m = map(int, input().split())
lr = [[int(i) for i in input().split()] for _ in range(m)]

imos = [0]*(n+2)
for l, r in lr:
    imos[l] += 1
    imos[r+1] -= 1
cum = list(accumulate(imos))
ans = 0
for i in cum:
    if i == m:
        ans += 1
print(ans)

# ------------------ 入力例 -------------------
4 2
1 3
2 4

10 3
3 6
5 7
6 9

100000 1
1 100000


# ----------------- 解答時間 ------------------
# 11分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc127/editorial.pdf
# 解説が変な方法で解いてる

# ----------------- カテゴリ ------------------
#AtCoder #abc
#いもす法
#imos #累積和
