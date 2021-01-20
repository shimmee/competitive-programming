# ABC167C - Peaks
# URL:https://atcoder.jp/contests/abc166/tasks/abc166_c
# 日付: 2020/11/22

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 良い展望台のフラッグ用意
# 入力を入れて，頂点aの高さが相手頂点b以下の高さだったらflagをfalseにする
# 最後にTrueの数を数える


# ------------------- 解答 --------------------
#code:python
n, m = map(int, input().split())
h = list(map(int, input().split()))
flag = [True]*n

# 入力のうち最高の高さの展望台のみ保存
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if h[a] <= h[b]:
        flag[a] = False
    if h[b] <= h[a]:
        flag[b] = False
print(sum(flag))

# ------------------ 入力例 -------------------
4 3
1 2 3 4
1 3
2 3
2 4


6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6

# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc166/editorial.pdf


# ----------------- カテゴリ ------------------
#AtCoder #abc
#flagを上手く使う
