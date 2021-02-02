# ABC171D - Replacing
# URL: https://atcoder.jp/contests/abc171/tasks/abc171_d
# Date: 2021/02/01

# ---------- Ideas ----------
# 各数字のカウンターを管理: 10**5
# 最初から和=totalを持っておいて管理
# bの個数分，totalからbが減って，cが増える
# カウンターのbは0になって，cがb個分増える

# ------------------- Solution --------------------
# bが個数分減って，cが個数分増える

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))
count = [0]*(10**5+1)
for i in a:
    count[i] += 1
q = int(input())
total = sum(a)
for _ in range(q):
    b, c = map(int, input().split())
    cnt_b = count[b]
    total = total - b*cnt_b + c*cnt_b
    print(total)
    count[b] = 0
    count[c] += cnt_b

# ------------------ Sample Input -------------------
4
1 2 3 4
3
1 2
3 4
2 4


# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# 解説: https://img.atcoder.jp/abc171/editorial.pdf
# けんちょん: https://drken1215.hatenablog.com/entry/2020/06/21/224900
# けんちょんさんいわく，今回用意したcountみたいな配列をバケットと呼ぶらしい

# ----------------- Category ------------------
#AtCoder
#バケット
#クエリ処理問題
#茶diff
#集計処理
#ABC-D