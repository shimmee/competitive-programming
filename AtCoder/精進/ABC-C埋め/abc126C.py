# ABC126C - Dice and Coin
# URL: https://atcoder.jp/contests/abc126/tasks/abc126_c
# 日付: 2020/11/28

# ---------- 思ったこと / 気づいたこと ----------
# ノート参照


# ------------------- 解答 --------------------
#code:python
n, k = map(int, input().split())
m = [float('INF')]*n

def get_min_m(i):
    j = 0
    while True:
        if i*2**j >= k:
            break
        j += 1
    return j


for i in range(1, n+1):
    m[i-1] = get_min_m(i)

ans = 0
for i in range(n):
    ans += ((0.5)**m[i])/n
print(ans)

# 以下だとバグった！！！少数の計算ってセンシティブ
ans = 0
for i in range(n):
    ans += ((0.5)**m[i])
print(ans/n)


# 小数点がバグったので有理数の計算で小数が狂ったか？と思いfractions.Fractionを使ってみたが変わらず。
from fractions import Fraction
# ans = Fraction(0, 1)
# for i in range(n):
#     ans += Fraction(1,2)**Fraction(m[i])
# print(float(ans/n))


# ------------------ 入力例 -------------------
3 10

100000 5

# ----------------- 解答時間 ------------------
# 33分

# -------------- 解説 / 感想 / 反省 -------------
# 小数点が合わなくて大変だった
# 1/3を最後にするか，ループの中で各々についてするかの違いだった
# 「計算は細かく行う」 ことを学んだ

# ----------------- カテゴリ ------------------
#AtCoder #abc
#小数バグ

