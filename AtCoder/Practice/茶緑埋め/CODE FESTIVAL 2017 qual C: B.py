# CODE FESTIVAL 2017 qual C: B - Similar Arrays
# URL: https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_b
# Date: 2021/02/06

# ---------- Ideas ----------
# 各aに対して，3種類のbがとれる: 10なら9,10,11
# 全通りは3**n
# 1つでも偶数があれば積が偶数になるので，余事象を考える
# 全て奇数のものを全通りから除けばいい
# aが奇数のとき，3通りのうち2つ偶数，1つ奇数，
# aが偶数の時，3通りのうち1つ偶数，2つ奇数
# 奇数になる組み合わせは掛け算


# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))

odd = 1
for a in A:
    if a % 2 == 0:
        odd *= 2
print(3**n - odd)

# ------------------ Sample Input -------------------
2
2 3


# ----------------- Length of time ------------------
# 5分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/code-festival-2017-qualc/editorial

# ----------------- Category ------------------
#AtCoder
#偶奇に注目
#パリティ
#場合の数
