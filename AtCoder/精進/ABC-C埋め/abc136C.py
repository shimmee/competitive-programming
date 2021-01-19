# ABC136C - Build Stairs
# URL: https://atcoder.jp/contests/abc136/tasks/abc136_c
# 日付: 2020/11/25

# ---------- 思ったこと / 気づいたこと ----------
# 逆から考えたらよさそう

# ------------------- 方針 --------------------
# 右から左に進む
# 一つ隣が自分以下ならOK，もし自分より大きくても1差ならOK,2差以上ならダメ

# ------------------- 解答 --------------------
#code:python
n = int(input())
h = list(map(int, input().split()))
h = h[::-1]

flag = True
for i in range(n-1):
    if h[i+1] <= h[i]:
        continue
    elif h[i + 1] - h[i] == 1:
        h[i+1] = h[i]
    else:
        flag = False
if flag: print('Yes')
else: print('No')

# ------------------ 入力例 -------------------
5
1 2 1 1 3

4
1 3 2 1


# ----------------- 解答時間 ------------------
# 9分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc136/editorial.pdf
# 解説通りに解けた

# ----------------- カテゴリ ------------------
#AtCoder #abc
#逆から考える
