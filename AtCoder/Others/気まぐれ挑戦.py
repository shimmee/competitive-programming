

##############################################################
# カテゴリ: 全探索?
# タイトル: AtCoder Beginner Contest 178: E - Dist Max
# URL: https://atcoder.jp/contests/abc178/tasks/abc178_e
# 日時: 2020/10/10
##############################################################
n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

max_dist = 0
for i in range(n):
    for j in range(i+1, n):
        dist = abs(x[i]-x[j]) + abs(y[i]-y[j])
        if dist > max_dist:
            max_dist = dist
print(max_dist)

# これだとO(N^2)でTLE
# マンハッタン距離の数式を展開して，上手いことO(N)にする
# 解答: https://img.atcoder.jp/abc178/editorial-E-phcdiydzyqa.pdf




##############################################################
# カテゴリ: ひらめき？
# タイトル: AtCoder Beginner Contest 173: D - Chat in a Circle
# URL: https://atcoder.jp/contests/abc173/tasks/abc173_d
# 日時: 2020/10/16
##############################################################
import math
N = int(input())
A = list(map(int,input().split()))

p = math.ceil((N-2)/2)+1
A.sort(reverse=True)
ans = 0
ans += A[0]
ans += sum(A[1:p])*2
if N % 2 == 0:
    print(ans)
else:
    print(ans - A[p-1])



##############################################################
# カテゴリ: 大きい数の処理
# タイトル: AtCoder Beginner Contest 169: B - Multiplication 2
# URL: https://atcoder.jp/contests/abc169/tasks/abc169_b
# 日時: 2020/10/19
##############################################################
N = int(input())
A = list(map(int,input().split()))

A.sort()
if A[0] == 0:
    print(0)
else:
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            ans = -1
            break
    print(ans)


##############################################################
# カテゴリ: 大きい数の処理
# タイトル: AtCoder Beginner Contest 169: C - Multiplication 3
# URL: https://atcoder.jp/contests/abc169/tasks/abc169_c
# 日時: 2020/10/19
##############################################################
a, b = input().split()
a = int(a)
b = int(b.replace('.', ''))
print(a*b // 100)

# 小数を切り落として整数部分だけほしい場合は//で良い


##############################################################
# カテゴリ: ABC 200点レベル
# タイトル: AtCoder Beginner Contest 117: B - Polygon
# URL: https://atcoder.jp/contests/abc117/tasks/abc117_b
# 日時: 2020/10/22
##############################################################

n = int(input())
l = list(map(int,input().split()))
l.sort()
if sum(l[0:-1]) > l[-1]:
    print('Yes')
else:
    print('No')
4
3 8 5 1


##############################################################
# カテゴリ: ABC 300点レベル
# タイトル: AtCoder Beginner Contest 116: C - Grand Garden
# URL: https://atcoder.jp/contests/abc116/tasks/abc116_c
# 日時: 2020/10/22
##############################################################
from itertools import groupby

n = int(input())
h = list(map(int,input().split()))
h_ = h.copy()
h = h_.copy()

def rec(h, ans):
    ans = 0
    while h.count(0) == 0:
        h = [j - 1 for j in h]
        ans += 1

    groupby(h, lambda x: x == 0)
    h = [list(group) for k, group in groupby(h, lambda x: x == 0) if not k]

    if h == []:
        return ans

    for i in h:
        ans += rec(i, ans)

    return ans

ans = rec(h, 0)
print(ans)


##############################################################
# カテゴリ: ABC 緑レベル
# タイトル: AtCoder Beginner Contest 1: C - Streamline
# URL: https://atcoder.jp/contests/abc117/tasks/abc117_c
# 日時: 2020/10/22
##############################################################

n, m = list(map(int,input().split()))
x = list(map(int,input().split()))
x = sorted(x)

x[-1] - x[0]
[abs(x[i] - x[i+1]) for i in range(len(x)-1)]


# おもいつかなくて解答見た


##############################################################
# カテゴリ: 数学
# タイトル: AtCoder Beginner Contest 106: C - 106
# URL: https://atcoder.jp/contests/abc117/tasks/abc117_c
# 日時: 2020/10/25
##############################################################
import math
n = int(input())

b = 1
while True:
    if 5**b > n:
        break
    else:
        a = math.log(n - 5 ** b, 3)
        if a == math.floor(a):
            break
        else:
            b += 1
if a == math.floor(a):
    print(f'{math.floor(a)} {b}')
else:
    print(-1)

# REなどあった。普通に2重ループでいい
import math
n = int(input())

for a in range(1, 38):
    for b in range(1, 26):
        if 3**a + 5**b == n:
            print(f'{a} {b}')
            exit()
print(-1)


##############################################################
# カテゴリ: 数学
# タイトル: AtCoder Beginner Contest 106: E - Medals
# URL: https://atcoder.jp/contests/abc117/tasks/abc117_c
# 日時: 2020/10/25
##############################################################

n, k = map(int, input().split())
a = list(map(int,input().split()))

def fun(m, d):
    q = m // d
    r = m % d

    if q % 2 == 0 and (q*d+1 <= m <= (q+1)*d):
        return True
    else:
        return False

fun(4, 4)

t = [[False]*(n*k*2)]*n
for i in range(n):

##############################################################
# カテゴリ: 素因数分解
# タイトル: 荷物
# URL: http://icpc.iisf.or.jp/past-icpc/domestic2020/contest/all_ja.html
# 日時: 2020/11/05
##############################################################

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

n = 12137858827249
div = set(make_divisors(n))
ans = float('INF')
for i in div:
    for j in div:
        k = (n // i) // j
        if k in div:
            if ans > i + j + k:
                ans = min(ans, i + j + k)
                com = [i, j, k]
print(ans)

# これで合ってるはずだけど，15桁の素因数分解に2秒かかってるので，通るかどうかわからん