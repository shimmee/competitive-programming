# AGC017A - Biscuits
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc017/tasks/agc017_a
# 日付: 2020/12/30

# ---------- 思ったこと / 気づいたこと ----------
# 簡単なDPかな？

# ------------------- 方針 --------------------
# P=1なら，偶数をいくつか選んで奇数を奇数個選ぶ
# P=0なら，偶数をいくつか選んで奇数から偶数個とる

# ------------------- 解答 --------------------
#code:python

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n, p = map(int, input().split())
a = list(map(int, input().split()))

# 偶数の個数と奇数の個数を数える
even = 0
odd = 0
for i in range(n):
    if a[i] % 2 == 0: even += 1
    else: odd += 1

ans = 0
if p == 0:  # 偶数をいくつか選んで奇数から偶数個とる
    # 偶数を選ぶ
    if even > 0:
        ans += 2**even

    # 奇数から偶数個とる
    if odd >= 2:
        p = 0
        for i in range(0, odd+1, 2):
            p += cmb(odd, i)
        if ans == 0:
            ans = p
        else:
            ans = ans*p
    print(ans)
    exit()
else:
    if odd > 0:
        if even > 0:
            ans = 2 ** even

            # 奇数から奇数個とる
            p = 0
            for i in range(1, odd + 1, 2):
                p += cmb(odd, i)
            print(ans*p)
            exit()
print(ans)


# 50行も書いてしまったけど
# 超短く書ける: https://atcoder.jp/contests/agc017/submissions/11695311
n, p = map(int, input().split())
a = list(map(int,input().split()))

# Aの要素すべてが偶数だったら，p=1は実現できないので0を出力，p=0はそれぞれ選ぶ選ばないの2**n通り
if all(i % 2==0 for i in a):
    print(0 if p==1 else 2**n)
else:
    # Aの要素に奇数があれば，使用する奇数を取り除いたn-1個から好きにとる。
    # hogehoge
    print(2**(n-1))

# ------------------ 入力例 -------------------
2 0
1 3

1 1
50


3 0
1 1 1

45 1
17 55 85 55 74 20 90 67 40 70 39 89 91 50 16 24 14 43 24 66 25 9 89 71 41 16 53 13 61 15 85 72 62 67 42 26 36 66 4 87 59 91 4 25 26

# ----------------- 解答時間 ------------------
# 23分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/agc017/editorial.pdf
# 超簡潔に書けるのに，50行も書いてしまった

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#medium復習