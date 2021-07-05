# 典型90問082 - Counting Numbers（★3）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_cd
# Date: 2021/06/28

# ---------- Ideas ----------
# たぶんAとBの合計の差が4の倍数なら行ける？
# 普通にシミュレーションすれば良さそう

# ------------------- Answer --------------------
#code:python
h, w = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(h)]
B = [[int(i) for i in input().split()] for _ in range(h)]

ans = 0
for y in range(h-1):
    for x in range(w-1):
        cnt = A[y][x] - B[y][x]
        ans += abs(cnt)

        for dx in range(2):
            for dy in range(2):
                A[y+dy][x+dx] -= cnt

print(f'Yes\n{ans}' if A==B else 'No')

# ------------------ Sample Input -------------------
3 3
0 0 0
0 0 0
0 0 0
1 1 0
1 1 0
0 0 0

5 5
6 17 18 29 22
39 50 25 39 25
34 34 8 25 17
28 48 25 47 42
27 47 24 32 28
4 6 3 29 28
48 50 21 48 29
44 44 19 47 28
4 49 46 29 28
4 49 45 1 1

# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# noになるときの条件がよくわからなかったけど，できたらできるし，できなかったらできない

# ----------------- Category ------------------
#AtCoder
#シミュレーション
#操作の順番は関係ない