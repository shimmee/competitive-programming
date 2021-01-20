########################################################################################
# レッドコーダーが教える、競プロ・AtCoder上達のガイドライン: 初中級者が解くべき過去問精選 100 問
# https://qiita.com/e869120/items/eb50fdaece12be418faa#2-3-%E5%88%86%E9%87%8E%E5%88%A5%E5%88%9D%E4%B8%AD%E7%B4%9A%E8%80%85%E3%81%8C%E8%A7%A3%E3%81%8F%E3%81%B9%E3%81%8D%E9%81%8E%E5%8E%BB%E5%95%8F%E7%B2%BE%E9%81%B8-100-%E5%95%8F
########################################################################################


# テンプレ

##############################################################
# 問目
# カテゴリ:
# タイトル:
# URL:
# 日時: 2020/
##############################################################

def getN(): return int(input())
def getLI(): return list(map(int,input().split()))
def getX(n): return [int(input()) for i in range(n)]
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

def get_dist(x1, x2, y1, y2):
    import math
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


##############################################################
# 1問目
# カテゴリ: 全探索：全列挙
# タイトル: ITP1_7_B - How Many Ways?
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
# 日時: 2020/
##############################################################

import numpy as np
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break

    count = 0
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            for c in range(b+1, n+1):
                if a+b+c == x:
                    count += 1
    print(count)

# rangeの設定が紛らわしい
# 1からnの整数をループで回すならrange(1, n+1)


##############################################################
# 2問目
# カテゴリ: 全探索：全列挙
# タイトル: AtCoder Beginner Contest 106 B - 105
# URL: https://atcoder.jp/contests/abc106/tasks/abc106_b
# 日時: 2020/10/09
##############################################################

# 素因数分解
# 参考: https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(25)

N = int(input())
N_list = [i for i in range(1, N+1) if i%2 == 1]
count = 0
for n in N_list:
    factor_list = factorization(n)
    num_divisor = 1
    for factor in factor_list:
        num_divisor *= (factor[1]+1)
    if num_divisor == 8:
        count += 1
print(count)

# 先に奇数のリストを作ったほうが吉。全整数をループで回すと，Nが多い時偶数が無駄になる。
# 約数の個数を数える方法，ループ回さずにもっと良いのありそう。


##############################################################
# 3問目
# カテゴリ: 全探索：全列挙
# タイトル: AtCoder Beginner Contest 122 B - ATCoder
# URL: https://atcoder.jp/contests/abc122/tasks/abc122_b
# 日時: 2020/10/09
##############################################################
S = input()
length = 0
for i in range(0, len(S)+1):
    for j in range(i, len(S)+1):
        T = S[i:j]
        if T.replace('A', '').replace('C', '').replace('G', '').replace('T', '') == '':
            if len(T) > length:
                length = len(T)
print(length)

# "ACGT"以外の文字を含まない，の判定は文字の置き換えが最適なのか？


##############################################################
# 4問目
# カテゴリ: 全探索：全列挙
# タイトル: パ研杯2019 C - カラオケ
# URL: https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
# 日時: 2020/10/09
##############################################################
import numpy as np
n, m = map(int, input().split())
A = [list(map(int, input().split())) for l in range(n)]
A = np.array(A)

max_point = 0
for i in range(0, m):
    for j in range(i+1, m):
        point = np.maximum(A[:, i], A[:, j]).sum()
        if point > max_point:
            max_point = point
print(max_point)

# 最後の部分はmax_point = max(max_point, point)の方が綺麗だけどifの方が速いらしい
# import numpy入れるの忘れずに


##############################################################
# 5問目
# カテゴリ: 全探索：工夫して通り数を減らす全列挙
# タイトル: AtCoder Beginner Contest 095 C - Half and Half
# URL: https://atcoder.jp/contests/abc095/tasks/arc096_a
# 日時: 2020/10/09
##############################################################
import math
A, B, C, X, Y = list(map(int,input().split()))

min_p = 100000000000000
for c in range(0, max(X, Y)*2+1):
    a = X - int(c / 2)
    b = Y - int(c / 2)

    if a < 0:
        a = 0
    if b < 0:
        b = 0

    p = A*a+B*b+C*c
    min_p = min(min_p, p)
print(min_p)

# O(N^2)をO(N)にする典型的な全探索
# AとBでループを回したら回したらTLEになる
# aとbが負の場合に0とする処理が必要


##############################################################
# 6問目
# カテゴリ: 全探索：工夫して通り数を減らす全列挙
# タイトル: 三井住友信託銀行プログラミングコンテスト 2019 D - Lucky PIN
# URL: https://atcoder.jp/contests/abc095/tasks/arc096_a
# 日時: 2020/10/09
##############################################################
import itertools

N = int(input())
S = input()

all_pattern = [f'{i}{j}{k}' for i,j,k in itertools.product(range(0,10), range(0,10), range(0,10))]
count = 0
for pattern in all_pattern:
    if S.find(pattern[0]) >= 0:
        S1 = S[S.find(pattern[0])+1:]
        if S1.find(pattern[1]) >= 0:
            S2 = S1[S1.find(pattern[1])+1:]
            if S2.find(pattern[2]) >= 0:
                count += 1
print(count)

# 良問!!
# 「Sの桁数分のループを回す」という発想を逆転して，「1000パターンしかないんだからそれで終わるじゃん」という発想
# ループの中身が汚いからもう少し綺麗になりそうだけど，まあいいや


##############################################################
# 7問目
# カテゴリ: 全探索：工夫して通り数を減らす全列挙
# タイトル: JOI 2007 本選 3 - 最古の遺跡
# URL: https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c
# 日時: 2020/10/09
##############################################################

# 方針
# 2重のループで正方形の2点を選ぶ
# 2点が決まれば正方形を作るために必要な他の2点の座標が決まるので，これをget_other_coord関数で得る
# なお，正方形の作り方は辺対称の2パターンあるので，どちらで正方形を作れてもよい。

n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
coord = {i: [x[i], y[i]] for i in range(n)}

def area(i, j): return (coord.get(i)[0]-coord.get(j)[0])**2 + (coord.get(i)[1]-coord.get(j)[1])**2

def get_other_coord(i, j):
    x_i = coord.get(i)[0]
    x_j = coord.get(j)[0]
    y_i = coord.get(i)[1]
    y_j = coord.get(j)[1]

    x_k1 = x_i - (y_j - y_i)
    y_k1 = y_i + (x_j - x_i)
    x_l1 = x_j - (y_j - y_i)
    y_l1 = y_j + (x_j - x_i)

    x_k2 = x_i + (y_j - y_i)
    y_k2 = y_i - (x_j - x_i)
    x_l2 = x_j + (y_j - y_i)
    y_l2 = y_j - (x_j - x_i)

    return [[x_k1, y_k1], [x_l1, y_l1], [x_k2, y_k2], [x_l2, y_l2]]

max_area = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        k1, l1, k2, l2 = get_other_coord(i, j)
        if (k1 in coord.values() and l1 in coord.values()) or (k2 in coord.values() and l2 in coord.values()):
            max_area =  max(max_area, area(i, j))
print(max_area)


# たぶんこれで合ってるけど，TLEになる。高速化するためにPypy3が必要
# k1 in coord.values()の検索の部分をlistにしてるとO(N)だが，辞書のおかげでO(1)になってるはず。
# C++の解答のブログを見てみると，同じ方だったので，もうOK: https://tech-kyopro.com/joi-2007-3-c

##############################################################
# 8問目
# カテゴリ: 全探索：工夫して通り数を減らす全列挙
# タイトル: Square869120Contest #6 B - AtCoder Markets
# URL: https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
# 日時: 2020/10/09
##############################################################

# 方針
# 図示して見た感じ，Aの中央値を入り口，Bの中央値を出口とするのが良さそう
# 各iの歩く距離は(入り口からAまで)+(AからBまで)+(Bから出口まで)

import numpy as np

n = int(input())
AB = [map(int, input().split()) for _ in range(n)]
A, B = [list(i) for i in zip(*AB)]
A = np.array(A)
B = np.array(B)
ENTER = int(np.median(A))
EXIT = int(np.median(B))

ENTER_to_A = abs(ENTER-A)
A_to_B = abs(A-B)
B_to_EXIT = abs(B-EXIT)

total = (ENTER_to_A + A_to_B + B_to_EXIT).sum()
print(total)

# サンプル問題と答えがなかったら中央値のアイデアは思いつかなかった。
# なぜ中央値で本当に常に最適なのか，解けた今でも半信半疑
# 雑に書けば1行で書けた。


##############################################################
# 9問目
# カテゴリ: 全探索：工夫して通り数を減らす全列挙
# タイトル: JOI 2008 予選 4 - 星座探し
# URL: https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
# 日時: 2020/10/09
##############################################################

# 方針
# 目的の星座において1点星を固定し，他の星との関係性(xとyがいくつ動くか)をメモる: move_x, move_y
# 写真の星すべてをループで回して，それぞれに対してmove_x, move_yした点が，写真の中にあるかどうかを判定する
# これでO(N)

import numpy as np
m = int(input())
xy = [map(int, input().split()) for _ in range(m)]
x, y = [list(i) for i in zip(*xy)]
x, y = np.array(x), np.array(y)
x0, y0 = x[0], y[0]
move_x = x-x0
move_y = y-y0

n = int(input())
x_y_ = [map(int, input().split()) for _ in range(n)]
x_, y_ = [list(i) for i in zip(*x_y_)]
x_, y_ = np.array(x_), np.array(y_)
coord = {k: [x_[k], y_[k]] for k in range(len(x_))}
for i in range(len(x_)):
    x_moved = x_[i] + move_x
    y_moved = y_[i] + move_y

    count = 0
    for j in range(len(x_moved)):
        if [x_moved[j], y_moved[j]] in coord.values():
            count += 1
    if count == len(x_moved):
        print(x_[i]-x0, y_[i]-y0)

# 発想を思いついてもあんまりおもしろくなかった



##############################################################
# 10問目:
# カテゴリ: 全探索：ビット全探索
# タイトル: ALDS_5_A - 総当たり
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
# 日時: 2020/10/10
##############################################################
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
M = list(map(int,input().split()))

flag = [False]*2000
for i in range(2**N):
    total = 0
    for j in range(N):
        if (i >> j) & 1:
            total += A[j]
    flag[total] = True

for m in M:
    if flag[m]:
        print('yes')
    else: print('no')

# 始めてのbit探索: (i >> j) & 1がポイント
# 最初Mのループも加えて3重ループで回していたが，TLEになった。
# Falseで埋め尽くしたリスト(flag)の各総計(total)番目にTrueを入れるアイデアを解答から頂いた
# 参考: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3979304#1

##############################################################
# 11問目
# カテゴリ: 全探索：ビット全探索
# タイトル: AtCoder Beginner Contest 128 C - Switches
# URL: https://atcoder.jp/contests/abc128/tasks/abc128_c
# 日時: 2020/10/10
##############################################################

# 方針
# bit全探索で，スイッチのオンオフを全パターン試す
# Mでもループを回して，各電球がついてるかどうかチェック
# スイッチのパターン1つごとに，全電球がついてればincrement

# 入力が複雑なので，とりあえず1行ずつリストに格納
all_input=[]
while True:
    try:
        all_input.append(list(map(int, input().split())))
    except:
        break;

N, M = all_input[0][0], all_input[0][1]
p = all_input[-1]
all_input.pop(0), all_input.pop(-1)
switch = [all_input[i][1:] for i in range(M)]
num_switch = [all_input[i][0] for i in range(M)]

all_on = 0
for i in range(2**N):
    num_light_on = 0 # M個の電球のうち，点灯するものの個数をincrementする
    for m in range(M):
        switch_on = 0
        for j in range(N):
            if (i >> j) & 1:
                if j+1 in switch[m]:
                    switch_on += 1
        if switch_on % 2 == p[m]:
            num_light_on += 1
    if num_light_on == M:
        all_on += 1
print(all_on)


# これまでで一番頭使った。
# if j+1 in switch[m]の部分が重要で，jは0から始まるけど，switchの場所は1から始まるから，jに1足す必要がある。


##############################################################
# 12問目
# カテゴリ: 全探索：ビット全探索
# タイトル: AtCoder Beginner Contest 002 D - 派閥
# URL: https://atcoder.jp/contests/abc002/tasks/abc002_4
# 日時: 2020/10/10
##############################################################

# 方針
# 各個人がグループに入るか入らないかのbit全探索を行う
# 各グループ(パターンi)において，そこに含まれる各個人が関係を持ってるかどうか調べる
# 全員がお互いに関係を持ってたらOKなので，最大派閥の人数を更新する

all_input=[]
while True:
    try:
        all_input.append(list(map(int, input().split())))
    except:
        break;
if len(all_input) == 1:
    print(1)
else:
    N, M = all_input[0][0], all_input[0][1]
    all_input.pop(0)
    relat = all_input

    max_group = 0
    for i in range(2 ** N):
        group = []
        for j in range(N):
            if (i >> j) & 1:
                group.append(j + 1)
        if len(group) == 0 or len(group) == 1:
            max_group = max(max_group, len(group))
        else:
            count = 0
            for k in range(len(group)):
                for l in range(k + 1, len(group)):
                    if [group[k], group[l]] in relat:
                        count += 1
            if count == int(len(group) * (len(group) - 1) / 2):
                if len(group) > max_group:
                    max_group = len(group)
    print(max_group)

# 11問目の電球をやったおかげで，11問目よりはスラスラ書けた。
# 関係性が1つもない場合の例外処理を忘れると，REがつく



##############################################################
# 13問目
# カテゴリ: 全探索：ビット全探索
# タイトル: JOI 2008 予選 5 - おせんべい
# URL: https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
# 日時: 2020/10/10
##############################################################

# 目的: 0をたくさん増やしたい

# 方針
# 行が最大10なので，行をひっくり返すかひっくり返さないかの2^10でbit全探索
# 行をひっくり返したあとは，各列について見ていって，列のsumがR-sumより小さければ列を引っくり返す
# この各列に見る作業をループで回すと間に合わなさそう

# 適当に提出した感じ，O(C*R*2^R)はTLEで，O(R*2^R)ならいけそうだった

import numpy as np
R, C = map(int, input().split())
A = np.array([list(map(int, input().split())) for l in range(R)])

max_cookie = 0
for i in range(2**R):
    A_ = A.copy()
    for j in range(R):
        if (i >> j) & 1:
            A_[j] = [A_[j][k] ^ 1 for k in range(C)]
    A_ = np.array(A_)
    for l in range(C):
        col_sum = A_.sum(axis=0)
        num_cookie = np.maximum(R - col_sum, col_sum).sum()
        if num_cookie > max_cookie:
            max_cookie = num_cookie
print(max_cookie)


# 初見でこれ(上)書いた。これだとTLE
# 行列計算で済むのにいちいち要素ごとの計算をしたり，無駄な処理が多く，そのせいでO(C*R*2^R)くらいになってる


# 模範解答
# https://qiita.com/rudorufu1981/items/74d5f37c26c62fc7a27f
import numpy as np
R, C = map(int, input().split())
A = np.array([list(map(int, input().split())) for l in range(R)])

ans = 0
for i in range(2**R):
    bit = np.array([[i>>j & 1 for j in range(R)]]).T
    col_sum = (A^bit).sum(axis=0)
    num_cookie = np.maximum(R - col_sum, col_sum).sum()
    if num_cookie > ans:
        ans = num_cookie
print(ans)

# ポイントはCをループで回さずに，numpyの行列の計算とXOR(排他的論理和 ^)を使ってる点
# O(R*2^R)で解ける

# 今までの問題で一番良問だった


##############################################################
# 14問目
# カテゴリ: 全探索：ビット全探索
# タイトル: Square869120Contest #4 B - Buildings are Colorful!
# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b
# 日時: 2020/10/12
##############################################################

# 方針
# それぞれの建物の高さを見えるようにするかで0/1でbit全探索
# 各パターン取得ののち，O(N)のループでhighestの更新とコストの追加を行う
# 一番手前の建物は高くする必要がないので，O(N*2^(N-1))で解ける

def getN(): return int(input())
def getLI(): return list(map(int,input().split()))
N, K = getLI()
A = getLI()

ans = 10000000000000
for i in range(2**(N-1)):
    if bin(i).count('1') < K-1:
        continue
    bit = [i >> j & 1 for j in range(N - 1)]
    bit.insert(0, 1)
    highest = A[0]
    cost = 0
    for k in range(N-1):
        if bit[k+1] == 1:
            if highest >= A[k+1]: # k番目の建物がhighest以下だったら，高くする分のコスト追加して，highestを更新
                cost += highest-A[k+1]+1
                highest = highest + 1
            else: # k番目の建物がhighestより高かったらhighestを更新
                highest = A[k+1]
        elif highest < A[k+1]: #選んでないビルでも，highestを更新 (ここ注意！)
            highest = A[k+1]
    ans = min(ans, cost)
print(ans)

# アイデアを思いつくまでに今までで一番時間かかったけど，面白かった

##############################################################
# 15問目
# カテゴリ: 全探索：順列全探索
# タイトル: AtCoder Beginner Contest 145 C - Average Length
# https://atcoder.jp/contests/abc145/tasks/abc145_c
# 日時: 2020/10/13
##############################################################
def getN(): return int(input())
def getLI(): return list(map(int,input().split()))
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

import numpy as np
N = getN()
x, y = getXY(N)

# 各点同士の距離を総当りで計算してN*Nの行列に詰め込む
dist = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        dist[i, j] = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
print(dist.sum(axis=1).mean())

# itertools.permutationが必要かと思ったけどいらなかった
# 適当に解けたので順列全探索については学べてない涙


##############################################################
# 16問目
# カテゴリ: 全探索：順列全探索
# タイトル: AtCoder Beginner Contest 150 C - Count Order
# https://atcoder.jp/contests/abc150/tasks/abc150_c
# 日時: 2020/10/13
##############################################################

# itertoolsのpermutationは辞書順に順列を並べてくれてるから，PとQのインデックス(場所)を出せばいいだけ

def getN(): return int(input())
def getLI(): return list(map(int,input().split()))

N = getN()
P = tuple(getLI())
Q = tuple(getLI())

from itertools import permutations
pattern = list(permutations([i+1 for i in range(N)]))
print(abs(pattern.index(P)-pattern.index(Q)))

# 他人の解答も全く同じだった: https://nashidos.hatenablog.com/entry/2020/05/24/175618

##############################################################
# 17問目
# カテゴリ: 全探索：順列全探索
# タイトル: ALDS_13_A - 8 クイーン問題
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja
# 日時: 2020/10/13
##############################################################

# 方針
import numpy as np
from itertools import permutations

def getN(): return int(input())
def getLI(): return list(map(int,input().split()))
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

k = getN()
r, c = getXY(k)

def update_board(board, x, y):
    board[x, :] = np.where(board[x, :] == '-', '.', board[x, :]) # 行方向にドットを埋める
    board[:, y] = np.where(board[:, y] == '-', '.', board[:, y]) # 行方向にドットを埋める
    a = min(x, y)
    for i in range(10):
        try:
            if x - a + i >= 0 and  y - a + i >= 0:
                board[x - a + i, y - a + i] = np.where(board[x - a + i, y - a + i] == '-', '.', board[x - a + i, y - a + i])
        except:
            pass
        try:
            if x - a + i >= 0 and y + a - i >= 0:
                board[x - a + i, y + a - i] = np.where(board[x - a + i, y + a - i] == '-', '.', board[x - a + i, y + a - i])
        except:
            pass
    return board

start = np.full((8, 8), '-')
for i in range(k):
    start[r[i], c[i]] = 'Q'
    start = update_board(start, r[i], c[i])

# 順列全探索を列(y)について行う
all_pattern = list(permutations([i for i in range(8)]))
for pattern in all_pattern:
    board = start.copy()
    for j in range(8):
        if board[j, pattern[j]] == 'Q':
            continue
        if board[j, pattern[j]] == '.':
            break
        if board[j, pattern[j]] == '-':
            board[j, pattern[j]]  = 'Q'
        board = update_board(board, j, pattern[j])
    if (board == 'Q').sum() == 8:
        break

for i in range(8):
    ans = ''
    for j in range(8):
        ans += str(board[i, j])
    print(ans)

# AIZU ONLINE JUDGEがnumpyを受け付けてなかった!!!

##############################################################
# 18問目
# カテゴリ: 二分探索
# タイトル: ALDS_4_B - 二分探索
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
# 日時: 2020/10/31
##############################################################

# 方針
# Tの要素をループで回して，1つ1つがSに含まれるかどうかをかどうかを二分探索でサーチ

def getN(): return int(input())
def getLI(): return list(map(int,input().split()))

n = getN()
S = getLI()
q = getN()
T = getLI()

ans = 0
for t in T:
    ok = n
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if S[mid] == t:
            ans += 1
            break
        if S[mid] > t:
            ok = mid
        else: ng = mid
print(ans)

# 一番シンプルな二分探索！ アルゴリズム本を読めば余裕


##############################################################
# 19問目
# カテゴリ: 二分探索
# タイトル: JOI 2009 本選 2 - ピザ
# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b
# 日時: 2020/10/31
##############################################################

# 方針
# kをループで回して，各宅配先に対して最も近い店舗の距離を知りたい
# 単純に宅配先と全店舗の距離を測る線形探索でとりあえずやってみる
# 反時計回りでもOKであることに注意

def getX(n): return [int(input()) for i in range(n)]

d = int(input())
n = int(input())
m = int(input())
di = getX(n-1)
k = getX(m)
di.append(0)
di.sort()

import numpy as np
di = np.array(di)
ans = 0
for j in range(m):
    d1 = min(abs(di - k[j]))
    d2 = min(abs(di+d - k[j]))
    ans += min(d1, d2)
print(ans)

# 多分答えはあってるんだけど，TLE
# nが10万，mが1万なので，ループの中でかなり回ってて，O(nm)になってる
# たぶんdi-k[j]の部分を二分探索する必要がある

def getX(n): return [int(input()) for i in range(n)]

d = int(input())
n = int(input())
m = int(input())
di = getX(n-1)
k = getX(m)
di.append(0)
di.append(d)
di.sort()

import math

ans = 0
for j in range(m):
    left = 0
    right = len(di)-1
    min_d = 10**10
    for _ in range(math.ceil(math.log2(n))):
        mid = (left + right) // 2
        if k[j] > di[mid]:
            left = mid
        else: right = mid
        min_d = min(min_d, abs(di[left] - k[j]), abs(di[right] - k[j]))
    ans += min_d
print(ans)

# dをdiにappendすれば反時計回りの計算がそのままできるから楽
# rightかleftかよくわからんので，とりあえず小さくなる方を探してキープする戦略でAC (コードが汚い)
# 二分探索でピッタリ探すのではなく，近くを探すというのは初めてだったから時間がかかった


##############################################################
# 20問目
# カテゴリ: 二分探索
# タイトル: ABC 077 - C: Snuke Festival
# https://atcoder.jp/contests/abc077/tasks/arc084_a
# 日時: 2020/10/29
##############################################################
import bisect
def getN(): return int(input())
def getLI(): return list(map(int,input().split()))

n = getN()
a = sorted(getLI())
b = sorted(getLI())
c = sorted(getLI())

ans = 0
for i in range(n):
    b_idx = bisect.bisect_right(b, a[i])
    b_ = b[b_idx:]
    for j in range(len(b_)):
        c_idx = bisect.bisect_right(c, b_[j])
        ans += len(c[c_idx:])
print(ans)

# これだとO((NlogN)^2)になって間に合わない
# 発想を転換してjを固定する
# bisectだと境界を含んで上手く行かないので，自分で書く

import bisect
def getN(): return int(input())
def getLI(): return list(map(int,input().split()))

n = getN()
a = sorted(getLI())
b = sorted(getLI())
c = sorted(getLI())

# OKが右側の場合
def is_ok_right(arg):
    return b[j] < c[arg]
def bisect_right(ok, ng):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok_right(mid):
            ok = mid
        else: ng = mid
    return ok

# OKが左側の場合
def is_ok_left(arg):
    return b[j] > a[arg]
def bisect_left(ok, ng):
    while (abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if is_ok_left(mid):
            ok = mid
        else: ng = mid
    return ok

ans = 0
for j in range(n):

    c_idx = bisect_right(n, -1)
    a_idx = bisect_left(-1, n)
    ans += (a_idx+1) * (n-c_idx)
print(ans)

# 模範解答見ると，もっと短く書けたっぽい


##############################################################
# 21問目
# カテゴリ: 二分探索
# タイトル: 射撃王: ABC 023 - D
# https://atcoder.jp/contests/abc023/tasks/abc023_d
# 日時: 2020/10/28
##############################################################

# 初見じゃ絶対思いつかない

def getN(): return int(input())
def getLI(): return list(map(int,input().split()))
def getX(n): return [int(input()) for i in range(n)]
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

n = getN()
h, s = getXY(n)

# 解説: https://www.slideshare.net/chokudai/abc023
# 超えてはならない高さxが決まっている時，(x-h_i)/s_iで「風船iにあと何秒猶予があるか」がわかる: ここは自力で思いつく必要がある
# そこまでわかれば，猶予の短い順に割っていけばいい: これは貪欲法
# もし割れない風船があったら，そのxはクリアできないことになるので，もう少し高さが必要になる。
# このxを小さい順にまわしていって，初めてクリアしたらそれがスコアになる。 とりあえずこの貪欲法で書いてみる

for x in range(200000):
    t = [0]*n
    for i in range(n):
        if x < h[i]:
            break
        else:
            t[i] = (x - h[i])/s[i]
    if x < h[i]:
        continue
    t.sort()
    if min([t[i] - i for i in range(n)]) >= 0:
        print(x)
        break
    else: continue


# この解法はxの線形探索になっており，非常に効率が悪い。
# 問題をクリアするための最小のxを探す，という課題は，まさに二分探索が得意とする対象なので，上手く使う。
# ある境界M以上のxであればクリアできるが，M未満のxのときクリアできない，そんなMを二分探索で探したい。
# 以下は本のC++の解答をpython用に翻訳したもの
# 美しすぎて涙がでそう

def getN(): return int(input())
def getLI(): return list(map(int,input().split()))
def getX(n): return [int(input()) for i in range(n)]
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

n = getN()
h, s = getXY(n)

inf = 10**20
left = 0
right = inf

while right - left > 1:
    mid = int((left + right)/2) # 二分探索に必要な真ん中を取る。各風船がこのmidをクリアできるかどうかを知りたい
    ok = True
    t = [0]*n # 各iに何秒猶予があるか

    for i in range(n):
        if mid < h[i]: ok = False # そもそもh_iが初期地点でmidより小さかったらダメ
        else: t[i] = (mid - h[i])/s[i]

    t = sorted(t) # 猶予時間の少ない順にならべる。i秒かけてもプラスであれば，クリアできることになる
    for i in range(n):
        if t[i] < i: ok = False

    if ok: right = mid # 全風船がクリアできるので，小さい側に範囲を狭める
    else: left = mid # クリアできない風船があったので，余裕をもたせる。
print(int(right))



##############################################################
# 22問目
# カテゴリ: 二分探索
# タイトル: AtCoder Regular Contest 054 B - ムーアの法則
# https://atcoder.jp/contests/arc054/tasks/arc054_b
# 日時: 2020/10/31
##############################################################

# 関数の最小値を答える問題
# 解析的に微分して解いてみた

from math import log, log2
p = float(input())
def fun(p):
    return 3.0/2.0*log2(2.0/3.0*p*log(2))

x = fun(p)
if x >= 0:
    print(x + p*2**(-2*x/3))
else :
    print(p)

# 本当は三分探索ってのをやるらしい

##############################################################
# 23問目
# カテゴリ: 二分探索
# タイトル: JOI 2007/2008 本選 問題3 - ダーツ
# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
# 日時: 2020/10/30
##############################################################

# 方針
# N=1000なので4重ループは絶対ムリ
# 1. 数列pに0をappend (数字を選ばない選択肢もあるので)
# 2. pをソート
# 3. pの任意の2つの要素の和のリストを作成 = p2
# 4. このリストの要素を2つ組み合わせてmに近づければいいので，m-p2要素で二分探索 (bisect)

import bisect
def getLI(): return list(map(int,input().split()))
def getX(n): return [int(input()) for _ in range(n)]

n, m = getLI()
p = getX(n)
p.append(0)
n = len(p)

p2 = [0]*(len(p)**2)
k=0
for i in range(n):
    for j in range(i, n):
        p2[k] = p[i] + p[j]
        k +=1

p2.sort()

ans = 0
for i in p2:
    if i <= m:
        gap = m-i
        idx = max(0, bisect.bisect_right(p2, gap)-1)
        ans = max(ans, i + p2[idx])
print(ans)

# 最初，下みたいな感じでp2のリストを作る祭にsetを使ったらMLE (メモリオーバー)になった
# 模範解答を参考にループで単純なリストを作ったら通った　(重複してるけど)

from itertools import product
p2 = sorted(list(set([i + j for i,j in product(p, p)])))

# Pypyでは通らないけどPythonでは通るという謎の問題だった
# 思いついた解答が公式の想定解答と同じで嬉しかった
# https://www.ioi-jp.org/joi/2007/2008-ho-prob_and_sol/2008-ho-review.pdf


##############################################################
# 24問目
# カテゴリ: 深さ優先探索 (DFS)
# タイトル: ALDS_11_B - 深さ優先探索
# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
# 日時: 2020/11/01
##############################################################

n = int(input())
G = [None]*(n+1)
for _ in range(n):
    v, k, *e = list(map(int,input().split()))
    G[v] = e

d = [-1]*(n+1) # 発見時間
f = [-1]*(n+1) # 完了時間
now = 1

seen = [False] * (n + 1)  # seenとtodoを初期化

# dfs関数: 頂点vからたどることのできる頂点のうち，まだ訪問していない頂点を全て訪問する
def dfs(v, now):
    d[v] = now
    now += 1
    seen[v] = True # vを訪問済みにする
    for w in G[v]: # vに隣接する頂点wを1つずつ巡る
        if seen[w]: # seen[w]がTrueであれば何もしない
            continue
        now = dfs(w, now) # 再帰的に探索
    f[v] = now
    return now + 1

for v in range(1, n+1):
    if seen[v]: # もしcが訪問済みなら探索しない
        continue
    now = dfs(v, now)

for i in range(1, n+1):
    print(i, d[i], f[i])


##############################################################
# 25問目
# カテゴリ: 深さ優先探索 (DFS)
# タイトル: AOJ 1160 - 島はいくつある？
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp
# 日時: 2020/11/02
##############################################################
import sys
sys.setrecursionlimit(10**7)

def getNest(n):
    nested = [[int(i) for i in input().split()] for _ in range(n)]
    return nested

# dfs関数: 頂点vからたどることのできる頂点のうち，まだ訪問していない頂点を全て訪問する
def dfs(vi, vj):
    seen[vi][vj] = True # vを訪問済みにする
    for wi, wj in G[vi][vj]: # vに隣接する頂点wを1つずつ巡る
        if seen[wi][wj]: # seen[w]がTrueであれば何もしない
            continue
        dfs(wi, wj) # 再帰的に探索


while True:
    w, h = list(map(int, input().split()))
    if w == h == 0:
        break
    c = getNest(h)

    seen = [[False]*w for _ in range(h)]

    # 各マスが隣り合う8方向に陸を持っているかどうかのグラフを作る
    G = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            G[i][j] = []
            if c[i][j] == 1:
                if i > 0 and j > 0 and c[i-1][j-1] == 1: # 左上のマス
                    G[i][j].append([i-1, j-1])
                if i > 0 and c[i-1][j] == 1: # 上のマス
                    G[i][j].append([i-1, j])
                if i > 0 and j < w-1 and c[i-1][j+1] == 1: # 右上のマス
                    G[i][j].append([i-1, j+1])
                if j < w - 1 and c[i][j + 1] == 1:  # 右のマス
                    G[i][j].append([i, j + 1])
                if i < h-1 and j < w-1 and c[i+1][j+1] == 1: # 右下のマス
                    G[i][j].append([i+1, j+1])
                if i < h-1 and c[i+1][j] == 1: # 下のマス
                    G[i][j].append([i+1, j])
                if i < h-1 and j > 0 and c[i+1][j-1] == 1: # 左下のマス
                    G[i][j].append([i+1, j-1])
                if j > 0 and c[i][j-1] == 1: # 左のマス
                    G[i][j].append([i, j-1])

    # すべてのマスに対してdfs関数を使う
    ans = 0
    for vi in range(h):
        for vj in range(w):
            if seen[vi][vj]: # もしcが訪問済みなら探索しない
                continue
            else:
                if c[vi][vj] == 1: ans += 1
                dfs(vi, vj)
    print(ans)

# これだとRuntime Errorになる。もしかすると，Gが大きすぎるのかもしれない -> 再帰の回数限界突破の呪文入れたら通った！
# 解答を参考に，Gを準備するのではなくて座標のmoveで表現してみる
import sys
sys.setrecursionlimit(10**7)

def getNest(n):
    nested = [[int(i) for i in input().split()] for _ in range(n)]
    return nested

# 8方向の移動の座標を準備
x_move = [-1, 0, 1, 1, 1, 0, -1, -1]
y_move = [1, 1, 1, 0, -1, -1, -1, 0]

# dfs関数: 頂点vからたどることのできる頂点のうち，まだ訪問していない頂点を全て訪問する
def dfs(vi, vj):
    seen[vi][vj] = True # vを訪問済みにする

    for x, y in zip(x_move, y_move): # vに隣接する頂点wを1つずつ巡る
        wi = vi + x
        wj = vj + y
        if 0 <= wi < h and 0 <= wj < w:
            if seen[wi][wj]: # seen[w]がTrueであれば何もしない
                continue
            elif c[wi][wj] == 1: # 隣のマスが陸(1)だったら更に探索を進める
                dfs(wi, wj) # 再帰的に探索


# すべてのマスに対してdfs関数を使う
while True:
    w, h = list(map(int, input().split()))
    if w == h == 0:
        break
    c = getNest(h)
    seen = [[False]*w for _ in range(h)]
    ans = 0
    for vi in range(h):
        for vj in range(w):
            if seen[vi][vj]: # もしcが訪問済みなら探索しない
                continue
            else:
                if c[vi][vj] == 1:
                    ans += 1
                    dfs(vi, vj)
    print(ans)

# AC!!!!!!!!


##############################################################
# 26問目
# カテゴリ: 深さ優先探索 (DFS)
# タイトル: # AtCoder Beginner Contest 138 D - Ki　
# https://atcoder.jp/contests/abc138/tasks/abc138_d
# 日時: 2020/11/03
##############################################################
import sys
sys.setrecursionlimit(10**7)
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

n, q = map(int, input().split())
a, b = getXY(n-1)
p, x = getXY(q)

# prepare graph
G = [[]*1 for _ in range(n+1)]
for i in range(n-1):
    G[a[i]].append(b[i])

counter = [0]*(n+1)

# dfs関数: 頂点vからたどることのできる頂点のうち，まだ訪問していない頂点を全て訪問する
def dfs(v):
    counter[v] += c
    for w in G[v]: # vに隣接する頂点wを1つずつ巡る
        if w != []:
            dfs(w) # 再帰的に探索

# すべての頂点に対してdfs関数を使う
for i in range(len(p)):
    v = p[i]
    c = x[i]
    dfs(v)
counter.pop(0)

for count in counter:
    print(count, end=" ")

################################################################
# これだとなぜかTLEとWAがでるので，キューを使って書き直してみる
################################################################
import sys
from collections import deque
sys.setrecursionlimit(10**7)
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

n, q = map(int, input().split())
a, b = getXY(n-1)
p, x = getXY(q)

# prepare graph
G = [[]*1 for _ in range(n+1)]
for i in range(n-1):
    G[a[i]].append(b[i])

counter = [0]*(n+1)

# todoを初期化
todo = deque([])

# todoが空になるまで繰り返す: dequeがemptyであればboolがFalseになるので，これを利用してPythonicに書く
for i in range(len(p)):
    todo.appendleft(p[i])
    add = x[i]
    while todo:
        v = todo.popleft() # todoの頭から1つ頂点を取り出す
        counter[v] += add
        for w in G[v]: # g(v)の各要素wに対して，
            todo.appendleft(w)
counter.pop(0)
for count in counter:
    print(count, end=" ")

# 同様にTLEとWA: 解説読む: https://img.atcoder.jp/abc138/editorial.pdf
# 親はaだけではなくbもありうる: これがおそらくWAの原因
# 問題の文面通りにdfsで計算するとO(NQ)=400億回となりTLEとなる

# 解答を見たところステップは4つ
# 1. c1, c2, . . . , cN = 0, 0, . . . , 0 とする。
# 2. 各操作 j に対し、cpj に xj を加算する。
# 3. i = 2, . . . , N の順に、ci に ci−1 を加算する。
# 4. c1, c2, . . . , cN を出力する。

import sys
from collections import deque
sys.setrecursionlimit(10**7)
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

n, q = map(int, input().split())
a, b = getXY(n-1)
p, x = getXY(q)

# prepare graph
G = [[]*1 for _ in range(n+1)]
for a_, b_ in zip(a, b):
    G[a_].append(b_)
    G[b_].append(a_)

# ステップ1. [c1, c2, . . . , cN] = [0, 0, . . . , 0] とする。
ans = [0]*(n+1)

# ステップ2. 各操作 j に対し、cpj に xj を加算する。
for i in range(q):
    ans[p[i]] += x[i]

# ステップ3. i = 2, . . . , N の順に、ci に ci−1 を加算する。
# つまり，ci-1をcqi(qiは頂点iの親)として，根に近い頂点から処理を行う

# todoを初期化
todo = deque()
todo.append([1, 0]) # ciとci-1の始点

# todoが空になるまで繰り返す: dequeがemptyであればboolがFalseになるので，これを利用してPythonicに書く
while todo:
    now, pre = todo.popleft()
    for next_v in G[now]:  # g(v)の各要素wに対して，
        if next_v == pre:
            continue
        ans[next_v] += ans[now]
        todo.appendleft([next_v, now])
ans.pop(0)
for i in ans:
    print(i, end=" ")

# こちらを参考にした: https://atcoder.jp/contests/abc138/submissions/17775928
# 解答見ても自力で解けなかったので，もう一度挑戦した方がいい。



##############################################################
# 27問目
# カテゴリ: 深さ優先探索 (DFS)
# タイトル: JOI 2009 予選 4 - 薄氷渡り
# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d
# 日時: 2020/11/04
##############################################################

import sys
sys.setrecursionlimit(10**7)

def getNest(n):
    nest = [[int(i) for i in input().split()] for _ in range(n)]
    return nest

m = int(input())
n = int(input())
c = getNest(n)
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# dfs関数: 頂点vからたどることのできる頂点のうち，まだ訪問していない頂点を全て訪問する
def dfs(y, x):
    seen[y][x] = True # vを訪問済みにする
    ans = 1
    cnt = 0
    for dx, dy in d:
        X = x + dx
        Y = y + dy
        if 0 <= Y < n and 0 <= X < m and (not seen[Y][X]):
            if c[Y][X] == 1:
                cnt = max(cnt, dfs(Y, X))
    ans += cnt
    seen[y][x] = False
    return ans

# すべての頂点に対してdfs関数を使う
ans = 0
for y in range(n):
    for x in range(m):
        seen = [[False] * m for _ in range(n)]
        if c[y][x] == 1:
            ans = max(dfs(y, x), ans)
print(ans)

# 90%は自力で書けてサンプルもACしたけど本番バグってWA
# 解答: https://atcoder.jp/contests/joi2009yo/submissions/17687907
# 間違いポイント1: 初め，cntをdfs()の外側に置いていたが，よく考えたら各初期地点による試行で独立してるから，dfsの中にcntは入れるべきだった
# 間違いポイント2: dfsをreturnする前にseen[y][x] = Falseが必要だった。なんで?????
# 間違いポイント3: moveが8方向に行くような仕様だったが，4方向しか行けない事に気づいた

##############################################################
# 28問目
# カテゴリ: 幅優先探索 (BFS)
# タイトル: JOI 2009 予選 4 - 薄氷渡り
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja
# 日時: 2020/11/06
##############################################################

from collections import deque

n = int(input())
G = [None]*(n+1)
for i in range(n):
    v, k, *e = map(int, input().split())
    G[v] = e

# dist(始点から各頂点までの距離)とque(回るべき頂点のリスト)を用意
dist = [-1]*(n+1)
que = deque([])

# distとqueを初期化
dist[1] = 0
que.append(1)

while que:
    v = que.popleft()
    for w in G[v]:
        if dist[w] != -1:
            continue
        dist[w] = dist[v] + 1
        que.append(w)

for i in range(1, n+1):
    print(i, dist[i])

# けんちょん本の通りに書いただけ！


##############################################################
# 29問目
# カテゴリ: 幅優先探索 (BFS)
# タイトル: AtCoder Beginner Contest 007 C - 幅優先探索
# https://atcoder.jp/contests/abc007/tasks/abc007_3
# 日時: 2020/11/06
##############################################################
from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
G = [input() for _ in range(r)]

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

dist = [[-1 for _ in range(c)] for _ in range(r)]
que = deque([])

dist[sy-1][sx-1] = 0
que.append([sy-1, sx-1])

while que:
    y, x = que.popleft()

    for dy, dx in d:
        Y = y + dy
        X = x + dx
        if G[Y][X] == '.' and dist[Y][X] == -1:
            dist[Y][X] = dist[y][x] + 1
            que.append([Y, X])
print(dist[gy-1][gx-1])

# 28問目を2次元にしただけ！
# きれいに書けて嬉しい！


##############################################################
# 30問目
# カテゴリ: 幅優先探索 (BFS)
# タイトル: JOI 2011 予選 5 - チーズ
# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
# 日時: 2020/11/06
##############################################################
from collections import deque
# 方針
# まずSをスタート，第1チーズまでをゴールとして，距離を測定
# 次に第1チーズをスタート，第2チーズをゴールとして距離を測定 and so on...
# 各ループで29問目と同じ単純なBFSをやる

h, w, n = map(int, input().split())
G = [input() for _ in range(h)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 巣，チーズの座標を探す
place = ['S'] + [str(i+1) for i in range(n)]
coord = []
for p in place:
    for y in range(h):
        for x in range(w):
            if G[y][x] == p:
                coord.append([y, x])

# distの初期化
dist = [[-1 for _ in range(w)] for _ in range(h)]
dist[coord[0][0]][coord[0][1]] = 0

# スタートとゴールのペアを1つずつ回して行く
for i in range(len(coord)-1):

    # スタート地点とゴール地点の用意
    sy, sx = coord[i]
    gy, gx = coord[i+1]
    que = deque([[sy, sx]])

    while que:
        y, x = que.popleft()
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < h and 0 <= X < w:
                if G[Y][X] != 'X' and dist[Y][X] == -1:
                    dist[Y][X] = dist[y][x] + 1
                    que.append([Y, X])

    d_goal = dist[gy][gx] # 一旦ゴールまでの距離を保存
    dist = [[-1 for _ in range(w)] for _ in range(h)] # 距離行列を初期化
    dist[gy][gx] = d_goal # ゴールは次のループのスタートなので，入れる
print(dist[gy][gx])

# 一発AC!!!


##############################################################
# 31問目
# カテゴリ: 幅優先探索 (BFS)
# タイトル: JOI 2012 予選 5 - イルミネーション
# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e
# 日時: 2020/11/06
##############################################################
from collections import deque
w, h = map(int, input().split())
G = [[int(i) for i in input().split()] for _ in range(h)]

# [x, y]の順
d_even = [[1, 0],  # 東隣接
         [-1, 0], # 西隣接
         [0, -1], # 北西
         [1, -1], # 北東
         [1, 1], # 南東
         [0, 1] # 南西
         ]

d_odd = [[1, 0],  # 東隣接
          [-1, 0], # 西隣接
          [-1, -1], # 北西
          [0, -1], # 北東
          [0, 1], # 南東
          [-1, 1] # 南西
          ]

# 1に完全に囲まれてる0を探すため
# 0のマスからスタートして，枠外に出られるかどうか判定する。出られない場合は囲まれてる

surrounded = []
seen = [[False for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if seen[i][j] or G[i][j] == 1:
            continue

        que = deque([])
        que.append([j, i])

        flag = False
        keep = []
        while que:
            x, y = que.popleft()
            if y % 2:
                d = d_odd  # yが奇数ならば
            else:
                d = d_even

            if seen[y][x]:
                continue
            keep.append([x, y])
            seen[y][x] = True
            for dx, dy in d:
                X = x + dx
                Y = y + dy
                if 0 > X or w <= X or 0 > Y or h <= Y: # 枠外に出られる条件
                    flag = True
                    break
                else:
                    if G[Y][X] == 0 and seen[Y][X] == False and (not [X, Y] in que):
                        que.append([X, Y])
            if flag: break
        if not flag and G[i][j] == 0:
            surrounded += keep


for coord in surrounded:
    x, y = coord
    G[y][x] = 1


ans = 0
for y in range(h):
    for x in range(w):
        if y % 2: d = d_odd # yが奇数ならば
        else: d = d_even

        touch = 0
        for dx, dy in d:
            X = x + dx
            Y = y + dy
            if 0 <= X < w and 0 <= Y < h:
                if G[Y][X] == 1:
                    touch += 1
        if G[y][x] == 1:
            ans += 6-touch
print(ans)

# 2時間以上頑張ったのにWA。つらい。今までで一番つらい
# 解説見た: https://www.ioi-jp.org/joi/2011/2012-yo-prob_and_sol/2012-yo-t5/review/2012-yo-t5-review.html
# リベンジ！
# 方針: 枠の一番外側を周遊して，幅優先で埋めていく。もし周りに壁をみつけたら1を加える
# まずは枠の外側に1層加える必要がある


from collections import deque
w, h = map(int, input().split())

# 0で取り囲みながらグラフを入力
G=[[0]*(w+2)]
for i in range(h):
  G.append([0]+list(map(int,input().split()))+[0])
G.append([0]*(w+2))


# [x, y]の順
d_even = [[1, 0],  # 東隣接
         [-1, 0], # 西隣接
         [0, -1], # 北西
         [1, -1], # 北東
         [1, 1], # 南東
         [0, 1] # 南西
         ]

d_odd = [[1, 0],  # 東隣接
          [-1, 0], # 西隣接
          [-1, -1], # 北西
          [0, -1], # 北東
          [0, 1], # 南東
          [-1, 1] # 南西
          ]

seen = [[False for _ in range(w+2)] for _ in range(h+2)]
que = deque([])
que.append([0, 0]) # スタート地点

ans = 0
while que:
    x, y = que.popleft()
    if seen[y][x]: continue
    seen[y][x] = True

    if y % 2: d = d_even # yが奇数ならば
    else: d = d_odd

    for dx, dy in d:
        X = x + dx
        Y = y + dy
        if 0 <= X < w + 2 and 0 <= Y < h + 2 and not seen[Y][X]:
            if G[Y][X] == 0:
                que.append([X, Y])
            else:
                ans += 1
print(ans)

# 周りから塗っていくという発想が思いつかなかった
# グラフの周りを用意するという他人のコードが参考になった


##############################################################
# 32問目
# カテゴリ: 幅優先探索 (BFS)
# タイトル: AOJ 1166 - 迷図と命ず
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=jp
# 日時: 2020/11/07
##############################################################

# 方針
# 現在地から次に行く場所の選択肢を探すとき，「4方向全て行ける」ではなくて「壁がない方向だけ行ける」ようにする

from collections import deque
def solve(w, h, G):
    lr = [] # 右側に壁があるか
    ud = [] # 下側に壁があるか

    for i in range(h):
        lr.append(G[i*2]+[1]) # 最後の列の右側は壁で閉じられているので，1を加える
    for i in range(h-1):
        ud.append(G[i*2+1])
    ud.append([1]*w)


    dist = [[0 for _ in range(w)] for _ in range(h)]
    que = deque([])

    dist[0][0] = 1
    que.append([0, 0])

    while que:
        x, y = que.popleft() # 現在の位置

        # 左右上下に壁があるか
        right = lr[y][x]
        left  = lr[y][x-1]
        down  = ud[y][x]
        up    = ud[y-1][x]

        # 行ける方向のリスト
        d = []
        if not right:
            d.append([1, 0])
        if not left:
            d.append([-1, 0])
        if not down:
            d.append([0, 1])
        if not up:
            d.append([0, -1])

        for dx, dy in d:
            Y = y + dy
            X = x + dx
            if dist[Y][X] == 0:
                dist[Y][X] = dist[y][x] + 1
                que.append([X, Y])
    print(dist[h-1][w-1])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    G = [[int(i) for i in input().split()] for _ in range(h * 2 - 1)]
    solve(w, h, G)

# 一発AC!


##############################################################
# 33問目
# カテゴリ: 幅優先探索 (BFS)
# タイトル: AtCoder Beginner Contest 088 D - Grid Repainting
# https://atcoder.jp/contests/abc088/tasks/abc088_d
# 日時: 2020/11/07
##############################################################

# 方針
# 1. 普通にBFSをまず解く
# 2. 最短経路を復元する: https://qiita.com/drken/items/0c7bab0384438f285f93
# 3. 経路に必要なマス以外で白い部分は必要ないので，黒く塗りつぶせる

from collections import deque
h, w = map(int, input().split())
G = [input() for _ in range(h)]

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dist = [[-1 for _ in range(w)] for _ in range(h)]
que = deque([])

dist[0][0] = 0
que.append([0, 0])

while que:
    x, y = que.popleft()

    for dx, dy in d:
        Y = y + dy
        X = x + dx
        if 0 <= Y < h and 0 <= X < w:
            if G[Y][X] == '.' and dist[Y][X] == -1:
                dist[Y][X] = dist[y][x] + 1
                que.append([X, Y])

if dist[h-1][w-1] == -1: # もし迷路が解けてなかったら-1を出力
    print(-1)
else: #迷路が解けてたら，経路を再現
    x = w-1
    y = h-1
    step = dist[y][x]
    route = [[x, y]] # 再現経路の座標

    while dist[y][x] != 0:
        for dx, dy in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < h and 0 <= X < w:
                if dist[Y][X] == dist[y][x] - 1:
                    route.append([X, Y])
                    x = X
                    y = Y
                    break

    # 経路に必要なマス以外で白い部分は必要ないので，カウントする
    ans = 0
    for y in range(h):
        for x in range(w):
            if not ([x, y] in route) and G[y][x] == '.':
                ans += 1
    print(ans)

# AC!!
# 解答みたら，復元なんてしてなくても個数数えるだけで良い事に気づいた (今更)
# でも勉強になったからよし！

##############################################################
# 34問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: ALDS_10_A - フィボナッチ数
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja
# 日時: 2020/10/15
##############################################################

n = int(input())
dp = [-1]*(n+1)
def fib(n):
    if n == 0 or n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]

print(fib(n))

# アルゴリズム本で習ったとおりにメモ化再帰を用いた



##############################################################
# 35問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: DPL_1_B - 0,1ナップザック問題
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja
# 日時: 2020/10/19
##############################################################
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

N, W = list(map(int,input().split()))
value, weight = getXY(N)

dp = [[-1 for j in range(W+1)] for i in range(N+1)]
dp[0] = [0]*(W+1)

for i in range(N):
    for w in range(W+1):
        # print(i, w, dp[i][w])
        # 品物iを選ぶ
        if w-weight[i] >= 0:
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - weight[i]] + value[i])

        # 品物iを選ばない
        dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
print(dp[N][W])

# アルゴリズム本と同じ！
# dp[i+1]とvalue[i]は全く同じ商品を表していることに注意: dpは0を含んでN+1行持ってる一方で，valueはN個のベクトル


##############################################################
# 36問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: DPL_1_C - ナップザック問題
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja
# 日時: 2020/10/20
##############################################################

def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y


def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

# 方針
# まず重複を削る
# 1kgあたりの価値が高い順に並べる。単位あたり価値が同じ品物がある場合，重い品物を削る。
# 単位あたり価値が高いものから，ザックに入り切らなくなるまで入れ続けてループを回す。


N, W = list(map(int,input().split()))
value, weight = getXY(N)
unit = [value[i]/weight[i] for i in range(N)]


li = [value, weight, unit]
li = get_unique_list(li)
li = zip(*li)
li = sorted(li, key=lambda x: (x[2], x[1]), reverse=True)
li = [[li[i][j] for i in range(N)] for j in range(3)]

i = 0
while len(li[0]) != i + 1:
    while li[2][i] == li[2][i+1]:
        li[0].pop(i)
        li[1].pop(i)
        li[2].pop(i)
        if len(li[0]) == i + 1:
            break
    else:
        i += 1
        continue
    break

value, weight, unit = li[0], li[1], li[2]

value_sum = 0
weight_room = W
for i in range(len(value)):
    value_sum += (weight_room // weight[i])*value[i]
    weight_room -= (weight_room // weight[i])*weight[i]
print(value_sum)

# なぜか10ケース目でエラーがでる。答えが1251なのに1248と出力されてしまう。
# 解答をパット見た感じ，凄い簡単そうなDPだった。

# DP使ってやり直し
N, W = list(map(int,input().split()))
item = [list(map(int,input().split())) for i in range(N)]

dp = [-1]*(W+1)
dp[0] = 0
# dp[w]: 耐荷重をwとした時の価値の最大値
for w in range(W+1):
    for i in range(N):
        if w-item[i][1] >= 0:
            dp[w] = max(dp[w], dp[w-item[i][1]] + item[i][0])
print(max(dp))

# ポイントはループのwごとに最適な価値が確定してて，wが1kgずつ増えるのであれば，確定したものが変わらない


##############################################################
# 37問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: DPL_1_A - コイン問題
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
# 日時: 2020/10/20
##############################################################

# m種類のコインでn円払いたい

n, m = list(map(int,input().split()))
c = list(map(int,input().split()))

inf = float('INF')
dp = [[inf for j in range(n+1)] for i in range(m+1)]
# dp[i][j]: コインをi枚目までつかって，j円を払う時に必要な最低枚数
dp[0][0] = 0

for i in range(m):
    for j in range(n+1):
        # i枚目のコインを使う時
        if j-c[i] >= 0:
            dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-c[i]] + 1)

        # i枚目のコインを使わない時
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
print(dp[m][n])

# ナップザックに慣れてきた!!
# まずdpテーブルの行列に何を入れるかを考える。どういう推移か考える
# dpテーブルをノートに描いて，具体的な1マスをピックアップして，dp[i+1]がどう表せるか具体的な式で書いてみる
# 具体的な式をiとjを用いて一般化する


##############################################################
# 38問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: ALDS_10_C - 最長共通部分列
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja
# 日時: 2020/10/20
##############################################################

from sys import stdin
n = int(input())
xy = [stdin.readline()[:-1] for _ in range(n*2)]

for k in range(n):
    x = xy[2*k]
    y = xy[2*k+1]

    dp = [[0 for j in range(len(y))] for i in range(len(x))]

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                dp[i][j] = max(dp[i][j], dp[i][j-1])
    print(dp[len(x)-1][len(y)-1])

# 最初普通にinput()しててTLEで，stdinに変えたけど，それでもTLE
# ループが時間かかってる
# 他の人の回答見ると，dpテーブルが2次元ではなく1次元ベクトルを2つ使ってる。
# 1000*1000のテーブルを毎回呼び出すのが時間かかってる模様
# 1次元のdpテーブルで書き直し

# 結局解けなくて解答見たらこんな感じだった
# j = 0のときは無視してる。dp1とdp2のj番目が既知で，dp2のj+1を更新する感じ
from sys import stdin
n = int(input())
xy = [stdin.readline()[:-1] for _ in range(n*2)]

for k in range(n):
    x = xy[2*k]
    y = xy[2*k+1]

    dp2 = [0] * (len(y) + 1)

    for i in range(len(x)):
        dp1 = dp2[:]
        for j in range(len(y)):
            if x[i] == y[j]:
                dp2[j+1] = dp1[j] + 1
            elif dp2[j+1] < dp2[j]:
                dp2[j + 1] = dp2[j]

    print(dp2[-1])

# しかし！これでもTLE。
# 一気に最初に入力を読み込むのではなく，1ケースずつ読み込んで処理する。
# そのためにケースごとに答えを出力する関数を用意しておいて，ループでケースを回す。
# これは大きな学び

# 模範解答: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=2492662#1
def get_longest(x, y):
    dp2 = [0] * (len(y) + 1)

    for i in range(len(x)):
        dp1 = dp2[:]
        for j in range(len(y)):
            if x[i] == y[j]:
                dp2[j+1] = dp1[j] + 1
            elif dp2[j+1] < dp2[j]:
                dp2[j + 1] = dp2[j]

    return dp2[-1]

n = int(input())
for _ in range(n):
    x = input()
    y = input()
    res = get_longest(x, y)
    print(res)

##############################################################
# 39問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: D - 1年生 (A First Grader)
# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d
# 日時: 2020/10/21
##############################################################

# dp[i][j]: i番目までの数字を使って，数jができる通りの数
# 推移: dp[i+1][j]はdp[i]のj-値とj+値からそれぞれ来る値の和

n = int(input())
x = list(map(int, input().split()))
a = x[-1]
x.pop(-1)

dp = [[0 for j in range(20 + 1)] for i in range(len(x) + 1)]
dp[0] = [1] + [0] * 20

for i in range(len(x)):
    for j in range(21):
        if j - x[i] >= 0:
            dp[i + 1][j] += dp[i][j - x[i]]
        if j + x[i] <= 20:
            dp[i + 1][j] += dp[i][j + x[i]]
print(dp[len(x)][a])

# これで提出したら最後のケースでWAだった
# 問題は数列の初項が0だった場合，dp[1][0]が2になって誤りになる点
# 面倒なので「数字を使わない」というケースを除いたdpテーブルの形にして，初項=0に対応する

n = int(input())
x = list(map(int,input().split()))
a = x[-1]
x.pop(-1)

dp = [[0 for j in range(20+1)] for i in range(len(x))]
dp[0][x[0]] = 1

for i in range(len(x)-1):
    for j in range(21):
        if j-x[i+1] >= 0:
            dp[i + 1][j] += dp[i][j - x[i+1]]
        if j+x[i+1] <= 20:
            dp[i + 1][j] += dp[i][j + x[i+1]]
print(dp[len(x)-1][a])

# 良問だった!!!


##############################################################
# 40問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: JOI 2012 予選 4 - パスタ
# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
# 日時: 2020/10/21
##############################################################
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

n, k = list(map(int,input().split()))
a,b = getXY(k)
a = [i-1 for i in a]
b = [i-1 for i in b]

# 難しすぎて他人の解答みた
# dp[i日目][i-1日目のパスタ][i日目のパスタ] = 場合の数
dp = [[[0 for k in range(3)] for j in range(3)] for i in range(n+1)]
dp[0][0][0] = 1

# 必ず食べるパスタのベクトル
# インデックスがi日目, 0/1/2がパスタの種類，-1なら何でもOK
pasta = [-1]*n
for i in range(len(a)):
    pasta[a[i]] = b[i]

for i in range(n):
    for j in range(3):
        for k in range(3):
            # 食べるものが決まってる場合
            if pasta[i] != -1:
                # 食べるものは1種類
                eat_list = [pasta[i]]
            else:
                # 3種類ぜんぶ食べられる
                eat_list = [0, 1, 2]

            for eat in eat_list:
                if i >= 2 and j==k==eat:
                    continue
                dp[i+1][j][eat] += dp[i][k][j]
                dp[i+1][j][eat] %= 10**4

print(sum([sum(i)%10**4 for i in dp[n]])%10**4)

##############################################################
# 41問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: JOI 2013 予選 4 - 暑い日々
# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d
# 日時: 2020/10/21
##############################################################

# 最初，パスタのアイデアを真似てdpを3次元配列で考えていたが，複雑になりすぎた
# 解答を見たらdp[i][j]=「i 日目に服 j を選ぶとしたときの，i 日目までの連続する日に着る服の派手さの差の絶対値の合計」
# これを参考にペンとノートでテーブル具体例かいて，一般化した

# 推移: dp[i][i日目の服の選択肢] = max(dp[i][i日目の服の選択肢], dp[i-1][i-1日目の服の選択肢] + abs(i-1の派手さ - iの派手さ))

# i日目に着る服の選択肢を事前に用意しておくと本番のループが楽

d, n = list(map(int,input().split()))
t = [int(input()) for i in range(d)]
abc = [map(int, input().split()) for _ in range(n)]
a, b, c = [list(i) for i in zip(*abc)]

dp = [[0 for _ in range(n)] for _ in range(d)]

option_list = []
for i in range(d):
    option = []
    for j in range(n):
        if a[j] <= t[i] <= b[j]:
            option.append(j)
    option_list.append(option)

for i in range(d):
    for x in option_list[i-1]:
        for y in option_list[i]:
            if i > 0:
                dp[i][y] = max(dp[i][y], dp[i-1][x] + abs(c[x] - c[y]))

print(max(dp[d-1]))


##############################################################
# 42問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: JOI 2015 予選 4 - シルクロード
# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d
# 日時: 2020/10/22
##############################################################

# 方針
# dp[i][j]: i日目までの疲労の蓄積 at 都市j
# dpテーブルのj=0列目は，ずっと都市0に引きこもっていることになるので，全て0。初期値として与える。
# 推移は，min(自分, 前日までの疲労(滞在)，前日までの前の都市での疲労 + 移動してその分の疲労)


def getX(n): return [int(input()) for i in range(n)]
n, m = list(map(int,input().split()))
d = getX(n)
c = getX(m)

inf = float('INF')
dp = [[inf for _ in range(n+1)] for _ in range(m+1)]
dp[0][0] = 0
for i in range(m+1):
    dp[i][0]=0


for i in range(m):
    for j in range(n):
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1], dp[i][j] + d[j]*c[i])
print(min([l[n] for l in dp]))


# 1発AC!!!!!
# DPテーブルが2次元配列だと図示しやすくて解きやすい


##############################################################
# 43問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: パ研杯2019 D - パ研軍旗
# https://atcoder.jp/contests/pakencamp-2019-day3
# 日時: 2020/10/22
##############################################################

# 方針
# # dp[i列目までに塗り替えたマスの個数の合計の最小値][i-1列目の色][i列目の色] = 場合の数
# パスタの問題と同じ考え方


import numpy as np
def getX(n): return [int(input()) for i in range(n)]
n = int(input())
s = [input() for i in range(5)]
s = [[j for j in i] for i in s]
s = np.array(s).T.tolist()
s = [''.join(i) for i in s]

color = ['R', 'B', 'W']

inf = float('INF')
dp = [[[inf for k in range(3)] for j in range(3)] for i in range(n)]

for i in range(n):
    for x in range(3):
        for y in range(3):
            num = 5 - s[i].count(color[y])
            if x != y:
                if i == 0:
                    dp[i][x][y] = num
                else:
                    l = [0, 1, 2]
                    l.remove(y)
                    for j in l:
                        dp[i][x][y] = min(dp[i][x][y], dp[i-1][y][j] + num)

print(min([min(i) for i in dp[n-1]]))


# 遷移の添字が紛らわしくて大変だった
# 解答も一切見ずに解けた!
# たぶん暑い日々と同じように，3次元じゃなくて2次元配列でいけた (今更)


##############################################################
# 44問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: AOJ 1167 - ポロック予想
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1167&lang=jp
# 日時: 2020/10/23
##############################################################


# 解釈を間違えてた。1,4,10,20,35の和で表せるという問題かと思ったら，任意の正四面体5つだった

# 10**6までの正四面体数は180個
# いわゆるO(数列の大きさ×10**6)で解ける。180*10**6 = 1.8億: ぎりぎり間に合う
# でも1.8億のリストは厳しいかも？
# とりあえず最大のdpテーブル作って，入力のnごとに出力を返す

# dpテーブルは1次元でいいのではないか？
# 初見で正しい答えは出したがTLE
# 色々工夫してみるが，間に合わない，今までの問題で一番時間がシビア
# 解答を見てみた: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=2912388#1

m = 10**6
inf = float('INF')
a = [int(n*(n+1)*(n+2)/6) for n in range(1, 1000) if int(n*(n+1)*(n+2)/6) < 10**6]

dp_all = [inf] * (m+1)
dp_odd = [inf] * (m+1)
dp_all[0] = 0
dp_odd[0] = 0


for i in a:
    for j in range(i, min(i*5, m+1)):
        if dp_all[j] > dp_all[j-i] + 1:
            dp_all[j] = dp_all[j - i] + 1


for i in [i for i in a if i % 2 == 1]:
    for j in range(i, m+1):
        if dp_odd[j] > dp_odd[j-i] + 1:
            dp_odd[j] = dp_odd[j - i] + 1

while True:
    n = int(input())
    if n == 0:
        break
    print(f'{dp_all[n]} {dp_odd[n]}')



# dpテーブルは100万で済んだが，ループに時間がかかりすぎ
# ループが1.8億回回ってる

# 改良する必要があった点
# jを1からmまで回す -> jをiからmin(i*5, m+1) : i*5ってなんぞ？
# 推移のminをif文にした
# iを使わない場合の推移が必要ない


##############################################################
# 45問目
# カテゴリ: 動的計画法：ナップザック DP
# タイトル: AOJ 2199 - 差分パルス符号変調
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2199&lang=jp
# 日時: 2020/10/25
##############################################################

# dp[i][j][k]: 入力iまでの差の二乗和の最小値 at j=iにおけるcodebook，k=i-1におけるcodebook
# tb[i][j][k]: 入力iまで(nまで)の初期値128にcodebookを足し続けたもの at j=iにおけるcodebook，k=i-1におけるcodebook

# 超試行錯誤して2日かけて解いた...
# 初めは2次元配列で考えてたけど，i-1を考慮できなかった
# 数列の値を保持するためにtbテーブルが別で必要になって用意するのに時間がかかった

def getX(n): return [int(input()) for i in range(n)]

def run_dp(n, m, c, x):

    inf = float('INF')
    dp = [[[inf for _ in range(m)] for _ in range(m)] for _ in range(n)]
    tb = [[[inf for _ in range(m)] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(m):
                if i == 0:
                    y = 128 + c[k]
                    if y < 0:
                        y = 0
                    elif y > 255:
                        y = 255
                    tb[i][j][k] = y
                    dp[i][j][k] = (y - x[i])**2
                else:
                    for l in range(m):
                        y = tb[i-1][l][j] + c[k]
                        if y < 0:
                            y = 0
                        elif y > 255:
                            y = 255
                        if dp[i][j][k] > dp[i-1][l][j] + (y-x[i])**2:
                            dp[i][j][k] = dp[i - 1][l][j] + (y - x[i]) ** 2
                            tb[i][j][k] = y
    return min([min(i) for i in dp[n-1]])

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        c = getX(m)
        x = getX(n)

        print(run_dp(n, m, c, x))

# ただこれだとTLE: たぶんm=16, n=20000のときにdpテーブルがでかすぎるのが問題
# 大きいリストを2本のリストだけに絞る


def getX(n): return [int(input()) for i in range(n)]

def run_dp(n, m, c, x):
    inf = float('INF')
    dp1 = [[inf for _ in range(m)] for _ in range(m)]
    dp2 = [[inf for _ in range(m)] for _ in range(m)]
    tb1 = [[inf for _ in range(m)] for _ in range(m)]
    tb2 = [[inf for _ in range(m)] for _ in range(m)]


    for i in range(n):
        for j in range(m):
            for k in range(m):
                if i == 0:
                    y = 128 + c[k]
                    if y < 0:
                        y = 0
                    elif y > 255:
                        y = 255
                    tb1[j][k] = y
                    dp1[j][k] = (y - x[i])**2
                else:
                    for l in range(m):
                        y = tb1[l][j] + c[k]
                        if y < 0:
                            y = 0
                        elif y > 255:
                            y = 255
                        if dp2[j][k] > dp1[l][j] + (y - x[i])**2:
                            dp2[j][k] = dp1[l][j] + (y - x[i]) ** 2
                            tb2[j][k] = y
    return min([min(i) for i in dp2])

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        c = getX(m)
        x = getX(n)

        print(run_dp(n, m, c, x))

# y＜0なら0，y>255なら255に丸めるルール忘れてたので足した
# これでもTLEなので解答見る！
# https://www.utakata.work/entry/2015/05/23/104921
# 同じような方法でN*256*Mで回ると言ってるので，たぶんPythonが悪い
# 他人の解答がきれい: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4937813#1

##############################################################
# 46問目
# カテゴリ: 動的計画法：区間 DP
# タイトル: ALDS_10_B - 連鎖行列積
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_B&lang=ja
# 日時: 2020/10/25
##############################################################


# 方針
# 隣り合う2つの行列を選んで積を取り，スカラー乗算の回数をそれぞれについて数えてminのものをincrement
# 行数と列数のテーブルを更新する
def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

n = int(input())
r,c = getXY(n)

inf = float('INF')
dp = [inf]*n

for i in range(n):
    print(r, c)
    b_j = 0
    for j in range(len(r)-1):
        if dp[i] > r[j]*c[j]*c[j+1]:
            dp[i] = r[j]*c[j]*c[j+1]
            b_j = j
    if len(r) == 1 and len(c) == 1:
        break
    r.pop(b_j+1)
    c.pop(b_j)


# とけなかった



##############################################################
# 56問目
# カテゴリ: ダイクストラ法
# タイトル: GRL_1_A - 単一始点最短経路
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
# 日時: 2020/11/08
##############################################################

# ステップ1: 始点を0とし，distも0とする
# ステップ2: 未使用の地点(usedでない地点)の中から最もdistの小さいものを選び，その値をmin_vとして使用済みにする (usedにする)
# min_vがなければ終了，もしあれば
# ステップ3: min_vから行ける頂点を全て巡り，それぞれの距離を計算する
# ステップ4: min_vが見つからなくなるまで2, 3を繰り返す

# 入力
n, m, s = map(int, input().split())
G = [[] for _ in range(n)]

# グラフは隣接リストで行き先と重みをセットに格納する
for i in range(m):
    v, e, w = map(int, input().split())
    G[v].append([e, w])

# 始点から各頂点までの最短距離をinfで初期化
inf = float('INF')
dist = [inf]*n
dist[s] = 0 # 始点の設定

# 各頂点が使用済みかどうかのリスト: すでに最短路が求められていることが確定している頂点の集合S
used = [False]*n

for _ in range(n):
    # ステップ2: 使用済みでない頂点のうちdistが最小の頂点を探す
    min_dist = inf
    min_v = -1
    for v in range(n):
        if (not used[v]) and dist[v] < min_dist:
            min_dist = dist[v]
            min_v = v

    # もしそのような頂点が見つからなければ終了
    if min_v == -1: break

    # min_vを使用済みとする
    used[min_v] = True

    # ステップ3: 頂点vの推移先を全て巡る
    for ew in G[min_v]:
        e = ew[0]  # 行き先
        w = ew[1]  # 重み
        if dist[e] > dist[min_v]+ w:
            dist[e] = dist[min_v] + w

for i in dist:
    if i == inf:
        print('INF')
    else:
        print(i)

# けんちょん本の通りに解いたこれだとTLE!!
# 他の人の解答見てみると，heapの解法でACの人が多いけど，heapじゃなくても通ってる解答があった
# これとか: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=1925454#1


n, m, s = map(int, input().split())
G = []
for i in range(m):
    G.append(list(map(int, input().split())))

# 始点から各頂点までの最短距離をinfで初期化
inf = float('INF')
dist = [inf]*n
dist[s] = 0 # 始点の設定

while True:
    update = False
    for i in range(m):
        v, e, w = G[i][0], G[i][1], G[i][2]
        if dist[v] != inf and dist[e] > dist[v] + w:
            dist[e] = dist[v] + w
            update = True
    if update == False: break

for i in dist:
    if i == inf:
        print('INF')
    else:
        print(i)

# しかしこれはダイクストラ法ではない!! ヒープを使う必要がある!!
# 学んだけどよくわかってない。本の通りに書いてみる


# 「使用済みでない頂点のうちdistの値が最小の頂点を求める」というステップ2を高速化したい

from heapq import heappush, heappop
# 入力
n, m, s = map(int, input().split())
G = [[] for _ in range(n)]

# グラフは隣接リストで行き先と重みをセットに格納する
for i in range(m):
    v, e, w = map(int, input().split())
    G[v].append([e, w])

# 始点から各頂点までの最短距離をinfで初期化
inf = float('INF')
dist = [inf]*n
dist[s] = 0 # 始点の設定

que = [] # ヒープに入れる空のリスト
heappush(que, (0, s))

while que:
    c, v = heappop(que)
    if dist[v] < c: #
        continue
    for e, w in G[v]:
        if dist[e] > dist[v] + w: # 距離の更新
            dist[e] = dist[v] + w
            heappush(que, (dist[e], e))

for i in dist:
    if i == inf:
        print('INF')
    else:
        print(i)

# これでAC！だけど復習が必要

##############################################################
# 57問目
# カテゴリ: ダイクストラ法
# タイトル: JOI 2008 予選 6 - 船旅
# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
# 日時: 2020/11/09
##############################################################
from heapq import heappush, heappop
def lint(): return list(map(int,input().split()))

# 方針
# 入力をループで受け取り，運行情報であればグラフを拡張し，注文票であれば現在のグラフで最短経路を求める

n, k = map(int, input().split())
G = [[] for _ in range(n)] # 空のグラフの用意

for _ in range(k):
    l = lint()

    if l[0] == 1: # 入力が運行情報の場合，グラフを作成する
        a, b, w = l[1], l[2], l[3]
        G[a - 1].append([b - 1, w]) # aからb
        G[b - 1].append([a - 1, w]) # bからa

    elif l[0] == 0: # 入力が注文票の場合，現在のグラフでダイクストラ法を使う
        s = l[1]-1 # スタート地点
        g = l[2]-1 # ゴール地点

        # 始点から各頂点までの最短距離をinfで初期化
        inf = float('INF')
        dist = [inf] * n
        dist[s] = 0  # 始点の設定

        que = []  # ヒープに入れる空のリスト
        heappush(que, (0, s))

        while que:
            c, v = heappop(que)
            if dist[v] < c:  #
                continue
            for e, w in G[v]:
                if dist[e] > dist[v] + w:  # 距離の更新
                    dist[e] = dist[v] + w
                    heappush(que, (dist[e], e))

        if dist[g] == inf: print(-1)
        else: print(dist[g])

# 一発AC!


##############################################################
# 58問目
# カテゴリ: ダイクストラ法
# タイトル: JOI 2016 予選 5 - ゾンビ島
# https://atcoder.jp/contests/joi2016yo/tasks/joi2016yo_e
# 日時: 2020/11/09
##############################################################

# 方針
# ステップ1. まずは各街がゾンビ街からS以内で来られる危険な街かどうか幅優先探索で判断する
# 結果によってpかq (宿の料金)をグラフに追加する : これでやっと材料が揃う
#

from heapq import heappush, heappop
from collections import deque
inf = float('INF')

n, m, k, s = map(int, input().split())
p, q = map(int, input().split()) # pが危険でない宿の料金，qが危険な宿の料金
z = [] # ゾンビのいる街
for i in range(k):
    z.append(int(input())-1)


G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# まずは各ゾンビ街から他の街への最短距離を幅優先探索で求める
dist_z = [inf]*n
for zombi in z:
    # dist(始点から各頂点までの距離)とque(回るべき頂点のリスト)を用意
    dist = [-1] * n
    que = deque([])

    # distとqueを初期化
    dist[zombi] = 0
    que.append(zombi)

    while que:
        v = que.popleft()
        for w in G[v]:
            if dist[w] != -1:
                continue
            dist[w] = dist[v] + 1
            que.append(w)

    for i in range(n):
        dist_z[i] = min(dist_z[i], dist[i])

# ゾンビ街からS以内で来られる場合は危険な街
danger = [i <= s for i in dist_z]

# 危険ならばQ円，危険でないならP円
price = [inf]*n
for i in range(n):
    if danger[i]: price[i] = q
    else: price[i] = p
price[n-1] = 0# 最後の街では宿泊しないので0円

# 材料が揃ったのでダイクストラ法で街1から街nに行く最安ルートを探す
# 始点から各頂点までの最短距離をinfで初期化
dist = [inf]*n
dist[0] = 0 # 始点の設定

que = [] # ヒープに入れる空のリスト
heappush(que, (0, 0))

while que:
    c, v = heappop(que)
    if dist[v] < c: #
        continue
    for e in G[v]:
        if e in z: # もしゾンビ街だったら訪れられない
            continue
        w = price[e]
        if dist[e] > dist[v] + w: # 距離の更新
            dist[e] = dist[v] + w
            heappush(que, (dist[e], e))
print(dist[n-1])

# 一発AC!!!!

##############################################################
# 59問目
# カテゴリ: ダイクストラ法
# タイトル: JOI 2014 予選 5 - タクシー
# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e
# 日時: 2020/11/10
##############################################################

# 方針
# R本先の街までいけるタクシーがある街は，R本以内の街と直接つながってると考えて問題ない
# まずはそれを幅優先探索で見つけて，グラフを変形する

from collections import defaultdict, deque
from heapq import heappush, heappop
inf = float('INF')

n, k = map(int, input().split())
cr = [map(int, input().split()) for _ in range(n)]
c, r = [list(i) for i in zip(*cr)]

G = [[] for _ in range(k)]
for _ in range(k):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


# まずは各街から他の街への最短距離を幅優先探索で求める
G2 = [[] for _ in range(n)]
for s in range(n):
    # dist(始点から各頂点までの距離)とque(回るべき頂点のリスト)を用意
    dist = [-1] * n
    que = deque([])

    # distとqueを初期化
    dist[s] = 0
    que.append(s)

    while que:
        v = que.popleft()
        for w in G[v]:
            if dist[w] != -1:
                continue
            dist[w] = dist[v] + 1
            que.append(w)

    # 街sからr本以内の道路でいける街をピックアップ
    access = [r[s] >= i for i in dist]
    for i in range(n):
        if access[i]:
            G2[s].append(i)

# 材料が揃ったのでダイクストラ法で街1から街nに行く最安ルートを探す
# 始点から各頂点までの最短距離をinfで初期化
dist = [inf]*n
dist[0] = 0 # 始点の設定

que = [] # ヒープに入れる空のリスト
heappush(que, (0, 0))

while que:
    d, v = heappop(que)
    if dist[v] < d: #
        continue
    w = c[v] # 街vからの運賃はどこにいこうと一定
    for e in G2[v]:
        if dist[e] > dist[v] + w: # 距離の更新
            dist[e] = dist[v] + w
            heappush(que, (dist[e], e))
print(dist[n-1])

# 5ケース中4ケースACで1ケースRE
# 解法自体は解説と同じように溶けていたのでOK
# ACするためにmaspyさんのコードをコピペ

##############################################################
# 60問目
# カテゴリ: 最短経路問題：ワーシャルフロイド法
# タイトル: GRL_1_C - 全点対間最短経路　
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja
# 日時: 2020/11/11
##############################################################

# けんちょん本の通りに解く

inf = float('INF')
n, m = map(int, input().split())

# dp[k][i][j]: 頂点0, 1, ..., k-1のみを中継頂点として通って良いとした場合の頂点iから頂点jへの最短距離
# kをin-placeに表現すれば，二次元配列で十分
dp = [[inf for _ in range(n)] for _ in range(n)]

# dpの各要素がaからbへの重みを表すので，入力の有向グラフを初期状態として埋め込む
for _ in range(m):
    a, b, w = map(int, input().split())
    dp[a][b] = w

# スタートとゴールが同じ場合(i=jのとき)は距離がゼロ
for i in range(n):
    dp[i][i] = 0

# 新たに頂点kを使用しない場合: dp[k][i][j]
# 新たに頂点kを使用する場合: dp[k][i][k] + dp[k][k][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 負閉路がある場合は報告する: dp[v][v]が負であれば負閉路がある
exist_negative_cycle = False
for i in range(n):
    if dp[i][i] < 0:
        exist_negative_cycle = True

if exist_negative_cycle:
    print('NEGATIVE CYCLE')
else:
    for i in range(n):
        s = f''
        for j in range(n):
            if dp[i][j] == inf:
                s += 'INF '
            else:
                s += f'{dp[i][j]} '
        print(s[:-1])


##############################################################
# 61問目
# カテゴリ: 最短経路問題：ワーシャルフロイド法
# タイトル: AtCoder Beginner Contest 012 D - バスと避けられない運命
# https://atcoder.jp/contests/abc012/tasks/abc012_4
# 日時: 2020/11/11
##############################################################

# 普通のワーシャルフロイドの問題と全く同じ！
# コード使い回せる！

n, m = map(int, input().split())
inf = float('INF')

# dp[k][i][j]: 頂点0, 1, ..., k-1のみを中継頂点として通って良いとした場合の頂点iから頂点jへの最短距離
# kをin-placeに表現すれば，二次元配列で十分
dp = [[inf for _ in range(n)] for _ in range(n)]

# dpの各要素がaからbへの重みを表すので，入力の有向グラフを初期状態として埋め込む
for _ in range(m):
    a, b, w = map(int, input().split())
    dp[a - 1][b - 1] = w
    dp[b - 1][a - 1] = w

# スタートとゴールが同じ場合(i=jのとき)は距離がゼロ
for i in range(n):
    dp[i][i] = 0

# 新たに頂点kを使用しない場合: dp[k][i][j]
# 新たに頂点kを使用する場合: dp[k][i][k] + dp[k][k][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 各出発点からその他のゴールまでの最長距離が一番短いような出発点を探す
ans = inf
for i in range(n):
    ans = min(ans, max(dp[i]))
print(ans)


##############################################################
# 62問目
# カテゴリ: 最短経路問題：ワーシャルフロイド法
# タイトル: AtCoder Beginner Contest 079 D - Wall
# https://atcoder.jp/contests/abc079/tasks/abc079_d
# 日時: 2020/11/11
##############################################################

# 方針
# 数字iをjに変えるとき，遠回りした方がコストの低い場合がある
# つまり，8->1と直接変えるより，8->9->3->1のように遠回りしたほうがいいかもしれない
# 各数字の総当りの最短距離をワーシャルフロイドで求める

h, w = map(int, input().split())
dp = [[int(i) for i in input().split()] for _ in range(10)]
A = [[int(i) for i in input().split()] for _ in range(h)]
A = [item for sublist in A for item in sublist]

# 新たに頂点kを使用しない場合: dp[k][i][j]
# 新たに頂点kを使用する場合: dp[k][i][k] + dp[k][k][j]
for k in range(10):
    for i in range(10):
        for j in range(10):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = 0
for i in range(h*w):
    if A[i] == -1:
        continue
    else:
        ans += dp[A[i]][1]
print(ans)

##############################################################
# 63問目
# カテゴリ: 最短経路問題：ワーシャルフロイド法
# タイトル: AtCoder Beginner Contest 04 D - Restoring Road Network
# https://atcoder.jp/contests/abc079/tasks/abc074_d
# 日時: 2020/11/11
##############################################################

# 方針
# 入力に対してワーシャルフロイドを適用し，グラフが変わらないのであればOK(入力のような道路の構造が存在する)
# グラフが変わって，ある道において元の距離より短くなることがあれば，入力と矛盾するので，存在しないことになる

# 各道路A_uvを消してもいいかどうかの判定は，その道A_uvがないと仮定した上でA_uvの迂回路の最短距離を求めてみて，
# それが元のA_uvと同じ距離であれば必要ないということになる
# が，こんな総当りみたいなことやるとO(N^5)とかになっちゃってどうしようもない

from copy import deepcopy
import math
inf = float('INF')

n = int(input())
dp = [[int(i) for i in input().split()] for _ in range(n)]
origin = deepcopy(dp)

# apply ワーシャルフロイド
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


flag = False
total = 0
for i in range(n):
    for j in range(i+1, n):
        if origin[i][j] > dp[i][j]:
            flag = True
        total += dp[i][j]


# もっかい ワーシャルフロイド
# 頂点aからbへの道がないと仮定して，最短路を求めて，それでも同じ距離なのであれば，直接の道は必要ないということになる
# もしそうであれば，現在ある道の合計値(total)から，そのいらない道の距離を引いていく
no_need = []
for a in range(n):
    for b in range(a+1, n):
        G = deepcopy(origin)
        G[a][b] = inf
        G[b][a] = inf
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j])
        if origin[a][b] == G[a][b]:
            total -= G[a][b]
print(total)

# サンプルも解けるし多分合ってるけどTLE!!! 5重ループが悪い!!
# 参考解答: https://atcoder.jp/contests/abc074/submissions/18041684
# 解説: https://img.atcoder.jp/arc083/editorial.pdf


from copy import deepcopy
import math
inf = float('INF')

n = int(input())
dp = [[int(i) for i in input().split()] for _ in range(n)]
origin = deepcopy(dp)

# apply ワーシャルフロイド
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 道路の構造が存在しない場合を確認する
flag = False
for i in range(n):
    for j in range(i+1, n):
        if origin[i][j] > dp[i][j]:
            flag = True
if flag:
    print(-1)
    exit()

# ここから解答参考: なにやってるんだ？？？？
ans=0
for i in range(n):
  for j in range(i+1, n):
    m = 10**18
    for k in range(n):
      if i==j or j==k or k==i:
        continue
      m = min(m, dp[i][k] + dp[k][j])
    if m > dp[i][j]:
      ans += dp[i][j]
print(ans)

# よくわからん!!!



##############################################################
# 64問目
# カテゴリ: 最小全域木問題
# タイトル: GRL_2_A - 最小全域木
# http://judge.u-aizu.ac.jp/onlinejudge/submission.jsp#
# 日時: 2020/11/13
##############################################################

# けんちょん本の通りに解いた！

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n # 自分が根の場合，根を-1と表記: 初期状態ではみんなバラバラなのでみんな-1

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # xとyが同じグループに属するかどうか (根が一致するかどうか)
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループとを併合する
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)

        # すでに同じグループのときは何もしない
        if x == y: return False

        # union by size (y側のサイズが小さくなるようにする: xとyをスワップする: xをyの親にしたい)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    # xを含むグループのサイズ
    def size(self, x):
        return self.siz[self.root(x)]

    # グループ数を返す
    def group_count(self):
        parents = [i for i, x in enumerate(self.par) if x == -1]
        return len(parents)

    # 各グループに属する要素をリストで返す
    def all_group_members(self):
        from collections import defaultdict
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return list(group_members.values())



n, m = map(int, input().split())
G = []
for i in range(m):
    a, b, w = map(int, input().split())
    G.append([w, a, b])

# Gの各辺を重みが小さい順にソートする
G.sort()
uf = UnionFind(n)
ans = 0

for i in range(m):
    w, a, b = G[i]

    # 辺(a, b)の追加によってサイクルが形成されるときは追加しない
    # aとbが同じ親を持っていれば，サイクルが生まれることになる
    if uf.same(a, b): continue

    # 辺(a, b)を追加する
    ans += w
    uf.unite(a, b)
print(ans)


#############################################################
# 65問目
# カテゴリ: 最小全域木問題
# タイトル: JOI 2010 春合宿 - Finals
# https://atcoder.jp/contests/joisc2010/tasks/joisc2010_finals
# 日時: 2020/11/13
##############################################################

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n # 自分が根の場合，根を-1と表記: 初期状態ではみんなバラバラなのでみんな-1

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # xとyが同じグループに属するかどうか (根が一致するかどうか)
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループとを併合する
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)

        # すでに同じグループのときは何もしない
        if x == y: return False

        # union by size (y側のサイズが小さくなるようにする: xとyをスワップする: xをyの親にしたい)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

# 方針
# クラスカル法でとりあえず最小全域木を求めながら，使用する道のコストを保存しておく
# 使用するコストの高い道が通じる都市を開催国とすれば，そのコストが浮く
# 例えば全部で5都市あって，コストが[6, 5, 4, 3]で，開催都市が3箇所であれば，[6, 5]を削って，残りのコストを総和を求めればいい

n, m, k = map(int, input().split())

G = []
for _ in range(m):
  a, b, c = map(int, input().split())
  G.append([c, a - 1, b - 1])
G.sort()

uf = UnionFind(n)
used = [] #使用する道のコストを保存
for i in range(m):
    c, a, b= G[i]

    if uf.same(a, b): continue
    else:
        uf.unite(a, b)
        used.append(c)

print(sum(used[::-1][k-1:]))

# Pypy3だとTLEだったけどPython3なら通った。謎
# 簡単だった


#############################################################
# 66問目
# カテゴリ: 最小全域木問題
# タイトル: AOJ 1127 - Building a Space Station
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1127
# 日時: 2020/11/13
##############################################################

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n # 自分が根の場合，根を-1と表記: 初期状態ではみんなバラバラなのでみんな-1

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # xとyが同じグループに属するかどうか (根が一致するかどうか)
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループとを併合する
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)

        # すでに同じグループのときは何もしない
        if x == y: return False

        # union by size (y側のサイズが小さくなるようにする: xとyをスワップする: xをyの親にしたい)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

###### 思ったこと/気づいたこと ######
# 問題文がわかりづらすぎて理解できない
# 重なってたら廊下はいらないってことかな？
# 任意の2点に着目して，2点の距離を図り，その距離が2点の半径の和より長ければ，2点は十分に離れてることになる。

###### 方針 ######
# とりあえず任意の2点間の距離を測り，半径の和を引く。もし負なら0にして，正ならそのまま扱い，それらを2点間の廊下の長さとする
# 廊下の長さを使ってクラスカル法を用いる

from math import sqrt

def solve(n):

    G = []
    for i in range(n):
        x, y, z, r = map(float, input().split())
        G.append([x, y, z, r])

    G2 = []
    for i in range(n):
        for j in range(i + 1, n):
            d = sqrt((G[i][0]-G[j][0])**2 + (G[i][1]-G[j][1])**2 + (G[i][2]-G[j][2])**2)
            w = max(d - (G[i][3] + G[j][3]), 0)
            G2.append([w, i, j])

    G2.sort()
    ans = 0
    uf = UnionFind(n)
    for i in range(len(G2)):
        w, a, b = G2[i]
        if uf.same(a, b): continue

        ans += w
        uf.unite(a, b)

    print('{:.03f}'.format(ans))

while True:
    n = int(input())
    if n == 0:
         break
    elif n == 1:
        x, y, z, r = map(float, input().split())
        print('0.000')
    else:
        solve(n)

# AC!
##### 反省 #####
# 出力が小数点3桁という特殊なやつなので，見逃してWA出した。ちゃんと問題読む。


#############################################################
# 67問目
# カテゴリ: 最小全域木問題
# タイトル: AtCoder Beginner Contest 065 D - Built?
# https://atcoder.jp/contests/abc065/tasks/arc076_b
# 日時: 2020/11/14
##############################################################

##### 思ったこと / 気づいたこと #####
# 問題文も短くて，パット見ではシンプルなクラスカル法で解けそう
# N=10**5だけど，普通に書いたら間に合わないのかな？とりあえず書いてみよう

##### 方針 #####
# 普通にクラスカル法で書いてみる
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n # 自分が根の場合，根を-1と表記: 初期状態ではみんなバラバラなのでみんな-1

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # xとyが同じグループに属するかどうか (根が一致するかどうか)
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループとを併合する
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)

        # すでに同じグループのときは何もしない
        if x == y: return False

        # union by size (y側のサイズが小さくなるようにする: xとyをスワップする: xをyの親にしたい)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True


n = int(input())
G = [[int(i) for i in input().split()] for _ in range(n)]

# 2点間の距離
G2 = []
for i in range(n):
    for j in range(i+1, n):
        w = min(abs(G[i][0]-G[j][0]), abs(G[i][1]-G[j][1]))
        G2.append([w, i, j])
G2.sort()
ans = 0
uf = UnionFind(n)

for i in range(len(G2)):
    w, a, b = G2[i]
    if uf.same(a, b): continue
    ans += w
    uf.unite(a, b)
print(ans)

# ここまで8分で書けたけどTLE
# 今はG2の線形探索でO(N^2)だけど，このサーチの部分で無駄があるし，そもそも2点間の距離図る2重ループの時点で間に合ってない
# 明らかに遠い2点同士は試す価値もないから，サーチの対象から外してよさそう

##### 方針 #####
# x, y軸を別々で見て，各軸でソートする
# 貪欲に隣合う点同士の距離を測って，「近い点同士の距離」というサイズnのリストをxとyについて作る。
# このリストには最低限見ればいい2点だけが凝縮されている。
# 2つのリストをガッちゃんこして，クラスカル法を用いる。
# これでO(N^2)


n = int(input())
G = []
for i in range(n):
    a, b = map(int, input().split())
    G.append([i, a, b]) # iは頂点のidとして扱う
Gx = sorted(G, key=lambda x: x[1])
Gy = sorted(G, key=lambda x: x[2])

dist_x = []
dist_y = []

for i in range(n-1):
    a = Gx[i][0]
    b = Gx[i+1][0]
    w = abs(Gx[i][1] - Gx[i+1][1])
    dist_x.append([w, a, b])

for i in range(n-1):
    a = Gy[i][0]
    b = Gy[i + 1][0]
    w = abs(Gy[i][2] - Gy[i + 1][2])
    dist_y.append([w, a, b])

G2 = dist_x + dist_y
G2.sort()
ans = 0
uf = UnionFind(n)

for i in range(len(G2)):
    w, a, b = G2[i]
    if uf.same(a, b): continue
    ans += w
    uf.unite(a, b)
print(ans)

# 35分で解けた！！！！！！ 初見で！！！！


##### 解答時間 #####
# 35分

##### 感想/反省 #####
# 距離の定義が特殊だからこそ適用できる方法だった。問題を考えた人とても賢い。
# オーダー的に間に合わないとわかっておきながら一度愚直にO(N^2)のクラスカル法を書いたが，
# 本番だと時間の無駄なので，一発で書く練習はした方がいい


##############################################################
# 68問目
# カテゴリ: 素因数分解
# タイトル: NTL_1_A - 素因数分解
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A&lang=ja
# 日時: 2020/11/14
##############################################################

##### 思ったこと / 気づいたこと #####
# エラトステネスのwikiの通りに書いてみよう
# https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9#:~:text=%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9%20(%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE,%E5%8D%98%E7%B4%94%E3%81%AA%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A7%E3%81%82%E3%82%8B%E3%80%82

##### 方針 #####
# ステップ 1: 探索リストに2からxまでの整数を昇順で入れる。
# ステップ 2: 探索リストの先頭の数を素数リストに移動し、その倍数を探索リストから篩い落とす。
# ステップ 3: 上記の篩い落とし操作を探索リストの先頭値がxの平方根に達するまで行う。
# ステップ 4: 探索リストに残った数を素数リストに移動して処理終了。

# とりあえず素数のリストを手に入れて，nをどんどん割っていく方法で書いてみる
# 参考: https://oku.edu.mie-u.ac.jp/~okumura/python/sieve.html

##### 解答 #####

n = int(input())
ans = f'{n}:'

def prime_sieve(n):
    # エラトステネスの篩: n以下の素数を見つける方法
    # 参考: https://oku.edu.mie-u.ac.jp/~okumura/python/sieve.html
    sq = int(n ** 0.5) + 1
    prime = [False] * 2 + [True] * (n-1) # 素数のboolリストを作る。最初の2マス(0と1)は素数でないのでFalse。

    for i in range(sq):
        if prime[i]:
            for j in range(i*2, n+1, i): # 素数の倍数倍は素数ではないので，Falseにする
                prime[j] = False

    return [i for i in range(n+1) if prime[i]]

prime = prime_sieve(n)
# エラトステネスで得られた素数で試し割りしていく
factors = []
for p in prime:
    if n == 1: break  # nを割り終わったらbreak
    while n % p == 0:  # nを素数で割り切れるなら，それがnの素因数
        factors.append(p)
        n //= p


for f in factors:
    ans += f' {f}'
print(ans)

# エラトステネス＋試し割り法だと遅くてTLE!! そもそもエラトステネスが遅いので，いらなさそう。
# でも勉強になった
# 普通の速い試し割りがこれ (wikiより)

n = int(input())
ans = f'{n}:'

def prime_factorize(n: int):
    # 試し割り法による素因数分解
    # https://en.wikipedia.org/wiki/Trial_division
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    f = 3 # 奇数でどんどん割っていって，素数を探す。
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f # nをfで割って減らす。
        else:
            f += 2 # 奇数なので+2ずつ足していく。
    if n != 1: factors.append(n)
    # Only odd number is possible
    return factors

factors = prime_factorize(n)
for f in factors:
    ans += f' {f}'
print(ans)

##### 解答時間 #####
# 勉強したので1時間以上かかった

##### 感想/反省 #####
# nが大きいときはエラトステネスが超遅いので，単純に素因数分解したときはシンプルな試し割りでいい


##############################################################
# 69問目
# カテゴリ: 素因数分解
# タイトル: AtCoder Beginner Contest 084 D - 2017-like Number
# https://atcoder.jp/contests/abc084/tasks/abc084_d
# 日時: 2020/11/14
##############################################################

##### 思ったこと / 気づいたこと #####
# n<=100000だから，まず「2017に似た数」をすべて列挙すれば良さそう
# 奇数全部試さなくても，nも素数なんだから，エラトステネスで素数リスト手に入れればいい


##### 方針 #####
# 100000までの素数のリストをエラトステネスで用意する: 10000個くらい (ハッシュで用意する)
# 素数リストの要素をループで回し，(n+1)//2も素数リストに入ってるものをピックアップする (like2017)
# 入力に対して個数を答える

##### 解答 #####
def prime_sieve(n):
    # エラトステネスの篩
    # 参考: https://oku.edu.mie-u.ac.jp/~okumura/python/sieve.html
    sq = int(n ** 0.5)
    prime = [False] * 2 + [True] * (n-1) # 素数のboolリストを作る。最初の2マス(0と1)は素数でないのでFalse。

    for i in range(sq):
        if prime[i]:
            for j in range(i*2, n+1, i): # 素数の倍数倍は素数ではないので，Falseにする
                prime[j] = False

    return [i for i in range(n+1) if prime[i]]

prime = set(prime_sieve(100000))

like2017 = []
for p in prime:
    if (p+1)//2 in prime:
        like2017.append(p)
like2017.sort()

# 入力を受け取る
n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    print(len([i for i in like2017 if l <= i and i <= r]))



##### 解答時間 #####
# 15分

##### 感想/反省 #####
# 一発ACだった。
# 最初に2017 like-numberを全て出しておくというのが味噌だった。思いついてよかった。

##### 問題カテゴリタグ #####
#素因数分解



##############################################################
# 70問目
# カテゴリ: 高速なべき乗計算
# タイトル: NTL_1_B - べき乗
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_B&lang=ja
# 日時: 2020/11/14
##############################################################

# 方針
# とりあえずm**n % modで出してみよう
mod = 1000000007
m, n = map(int, input().split())
print(m**n % mod)

# 39 5325621 みたいなケースでTLE!!!!
# ループで毎回modしてみようかと思ったけど10億回ループになるから無理
# 「高速なべき乗計算」でググった: https://kazu-yamamoto.hatenablog.jp/entry/20090223/1235372875
# nを2進数で表して，桁に対応して「2の桁乗」の和がnになっている，というアイデア

mod = 10**9 + 7
m, n = map(int, input().split())

m = 3
n = 13

def power(m, n):
    # a = m**n: mのn乗の計算
    bit_n = bin(n)[2::] # nを2進数で表す
    ans = 1
    for i in range(len(bit_n)):
        if bit_n[::-1][i] == '1':
            a = m ** (2 ** i) % mod
            ans = ans * a % mod
    return ans

# これだと結局 m ** (2 ** i) の計算で時間をつかってるので，ダメ
# 二乗の計算を溜め込む必要がある
# 参考: https://algo-logic.info/calc-pow/
# 参考: https://tex2e.github.io/blog/crypto/montgomery-ladder



m, n = map(int, input().split())
def power(m, n):
    """ m**n: mのn乗の計算をする関数 """
    mod = 10 ** 9 + 7
    bit_n = bin(n)[2::] # nを2進数で表す
    m2 = m # m2**2 -> (m2**2)**2 -> ((m2**2)**2)**2 と溜め込んでいく
    ans = 1

    # 2進数で桁が1になっていれば，現在のm2をansにかけていく
    for i in range(len(bit_n)):
        if bit_n[::-1][i] == '1':
            ans = ans * m2 % mod
        m2 = m2 ** 2 % mod
    return ans
print(power(m, n))


# アイデアは頂いてから，なんとか自力でかけた！
# nを2進数で表して，桁に対応して「2の桁乗」の和がnになっている

# なんと，Pythonではこんな簡単に書ける。powerなんていらない!!
mod = 1000000007
m, n = map(int, input().split())
print(pow(m, n, mod))



##############################################################
# 71問目
# カテゴリ: 高速なべき乗計算
# タイトル: Square869120Contest #1 E - 散歩
# https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_e
# 日時: 2020/11/14
##############################################################

##### 思ったこと / 気づいたこと #####
# 単純にべき乗計算すればよさそう

##### 方針 #####
# まず最初に全ての隣合う街の距離をリスト(dist)として作っておく
# 街xから街yに行く場合はdist[x:y]が対応する距離なので，その和を取る。
# ansにインクリメントしてく


##### 解答 #####
mod = 10 ** 9 + 7
def power(m, n):
    """ m**n: mのn乗の計算をする関数 """
    bit_n = bin(n)[2::] # nを2進数で表す
    m2 = m # m2**2 -> (m2**2)**2 -> ((m2**2)**2)**2 と溜め込んでいく
    ans = 1

    # 2進数で桁が1になっていれば，現在のm2をansにかけていく
    for i in range(len(bit_n)):
        if bit_n[::-1][i] == '1':
            ans = ans * m2 % mod
        m2 = m2 ** 2 % mod
    return ans

n, q = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
c = [i-1 for i in c]
c = [0] + c +[0]

dist = []
for i in range(n-1):
    dist.append(power(a[i], a[i+1]))

ans = 0
for i in range(q+1):
    # 街xから街yに行く
    x = c[i]
    y = c[i+1]

    # 大きい方を右にしたい
    if x > y:
        x, y = y, x

    ans += sum(dist[x:y]) % mod

print(ans)

# サンプルは全部正解なのに，なぜかWA
# 解説: https://img.atcoder.jp/data/other/s8pc-1/s8pc-1-E.pdf
# Pythonの解答を見てみよう: https://atcoder.jp/contests/s8pc-1/submissions/18078403
# 最後のループでsumを繰り返さないために累積和を使ってる

n, q =map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))+[1]
Amul=[pow(a[i-1], a[i], mod) for i in range(1,n)]
import itertools
Aacc=[0]+list(itertools.accumulate(Amul))
point,ans=0,0
for i in c:
    ans = (ans + abs(Aacc[i-1] - Aacc[point]) % mod) % mod
    point=i-1
print(ans)


# なんか色々いじってみよう
# powで行ける + 累積和を実施してみる +

mod = 10 ** 9 + 7

n, q = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
c = [i-1 for i in c]
c = [0] + c + [0]

dist = [pow(a[i-1], a[i], mod) for i in range(1,n)] # powで書ける

# 累積和
from itertools import accumulate
acum = [0] + list(accumulate(dist))

ans = 0
for i in range(q+1):
    ans = (ans + abs(acum[c[i]] - acum[c[i+1]])) % mod
print(ans)


##### 解答時間 #####
# 解答見た

##### 感想/反省 #####
# modを入れる場所がおかしかった！！！！！！！！！！！！
# modのときは+=は使ってはならない！！！！！！！
# だめな例: ans += abs(acum[c[i]] - acum[c[i+1]])) % mod
# OKな例: ans = (ans + abs(acum[c[i]] - acum[c[i+1]])) % mod
# 累積和を思いつかなかったので，もしmodの場所が合ってたとしても不正解だった。
# もう一度ときたい。いい問題だった


##### 問題カテゴリタグ #####
#べき乗 #累積和



##############################################################
# 72問目
# カテゴリ: 逆元を使う問題
# タイトル: AtCoder Beginner Contest 034 C - 経路
# https://atcoder.jp/contests/abc034/tasks/abc034_c
# 日時: 2020/11/14
##############################################################

# 初めての逆元
# とりあえず愚直に組み合わせの数を計算してmodしてみる

mod = 10 ** 9 + 7
w, h = map(int, input().split())
from scipy.special import comb
print(comb((w+h-2), w-1, exact=True) % mod)

# TLE !!
# 解説で逆元を勉強: https://www.slideshare.net/chokudai/abc034
# なにかをbで割った時のmod pはb**(p-2)でかけて mod pしたのと同じ (フェルマーの小定理)

mod = 10 ** 9 + 7
w, h = map(int, input().split())

a = 1
for i in range(1, w+h-1):
    a = a * i % mod

for i in range(1, w):
    a = (a * pow(i, mod-2, mod)) % mod

for i in range(1, h):
    a = (a * pow(i, mod-2, mod)) % mod
print(a)

# AC!!!
# ライブラリにしてみよう

def inverse_mod(n, r, mod):
    ans = 1
    for i in range(1, n):
        ans = ans * i % mod
    for i in range(1, r):
        ans = (ans * pow(i, mod - 2, mod)) % mod
    for i in range(1, n-r+1):
        ans = (ans * pow(i, mod - 2, mod)) % mod
    return ans


##############################################################
# 73問目
# カテゴリ: 逆元を使う問題
# タイトル: AtCoder Beginner Contest 145 D - Knight
# https://atcoder.jp/contests/abc145/tasks/abc145_d
# 日時: 2020/11/14
##############################################################

##### 思ったこと / 気づいたこと #####
# 上の問題と同じやんと思ったら桂馬の動き方だった
# x+y=3k かつ x/y <= 2 かつ y/x <= 2の場所にはおける
# 30分考えてわからなかったのでギブアップ
# 解説: https://img.atcoder.jp/abc145/editorial.pdf
# (1, 2)の移動をn回，(2, 1)の移動をm回とすると連立方程式が建てられる
# X = n+2m, Y=2n+m，これを解くと
# n = (2Y-X)//3, m = (2X-Y)//3
# このn, mを使って組み合わせの数を求める: (n+m)C(n)

##### 方針 #####
# パターン分けで行けそう?

##### 解答 #####
mod = 10 ** 9 + 7
def comb_mod(n, r, mod):
    """powを用いて(nCr) mod p を求める"""
    ans = 1
    for i in range(1, n+1):
        ans = ans * i % mod
    for i in range(1, r+1):
        ans = (ans * pow(i, mod - 2, mod)) % mod
    for i in range(1, n-r+1):
        ans = (ans * pow(i, mod - 2, mod)) % mod
    return ans

x, y = map(int, input().split())
if (x+y) % 3 != 0:
    print(0)
    exit()

n = (2*y-x)//3
m = (2*x-y)//3
if n < 0 or m < 0:
    print(0)
    exit()

ans = comb_mod(n+m, n, mod)
print(ans)


##### 解答時間 #####
# 考察＋解答見てから自力ACまで1時間以上かかった

##### 感想/反省 #####
# 数学的考察が思いつかなかった
# この自力で書いた関数で乗り切っていいのか？

##### 問題カテゴリタグ #####
#逆元 #組み合わせ

# こんなコードもあったけど，これだとfactorialの大きさがでかくなりすぎてだめだった。自分で書いたのが良さそう
def comb(n, r, mod):
    # https://wakabame.hatenablog.com/entry/2017/09/21/211357
    """powを用いて(nCr) mod p を求める"""
    from math import factorial
    if n < 0 or r < 0 or n < r: return 0
    if n == 0 or r == 0: return 1
    a = factorial(n) % mod
    b = factorial(r) % mod
    c = factorial(n-r) % mod

    return (a*pow(b, mod-2, mod)*pow(c, mod-2, mod)) % mod



##############################################################
# 74問目
# カテゴリ: 逆元を使う問題
# タイトル: AtCoder Beginner Contest 021 D - 多重ループ
# https://atcoder.jp/contests/abc021/tasks/abc021_d
# 日時: 2020/11/14
##############################################################

##### 思ったこと / 気づいたこと #####
# 30分考えてわからんかった
# 解説: https://www.slideshare.net/chokudai/abc021
# 重複組合せ: n個から重複を許してk個選ぶ
# これは「k個の○とn-1個の仕切りを一列に並べる」と同じ
# (n+k-1)C(k)で計算できる

##### 解答 #####
mod = 10**9+7
n = int(input())
k = int(input())

mod = 10 ** 9 + 7
def comb_mod(n, r, mod):
    """powを用いて(nCr) mod p を求める"""
    ans = 1
    for i in range(1, n+1):
        ans = ans * i % mod
    for i in range(1, r+1):
        ans = (ans * pow(i, mod - 2, mod)) % mod
    for i in range(1, n-r+1):
        ans = (ans * pow(i, mod - 2, mod)) % mod
    return ans

print(comb_mod(n+k-1, k, mod))

##### 解答時間 #####
# 30分かけて解答みた

##### 感想/反省 #####
# 重複組合せをググればよかった。
# 逆元の関数はそのまま活用できた。

##### 問題カテゴリタグ #####
#逆元 #重複組合せ


##############################################################
# 75問目
# カテゴリ: 逆元を使う問題
# タイトル: AtCoder Beginner Contest 149 F - Surrounded Nodes
# https://atcoder.jp/contests/abc149/tasks/abc149_f
# 日時: 2020/11/14
##############################################################

##### 思ったこと / 気づいたこと #####
# 絵を色々書いてみたけど，各パターンにおいての穴あき度を計算する方法が思いつかない
# 解答見た: https://img.atcoder.jp/abc149/editorial.pdf


##############################################################
# 76問目
# カテゴリ: 累積和
# タイトル: 全国統一プログラミング王決定戦本戦 A - Abundant Resources
# https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a
# 日時: 2020/11/14
##############################################################


##### 方針 #####
# とりあえず累積和を取ってみる
# itertoolsのaccumulate関数を使いたい
# 連続するk個を取ったときの

##### 解答 #####
from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
cum = [0] + list(accumulate(a))

for k in range(1, n+1):
    ans = 0
    for i in range(1, n-k+2):
        ans = max(ans, cum[i+k-1]-cum[i-1])
    print(ans)


##### 解答時間 #####
# 20分くらい

##### 感想/反省 #####
# 添字が地獄のよう。試行錯誤しまくった


##### 問題カテゴリタグ #####
#累積和

# もう少しきれいに書きたい
# 参考に: https://atcoder.jp/contests/nikkei2019-final/submissions/17600475
from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
cum = [0] + list(accumulate(a))

for k in range(1, n+1):
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, cum[i+k]-cum[i])
    print(ans)


##############################################################
# 77問目
# カテゴリ: 累積和
# タイトル: JOI 2010 本選 1 - 旅人
# https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_a
# 日時: 2020/11/14
##############################################################

##### 解答 #####
mod = 10**5
n, m = map(int, input().split())
s = [int(input()) for i in range(n-1)]
a = [int(input()) for i in range(m)]

from itertools import accumulate
cum = [0] + list(accumulate(s)) # cumsum
pos = [0] + list(accumulate(a)) # position

ans = 0
now = 0
for i in range(m):
    d = abs(cum[pos[i + 1]] - cum[pos[i]]) % mod
    ans = (ans + d) % mod

print(ans)



##### 解答時間 #####
# 30分くらい: 一応自力でAC

##### 感想/反省 #####
# 移動距離だけじゃなくて座標の累積も必要であることに気づくのに時間がかかった
# 出力が10**5で割る必要があることに気づかなかった

##### 問題カテゴリタグ #####
#累積和


##############################################################
# 78問目
# カテゴリ: 累積和
# タイトル: JOI 2011 本選 1 - 惑星探査
# https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho1
# 日時: 2020/11/14
##############################################################

##### 思ったこと / 気づいたこと #####
# 累積するものがJ,O,Iの三種類あるのが大変
# J, O, Iの累積のテーブルは分けなきゃいけないっぽい
# 行ごとor列ごとに集計してテーブル作る
# 入力Kが10万もあったら，一気にリストに溜め込んでしまうとメモリオーバーになるのでは？

##### 方針 #####
# まずは累積和のテーブルを作る
#

##### 解答 #####

m, n = map(int, input().split())
k = int(input())
joi = [str(input()) for i in range(m)]
G = [[int(i) for i in input().split()] for _ in range(k)]


I = [[0]*(n+1) for _ in range(m)]
O = [[0]*(n+1) for _ in range(m)]
J = [[0]*(n+1) for _ in range(m)]

for i in range(m):
    for j in range(1, n+1):
        if joi[i][j-1] == 'I':
            I[i][j] = 1
        elif joi[i][j-1] == 'O':
            O[i][j] = 1
        elif joi[i][j-1] == 'J':
            J[i][j] = 1

        I[i][j] += I[i][j - 1]
        O[i][j] += O[i][j - 1]
        J[i][j] += J[i][j - 1]



def counter(m1, n1, m2, n2, JOI):
    ans = 0
    for i in range(m1, m2+1):
        ans += JOI[i][n2+1]-JOI[i][n1]
    return ans

for g in G:
    m1, n1, m2, n2 = [i-1 for i in g]
    ans_i = counter(m1, n1, m2, n2, I)
    ans_o = counter(m1, n1, m2, n2, O)
    ans_j = counter(m1, n1, m2, n2, J)
    print(ans_j, ans_o, ans_i)

############################################
# TLEでした。たぶん二次元に累積する必要がある。
############################################

m, n = map(int, input().split())
k = int(input())
joi = [str(input()) for i in range(m)]
G = [[int(i) for i in input().split()] for _ in range(k)]

def cumsum_joi(JOI):
    # 二次元の累積和: https://qiita.com/drken/items/56a6b68edef8fc605821
    cum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if joi[i-1][j-1] == JOI:
                cum[i][j] = cum[i][j - 1] + cum[i - 1][j] - cum[i - 1][j - 1] + 1
            else:
                cum[i][j] = cum[i][j - 1] + cum[i - 1][j] - cum[i - 1][j - 1]
    return cum
J = cumsum_joi('J')
O = cumsum_joi('O')
I = cumsum_joi('I')

def counter(m1, n1, m2, n2, JOI):
    return JOI[m2][n2] - JOI[m2][n1-1] - JOI[m1-1][n2] + JOI[m1-1][n1-1]
for g in G:
    m1, n1, m2, n2 = g
    ans_j = counter(m1, n1, m2, n2, J)
    ans_o = counter(m1, n1, m2, n2, O)
    ans_i = counter(m1, n1, m2, n2, I)
    print(ans_j, ans_o, ans_i)


#################################################
# できたけど多分グラフがでかすぎる。入力ごとに出力しよう
#################################################
from sys import stdin
m, n = map(int, input().split())
k = int(input())
joi = [str(stdin.readline()) for i in range(m)]

def cumsum_joi(JOI):
    # 二次元の累積和: https://qiita.com/drken/items/56a6b68edef8fc605821
    cum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if joi[i-1][j-1] == JOI:
                cum[i][j] = cum[i][j - 1] + cum[i - 1][j] - cum[i - 1][j - 1] + 1
            else:
                cum[i][j] = cum[i][j - 1] + cum[i - 1][j] - cum[i - 1][j - 1]
    return cum
J = cumsum_joi('J')
O = cumsum_joi('O')
I = cumsum_joi('I')

def counter(m1, n1, m2, n2, JOI):
    return JOI[m2][n2] - JOI[m2][n1-1] - JOI[m1-1][n2] + JOI[m1-1][n1-1]
for _ in range(k):
    m1, n1, m2, n2 = list(map(int, stdin.readline().split()))
    ans_j = counter(m1, n1, m2, n2, J)
    ans_o = counter(m1, n1, m2, n2, O)
    ans_i = counter(m1, n1, m2, n2, I)
    print(ans_j, ans_o, ans_i)



##### 解答時間 #####
# 1時間以上考えて3つ解答書いて，TLE．つらい
# https://kakedashi-engineer.appspot.com/2020/06/20/joi2011hoa/
# PythonでもPypyでも厳しい問題らしい。この人と解答は全く同じっぽい。

##### 感想/反省 #####
# オーダー的には間に合いそうなのに，実際にはループが遅いっぽくてTLE
# numpyで上手いこと書く必要がある。
# 累積和はnumpyつかった方がよさそう。
# ぱっと調べた感じ，この問題に合うような二次元の累積和の関数はnumpyにはなさそう

##### 問題カテゴリタグ #####
#累積和 #二次元累積和 #itertools.accumulation




##############################################################
# 79問目
# カテゴリ: 累積和
# タイトル: AtCoder Beginner Contest 106 D - AtCoder Express 2
# https://atcoder.jp/contests/abc106/tasks/abc106_d
# 日時: 2020/11/16
##############################################################

##### 思ったこと / 気づいたこと #####
# 要素(n+1)の配列を作って，区間lrに+1していく？とか思ったけど意味わからんすぎて解答見た
# https://img.atcoder.jp/abc106/editorial.pdf

##### 方針 #####
# LRの二次元配列をつくる


##### 解答 #####
import numpy as np
n, m, Q = map(int, input().split())
LR = [[int(i) for i in input().split()] for _ in range(m)]
pq = [[int(i) for i in input().split()] for _ in range(Q)]

cum = np.zeros((n+1, n+1), int)
for l, r in LR:
    cum[l][r] += 1

for i in range(1, n+1):
    for j in range(1, n+1):
        cum[i][j] = cum[i][j] + cum[i][j - 1] + cum[i - 1][j] - cum[i - 1][j - 1]

for p, q in pq:
    ans = cum[q][q] - cum[p-1][q] - cum[q][p-1] + cum[p-1][p-1]
    print(ans)


##### 解答時間 #####
# 解説見て解法知ってからは10分くらい

##### 感想/反省 #####
# 二次元累積和の使い方がわからなくて解説を見てしまった。
# コーディング的には二次元の扱いになれてきた。

##### 問題カテゴリタグ #####
#累積和 #二次元累積和


##############################################################
# 80問目
# カテゴリ: 累積和
# タイトル: GigaCode 2019 D - 家の建設
# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_d
# 日時: 2020/11/16
##############################################################

##### 思ったこと / 気づいたこと #####
#

##### 方針 #####
# ステップ1: まず土地代の2次元累積和を作る
# ステップ2: 4重ループで，土地の始まりと終わりを管理して，コストを計算する

##### 解答 #####

H, W, K, V = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]

cum = [[0]*(W+1) for _ in range(H+1)]
for i in range(1, H+1):
    for j in range(1, W+1):
        cum[i][j] = A[i-1][j-1] + cum[i][j - 1] + cum[i - 1][j] - cum[i - 1][j - 1]

ans = 0
for i1 in range(1, H+1):
    for j1 in range(1, W+1):
        for i2 in range(i1, H+1):
            for j2 in range(j1, W+1):
                S = (i2+1-i1)*(j2+1-j1)
                cost = cum[i2][j2] - cum[i1-1][j2] - cum[i2][j1-1] + cum[i1-1][j1-1]
                total = cost + S*K
                if total <= V:
                    ans = max(ans, S)
print(ans)

##### 解答時間 #####
# 20分くらい?

##### 感想/反省 #####
# 最悪2億ループだったので，PythonだとTLEでPypyだと通った
# 1個前の問題と違って，二次元累積和の使い方が明らかだったので，初見で解けた。
# 二次元累積和は一次元にくらべてバグらないから好き。

##### 問題カテゴリタグ #####
#累積和 #二次元累積和



##############################################################
# 81問目
# カテゴリ: 累積和: いもす法
# タイトル: AtCoder Beginner Contest 014 C - AtColor
# https://atcoder.jp/contests/abc014/tasks/abc014_3
# 日時: 2020/11/17
##############################################################

##### 思ったこと / 気づいたこと #####
# 普通のimos法やん

##### 方針 #####
# 区間[l, r]にaを追加したいとき，配列imosを用意して
# ステップ1: imos[l] += a
# ステップ2: imos[r+1] -= a
# ステップ3: imosの累積和を取る (ここまでimos法)
# ステップ4: 累積和のmaxを取る

##### 解答 #####
from itertools import accumulate
n = int(input())
ab = [[int(i) for i in input().split()] for _ in range(n)]

imos = [0] * 1000003
for a, b in ab:
    imos[a] += 1
    imos[b+1] -= 1

cum = list(accumulate(imos))
print(max(cum))


##### 解答時間 #####
# 3分

##### 感想/反省 #####
# こんな複雑なことを一瞬でやってのけるimos法凄い

##### 問題カテゴリタグ #####
#imos法 #累積和 #


##############################################################
# 82問目
# カテゴリ: 累積和: いもす法
# タイトル: AOJ 2013 - 大崎
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2013
# 日時: 2020/11/17
##############################################################

##### 思ったこと / 気づいたこと #####
# ただのいもす法だけど，入力が面倒くさい
# 時刻を0時から何秒たったかで表現するとよさそう

##### 方針 #####
# 入力を0時からの秒に直す関数を用意
# 要素数3600*60のimos配列を用意
# imos法を用いてmaxを求める

##### 解答 #####
from itertools import accumulate

def solve(n):
    time = []

    def to_second(t):
        t = t.split(':')
        h = int(t[0])*3600
        m = int(t[1]) * 60
        s = int(t[2])

        return h+m+s

    for _ in range(n):
        a, b = input().split()
        a = to_second(a)
        b = to_second(b)
        time.append([a, b])

    imos = [0]*3600*91
    for a, b in time:
        imos[a] += 1
        imos[b] -= 1

    cum = accumulate(imos)
    print(max(cum))

while True:
    n = int(input())
    if n == 0:
        break
    solve(n)

##### 解答時間 #####
# 12分

##### 感想/反省 #####
# 1-3時の便と3-4時の便は被っても問題ないので，imosのステップ2ではimos[b+1] -= 1ではなくimos[b] -= 1である必要があった。これでWA

##### 問題カテゴリタグ #####
#いもす法 #累積和 #入力が特殊


##############################################################
# 83問目
# カテゴリ: 累積和: いもす法
# タイトル: JOI 2015 本選 1 - 鉄道運賃
# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_a
# 日時: 2020/11/17
##############################################################

##### 思ったこと / 気づいたこと #####
# まず各鉄道にのる回数をいもす法で求めて，ICかきっぷかどっちが安いか判断する

##### 方針 #####
# まず旅程Pだけ使って，各鉄道に乗る回数をimos法で求める
# 各鉄道における「乗車回数*きっぷの価格」と「ICカード+IC乗車価格*乗車回数」を比較する


##### 解答 #####
from itertools import accumulate
n, m = map(int, input().split())
P = list(map(int, input().split()))
P = [i-1 for i in P]
ABC = [[int(i) for i in input().split()] for _ in range(n-1)]

imos = [0]*1000009
for i in range(m-1):
    p1 = P[i]
    p2 = P[i+1]

    # iからi+1もi+1からiも同じ価格なので，p1を小さくしたい
    if p1 > p2:
        p1, p2 = p2, p1

    imos[p1] += 1
    imos[p2] -= 1
cum = list(accumulate(imos))

price = [0]*1000009
for i in range(n-1):
    a, b, c = ABC[i]
    # きっぷとICを比較
    price[i] = min(a*cum[i], c+b*cum[i])
print(sum(price))

##### 解答時間 #####
# 30分

##### 感想/反省 #####
# 毎回imos配列の大きさを間違えるので，ちゃんと問題文を読んで確かめる


##### 問題カテゴリタグ #####
#いもす法 #累積和


##############################################################
# 84問目
# カテゴリ: 累積和: いもす法
# タイトル: JOI 2012 本選 4 - 釘
# https://atcoder.jp/contests/joi2012ho/tasks/joi2012ho4
# 日時: 2020/11/17
##############################################################

##### 思ったこと / 気づいたこと #####
# 配列をどうもたせるかが悩みどころ
# N＜＝5000, M <= 500000なので，O(M)で回す必要がありそう
# 二次元の三角形の座標を一次元に変換する必要がありそう。それか二次元のimos配列を作るか。
# 解答みた: https://www.ioi-jp.org/joi/2011/2012-ho-prob_and_sol/2012-ho-t4-review.pdf
# out of my abilityという感じ


##### 方針 #####
#

##### 解答 #####

##### 解答時間 #####
# 諦めた

##### 感想/反省 #####
# これこそ紙で時間かけて考察する必要がある問題だった
# 二次元の正方形の座標に，三角形の座標を移して考える

##### 問題カテゴリタグ #####
#


##############################################################
# 85問目
# カテゴリ: Union-Find
# タイトル: DSL_1_A - 互いに素な集合
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=ja
# 日時: 2020/11/12
##############################################################

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n # 自分が根の場合，根を-1と表記: 初期状態ではみんなバラバラなのでみんな-1

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # xとyが同じグループに属するかどうか (根が一致するかどうか)
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループとを併合する
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)

        # すでに同じグループのときは何もしない
        if x == y: return False

        # union by size (y側のサイズが小さくなるようにする: xとyをスワップする: xをyの親にしたい)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    # xを含むグループのサイズ
    def size(self, x):
        return self.siz[self.root(x)]

    # グループ数を返す
    def group_count(self):
        parents = [i for i, x in enumerate(self.par) if x == -1]
        return len(parents)

    # 各グループに属する要素をリストで返す
    def all_group_members(self):
        from collections import defaultdict
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return list(group_members.values())


for i, x in enumerate(uf.par):
    print(i, x)

n, k = map(int, input().split())
uf = UnionFind(n)

for _ in range(k):
    c, x, y = map(int, input().split())
    if c == 0:
        uf.unite(x, y)
    else:
        if uf.same(x, y): print(1)
        else: print(0)

# Union-Find理解した！
# AC!!






##############################################################
# 86問目
# カテゴリ: Union-Find
# タイトル: AtCoder Beginner Contest 075 C - Bridge
# https://atcoder.jp/contests/abc075/tasks/abc075_c?lang=ja
# 日時: 2020/11/12
##############################################################

# 方針
# 各辺ごとにループを回して，辺がないことにしてunion-findする。
# もし親が2種類あれば非連結になってしまうので，その辺が橋だと判断できる

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n # 自分が根の場合，根を-1と表記: 初期状態ではみんなバラバラなのでみんな-1

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # xとyが同じグループに属するかどうか (根が一致するかどうか)
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループとを併合する
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)

        # すでに同じグループのときは何もしない
        if x == y: return False

        # union by size (y側のサイズが小さくなるようにする: xとyをスワップする: xをyの親にしたい)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    # xを含むグループのサイズ
    def size(self, x):
        return self.siz[self.root(x)]

    # グループ数を返す
    def group_count(self):
        parents = [i for i, x in enumerate(self.par) if x == -1]
        return len(parents)

    # 各グループに属する要素をリストで返す
    def all_group_members(self):
        from collections import defaultdict
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return list(group_members.values())


n, m = map(int, input().split())
e = [[int(i)-1 for i in input().split()] for _ in range(m)]

ans = 0
# 各頂点を除いてunion-findする
for i in range(m):
    e_ = e[:]
    e_.pop(i)

    # Union-findで各辺を連結させる
    uf = UnionFind(n)
    for a, b in e_:
        uf.unite(a, b)

    # グループ数が1より多い，つまり非連結成分が2以上あれば，消し去った辺が橋なので，カウントする
    if uf.group_count() > 1:
        ans += 1
print(ans)


# AC!!!


##############################################################
# 87問目
# カテゴリ: Union-Find
# タイトル: AtCoder Beginner Contest 120 D - Decayed Bridge
# https://atcoder.jp/contests/abc120/tasks/abc120_d
# 日時: 2020/11/12
##############################################################

# 方針
# 橋を崩壊させるごとにUnion-findして，島が属するグループを作り上げる
# グループの数とグループ内の要素数から，互いに行き来できない島の組み合わせを数え上げる (どうやって？)
from scipy.special import comb


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.siz = [1] * n
        self.par = [-1] * n # 自分が根の場合，根を-1と表記: 初期状態ではみんなバラバラなのでみんな-1

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # xとyが同じグループに属するかどうか (根が一致するかどうか)
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループとを併合する
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)

        # すでに同じグループのときは何もしない
        if x == y: return False

        # union by size (y側のサイズが小さくなるようにする: xとyをスワップする: xをyの親にしたい)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    # xを含むグループのサイズ
    def size(self, x):
        return self.siz[self.root(x)]

    # グループ数を返す
    def group_count(self):
        parents = [i for i, x in enumerate(self.par) if x == -1]
        return len(parents)

    # 各グループに属する要素をリストで返す
    def all_group_members(self):
        from collections import defaultdict
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return list(group_members.values())

n, m = map(int, input().split())
e = [[int(i)-1 for i in input().split()] for _ in range(m)]

for _ in range(m):
    e.pop(0) # 順番に橋が崩壊する

    # Union-findで各島をグループ化
    uf = UnionFind(n)
    for a, b in e:
        uf.unite(a, b)

    # グループごとの島番号のリスト
    group = uf.all_group_members()
    if len(group) == 1: # もしグループが1つなら0を出力
        print(0)
    else:
        ans = 0
        # 異なる2つのグループをpick upして，要素数をかけ合わせる。これを全グループの組み合わせ行う
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                ans += len(group[i])*len(group[j])
        print(ans)

# n <= 10**5なので，最後の組み合わせの計算でO(10億)になってTLE
# 解答見た: https://img.atcoder.jp/abc120/editorial.pdf
# まず，辺を消し去るより，辺を足していく方針が良いっぽい (逆で考える)
# 辺を加えたとき，連結の変化には2パターンある
# パターン1. ある辺e=(a, b)を加えることで，非連結だったグループ同士がくっつく
# パターン2. 何もかわらない


n, m = map(int, input().split())
e = [[int(i)-1 for i in input().split()] for _ in range(m)]

# 参考解答: https://atcoder.jp/contests/abc120/submissions/10913807
# 畏すぎる
uf = UnionFind(n) # Union-findの初期化
k = []
for a, b in e[::-1]: # 入力の辺をひっくり返す
    ra = uf.root(a)
    rb = uf.root(b)
    if ra == rb: # 頂点同士の親が同じならば，辺を足しても意味がないので，kに0を加える
        k.append(0)
    else: # 頂点同士が違うなら，お互いの属するグループの要素数の積が，新たに訪問できるようになる点の数となる
        k.append(uf.size(a)*uf.size(b))
        uf.unite(a, b)

ans = 0
for c in k[::-1]:
    ans += c
    print(ans)

# 解答が賢すぎた
# もう一度挑戦して自力で解いてみたい


##############################################################
# 91問目
# カテゴリ: その他のテクニック
# タイトル: AtCoder Beginner Contest 144 D - Water Bottle
# https://atcoder.jp/contests/abc144/tasks/abc144_d
# 日時: 2020/10/20
##############################################################

import math

a, b, x = list(map(int,input().split()))
if (a**2)*b*0.5 >= x:
    print(math.degrees(math.atan((a*(b**2)/(2*x)))))
else:
    print(math.degrees(math.atan((2*(a**2*b-x))/(a**3))))

# 図を書いたらいけた
# なす角がボトルの右側と左側どちらを指してるのかわかりづらい



##############################################################
# 95問目
# カテゴリ: 数学的な問題
# タイトル: AtCoder Beginner Contest 149 B - Greedy Takahashi
# https://atcoder.jp/contests/abc149/tasks/abc149_b
# 日時: 2020/10/21
##############################################################

a, b, k = list(map(int,input().split()))
rest = k-a
if rest > 0:
    print(f'{0} {max(b-rest, 0)}')
else:
    print(f'{a-k} {b}')

# 簡単だった



