# ABC137D - Summer Vacation
# URL: https://atcoder.jp/contests/abc137/tasks/abc137_d
# Date: 2021/04/01

# ---------- Ideas ----------
# 貪欲か？
# 報酬を降順にソート，次に受取日を降順にソートして，貪欲に選んでいく -> 嘘貪欲でした

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(n)]
ab = sorted(ab, key=lambda x: (x[1], x[0]), reverse=True)

today = 0
ans = 0
for a, b in ab:
    if a+today <= m:
        ans += b
        today += 1
print(ans)

# 嘘貪欲でした。下の例のとき，答えは5なのに，3になっちゃう
# 2 4
# 3 3
# 4 2

# 赤坂からヒントもらった: 残りあと1日でm日になる，残りあと2日でm日になる，みたいに逆算して考える
# 残りあとi日のとき，i日までの中から最大報酬のものを選ぶ
# 残りi日をループで走査
# まずはa <= iになるような仕事をすべてpriority queに入れる
# その中から最大のものを選んでインクリメント

import heapq
n, m = map(int, input().split())
ab = sorted([[int(i) for i in input().split()] for _ in range(n)])

h = []
heapq.heapify(h)
j = 0
ans = 0
for i in range(1, m+1):
    while j < n and ab[j][0] <= i:
        heapq.heappush(h, -ab[j][1])
        j += 1
    if h:
        max_b = heapq.heappop(h) * (-1) # 最大値を取り出す
        ans += max_b
print(ans)


# ------------------ Sample Input -------------------

3 4
4 3
4 1
2 2

5 3
1 2
1 3
1 4
2 1
2 3

# ----------------- Length of time ------------------
# 1時間くらい考えて解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc137/editorial.pdf
# 嘘貪欲にハマってしまった
# 逆から考える かつheapを使うという2段階の考察が必要な問題だった
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/12/29/195900

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#後ろから考える
#後ろから考える
#水色diff
#Greedy
#貪欲
#嘘貪欲
#priority_queue
#heap
#データ構造
#端から順に決まって行くGreedy
#探索順序を工夫して解く
#マトロイド
#ヒープ
#優先度付きキュー