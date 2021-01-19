# キーエンス プログラミング コンテスト 2021 B:
# URL: https://atcoder.jp/contests/keyence2021/tasks/keyence2021_b
# Date: 2021/01/16

# ---------- Ideas ----------
# できるだけバラバラに入れたほうがいい

# ------------------- Solution --------------------
# 管理する変数
# 現在，K個中何個クリアしてるか
# 脱落した子をインクリメント


# ------------------- Answer --------------------
#code:python

n,k = map(int, input().split())
a = sorted(list(map(int, input().split())))

from collections import Counter
counter = Counter(a)

ans = 0
now = k # 現在残ってる個数
for i in range(max(a)+2):
    value = counter[i]
    if now > value:
        ans += (now-value)*i

    now = min(now, value)
print(ans)


# ------------------ Sample Input -------------------
4 2
0 1 0 2

5 2
0 1 1 2 3

20 4
6 2 6 8 4 5 5 8 4 1 7 8 0 3 6 1 1 8 3 0


# ----------------- Length of time ------------------
# 21分

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#キーエンスプログラミングコンテスト2021
#400点問題
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
