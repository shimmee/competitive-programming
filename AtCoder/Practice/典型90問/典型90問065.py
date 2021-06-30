# 典型90問065 - RGB Balls 2（★7）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bm
# Date: 2021/06/11

# ---------- Ideas ----------
# otoshidamaの感じで2つ固定する
# 組み合わせを計算するのにパスカルの三角形を使う
# ループの中で計算したらTLEになるから

# ------------------- Answer --------------------
#code:python
mod = 998244353
r, g, b, k = map(int, input().split())
x, y, z = map(int, input().split())

# nCr をパスカルの三角形で作成する
pascal = [[1]]
for i in range(1, max([r,g,b])+1):
    tmp = [1]
    if i > 1:
        for j in range(1, i):
            tmp.append(pascal[i-1][j-1]+pascal[i-1][j] % mod)
    tmp.append(1)
    pascal.append(tmp)

# Otoshidamaの要領で2種類固定する
ans = 0
for rn in range(r+1): # 赤玉の個数
    for gn in range(g+1): # 緑玉の個数
        bn = k - rn - gn # 青玉の個数
        if 0 <= bn <= b and rn+gn <= x and gn+bn <= y and bn+rn <= z:
            cnt = (pascal[r][rn] % mod) * (pascal[g][gn] % mod) * (pascal[b][bn] % mod)
            ans = (ans + cnt) % mod
print(ans)


# ------------------ Sample Input -------------------
3 1 2 5
4 2 4

65 6 12 35
30 18 35

23502 65936 72385 95835
72759 85735 72385
# ----------------- Length of time ------------------
# 15分

# -------------- Editorial / my impression -------------
# 初めてパスカルの三角形作った

# ----------------- Category ------------------
#AtCoder
#典型90問
#数え上げ
#パスカルの三角形
#二項定理