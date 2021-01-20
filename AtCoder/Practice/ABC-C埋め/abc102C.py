# ABC102C - Linear Approximation
# URL: https://atcoder.jp/contests/arc100/tasks/arc100_a
# 日付: 2020/12/05

# ---------- 思ったこと / 気づいたこと ----------
# mean absolute errorと同じ感じ
# MAEは予測値がconstantの場合，入力の中央値=constantでMAEが最小になる

# ------------------- 方針 --------------------
# abs(a[i]-i)のリストを作って，そのmedianとする

# ------------------- 解答 --------------------
code:python
    import numpy as np
    n = int(input())
    a = list(map(int, input().split()))
    a_ = [abs(a[i]) -  (i+1) for i in range(n)]
    med = int(np.median(a_))

    def fun(a, b):
        ans = 0
        for i in range(1, len(a)+1):
            ans += abs(a[i-1]-(b+i))
        return ans

    print(fun(a, med))


# ------------------ 入力例 -------------------
5
2 2 3 5 5

9
1 2 3 4 5 6 7 8 9

6
6 5 4 3 2 1

7
1 1 1 1 2 3 4

# ----------------- 解答時間 ------------------
# 24分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc100/editorial.pdf
# 最初三角不等式とかで式変形してたけど，MAEであることに気づいて中央値に辿り着いた


# ----------------- カテゴリ ------------------
#AtCoder #abc
#MAE
#中央値
#median
