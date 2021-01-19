# ABC082C - Good Sequence
# URL: https://atcoder.jp/contests/abc082/tasks/arc087_a
# 日付: 2020/12/09

# ---------- 思ったこと / 気づいたこと ----------
# Counterつかえる！

# ------------------- 方針 --------------------
# ans=0で初期化
# collections.Counter()で各数字の出現回数を得てdictionaryにする
# 自分自身(key)より出現回数(value)が小さければ，全部消すしかないので，value分をansにインクリメント
# 出現回数(value)が自分自身(key)以上であれば，value-key分減らせばいいので，value-keyをansにインクリメント

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

import collections
dict = collections.Counter(a)
ans = 0
for key, value in dict.items():
    if key > value:
        ans += value
    else:
        ans += value-key
print(ans)


# ------------------ 入力例 -------------------
4
3 3 3 3

5
2 4 1 4 2

6
1 2 2 3 3 3

1
1000000000

8
2 7 1 8 2 8 1 8


# ----------------- 解答時間 ------------------
# 8分AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc082/editorial.pdf
# 解説通りの完璧な解答

# ----------------- カテゴリ ------------------
#AtCoder #abc
#collections.Counter()
#Counter
