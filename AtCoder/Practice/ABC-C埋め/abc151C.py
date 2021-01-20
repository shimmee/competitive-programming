# ABC151-C: We:come to AtCoder
# URL: https://atcoder.jp/contests/abc151/tasks/abc151_c
# 日付: 2020/11/20

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# piごとにWA=0，AC=1として，累積和とって，bisectで最初の1を見つける
# なぜかこれが間に合ったから，普通の二重ループも間に合いそう


# ------------------- 解答 --------------------
#code:python
import itertools
import bisect
n, m = map(int, input().split())
S = [[] for _ in range(n)]
for i in range(m):
    p, s = input().split()
    p= int(p)-1
    if s == 'WA': s=0
    else: s=1
    S[p].append(s)

ac = 0
wa = 0
for i in range(n):
    cum = list(itertools.accumulate(S[i]))
    index = bisect.bisect_left(cum, 1)
    if index == len(S[i]):
        wa += len(S[i])
    else:
        wa += index
        ac += 1
print(ac, wa)


# 単純にリストのsumが1を超えてればACしてることになる。
# 2重ループで書いてみよう
n, m = map(int, input().split())
S = [[] for _ in range(n)]
for i in range(m):
    p, s = input().split()
    p= int(p)-1
    if s == 'WA': s=0
    else: s=1
    S[p].append(s)


ac = 0
wa = 0
for i in range(n):
    s = S[i]
    if sum(s) > 0:
        ac += 1
        for j in s:
            if j == 0:
                wa += 1
            else: break
    else:
        wa += len(s)
print(ac, wa)

# 同じWAの出し方してる。TLEかと思ったら間に合ってるし。たぶん問題読み間違えてる
# 1重ループでpごとにACのフラグ立てればいいやん

n, m = map(int, input().split())
wa = [0]*n
ac = [False]*n
for i in range(m):
    p, s = input().split()
    p  = int(p) - 1
    if s == 'AC':
        ac[p] = True
    elif s == 'WA' and not ac[p]:
        wa[p] += 1
print(sum(ac), sum(wa))

# こんなきれいなコードなのにWA!!???!
# WAの出し方が全くおなじ。今までのコードも，他人のWA出してる人も，みんな同じケースでWA出してる


# なぜかこのコードが通ってる！！！https://atcoder.jp/contests/abc151/submissions/12967237
# 90%くらい同じ書き方なのに！！！！
n, m = map(int, input().split())
ac = [0] * n
wa = [0] * n
for _ in range(m):
    p, s = input().split()
    p = int(p) - 1
    if ac[p] == 0 and s == 'WA':
        wa[p] += 1
    elif s == 'AC':
        ac[p] = 1
n_ac = 0
n_wa = 0
for i in range(n):
    n_ac += ac[i]
    if ac[i] == 1:
        n_wa += wa[i]
print(n_ac, n_wa)

# 最後のWAの数え方が問題っぽい
# WAを数えるのは1回以上ACした問題だけ！！！！！！！ WAしか出してない問題のWAは答えなくていい

n, m = map(int, input().split())
ac = [False]*n
wa = [0]*n
for i in range(m):
    p, s = input().split()
    p  = int(p) - 1
    if s == 'AC':
        ac[p] = True
    elif s == 'WA' and not ac[p]:
        wa[p] += 1

n_wa = 0
for i in range(n):
    if ac[i]:
        n_wa += wa[i]
print(sum(ac), n_wa)



# ------------------ 入力例 -------------------
2 5
1 WA
1 AC
2 WA
2 AC
2 WA

100000 3
7777 AC
7777 AC
7777 AC

6 0


# ----------------- 解答時間 ------------------
# 1h以上かかった？

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc151/editorial.pdf
# 問題を読み間違えていた
# WAしか出してない問題のWAは数えなくていい。ACを出してる問題のうち，ACするまでのWAだけ数える
# 読み間違えが多くて反省してる。
# WAが多いときはやっぱり解法がおかしいor読み間違いなんだなぁ

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#flagを上手く使う
