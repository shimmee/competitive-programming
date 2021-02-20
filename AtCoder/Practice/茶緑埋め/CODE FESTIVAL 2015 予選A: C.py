# CODE FESTIVAL 2015 予選A: C - 8月31日
# URL: https://atcoder.jp/contests/code-festival-2015-quala/tasks/codefestival_2015_qualA_c
# Date: 2021/02/18

# ---------- Ideas ----------
# ソートしてから累積和
# 写して恩恵のない問題から自力で解くべき: A-Bでソート
# 1~i問までは自力，i+1~n問目は写したい: iを走査してTを超えた時点でダメ

# ------------------- Answer --------------------
#code:python
n, T = map(int, input().split())
abc = []
for _ in range(n):
    a, b = map(int, input().split())
    abc.append([a,b,a-b])

if sum([abc[i][1] for i in range(n)]) > T: # 全部写してもTを超えるときは無理
    print(-1); exit()


abc = sorted(abc, key=lambda x: x[2])
a_cum = [0]
b_cum = [0]
for i in range(n):
    a_cum.append(a_cum[i] + abc[i][0])
    b_cum.append(b_cum[i] + abc[i][1])

# aを解く数を線形探索で増やしていき，解けなくなった時点で出力
for i in range(1, n+1):
    time = a_cum[i] + b_cum[n] - b_cum[i]
    if time > T:
        print(n-i+1); exit()
print(0)


# ------------------ Sample Input -------------------
1 1000000000
5 0

1 0
100 99


5 7
1 0
3 0
5 0
2 0
4 0


3 11
5 2
6 4
7 3


# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/codefestival2015quala
# 累積和使わなくても，A-Bのリストで上手いことできたっぽい
# 「かかる時間は，最初Bの総和にしておき，i番目の宿題を終えた時点でA-Bを足して行けばいい」
# こんなの思いつくか？

# ----------------- Category ------------------
#AtCoder
#累積和じゃなかった
#累積和いらない
#ソートして貪欲
#貪欲
#greedy
#差をとってソート
#差でソート