# ABC201 - D - Game in Momotetsu World
# URL: https://atcoder.jp/contests/abc201/tasks/abc201_d
# Date: 2021/05/15

# ---------- Ideas ----------
# h+w が偶数ならアオキで終わる，
# いつドローか？
# ケースが15しかないのでハックできる
# 全部同じのは2ケース
# ドローは全部で3

# ------------------- Answer --------------------
#code:python
h, w = map(int, input().split())
A = [input() for _ in range(h)]

if h == w == 1:
    print('Draw')
    exit()

l = []
for y in range(h):
    l += A[y]

if len(set(l)) == 1:
    if (h + w) % 2 == 0: # 同じ回数動くのでドロー
        print('Draw')
    else: # 高橋が1回多く動く
        if A[0] == 'o':
            print('Takahashi')
        else:
            print('Aoki')
    exit()

# 絶対ドロー
l = [set() for _ in range(h+w-1)]
for y in range(h):
    for x in range(w):
        l[y+x].add(A[y][x])
l = l[1:]

flag= True
for i in range(0, len(l)-1, 2):
    if len(l[i]) == 1 and l[i] == l[i+1]:
        pass
    else:
        flag = False

if flag:
    print('Draw')
    exit()

tk_plus = 0
ao_plus = 0
for y in range(h):
    for x in range(w):
        if (y + x) % 2 == 0:
            if A[y][x] == '+':
                ao_plus += 1
            else:
                ao_plus -= 1
        else:
            if A[y][x] == '+':
                tk_plus += 1
            else:
                tk_plus -= 1

if A[0][0] == '+':
    ao_plus -= 1
else:
    ao_plus += 1

if tk_plus >= ao_plus:
    print('Takahashi')
else:
    print('Aoki')


# ダメでした。
# 解説ACしましょう
# ユーザー解説: https://blog.hamayanhamayan.com/entry/2021/05/15/235741
# dp[y][x] := 駒が(x,y)にあるときの「高橋君の点数-青木君の点数」の最適値
# (x+y)%2==0なら高橋，(x+y)%2==1なら青木の手番
# 高橋はdp値が大きくなるように移動先を決める
# 青木はdp値が小さくなるように移動先を決める


h, w = map(int, input().split())
A = [input() for _ in range(h)]

dp = [[-10**10]*w for _ in range(h)]
dp[h-1][w-1] = 0

for y in reversed(range(h)):
    for x in reversed(range(w)):
        if y == h-1 and x == w-1: continue # 右下は飛ばす
        if (x+y) % 2 == 0: # 高橋の手番: dpの値を最大化したい
            if y == h-1: # 一番下の段のときは右に行くしかない
                if A[y][x+1] == '+':
                    dp[y][x] = dp[y][x+1] + 1
                else:
                    dp[y][x] = dp[y][x+1] - 1
            elif x == w-1: # 一番右の段のときは下に行くしかない
                if A[y+1][x] == '+':
                    dp[y][x] = dp[y+1][x] + 1
                else:
                    dp[y][x] = dp[y+1][x] - 1
            else: # 右にも下にも行ける時
                dp[y][x] = max(dp[y+1][x] + (1 if A[y+1][x] == '+' else -1),
                               dp[y][x+1] + (1 if A[y][x+1] == '+' else -1))

        else: # 青木の手番の時: dp値を小さくしたい
            if y == h-1: # 一番下の段のときは右に行くしかない
                if A[y][x+1] == '+':
                    dp[y][x] = dp[y][x+1] - 1
                else:
                    dp[y][x] = dp[y][x+1] + 1
            elif x == w-1: # 一番右の段のときは下に行くしかない
                if A[y+1][x] == '+':
                    dp[y][x] = dp[y+1][x] - 1
                else:
                    dp[y][x] = dp[y+1][x] + 1
            else: # 右にも下にも行ける時
                dp[y][x] = min(dp[y + 1][x] + (-1 if A[y + 1][x] == '+' else 1),
                               dp[y][x + 1] + (-1 if A[y][x + 1] == '+' else 1))

if dp[0][0] > 0:
    print('Takahashi')
elif dp[0][0] < 0:
    print('Aoki')
else:
    print('Draw')


# ------------------ Sample Input -------------------
3 3
---
+-+
+--

2 4
+++-
-+-+

1 1
-

# ----------------- Length of time ------------------
# 本番解けず。解説AC

# -------------- Editorial / my impression -------------
# この解説のおかげでようやくわかった: https://blog.hamayanhamayan.com/entry/2021/05/15/235741
# スコアが絡むゲームは，2人の点差 (先手-後手)をdp値として，最後から逆算していく
# それぞれの手番で，先手はdp値を大きくするように，後手は小さくするように行動する
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#ミニマックス法
#DP
#動的最適化
#ゲーム
#2人ゲーム
#点差を最適化するゲーム
