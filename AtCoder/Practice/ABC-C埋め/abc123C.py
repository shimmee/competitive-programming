# ABC123C - Five Transportations
# URL: https://atcoder.jp/contests/abc123/tasks/abc123_c
# 日付: 2020/11/29

# ---------- 思ったこと / 気づいたこと ----------
# 一番狭いところがポイント
# 「n/狭い所の定員」が遅れの分数になりそう
# 数が大きいのでO(1)で解く必要あり

# ------------------- 方針 --------------------
# a,b,c,d,eのうち一番狭い所 (narrow)をゲット
# int((n/narrow))+5 が答え

# ------------------- 解答 --------------------
#code:python
n = int(input())
abcde = [int(input()) for _ in range(5)]

narrow = min(abcde)
print(int(n/narrow)+5)

# これで3/20 WA
# 解法はあってるけどコーナーケースが間違ってるっぽい
# 解説見た: https://img.atcoder.jp/abc123/editorial.pdf
# おしかった！！
# ceil((n/narrow))+4だった

from math import ceil
n = int(input())
abcde = [int(input()) for _ in range(5)]

narrow = min(abcde)
print(ceil(n/narrow)+4)

# ------------------ 入力例 -------------------
10
1
1
1
1
1

5
3
2
4
3
5

10
123
123
123
123
123

10000000007
2
3
5
7
11

# ----------------- 解答時間 ------------------
# コーナーケースWAからの解説AC30分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc123/editorial.pdf
# 「数字が大きいのでO(1)でとく」という推測は見事に的中していて嬉しかった


# ----------------- カテゴリ ------------------
#AtCoder #abc
#O(1)で解く
