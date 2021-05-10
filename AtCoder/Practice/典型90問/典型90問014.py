# 典型90問014 - We Used to Sing a Song Together
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_n
# Date: 2021/05/09

# ---------- Ideas ----------
# ソートして貪欲するだけ


# ------------------- Answer --------------------
#code:python
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

print(sum([abs(a[i]-b[i]) for i in range(n)]))

# ------------------ Sample Input -------------------

6
8 6 9 1 2 0
1 5 7 2 3 9

# ----------------- Length of time ------------------
# 1分

# -------------- Editorial / my impression -------------
# 証明できてないけどこれ以上最適にするのは無理だろうという勘
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/014.jpg

# ----------------- Category ------------------
#AtCoder
#貪欲
#greedy
#ソートして貪欲
#典型90問