# ABC111C - /\/\/\/
# URL: https://atcoder.jp/contests/abc111/tasks/arc103_a
# 日付: 2020/12/01

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 偶数番目と奇数番目の数列に分ける: even, odd
# 数列ごとの各数字の出現回数をCounterでゲット
# 最頻値をゲットする: 最頻値以外の数の個数が書き換える個数となる
# evenとoddで最頻値が同じ場合には，出現回数が多い方をキープして，もう片方は2番目の最頻値を採用する

# ------------------- 解答 --------------------
#code:python
from collections import Counter
n = int(input())
v = list(map(int, input().split()))

# 数列を偶数番目と奇数番目に分ける
even = [v[i] for i in range(n) if i % 2 == 0]
odd = [v[i] for i in range(n) if i % 2 == 1]

# パターン1: evenとoddが同じ数列の場合, 全体の半分を書き換える必要がある
if even == odd:
    print(n//2)
    exit()


# 各数字の出現回数を数える
even = list(Counter(even).items())
odd = list(Counter(odd).items())

# valueでソートする
even = sorted(even, key=lambda x: x[1], reverse=True)
odd = sorted(odd, key=lambda x: x[1], reverse=True)

# パターン2: 片方に1種類の数字しかない場合
if len(even) == 1 and len(odd) == 1:
    print(0)
    exit()
if len(even) == 1:
    print(sum([l[1] for l in odd[1:]]))
    exit()
if len(odd) == 1:
    print(sum([l[1] for l in even[1:]]))
    exit()

# パターン3: evenとoddの最頻値が同じ場合
ans = n
if even[0][0] == odd[0][0]:
    if even[0][1] >= odd[0][1]: # evenは最頻値，oddは2番目の最頻値
        print(n - even[0][1] - odd[1][1])
        exit()
    else:
        print(n - even[1][1] - odd[0][1])
        exit()
# パターン4: その他
else:
    print(n - even[0][1] - odd[0][1])
    exit()


##############################
# 3/20 WA
##############################

from collections import Counter
n = int(input())
v = list(map(int, input().split()))

# 数列を偶数番目と奇数番目に分ける
even = [v[i] for i in range(n) if i % 2 == 0]
odd = [v[i] for i in range(n) if i % 2 == 1]

# パターン1: evenとoddが同じ数列の場合, 全体の半分を書き換える必要がある
if even == odd:
    print(n//2)
    exit()

# 各数字の出現回数を数えて, values でソート
even_dict = sorted(list(Counter(even).items()), key=lambda x: x[1], reverse=True)
odd_dict = sorted(list(Counter(odd).items()), key=lambda x: x[1], reverse=True)

# 最頻値をゲット
mode_even = even_dict[0][0]
mode_odd  = odd_dict[0][0]

if mode_even != mode_odd: # evenとoddで最頻値が異なる場合
    ans = sum([1 for i in even if i != mode_even]) + sum([1 for i in odd if i != mode_odd])
    print(ans)
    exit()
else: # evenとoddで最頻値が同じ場合
    mode2_even = even_dict[1][0]
    mode2_odd = odd_dict[1][0]
    ans1 = sum([1 for i in even if i != mode2_even]) + sum([1 for i in odd if i != mode_odd])
    ans2 = sum([1 for i in even if i != mode_even]) + sum([1 for i in odd if i != mode2_odd])
    print(min(ans1, ans2))
    exit()

# 1ケースWA
# パターン1の例外除去で，除去してはいけないものをしてるっぽい
# ギブアップ


# ちょう短い解答: https://atcoder.jp/contests/abc111/submissions/18439056
# 解答みたらmost_common()なんて便利なものがあった

from collections import Counter
n = int(input())
v = list(map(int, input().split()))

# 各数字の出現回数を数えて, values でソート
even = Counter(v[0::2]).most_common()
odd = Counter(v[1::2]).most_common()

if even[0][0] != odd[0][0]: # evenとoddで最頻値が異なる場合
    print(n - even[0][1] - odd[0][1])
else: # evenとoddで最頻値が同じ場合
    try:
        ans1 = n - even[1][1] - odd[0][1] # evenを2番目の最頻値，oddを1番目の最頻値つかう
        ans2 = n - even[0][1] - odd[1][1] # evenを1番目の最頻値，oddを2番目の最頻値つかう
        print(min(ans1, ans2))
    except:
        print(n//2)





# ------------------ 入力例 -------------------
4
3 1 3 2

6
105 119 105 119 105 119

4
1 1 1 1

8
1 1 2 2 1 1 3 4

# ----------------- 解答時間 ------------------
# 解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc103/editorial.pdf
# even, oddに1つの数字しか現れないときの処理が大変かと思ってたらtry, exceptで書いてる人いて感動した
# pythonの学びが多かった。
# Counterのmost_common()
# 偶数番目v[0::2] と 奇数番目v[1::2]


# ----------------- カテゴリ ------------------
#AtCoder #abc
#偶奇に注目
#Counter
#most_common()
#最頻値
