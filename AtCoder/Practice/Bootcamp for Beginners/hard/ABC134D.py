# ABC134D - Preparing Boxes
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc134/tasks/abc134_d
# Date: 2021/01/16

# ---------- Ideas ----------
# サンプルが少なすぎる: たった2つ
# リストaの半分以降の数字は，bの要素は自動で決まる: aと同じになる
# そのあとどんどん後ろから求めていく
# 入れるボールは，0or1
# いいボールの入れ方が存在しないケースが想像できない!!! 必ずできるのではないか？


# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

b = [-1]*n
for i in reversed(range(1, n+1)):
    if i-1 >= n//2:
        b[i-1] = a[i-1]
    else:
        t = [b[j-1] for j in range(2*i, n, i)]
        if (sum(t) % 2 == 0 and a[i-1] == 0) or (sum(t) % 2 == 1 and a[i-1] == 1):
            b[i-1] = 0
        else:
            b[i-1] = 1

m = sum(b)
print(m)
if m > 0:
    for i in range(n):
        if b[i]:
            print(i+1, end = ' ')

# 6/18がWA
# -1を出力するケースは多分ない。意地悪問題。だから解法が間違ってる。
# 554中断


n = int(input())
a = list(map(int, input().split()))
a = [0]+a # 1-indexedにするため，0をついか

b = [-1]*(n+1) # ボールの数を表すリスト
for i in reversed(range(1, n+1)):
    if i >= n//2 + 1: # 半分+1以降の数字は自動で決まる: n=6なら，4,5,6が自動でa[i]になる
        b[i] = a[i]
    else:
        # i番目の倍数の箱に入ってるボールのリスト: ただしi番目は含まない
        t = [b[j] for j in range(2*i, n+1, i)]

        # リストtの合計が偶数でかつa[i]が0なら，ボールを入れる必要はなく，またsum(t)が奇数でa[i]=1なら同様に入れる必要はない
        if (sum(t) % 2 == 0 and a[i] == 0) or (sum(t) % 2 == 1 and a[i] == 1):
            b[i] = 0
        else:
            b[i] = 1

b = b[1:] # 0-indexedに戻す
m = sum(b) # ボールを入れる個数
print(m)
if m > 0:
    for i in range(n):
        if b[i]:
            print(i+1, end = ' ')


# ------------------ Sample Input -------------------
12
1 0 0 1 0 0 1 1 1 0 0 1

3
1 0 0

5
0 0 0 0 0

# ----------------- Length of time ------------------
# 58分
# 添字バグらせで時間かかった

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc134/editorial.pdf
# サンプルが少ないので，添字が多少バグってもサンプルが通ってしまう
# 0-indexedにするか，1-indexedにするかが結構大事
# 最終的には1-indexedにした

# 添字バグらせだけで1時間もかかったので，復習するべき

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#wanna_review #hard復習 #復習したい
#ABC-D
#端から順に決まって行くGreedy
#後ろから解く
#貪欲?
