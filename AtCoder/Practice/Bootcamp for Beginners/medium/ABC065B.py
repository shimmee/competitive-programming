# ABC065B - Trained?
# Bootcamp for beginners - medium - 1
# URL: https://atcoder.jp/contests/abc065/tasks/abc065_b
# 日付: 2020/12/28

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 0indexにする
# 今光ってるボタンをnowで管理
# 次のボタンnowはa[now]で更新
# nowが1ならOK
# n回ボタンを押して1が光ってなかったらダメなので-1を出力

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = [int(input())-1 for _ in range(n)]

now = 0
cnt = 0
for _ in range(n):
    if now == 1:
        break
    else:
        now = a[now]
        cnt += 1
if now == 1:
    print(cnt)
else:
    print(-1)

# ------------------ 入力例 -------------------
3
3
1
2

4
3
4
1
2

5
3
3
4
2
4

# ----------------- 解答時間 ------------------
# 4分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc076/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder #ABC-B
#BootcampForBeginners-medium
