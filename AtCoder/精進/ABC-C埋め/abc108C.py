# ABC108C - Triangular Relationship
# URL: https://atcoder.jp/contests/abc108/tasks/arc102_a
# 日付: 2020/12/04

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# Kが奇数のとき，a,b,c全てが0になる必要があるので，p=[n以下のmod kが0となる整数の個数]として，3**pが答え
# Kが偶数のとき, a,b,cが全て0か，もしくはk/2か

# ------------------- 解答 --------------------
#code:python
n, k = map(int, input().split())
zero = 0
for i in range(1, n + 1):
    if i % k == 0:
        zero += 1

if k % 2 == 1:
    print(zero**3)
else:
    cnt = 0
    for i in range(1, n + 1):
        if i % k == k//2:
            cnt += 1
    print(cnt**3 + zero**3)


# ------------------ 入力例 -------------------
3 2

5 3


31415 9265
35897 932

# ----------------- 解答時間 ------------------
# 考察60分以上で解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc102/editorial.pdf
# 超惜しい所まで考えられてた
# aの余りを固定してO(N)で全探索する方法もあるらしい: https://drken1215.hatenablog.com/entry/2018/09/02/011000

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC
#整数論
#O(1)