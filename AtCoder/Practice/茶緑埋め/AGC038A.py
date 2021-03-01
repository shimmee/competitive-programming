# AGC038A - 01 Matrix
# URL: https://atcoder.jp/contests/agc038/tasks/agc038_a
# Date: 2021/02/28

# ---------- Ideas ----------
# ダメな時1: H//2 < B or W//2 < A
# ダメな時2: AとBの値が異なる (どちらかが0はOK)
# aとbが同じ時，またはどちらかが0のときだけOK?


# ------------------- Answer --------------------
#code:python
h,w,a,b = map(int, input().split())
if h//2 < b or w//2 < a:
    print(-1); exit()

if b == 0:
    for _ in range(h):
        print('1'*a + '0'*(w-a))
elif a == 0:
    for _ in range(b):
        print('1'*w)
    for _ in range(h-b):
        print('0' * w)
elif a == b:
    s = '1'*a + '0'*(w-a)
    for _ in range(h):
        print(s)
        s = s[-1] + s
        s = s[:w]
else:
    print(-1)

# 14ケース中4ケースWA
# カンニングしてみたところ，AとBの値が異なっていても行けそう。
# 解説みた。
# 「どの行/列においても少ない方の数字は同じ」と勝手に思い込んでいたが，そんなことはない
# h,w,a,b = (4,3,1,2)は無理だと思っていたが以下で行ける
# 011
# 011
# 100
# 100

h,w,a,b = map(int, input().split())
if h//2 < b or w//2 < a:
    print(-1); exit()
else:
    for _ in range(b):
        print('0' * a + '1' * (w - a))
    for _ in range(h-b):
        print('1' * a + '0' * (w - a))


# ------------------ Sample Input -------------------
1000 1000 333 0

3 3 1 1

1 5 2 0

5 1 0 2

7 7 3 3

# ----------------- Length of time ------------------
# 30分で解説AC

# -------------- Editorial / my impression -------------
# H//2 < B or W//2 < Aという最初につけた条件，必要なかった。制約でこれはないものだった。
# こんなの天才しか思いつかないやん。復習する気もなくなる。
# ツイッターみたけど皆思いつかなかったって言ってる。

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#構築問題
#行列の構築
#気付き系
#AGC-A
#緑diff
#構築
#グリッド
#0と1の問題
#入力が定数個