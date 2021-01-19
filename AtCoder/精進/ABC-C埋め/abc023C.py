# ABC023C - 収集王
# URL: https://atcoder.jp/contests/abc023/tasks/abc023_c
# 日付: 2020/12/20

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# まず各列，各行に含まれてるアメの個数を数えてリストを作る: O(R)とO(C)
# 各リストから，アメがp個(p=0~K)含まれてる行数 or 列数を表すリストを作る
# このうち行のリストでループを回して，p個アメが含まれている行がa個あって，対応するように列ではK-p個必要で，それはb個あって，
# そしたらa*bの組み合わせがあることになるので，これをインクリメントする

# この数え方だと，自分がアメのあるマスにいる時に重複して数えたり，取りこぼしてたりする
# 自分がいるマスの行と列のアメの総数がKのとき1除いて，K+1のときは1加える

# ------------------- 解答 --------------------
#code:python
R, C, K = map(int, input().split())
n = int(input())
rc = [[int(i) for i in input().split()] for _ in range(n)]
r = [i[0] for i in rc]
c = [i[1] for i in rc]

cnt_r = [0]*R
cnt_c = [0]*C # インデックスが表す列にあるアメの総数
for i in range(n):
    cnt_r[r[i] - 1] += 1
    cnt_c[c[i] - 1] += 1

value_cnt_c = [0]*(K+1) # インデックスがアメの個数を表し，その中身はそのアメの個数を持つ列数
for i in range(C):
    pos = cnt_c[i]
    if pos <= K:
        value_cnt_c[pos] += 1

value_cnt_r = [0]*(K+1) # インデックスがアメの個数を表し，その中身はそのアメの個数を持つ行数
for i in range(R):
    pos = cnt_r[i]
    if pos <= K:
        value_cnt_r[pos] += 1

ans = 0
for key_r, value_r in enumerate(value_cnt_r):
    rest = K - key_r
    value_c = value_cnt_c[rest]
    ans += value_c*value_r

remove = 0
add = 0
for i in range(n):
    ri = r[i]-1 # アメiのある行番号
    ci = c[i]-1 # アメiのある列番号
    if cnt_r[ri] + cnt_c[ci] == K:
        remove += 1

    # ここまで自力で書いてて，この部分だけ解説AC
    if cnt_r[ri] + cnt_c[ci] == K+1:
        add += 1

print(ans-remove+add)

# ------------------ 入力例 -------------------
3 5 3
5
1 2
2 1
2 5
3 2
3 5

7 3 1
4
3 2
3 3
4 2
4 3

5 5 2
5
1 1
2 2
3 3
4 4
5 5

# ----------------- 解答時間 ------------------
# 2時間+解説AC

# -------------- 解説 / 感想 / 反省 -------------
# めちゃくちゃ惜しいところまで行ってた。90%は解けてた
# 最後の最後のcnt_r[ri] + cnt_c[ci] == K+1なら+1するところだけ抜けてた
# 解説ACだけど復習はしたくない笑

# ----------------- カテゴリ ------------------
#AtCoder #abc
#工夫する全探索
#解説AC

