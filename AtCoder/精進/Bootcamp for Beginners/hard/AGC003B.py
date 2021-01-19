# AGC003B - Simplified mahjong
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc003/tasks/agc003_b
# 日付: 2020/12/28

# ---------- 思ったこと / 気づいたこと ----------
# 簡単じゃないか？

# ------------------- 方針 --------------------
# 貪欲にペアを作る

# ------------------- 解答 --------------------
#code:python
n = int(input())
ans = 0
a = int(input())
for i in range(n-1):
    b = int(input())

    # iの書かれたカードa枚からペアを作る
    q, r = divmod(a, 2)
    ans += q

    # iのカードa枚のうちの余ったカードr枚と(i+1)のカードb枚でペアを作る
    ans += min(r, b)
    b -= min(r, b)
    a = b

# 最後の余ったカードでペアをつくる
q, r = divmod(a, 2)
ans += q
print(ans)

# 24ケース中10ケースWAです。
# 貪欲が嘘解法っぽい?
# 最後の余ったカードの処理を忘れてた
#

# ------------------ 入力例 -------------------
3
100
3
50

4
2
1
2
1

4
4
0
3
2

8
2
0
1
6
0
8
2
1


# ----------------- 解答時間 ------------------
# 17分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/agc/003/editorial.pdf
#

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-hard
#貪欲法
