# ABC113C - ID
# URL: https://atcoder.jp/contests/abc113/tasks/abc113_c
# 日付: 2020/12/11


# ------------------- 方針 --------------------
# 入力の際に入力の順番jも一緒にリストに入れる
# 県の大きさのリストを作る[[], []]みたいな
# 県ごとのインデックスに，属する市の入力順jと年yをappendする
# 県でループを回して，属する市を年でソートする
# 回答用のリストを用意する
# for enumerateして，県番号とenumerateの順番から，出力用の文字列を作って，入力順にリストに入れる

# ------------------- 解答 --------------------
#code:python
n ,m = map(int, input().split())
py = []
for j in range(m):
    p, y = map(int, input().split())
    py.append([j, p-1, y])
# jは入力の順番: この順で出力する必要がある


l = [[] for _ in range(n)] # 県の大きさのリスト
# 県ごとに各市の入力順jと年yをappendする
for i in range(m):
    j, p, y = py[i]
    l[p].append([j, y])

ans = [None]*m
for k in range(n):
    lk = l[k] # 県kにおける全ての市を含んだリスト:
    lk = sorted(lk, key=lambda x: x[1])
    for i, jy in enumerate(lk): # iは県kにおけるできた順番
        j, y = jy
        num = str(k+1).zfill(6) + str(i+1).zfill(6)
        ans[j] = num

for i in ans:
    print(i)



# ------------------ 入力例 -------------------
2
3
1
32
2
63
1
12

# ----------------- 解答時間 ------------------
# 27分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc113/editorial.pdf
# 前に解いた方針見ながら説いた
# 次はノールックで解きたい！！！！

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#enumerate

