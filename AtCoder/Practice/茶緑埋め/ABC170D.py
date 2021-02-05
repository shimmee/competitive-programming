# ABC170D - Not Divisible
# URL: https://atcoder.jp/contests/abc170/tasks/abc170_d
# Date: 2021/02/03

# ---------- Ideas ---------- 
# 自分の約数が数列に1つでも入っていたらだめ
# 自分が素数だったとしても，同じ数がほかにあったらだめ

# ------------------- Solution -------------------- 
# 出現回数を数える
# 約数を列挙して，1つでも入っていたらダメ
# 約数列挙だとTLEになった
# エラトステネスの篩っぽく解く
# max(A)までの配列を用意して，Falseで初期化
# 各aを回して，aの倍数に当たる配列の箇所をTrueにする

# ------------------- Answer --------------------
#code:python
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
a = list(map(int, input().split()))

from collections import Counter
counter = Counter(a)

ans = 0
for i in range(n):
    divisor = make_divisors(a[i])
    flag = True
    for d in divisor:
        if d == a[i]:
            if counter[d] > 1:
                flag = False
        else:
            if counter[d] > 0:
                flag = False
    if flag:
        ans += 1
print(ans)

# 10分で 2つTLEまできた
# O(N*√A)じゃ間に合わないということか？

# エラトステネスっぽく解いてみる

n = int(input())
A = sorted(list(map(int, input().split())))
max_a = A[-1]
flag = [False]*(max_a+1) # aの倍数が出現したらTrueにする
counter = [0]*(max_a+1) # 出現回数を数える

for a in A:
    i = 1
    while i*a <= max_a:
        flag[i*a] = True
        counter[i*a] += 1
        i += 1

ans = 0
for a in A:
    if flag[a] and counter[a] == 1: # Aに出現していて，かつ出現回数が1回のものがOK
        ans += 1
print(ans)




# ------------------ Sample Input -------------------
5
24 11 8 3 16


# ----------------- Length of time ------------------
# 35分 エラトステネスというヒントだけもらってAC

# -------------- Editorial / my impression -------------
# 解説: https://img.atcoder.jp/abc170/editorial.pdf
# けんちょn: https://drken1215.hatenablog.com/entry/2020/12/30/081500
# 約数列挙で間に合わないのはO(N√N)で2億回回ってるからだね。
# エラトステネス


# ----------------- Category ------------------
#AtCoder  
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#ABC-D
#緑diff
#調和級数
#制約:数値が10^6以下
#バケット
#整数問題
#エラトステネスの篩