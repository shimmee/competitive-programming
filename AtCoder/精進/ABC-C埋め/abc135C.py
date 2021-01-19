# ABC135C - City Savers
# URL: https://atcoder.jp/contests/abc135/tasks/abc135_c
# 日付: 2020/11/26

# ---------- 思ったこと / 気づいたこと ----------
# 条件分岐とループで行けそう


# ------------------- 解答 --------------------
#code:python
n=int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] <= b[i]:
        ans += a[i]
        b[i] -= a[i]
    else:
        ans += b[i]
        b[i] = 0

    if a[i+1] <= b[i]:
        ans += a[i+1]
        b[i] -= a[i+1]
        a[i+1] = 0
    else:
        ans += b[i]
        b[i] = 0
        a[i+1] -= b[i]
print(ans)


# かつっぱ解説を見た: https://www.youtube.com/watch?v=LEcn4V8RRfM
# minを上手く使う
n=int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

killed = 0
for i in range(n):
    # Aiを倒す
    now_killed = min(a[i], b[i])
    killed += now_killed
    a[i] -= now_killed
    b[i] -= now_killed

    # Ai+1を倒す
    now_killed = min(a[i+1], b[i])
    killed += now_killed
    a[i+1] -= now_killed
    b[i] -= now_killed
print(killed)
# ------------------ 入力例 -------------------
2
3 5 2
4 5

3
5 6 3 8
5 100 8

2
100 1 1
1 100

# ----------------- 解答時間 ------------------
# 30分で半分WAでギブアップ
#

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc135/editorial.pdf
# かつっぱ解説の方がわかりやすい: https://www.youtube.com/watch?v=LEcn4V8RRfM
#

# ----------------- カテゴリ ------------------
#AtCoder #abc
#minmaxを上手く使う
