# ABC186E - Throne
# URL: https://atcoder.jp/contests/abc186/tasks/abc186_e
# 日付: 2020/12/19

# ------------------- 方針 --------------------
# 解説AC
# ノートを参照

# ------------------- 解答 --------------------
#code:python
T = int(input())
from math import gcd

def extgcd(a, b):
    # ax*by=cのa,bを与えることで，解の組(x0, y0)と右辺dを返してくれる
    # つまり，a*x0+b*y0=d を満たす
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

for _ in range(T):
    n, s, k = map(int, input().split())
    d = gcd(n, k)
    if s % d != 0: # ax+by=cのとき，cがaとbのgcdで割れなければ，解が存在しない
        print(-1)
    else:
        a = n
        b = -k
        c = s

        a_ = a // d
        b_ = b // d
        c_ = c // d

        c0, x0, y0 = extgcd(a_, b_)
        p = c_// c0
        l = (p*y0) // a_
        y = -a_*l + p*y0
        print(y)

# もう少し綺麗に書ける

T = int(input())
from math import gcd

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

for _ in range(T):
    n, s, k = map(int, input().split())
    d = gcd(n, k)
    if s % d != 0: # ax+by=cのとき，cがaとbのgcdで割れなければ，解が存在しない
        print(-1)
    else:
        a = n //d
        b = -k // d
        c = s // d

        c0, x0, y0 = extgcd(a, b)
        y = -a*(((c // c0)*y0) // a) + (c // c0)*y0
        print(y)

# powを使っても逆元
T = int(input())
from math import gcd

for _ in range(T):
    n, s, k = map(int, input().split())
    d = gcd(n, k)
    if s % d != 0: # ax+by=cのとき，cがaとbのgcdで割れなければ，解が存在しない
        print(-1)
    else:
        n //= d
        k //= d
        s //= d
        print(((-s * pow(k, -1, n)) % n))


# ------------------ 入力例 -------------------
4
10 4 3
1000 11 2
998244353 897581057 595591169
10000 6 14


# ----------------- 解答時間 ------------------
# 本番間に合わず

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/abc186/editorial/401
# 与えられた問題を式で書くと一次不定方程式になる
# 拡張ユークリッド互除法という方法で解く必要があったが，ググっても間に合わず
# コンテスト終わってからめっちゃ勉強した

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#gcd
#一次不定方程式
#拡張ユークリッド互除法
