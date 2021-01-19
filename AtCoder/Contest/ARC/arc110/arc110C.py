# ARC110C -Exoswap
# URL: https://atcoder.jp/contests/arc110/tasks/arc110_c
# 日付: 2020-12-05

# ---------- 思ったこと / 気づいたこと ----------
# 本番おもいつかず解説みてAC

# ------------------- 解答 --------------------
#code:python
n = int(input())
arr = list(map(int, input().split()))

cnt = 0
order = []
for i in range(n):
    # 3. 走査範囲を前からひとつ狭める
    for j in reversed(range(i+1, n)):
        # 1. 後ろから順に隣り合う要素を比較する。
        if arr[j-1] > arr[j]:
            # 2. 左が右の要素に比べ大きい場合交換する。
            cnt += 1
            order.append(j)
            arr[j-1], arr[j] = arr[j], arr[j-1]

if cnt == n-1:
    for i in order:
        print(i)
else:
    print(-1)
print(cnt)
print(order)

# このバブルソートだとO(N^2)になってTLE
# 解説: https://atcoder.jp/contests/arc110/editorial/387
# Pi=1となるiについて，P1=1となるまでスワップし続ける
# Pi−1までにPj=jとならないものがあればダメ
# OKならばPiから進む

n = int(input())
a = list(map(int, input().split()))
a = [i-1 for i in a]

# position of 0-n in A
pos = [0]*n
for i in range(n):
    pos[a[i]] = i


start = 0
goal = pos[start]
flag = False
order = []
while start < n:
    if goal <= start: break
    for i in reversed(range(start, goal)):
        a[i+1], a[i] = a[i], a[i+1]
        order.append(i+1)

    # Pi−1までにPj=jとならないものがあればダメのチェック
    for i in range(start, goal):
        if a[i] != i:
            flag = True
            break
    if flag:
        break
    start = goal
    goal = pos[start]

if flag:
    print(-1)
else:
    for i in order:
        print(i)

# 5/60 TLE
# enumerateで最初きれいに書ける
# 参考: https://atcoder.jp/contests/arc110/submissions/18581304

n = int(input())
a = list(map(int, input().split()))
a = [i-1 for i in a]

# position of 0-n in A
pos = [0]*n
for i, p in enumerate(a):
    pos[p] = i

start = 0
ans = []
while start < n:
    goal = pos[start]
    if goal <= start: break
    for i in reversed(range(start, goal)):
        a[i+1], a[i] = a[i], a[i+1]
        ans.append(i+1)
    start = goal


if len(ans)==n-1:
    if a == list(range(n)): # Pi−1までにPj=jとならないものがあればダメのチェック
        for out in ans:
            print(out)
    else:
        print(-1)
else:
    print(-1)



# ------------------ 入力例 -------------------
5
2 4 1 5 3

5
5 4 3 2 1

# ----------------- 解答時間 ------------------
# 1hで解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/arc110/editorial/387

# ----------------- カテゴリ ------------------
#AtCoder #arc
#解説AC
#ソート