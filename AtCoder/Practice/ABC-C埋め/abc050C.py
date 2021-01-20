# ABC050C - Lining Up
# URL: https://atcoder.jp/contests/arc066/tasks/arc066_a
# 日付: 2020/12/11

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 偶数と奇数で場合分け
# 偶数の時，数列が(n-1)が2人，(n-2)が2人,..., 1が2人という感じにならないとだめ。
# 奇数の時，数列が(n-1)が2人，(n-2)が2人,..., 0が1人という感じにならないとだめ。
# Counterを使って，2人ずつちゃんといるのか確認する
# もしOKなら。偶数の時2**(n/2)，，奇数の時2**((n-1)/2)が答えになるが，大きくなるのでpow使う

# ------------------- 解答 --------------------
#code:python
mod = 10**9+7
import collections
n = int(input())
a = list(map(int, input().split()))
a.sort()
dict1 = collections.Counter(a)

if n % 2 == 1: # 奇数の時
    # 0が1つ，(n-1)~2がそれぞれ2回ずつ出現しているのが条件: この条件を満たす辞書をdict2として作成して，dict1と一致するか調べる
    dict2 = {}
    for i in range(0, n, 2):
        if i == 0:
            dict2.update({0: 1})
        else:
            dict2.update({i: 2})

    if dict1 == dict2:
        print(pow(2, (n-1)//2, mod))
    else:
        print(0)
elif n % 2 == 0: # 偶数の時
    # (n-1)が2回，(n-2)が2回,..., 1が2回 出現が条件
    dict2 = {}
    for i in range(1, n, 2):
        dict2.update({i: 2})
    if dict1 == dict2:
        print(pow(2, n//2, mod))
    else:
        print(0)

# 解説のようにリストを使ってやってみる
mod = 10**9+7
n = int(input())
a = list(map(int, input().split()))
a.sort()

if n % 2 == 1: # 奇数の時
    l = [0]
    for i in range(2, n, 2):
        l += [i, i]
    if l == a:
        print(pow(2, (n-1)//2, mod))
    else:
        print(0)
elif n % 2 == 0:  # 偶数の時
    l = []
    for i in range(1, n, 2):
        l += [i, i]
    if l == a:
        print(pow(2, n//2, mod))
    else:
        print(0)
# ------------------ 入力例 -------------------
5
2 4 4 0 2

7
6 4 0 2 4 0 2

8
7 5 1 1 7 3 5 3

# ----------------- 解答時間 ------------------
#

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc066/editorial.pdf
# 辞書使わなくても単純にリストでよかった
# 皆同じような解き方してる
# 初めてpowを初見で使った

# ----------------- カテゴリ ------------------
#AtCoder #abc
#高速なべき乗計算