# ABC105D - Candy Distribution
# URL: https://atcoder.jp/contests/abc105/tasks/abc105_d
# Date: 2021/04/12

# ---------- Ideas ----------
# brute forceはlの固定，rの固定，lからrのsum，でO(N^3)
# 累積和を使えばlからrのsumがO(1)でできるのでO(N^2)
# ここまで分かったけどこの先わからなかったから解説の2行見た
# Aの累積和をBとすると
# A[l]からA[r]までの和 = B[r]-B[l-1]
# これらがmで割り切れるので
# sum(A[l] -> A[r]) % m = 0  <->  B[r]-B[l-1] % m = 0
# 展開すると B[r] % m = B[l-1] % m
# つまり，累積和の項のうち，mで割ったときの余りが同じになるような組を探せば良くて，それらがlとrになれる


# ------------------- Solution --------------------
# Aの累積和出す: B
# Bの要素をmで割って余りだす: C
# Cの要素の出現回数を数える
# 組み合わせの個数を数える

# ------------------- Answer --------------------
#code:python
from itertools import accumulate
from collections import deque, Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [0] + list(accumulate(a))
c = [i % m for i in b]

counter = Counter(c)
ans = 0
for key, value in counter.items():
    if value >= 2:
        ans += value*(value-1)//2

print(ans)
# ------------------ Sample Input -------------------
3 2
4 1 5

13 17
29 7 5 7 9 51 7 13 8 55 42 9 81

10 400000000
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000


# ----------------- Length of time ------------------
# 30分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc105/editorial.pdf
# 累積和をとって2点を見るのは頻出の考え方らしい
# けんちょん解説: https://drken1215.hatenablog.com/entry/2018/08/13/125300
# けんちょんさん: 「配列連続する区間」は、「累積和をとった配列上の 2 点」と同一視することができるという超頻出視点なん。

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#条件の言い換え
#いもす法的変換
#累積和
#数列
#ABC-D
#水色diff
#数え上げ問題
#O(N^2)個のものを考える問題
#nC2
#区間
#バケット
#Zero-Sum Ranges
#Counter