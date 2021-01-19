# ABC174C - Repsept
# URL: https://atcoder.jp/contests/abc174/tasks/abc174_c
# 日付: 2020/11/21

# ---------- 思ったこと / 気づいたこと ----------
# k桁目は必ずkの倍位数なので，ループはK回回せばいい。つまりO(K)で回る。
# 等比数列の和の公式で表せたので，modと組み合わせてかけそう
# pow使いそう

# ------------------- 解答 --------------------
code:python
    k = int(input())
    if k % 2 == 0:
        print(-1)
        exit()

    def S(n, k):
        return (7/9)*pow(10, n+1, k)-7/9

    for i in range(k):
        if S(i, k) % k == 0:
            print(i+1)
            exit()
            break
    print(-1)

    # 1時間かけて無理だったので
    # 解説見た
    # a[n] = a[1] or 10*a[n-1]+7で表せる

    k = int(input())
    if k % 2 == 0:
        print(-1)
        exit()
    inf = float('INF')
    a = [inf]*(k+1)
    for i in range(1, k+1):
        if i == 1:
            a[i] = 7 % k
        else:
            a[i] = (10*a[i-1]+7) % k

        if a[i] % k == 0:
            print(i)
            exit()
            break
    print(-1)
# ------------------ 入力例 -------------------
3
7
99
101
999983


# ----------------- 解答時間 ------------------
# 1時間以上かかって解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/abc174/editorial/28
# 等差数列の和の公式で考えてしまって，上手く行かないケースがあった。なぜうまく行かないのかよくわかってない。
# 漸化式で考えればよかった。

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#漸化式
