# Indeedなう（予選A）C - 説明会
# URL: https://atcoder.jp/contests/indeednow-quala/tasks/indeednow_2015_quala_3
# Date: 2021/04/18

# ---------- Ideas ----------
# 場合分け?

# ------------------- Answer --------------------
#code:python
n = int(input())
s = sorted([int(input()) for _ in range(n)])

q = int(input())
K = [int(input()) for _ in range(q)]
if all([i == 0 for i in s]):
    print(*[0 for _ in range(q)], sep='\n')
    exit()

for i in range(q):
    k = K[i]
    if k == 0: # 誰も収容できないので，最大得点+1点を出力
        print(s[-1] + 1)
    # 受験者数より収容人数の方が多い場合，全員通過してOKなので0点
    elif n <= k:
        print(0)
    # 上位k番目の人の点数が0点のとき，ボーダーを0点にしておけばk人以下になる
    elif s[n - k] == 0:
        print(0)
    # 上位k番目の人と，k-1番目の人が同じ点数なら，その点数をボーダーラインにすると人数オーバーになるので，1点増やす
    elif s[n - k] == s[n - k - 1]:
        print(s[n - k] + 1)
    elif s[n - k] != s[n - k - 1]: # 前の人とは点数が違う時
        if s[n-k] == 1: # 入力例1の最後の会場に対応
            print(0)
        else:
            print(s[n-k])

# WAが取れません
# 諦めます。。解説見ます
# まず0点の学生を除く。ソートする。k番目の点数+1を出力する

n = int(input())
S = []
for _ in range(n):
    s = int(input())
    if s != 0:
        S.append(s)
S.sort(reverse=True)

q = int(input())
if not S:
    print(*[0 for _ in range(q)], sep='\n')
    exit()
for _ in range(q):
    k = int(input())
    if k == 0: # 誰も収容できないので，最大得点+1点を出力
        print(S[0] + 1)
    elif len(S) <= k:
        print(0)
    else:
        print(S[k]+1)

# ------------------ Sample Input -------------------
3
0
0
0
2
1
2


6
1
2
3
3
3
4
2
2
3


4
0
0
0
0
1
0

9
3
3
3
2
2
2
1
1
1
1
4

15
0
0
0
1
1
2
3
4
5
6
6
6
8
9
10
3
0
4
12


# ----------------- Length of time ------------------
# 40分かけてWAで解説AC

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/indeednow-quala
# むずすぎた
# あんまり理解してない。
# もう二度と出さないでほしい

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#場合分け
#クエリ処理問題