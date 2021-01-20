# ABC046C - AtCoDeerくんと選挙速報
# URL: https://atcoder.jp/contests/arc062/tasks/arc062_a
# 日付: 2020/12/18

# ---------- 思ったこと / 気づいたこと ----------
# 次の比が前の比より小さかったら，前の比を超えられるように最小限k倍してあげる。これを1からNまでやる

# ------------------- 方針 --------------------
# t[i], a[i]とt[i+1]，a[i+1]を比較して
# t[i] <= k*t[i+1] かつ a[i] <= k*a[i+1]になるような最小のkを探して，t[i+1]をk*t[i+1]で，a[i+1]をk*a[i+1]で更新する

# ------------------- 解答 --------------------
#code:python
from math import ceil
n = int(input())
ta = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n-1):
    t1, a1 = ta[i]
    t2, a2 = ta[i+1]
    if t2 >= t1 and a2 >= a1: continue

    k = max(ceil(t1/t2), ceil(a1/a2))
    ta[i+1][0] = k*t2
    ta[i+1][1] = k*a2

print(ta[n-1][0]+ta[n-1][1])

# 15ケース中4ケースWA (サンプルは3ケースともOK)
# 大きめのコーナーケースを落としてそう
# 解説見た: https://img.atcoder.jp/data/arc/062/editorial.pdf
# 今高橋君に A票、青木君にB票入っていて、次に満たすべき比率が x : y だとすると、
# A ≤ nx ∧ B ≤ ny なるような最小の自然数 n を取れば、次にあり得る最小の得票数は nx, ny であることがわかります。
# このような n は max(⌈A/x⌉, ⌈B/y⌉) で計算できます。
# はじめに A = 1, B = 1 として、これを N 回繰り返すことで O(N) で答えが得られます。

from math import floor
n = int(input())
ta = [[int(i) for i in input().split()] for _ in range(n)]
A = B = 1

for i in range(n):
    t, a = ta[i]
    n = max(ceil(A/t), ceil(B/a))

    A = t*n
    B = a*n

print(A+B)

# 解説通りに解いても自分と同じ4WAやないか！！！！
# ceilがダメっぽい?

# 他の人のほぼ同じの解答: https://atcoder.jp/contests/arc062/submissions/18541989
# 割算からのceilを使う代わりに // を使ってる
n = int(input())
ta = [[int(i) for i in input().split()] for _ in range(n)]
A = B = 1
for t, a in ta:
    n = max((A-1)//t, (B-1)//a) + 1
    A = t*n
    B = a*n

print(A+B)

# 浮動点小数に関する解説
# https://qiita.com/greenteabiscuit/items/d36b74e4492ba028b136
# https://linus-mk.hatenablog.com/entry/2019/05/26/234642
# https://ja.stackoverflow.com/questions/67786/atcoder-regular-contest-062-c%E5%95%8F%E9%A1%8C%E3%81%A7%E4%B8%8D%E6%AD%A3%E8%A7%A3%E3%81%8C%E7%99%BA%E7%94%9F

# 例: 1を18桁含む数は9で割れる: 111111111111111111 = 9 * 12345679012345679
111111111111111111//9 # 12345679012345679でOK
111111111111111111/9 # 1.234567901234568e+16となり，最後の桁がおかしい
int(111111111111111111 / 9) # 12345679012345680 となり，最後の間違い

# これを踏まえて，改めて最初の方法で書いてみる
# 桁数が大きい(16桁以上)の割り算でceilやintをする場合
# math.ceil(a/b) これだと誤差が生じる

n = int(input())
ta = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n-1):
    t1, a1 = ta[i]
    t2, a2 = ta[i+1]
    if t2 >= t1 and a2 >= a1: continue

    k = max((t1 + t2 - 1) // t2, (a1 + a2 - 1) // a2)
    ta[i+1][0] = k*t2
    ta[i+1][1] = k*a2

print(ta[n-1][0]+ta[n-1][1])


# ------------------ 入力例 -------------------
5
13 11
11 9
9 7
7 5
5 3


3
2 3
1 1
3 2

4
1 1
1 1
1 5
1 100

5
3 10
48 17
31 199
231 23
3 2


# ----------------- 解答時間 ------------------
# コーナーケースでWAで解説AC
#

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/arc/062/editorial.pdf
# 解答の方針は合ってた
# この問題は割り算からのceilを使うことでWAがでる悪名高き問題
# 単純な割り算(/)は浮動点小数floatの計算になるが，pythonでは16桁くらいまでしか精度が保証されていない
# 今回は10**18まで桁があるので，こんな大きな桁だと誤差が生じてWAになる

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#浮動点小数
#浮動点小数の割り算

