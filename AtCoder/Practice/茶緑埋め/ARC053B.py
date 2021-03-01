# ARC053B - 回文分割
# URL: https://atcoder.jp/contests/arc053/tasks/arc053_b
# Date: 2021/02/23

# ---------- Ideas ----------
# 文字列をカウント，出現回数が全部偶数なら1つのSで行ける
# 回文 = 奇数1つ + 偶数いくつか
# 最終的に作る回文の個数は奇数個の種類数と同じ
# 貪欲に，一番短い奇数と一番長い偶数をマッチングさせて，それをまた奇数として扱う
# 偶数を全て使い切るまでやる:
# これは嘘貪欲!!!
# S = aaaabcのとき'aba'と'aca'で答えは3だが，上の解法だと1になる
# 偶数個のアルファベットはバラバラに使っていい: 奇数の左右に1文字ずつ足していくと考える

# これも嘘解法でした。

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
import heapq
S = input()
counter = Counter(S)
evens = []
odds = []
for key, value in counter.items():
    if value % 2 == 0:
        evens.append(value)
    else:
        odds.append(value)

# 奇数の文字列がなければ，Sがそのまま回文にできる
if not odds:
    print(len(S)); exit()

# 奇数があれば，短い奇数を探してきて，その左右に+2
dist_times = sum(evens)//2 # 偶数個の文字を分配できる回数
heapq.heapify(odds) # oddリストのヒープ化

for _ in range(dist_times):
    odd = heapq.heappop(odds)
    heapq.heappush(odds, odd+2)
print(min(odds))

# 半分WAなので解説見ます
# 偶数個を奇数個に振り分ける考え方をしていたが，奇数個も振り分けたほうがいい。
# S=aabbbbbbbcccccccccccdのとき，[cccdccc, accccca, bbbbbbb]が答えになるべき

from collections import deque, Counter
S = input()
n = len(S)
counter = Counter(S)
evens = []
odds = []
for key, value in counter.items():
    if value % 2 == 0:
        evens.append(value)
    else:
        odds.append(value)

# 奇数の文字列がなければ，Sがそのまま回文にできる
if not odds:
    print(len(S)); exit()

# oddsの長さ分の個数=kだけ，回文を作る。
# 奇数の長さのトータルを，k個の回文に均等に分ける
k = len(odds) # 回文の個数

ans = 2*((n-k)//(2*k)) + 1
print(ans)


# ------------------ Sample Input -------------------
aabbbbbbbcccccccccccd

aaaabc
aabcd
rokovoko

tomtom

vwxyz

succeeded

aabbccdefcc
# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/arc/053/editorial.pdf
# ちょっと難しかった
# 嘘解法にハマってしまった
# heapは使えなかった

# ----------------- Category ------------------
#AtCoder
#回文
#偶奇に注目
#Counter
#復讐したい
#解説AC