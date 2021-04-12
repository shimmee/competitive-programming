# ARC014C - 魂の還る場所
# URL: https://atcoder.jp/contests/arc014/tasks/arc014_3
# Date: 2021/04/10

# ---------- Ideas ----------
# 順番関係なく基本全部消せる (未証明)
# バラバラに出現してても，どうにかこうにか消せる
# 奇数個出現してる文字が1文字ずつ残るので，文字の出現回数を調べればOK
# 全部できる系の問題

# ------------------- Answer --------------------
#code:python
n = int(input())
S = input()

from collections import deque, Counter
counter = Counter(S)
ans = 0
for key, value in counter.items():
    ans += value % 2
print(ans)

# ------------------ Sample Input -------------------
9
RGBGGBGBR


# ----------------- Length of time ------------------
# 5分

# -------------- Editorial / my impression -------------
# ユーザー解説: https://kort0n.hatenablog.com/entry/2020/01/08/002039
# 制約の N <= 50がいやらしくて，何かしらのアルゴリズムを使うよということを匂わせてるが，全く必要ない
# こういう全部できる系問題は思いついたら勝ち

# ----------------- Category ------------------
#AtCoder
#偶奇に注目
#全部消せる
#対消滅
#全部できる