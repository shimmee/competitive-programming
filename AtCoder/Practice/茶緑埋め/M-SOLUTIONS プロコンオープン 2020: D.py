# M-SOLUTIONS プロコンオープン 2020: D - Road to Millionaire
# URL: https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d
# Date: 2021/02/18

# ---------- Ideas ----------
# 貪欲に極小値で買って極大値で売る

# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))

stock = 0
money = 1000
flag = True # 買いのフラッグ
for i in range(n):
    if i == 0: # 1日目は，次の日に高くなるなら買う
        if flag and A[i] < A[i+1]: # 極小値で買う
            stock, money = divmod(money, A[i]) # 所持金でありったけの株を買う
            flag = False
    elif 0 < i < n-1: #
        if flag and A[i-1] >= A[i] and A[i] < A[i+1]: # 極小値で買う
            stock, money = divmod(money, A[i])  # 所持金でありったけの株を買う
            flag = False
        elif not flag and A[i-1] <= A[i] and A[i] > A[i+1]: # 極大値で売る
            money += A[i]*stock
            stock = 0
            flag = True
    elif i == n-1:
        if stock > 0 and A[i-1] <= A[i]: # 最後に株が余ってたら売る
            money += A[i] * stock
print(money)

# 2ケースWA: 同じ価格が続く広義単調増加の数列において，売る行為を連続で行ってしまっていたので，買いのフラッグを立てた
# めちゃ簡単に解いてるひといる: https://cocoinit23.com/m-solutions2020/
# 極小，極大関係なく，次の日が高かったら今日買って，次の日売る，それだけ

n = int(input())
A = list(map(int, input().split()))

money = 1000
for i in range(n-1):
    if A[i] < A[i + 1]:
        stock, money = divmod(money, A[i]) # 今日買って
        money += stock*A[i + 1] # 次の日売る
print(money)


# ------------------ Sample Input -------------------
8
200 200 300 300 400 400 500 500


6
100 200 300 400 500 500

7
100 200 300 200 300 200 200

7
100 130 130 130 115 115 150


# ----------------- Length of time ------------------
# 37分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/m-solutions2020/editorial.pdf
# 2ケースWAで時間かかった
# 同じ価格が続く広義単調増加の数列において，売る行為を連続で行ってしまっていたので，買いのフラッグを立てたらAC
# 実際は極小で買って極大で売らなくても，今日より明日が高ければ買って売る，という単純な貪欲で良かった
# 非効率な貪欲で解いてしまった。非効率貪欲である。

# ----------------- Category ------------------
#AtCoder
#極値
#極大値
#極小値
#非効率貪欲
#貪欲
#greedy
#復讐したい