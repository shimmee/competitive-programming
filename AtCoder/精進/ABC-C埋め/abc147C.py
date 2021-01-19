# ABC147-C: HonestOrUnkind2
# URL: https://atcoder.jp/contests/abc147/tasks/abc147_c
# 日付: 2020/11/19

# ---------- 思ったこと / 気づいたこと ----------
# 親切or不親切でbit全探索して矛盾を見つける
# 不親切だと仮定したら，逆にすると親切になる
# 全員親切だった場合，矛盾が生じなくなる。
# 矛盾が生じないときのときの親切の人数を数えてmax(ans)する


# ------------------- 解答 --------------------
#code:python
n = int(input())

G = []
for i in range(n):
    A = int(input())
    xy = [[int(i) for i in input().split()] for _ in range(A)]
    G.append([A, xy])

ans = 0
for i in range(2**n):
    flag = [-1] * n
    for j in range(n):
        A = G[j][0]
        xy = G[j][1]
        if (i >> j) & 1: # このj番目の人は不親切だとする
            for a in range(A):
                xy[a][1] = 1 - xy[a][1] # 証言をスイッチする

        # 証言を1つずつ拾って，矛盾を見つける。矛盾があったらループを終える
        b = False # flag for breaking loop
        for x, y in xy:
            x -= 1 # 0indexになおす
            if flag[x] == -1:
                flag[x] = y
            elif flag[x] != y:
                b = True
                break

        if b: break
    if not b:
        ninzu = bin(i)[2:].count('0')
        ans = max(ans, ninzu)
print(ans)


# 解答見た: https://atcoder.jp/contests/abc147/submissions/10408073
# 矛盾の判定方法を「flagのx番目に証言入れて，次の証言と矛盾してるかどうか」で判定してたが，
# そもそもiのパターンで正直かどうか決まってるから，それで決めればいい
# 親切を1とした方がよさそう
# ハローさんから「不親切な人は常に嘘をつくわけなじゃない」と教えてもらった。問題を完全に読み間違えてた。

n = int(input())
G = []
for i in range(n):
    A = int(input())
    xy = [[int(i) for i in input().split()] for _ in range(A)]
    G.append([A, xy])

ans = 0
for i in range(2**n): # パターン
    kind = [0] * n
    # 正直な人のラベルを作る
    for j in range(n): # j人目
        if (i >> j) & 1: # このj番目の人は親切だとする: 1の人が親切
            kind[j] = 1

    flag = False  # flag for breaking loop
    for j in range(n):
        if kind[j] == 1: # 親切な人だったら証言を1つずつ確かめる
            xy = G[j][1]
            for x, y in xy:
                x -= 1
                if kind[x] != y:
                    flag = True
                    break
            if flag: break
    if not flag:
        ninzu = bin(i).count('1')
        ans = max(ans, ninzu)
print(ans)


# ------------------ 入力例 -------------------
3
1
2 1
1
1 1
1
2 0


3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0

2
1
2 0
1
1 0



# ----------------- 解答時間 ------------------
# 40分かかって解いて，全3サンプル含めて4ケースだけ正解で，他全部WA
# 1h40m

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc147/editorial.pdf
# 問題を読み間違えてた: 不親切な人は嘘しか吐かないと思ったら，真偽不明の証言だった。
# なので親切な人だけ調べればよかった。

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#bit全探索