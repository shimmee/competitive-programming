# ABC072D - Derangement
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc072/tasks/arc082_b
# 日付: 2020/12/31

# ---------- 思ったこと / 気づいたこと ----------
# 前から貪欲にとく

# ------------------- 方針 --------------------
# 連続で2つが共に異なってたら，一気に入れ替える。1回のスワップで2個入れ替えられてラッキー
# 1つしかない時は，1つ入れ替える。

# ------------------- 解答 --------------------
#code:python
n = int(input())
p = list(map(int, input().split()))
p = [i-1 for i in p]

flag = [False]*n
for i in range(n):
    if p[i] == i:
        flag[i] = True

ans = 0
i = 0
while i < n:
    if i < n-1:
        if flag[i] and flag[i+1]:
            ans += 1
            i += 2
            continue
    if flag[i]:
        ans += 1
    i += 1
print(ans)


# ------------------ 入力例 -------------------
9
1 2 4 9 5 8 7 3 6

2
2 1

2
1 2


# ----------------- 解答時間 ------------------
# 8分

# -------------- 解説 / 感想 / 反省 -------------
#  https://img.atcoder.jp/arc082/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#貪欲法