# ABC167D - Teleporter
# URL: https://atcoder.jp/contests/abc167/tasks/abc167_d
# Date: 2021/02/03

# ---------- Ideas ---------- 
# K<=10**18なので，K回のシミュレーションはできない
# 周期性が間違いなくあり，min(n, k)以内の探索で見つけられる
# スタート地点から周期の始まりまでの回数，周期の始まりから終わりまでの回数が必要


# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [i-1 for i in a]

visit = [0]*n # 訪問回数
visit[0] = 1

now = 0 # 今の居場所
flag = False # 周期があったかどうか
for i in range(min(k, n+1)):
    now = a[now]
    if visit[now] == 1:
        flag = True
        break
    else:
        visit[now] += 1

if not flag: # 周期してなかったら，現在いる場所
    print(now+1); exit()

# 周期がある場合
s = now # 周期が始まるインデックス
t1 = i+1 # スタートから周期が1回終わるまでの回数
now = 0
for i in range(n+1):
    if now == s:
        break
    now = a[now]
t2 = i # スタートから周期が始まるまでの回数
p = t1 - t2 # 周期1回分の回数

rest = (k - t2) % p
now = s
for i in range(rest):
    now = a[now]
print(now+1)





# ------------------ Sample Input -------------------
5 3
2 3 4 5 6

4 5
3 2 4 1

6 727202214173249351
6 5 2 5 3 2

# ----------------- Length of time ------------------
# 31分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc167/editorial.pdf
# 解説通りに説いてるけど，流石にもう少し短くかけそう

# ----------------- Category ------------------
#AtCoder  
#ABC-D
#グラフ問題
#シミュレーション問題
#なもりグラフ
#周期性に着目する
#K回操作後の結果を求める
#茶diff