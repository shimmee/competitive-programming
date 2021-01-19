# ABC157C-Guess The Number
# URL: https://atcoder.jp/contests/abc157/tasks/abc157_c
# 日付: 2020/11/19

# ---------- 思ったこと / 気づいたこと ----------
# 0indexに治そう
# N<=3，M<=5なので，ループで一瞬で回りそう
# ちょうどN桁だからN桁だけ考えればいい

# ------------------- 方針 --------------------
# 入力を0indexに治す
# N桁以下の整数を全て列挙
# クエリをループで回して，Nの各桁と一致してるか判定


# ------------------- 解答 --------------------
#code:python
N, M = map(int, input().split())
sc = [[int(i) for i in input().split()] for _ in range(M)]

l = [str(i) for i in range(10**(N-1), 10**N)]
if N==1:
    l = ['0'] + l

for n in l:
    flag = True
    for s, c in sc:
        s -= 1
        if n[s] != str(c):
            flag = False
    if flag:
        print(n)
        exit()
print(-1)

# ------------------ 入力例 -------------------
3 3
1 7
3 2
1 7

3 2
2 1
2 3


3 1
1 0


# ----------------- 解答時間 ------------------
# 20分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc157/editorial.pdf
# なにも難しくはない。pythonは文字列の処理が楽でよい

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#文字列