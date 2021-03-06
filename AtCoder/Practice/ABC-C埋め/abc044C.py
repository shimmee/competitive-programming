# ABC044C - 高橋君とカード
# URL: https://atcoder.jp/contests/arc060/tasks/arc060_a
# 日付: 2020/12/21

# ---------- 思ったこと / 気づいたこと ----------
# n<=50なのでbit全探索は無理
# 「数列からいくつか選んで平均をAにしたい」はDPの典型問題！！
# ググってみた: https://algo-logic.info/how-to-think-cp/
# 「合計値が K × 個数」となる組み合わせ
# 「元の値をすべて-K した数列で、合計値が 0」となる組み合わせ
# 「数列からいくつか選んで0にする」という典型的な部分和問題に帰着できるが
# 和の計算結果が負になることがあるので厄介
# 添字が負数になる場合は添字+baseをして、0をbaseにして使う: https://www.hamayanhamayan.com/entry/2017/02/27/021246

# ------------------- 方針 --------------------
# 数列のリストを，各要素から平均を引いたリストにする
# dp[i][j]: i番目までの数字を使って，総和をjにする場合の数
# i番目の数値を使う時は，
# dpテーブルで持つ総和の種類を-1000から1000くらいにしたいので，base=1000する
# dp[i+1][j]は，dp[i][j-x[i]]の場合の数とdp[i][j]の場合の数の和
# dpの更新の際には各jにbaseを足したものとする (単純に全てのjの部分をj+baseにするだめ)
# 「何も選ばずに0にする」という1通りがダメなので，最後に1引く

# ------------------- 解答 --------------------
#code:python
n, A = map(int, input().split())
x = list(map(int, input().split()))
x = [i-A for i in x]


base = 1000
dp = [[0 for j in range(2100)] for i in range(n+1)]
dp[0][base] = 1


for i in range(n):
    for j in range(-1000, 1000):
        dp[i + 1][base + j] = dp[i][base + j - x[i]] + dp[i][base + j]

print(dp[n][base]-1)

# ------------------ 入力例 -------------------
1 3
3

4 8
7 9 8 9

3 8
6 6 9


8 5
3 6 2 8 7 6 5 9

33 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3


# ----------------- 解答時間 ------------------
# 45分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/arc/060/editorial.pdf
# ここまでちゃんとしたナップザックDPを初見で解くのは初めて！
# 数列から平均Aを引く，という前処理なしだと，3次元のdpテーブルが必要になる (k枚選んで，みたいな次元が増える)

# ----------------- カテゴリ ------------------
#AtCoder #abc
#動的計画法
#ナップザックDP
