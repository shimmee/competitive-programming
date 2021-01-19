# ABC048C - Boxes and Candies
# URL: https://atcoder.jp/contests/abc048/tasks/arc064_a
# 日付: 2020/12/11

# ---------- 思ったこと / 気づいたこと ----------
# 何かしらの手順で貪欲に解く

# ------------------- 方針 --------------------
# 数列aの頭に[0]を加える
# 全てのiについてa[i]+a[i+1]を求めて，xを引くことで，あと何回減らせばいいのかのリスト=bを得る
# bの偶数番目の和と奇数番目の和を比較して，大きい方を出力する (根拠なし)

# ------------------- 解答 --------------------
#code:python
n, x = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a
b = []
for i in range(n):
    b.append(max(a[i]+a[i+1]-x, 0))

sum1 = sum([b[i] for i in range(n) if i%2 == 0])
sum2 = sum([b[i] for i in range(n) if i%2 == 1])

print(max(sum1, sum2))

# 20ケース中4ケースWA: 嘘解法か？
# 両隣を考える必要があるので，iとi+1じゃだめじゃないか？

n, x = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a + [0]
b = []
ans = 0
for i in range(1, n+1):
    if a[i] >= a[i-1] and a[i] > a[i+1]:
        sum_max = max(a[i] + a[i-1], a[i] + a[i+1])
        reduce = max(sum_max-x, 0)
        a[i] -= reduce
        ans += reduce
print(ans)


# 解説見た: https://img.atcoder.jp/arc064/editorial.pdf
# 「a[i] + a[i+1] ≤ x となるように，a の各要素を (非負整数の範囲で) 減らしていきます
# ai + ai+1 > x ならば，ai + ai+1 = x となるまで ai と ai+1 を減らさなければなりませんが，
# このとき ai+1 だけを減らすのが最適であることが分かります」

# 最初の解き方めっちゃ近いやん

n, x = map(int, input().split())
a = list(map(int, input().split()))
a_raw = a[:]
a = [0] + a
b = []

for i in range(n):
    if a[i]+a[i+1] <= x:
        continue
    else:
        a[i+1] -= a[i]+a[i+1]-x
ans = 0
for i in range(n):
    ans += a_raw[i] - a[i+1]
print(ans)

# ------------------ 入力例 -------------------
3 3
2 2 2

6 1
1 6 1 2 0 4

5 9
3 1 4 1 5

2 0
5 5

# ----------------- 解答時間 ------------------
# 1時間かかって解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc064/editorial.pdf
# 非常に惜しかった
# a[i]+a[i+1]-xを計算するところまでは行ってた
# 貪欲なのはわかってても，どうやって貪欲に解けば良いのか思いつかない良問だった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#貪欲法