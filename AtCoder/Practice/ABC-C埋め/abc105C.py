# ABC105C - Base -2 Number
# URL: https://atcoder.jp/contests/abc105/tasks/abc105_c
# 日付: 2020/12/04

# ---------- 思ったこと / 気づいたこと ----------
# そもそも2進数を10進数にするにはどういう手順なんだろうと思って調べた
# https://www.infraexpert.com/study/ip1.html
# nを2で割って行って，余りの0,1,1,0みたいなのが2進数になる。
# じゃあ-2で割っていけばいいやん

# ------------------- 方針 --------------------
# nを-2で割り続けて，0になるまで割る
# 余りを溜め込んでいく。
# 余りを文字列にして，reverseして出力

# ------------------- 解答 --------------------
#code:python
n = int(input())
import math

if n == 0:
    print(0)
    exit()
l = []
while n != 0:
    quotient = math.ceil(n / -2)
    remainder = n - quotient*(-2)
    l.append(remainder)
    n = quotient

ans = ''
for i in l:
    ans += str(i)
print(ans[::-1])



# ------------------ 入力例 -------------------
-9

0


123456789

# ----------------- 解答時間 ------------------
# 実質1時間くらいAC
# 自力だよ！

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc105/editorial.pdf
# 最初，二分探索とか規則探したり試行錯誤したけど，すごく単純だった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#O(logN)
#進数
#-2進数