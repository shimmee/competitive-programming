# AGC013A - Sorted Arrays
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc013/tasks/agc013_a
# 日付: 2020/12/29

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 単調増加だけ数える? 両方

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

ans = 0
if a[0] <= a[1]:
    now = 'inc'
else: now = 'dec'

for i in range(n-1):
    print(now, a[i])
    if now == 'inc':
        if a[i] <= a[i+1]: continue
        else:
            ans += 1
            now = 'dec'
    else:
        if a[i] >= a[i+1]: continue
        else:
            ans += 1
            now = 'inc'
    if i == n-2:
        ans += 1

print(ans)



# 切り替わりを見つける
n = int(input())
a = list(map(int, input().split()))


if a[0] <= a[1]:
    now = 'inc'
else: now = 'dec'

ans = 0
for i in range(n-2):
    if now == 'inc':
        if a[i] <= a[i + 1]:
            continue
        else:
            ans += 1
            if a[i+1] <= a[i+2]:
                now = 'inc'
            else:
                now = 'dec'
    else:
        if a[i] >= a[i + 1]:
            continue
        else:
            ans += 1
            if a[i + 1] >= a[i + 2]:
                now = 'dec'
            else:
                now = 'inc'
print(ans)

# わあああああああああムズい
# https://atcoder.jp/contests/agc013/submissions/8984573
# 上がってかつ下がる瞬間，もしくは下がっててかつ上がる瞬間を見つけるために，upとdownのフラグを持つ
# 両方Trueになったら，インクリメント
n = int(input())
s = list(map(int,input().split()))
cnt = 1
up = False
down = False

for i in range(n-1):
    if s[i] < s[i+1]:
        up = True
    elif s[i]>s[i+1]:
        down = True
    if up and down:
        cnt += 1
        up = False
        down = False
print(cnt)



# ------------------ 入力例 -------------------
6
1 2 3 2 2 1

9
1 2 1 2 1 2 1 2 1

7
1 2 3 2 1 999999999 1000000000

# ----------------- 解答時間 ------------------
# 解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/agc013/editorial.pdf
# 難しかった。解説読んでもかけなかったので，他の人の解答みた
# 一般に単調増加や単調減少はflagで管理した方がいいのかな？

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#解説AC #medium復習
#単調増加
#単調減少
#AGC-A