# ABC019C - 高橋くんと魔法の箱
# URL: https://atcoder.jp/contests/abc019/tasks/abc019_3
# 日付: 2020/12/22

# ---------- 思ったこと / 気づいたこと ----------
# 変な関数

# ------------------- 方針 --------------------
# 数列の各要素を2で割れなくなるまで割る (奇数になるまで)
# この新しい数列のuniqueな要素の数が答えなので，setのlength使う

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    x = a[i]
    while x % 2 == 0:
        x //= 2
    b.append(x)
print(len(set(b)))

# ------------------ 入力例 -------------------
3
1 2 3

4
2 4 8 16

4
2 3 5 7

# ----------------- 解答時間 ------------------
# 5分

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc019
# おもろな−い

# ----------------- カテゴリ ------------------
#AtCoder #abc
#偶奇に注目
