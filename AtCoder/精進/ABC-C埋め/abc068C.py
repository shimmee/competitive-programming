# ABC068C - Cat Snuke and a Voyage
# URL: https://atcoder.jp/contests/abc068/tasks/arc079_a
# 日付: 2020/12/15

# ---------- 思ったこと / 気づいたこと ----------
# 1とつながってる島を探す
# 1とつながっている島がNと繋がっていればOK
# ハッシュを用いる

# ------------------- 解答 --------------------
#code:python
n, m= map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(m)]

island_from1 = []
new_ab = [] # 島1以外を出発する便
for a, b in ab:
    if a == 1: # 出発地点が1なら，到着地点のbをキープ
        island_from1.append(b)
    else:
        new_ab.append([a, b])
island_from1 = set(island_from1) # 重複削除

for a, b in new_ab:
    if a in island_from1 and b == n: # 島aが島1とつながっていて，aからnに行けるならOK
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')

# 解説: https://img.atcoder.jp/arc079/editorial.pdf
# 島1とNに共に繋がってる島を見つければいいので
# 各島が繋がってる別の島のリストを作ってもできそう

n, m= map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for l in G:
    if (1 in l) and (n in l):
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')

# ------------------ 入力例 -------------------
3 2
1 2
2 3

4 3
1 2
2 3
3 4

100000 1
1 99999

5 5
1 3
4 5
2 3
2 4
1 4

# ----------------- 解答時間 ------------------
# 10分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc079/editorial.pdf
# 解説の方法が賢くて気持ちいい
# ダイクストラでも解けるっぽいからscipyで練習しようかと思ったけど，scipyのdijkstraが隣接リストを受け取ってくれなくて
# 隣接行列だけ入力として受け取ってくれるから，20万行の2次元配列はつらそうなので諦めた


# ----------------- カテゴリ ------------------
#AtCoder #abc
#グラフ
#単一始点最短経路問題
