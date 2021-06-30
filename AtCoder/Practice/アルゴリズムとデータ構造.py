########################################################################################
# アルゴリズムとデータ構造
# https://qiita.com/e869120/items/eb50fdaece12be418faa#2-3-%E5%88%86%E9%87%8E%E5%88%A5%E5%88%9D%E4%B8%AD%E7%B4%9A%E8%80%85%E3%81%8C%E8%A7%A3%E3%81%8F%E3%81%B9%E3%81%8D%E9%81%8E%E5%8E%BB%E5%95%8F%E7%B2%BE%E9%81%B8-100-%E5%95%8F
########################################################################################


# テンプレ

##############################################################
# 4章: p44
# 問題: 整数1からnまでの総和を再帰関数で書く
# 日時: 2020/10/13
##############################################################

def total(n):
    print(f'Call total({n})')
    if n == 0:
        return 0
    result = n + total(n - 1)
    print(f'Summation up to {n} = {result}')
    return result


total(10)


##############################################################
# 4章: p47
# 問題: ユークリッド互除法を再帰関数で書く
# 日時: 2020/10/13
##############################################################

# mをnで割ったときの余りをrとし，GCD(m, n)をmとnの最大公約数とすると
# GCD(m, n) = GCD(n, r) と表せる

def GCD_loop(m, n):
    while True:
        r = m % n
        if r == 0:
            break
        m = n
        n = r
    return n


GCD_loop(51, 15)


def GCD_recursive(m, n):
    print(f'Call GCD_recursive({m}, {n})')
    r = m % n
    if r == 0:
        return n
    return GCD_recursive(n, r)


GCD_recursive(243114, 1024)


##############################################################
# 4章: p048
# 問題: フィボナッチ数列を再帰関数で書く
# 日時: 2020/10/13
##############################################################

# fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)


fibo(5)


##############################################################
# 4章: p051
# 問題: フィボナッチ数列を再帰関数とメモ化を用いて書く
# 日時: 2020/10/13
##############################################################

# fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

def fibo_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)

    return memo[n]


n = 1000
memo = [-1] * (n + 1)
fibo_memo(n)

##############################################################
# 4章: p056
# 問題: 部分和問題を再帰関数を用いて書く
# 日時: 2020/10/13
##############################################################

# N個の整数を含む数列aの要素のうちi個を用いて和をとることでWにできるか？
# 例: N=4, a=(3, 2, 6, 5), W=14
# 解: 3つ用いて(i=3)で3+6+5=14

N = 4
W = 14
a = (3, 2, 6, 5)

def partial_sum(i, W, a):
    if i == 0:
        if W == 0:
            return True
        else:
            return False

    if partial_sum(i - 1, W, a) or partial_sum(i - 1, W - a[i - 1], a):
        return True

    return False

partial_sum(N, W, a)


##############################################################
# 4章: p058 - 章末問題 4.1
# 問題: トリボナッチ数列を再帰関数で書く
# 日時: 2020/10/13
##############################################################

def tribo(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    if n == 0:
        return 0

    return tribo(n-1) + tribo(n-2) + tribo(n-3)


tribo(6)


##############################################################
# 4章: p058 - 章末問題 4.2
# 問題: トリボナッチ数列を再帰関数でメモ化して書く
# 日時: 2020/10/13
##############################################################

memo = [-1]*100
def tribo_memo(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    if n == 0:
        return 0

    if memo[n] != -1:
        return memo[n]

    memo[n] = tribo(n-1) + tribo(n-2) + tribo(n-3)

    return memo[n]

tribo_memo(50)

##############################################################
# 4章: p058 - 章末問題 4.5
# 問題: ABC 114 - C - 755
# リンク: https://atcoder.jp/contests/abc114/tasks/abc114_c
# 日時: 2020/10/13
##############################################################

# 問題文
# 整数Nが与えられます。1以上N以下の整数のうち、七五三数 は何個あるでしょうか？
# ここで、七五三数とは以下の条件を満たす正の整数です。
# 十進法で表記したとき、数字 7, 5, 3 がそれぞれ 1回以上現れ、これら以外の数字は現れない。
N = int(input())

ans = 0
def get753(n, ans):
    if n > N: return

    if str(n).replace('7', '').replace('5', '').replace('3', '') == '':
        ans += 1
    get753(n * 10 + 7, ans)
    get753(n * 10 + 5, ans)
    get753(n * 10 + 3, ans)

ans = 0
get753(0, ans)

# このページを参考に考えてみたけど，難しい: https://drken1215.hatenablog.com/entry/2019/04/03/125400
# 再帰関数にまだ慣れていない。


# Qiitaの解答: https://qiita.com/kashi1mochi/items/a97552490fb54f4327e7
N = 999999999
def func(cur, use, counter):
  if cur > N: return
  if use == 0b111: counter.append(1)  # 答えを増やす

  # 7を付け加える
  func(cur * 10 + 7, use | 0b001, counter)
  # 5を付け加える
  func(cur * 10 + 5, use | 0b010, counter)
  # 3を付け加える
  func(cur * 10 + 3, use | 0b100, counter)

res = []
func(0, 0, res)
print(sum(res))


# 公式解答: https://img.atcoder.jp/abc114/editorial.pdf
def dfs(s): # 文字列 s で始まる七五三数の個数
    if int(s) > N:
    return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0 # s 自体が七五三数なら +1
    for c in '753':
    ret += dfs(s + c)
    return ret

dfs('3')


##############################################################
# 4章: p059 - 章末問題 4.6
# 問題: 部分和問題を再帰関数とメモ化を用いて解く
# 日時: 2020/10/14
##############################################################

# N個の整数を含む数列aの要素のうちi個を用いて和をとることでWにできるか？
# 例: N=4, a=(3, 2, 6, 5), W=14
# 解: 3つ用いて(i=3)で3+6+5=14

N = 4
W = 14
a = (3, 2, 6, 5)

import numpy as np

def partial_sum_memo(i, W, a):
    if i == 0:
        if W == 0:
            return True
        else:
            return False


    if memo[i - 1, W]:
        return True
    if memo[i - 1, W - a[i - 1]]:
        return True

    memo[i - 1, W] = partial_sum_memo(i - 1, W, a)
    memo[i - 1, W - a[i - 1]] = partial_sum_memo(i - 1, W - a[i - 1], a)

    return False

N = 12
W = 32
a = (1,2,3,4,5,6,7,8,10,11,12)
memo = np.full((N+1, W+1), False)
partial_sum_memo(N, W, a)


##############################################################
# 5章: p065
# 問題: AtCoder Educational DP Contest: A - Frog1
# 簡単にDPを用いて書く
# 日時: 2020/10/14
##############################################################

# N 個の足場があります。 足場には 1 , 2 , … , N と番号が振られています。
# 各 i ( 1 ≤ i ≤ N ) について、足場 i の高さは h i です。 最初、足場 1 にカエルがいます。
# カエルは次の行動を何回か繰り返し、足場 N まで辿り着こうとしています。
# 足場 i にいるとき、足場 i + 1 または i + 2 へジャンプする。
# このとき、ジャンプ先の足場を j とすると、コスト | h i − h j | を支払う。
# カエルが足場 N に辿り着くまでに支払うコストの総和の最小値を求めてください。

N = int(input())
h = list(map(int,input().split()))

dp = [float('inf')]*N
dp[0] = 0
dp[1] = abs(h[0]-h[1])
for i in range(2, N):
    cost_plus1 = dp[i-1] + abs(h[i] - h[i-1])
    cost_plus2 = dp[i-2] + abs(h[i] - h[i-2])
    dp[i] = min(cost_plus1, cost_plus2)
print(dp[N-1])

##############################################################
# 5章: p065
# 問題: AtCoder Educational DP Contest: A - Frog1
# DPだけど，緩和を意識して書く
# 日時: 2020/10/14
##############################################################

# 緩和: チャンピオンと挑戦者を比較して，min or maxを取って頂点の情報を更新すること
# グラフ上で頂点uから頂点vへと遷移する辺があって，その繊維のコストをcと表したときにchmin(dp[v], dp[u]+c)とする処理を緩和という

def chmin(a, b):
    if a > b:
        return b
    else: return a

N = int(input())
h = list(map(int,input().split()))

dp = [float('inf')]*N
dp[0] = 0
dp[1] = abs(h[0]-h[1])
for i in range(2, N):
    dp[i] = chmin(dp[i], dp[i-1] + abs(h[i] - h[i-1])) # i-1からの遷移
    dp[i] = chmin(dp[i], dp[i-2] + abs(h[i] - h[i-2])) # i-2からの遷移
print(dp[N-1])


##############################################################
# 5章: p072
# 問題: AtCoder Educational DP Contest: A - Frog1
# 再帰関数を用いて書く
# 日時: 2020/10/14
##############################################################
import sys
sys.setrecursionlimit(10**5+10)

def chmin(a, b):
    if a > b:
        return b
    else: return a

N = int(input())
h = list(map(int,input().split()))

inf = float('inf')
dp = [inf]*N
dp[0] = 0
dp[1] = abs(h[0]-h[1])

def rec(i):
    if dp[i] < inf:
        return dp[i]
    if i == 0: return 0

    res = inf
    res = chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]))
    res = chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]))

    dp[i] = res
    return res

print(rec(N-1))


# 初見で書けなかったので以下を参考
# https://yottagin.com/?p=1628


##############################################################
# 5章: p075
# 問題: ナップザック問題
# 再帰関数を用いて書く
# 日時: 2020/10/15
##############################################################

# Nこの品物があり，i番目(i=0~N-1)の品物の重さはweight_i, 価値はvalue_iで与えられる。
# このNこの品物から重さの総和がWを超えないようにいくつか選びます。
# 選んだ品物の価値の総和として考えられる最大値を求めよ

# 考え方
# dp[i][w]: 最初のi個の品物までの中から重さをwを超えないように選んだときの価値の総和の最大値
# iを選ぶ時: 選んだ後が(i+1, w)になるなら選ぶ前は(i, w - weight[i])
# iを選ばない時: 重さも価値も特に変化しない

# 理解しておくべき点
# 品物の順番はかわらず，品物1つ1つをループで回して，1つごとに選ぶ選ばないを考える
# ループは品物iごとに回すが，そのループで更新されるのは(i+1)における価値
# dpの表は矢印的には必ず右下に進む (本参照)
# i番目の品物を選ぶ時は，「耐荷重(w) >= iの重さ」の必要がある

def chmax(a, b):
    if a < b:
        return b
    else: return a

value = [3, 2, 6, 1, 3, 85]
weight = [2, 1, 3, 2, 1, 5]
N = len(value)
W = sum(weight)
dp = [[-1 for j in range(W+1)] for i in range(N+1)]
for w in range(W+1):
    dp[0][w] = 0

# wは耐荷重
for i in range(N):
    for w in range(W+1):
        if w - weight[i] >= 0:
            dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
        dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w])


##############################################################
# 5章: p081
# 問題: 編集距離
# 日時: 2020/10/16
##############################################################

# 2つの文字列S, T: Sに対して以下の3つの処理を施してTに変換したい。最小の操作回数を求めよ
# (1) 変更: Sの文字を1つ選んで任意の文字に変更
# (2) 削除: Sの文字を1つ選んで削除
# (3) 挿入: Sの好きな箇所に文字を1文字挿入する

# アイデア
# dp[i][j]: Sの最初のi文字分と，Tの最初のj文字分との間の編集距離
# 例: dp[0][3]はSに何もない状態からT[:3] ('alg')を作るための編集距離
# 例: dp[1][2]はSが'l'の状態からT[:2] ('al')を作るための編集距離

# Sへの1文字挿入とTからの1文字削除は同等である
# Sの中身を1文字ずつループでピックアップして，3つの処理を行ってそれぞれ距離を求めていく
# dpテーブルは|S|*|T|の行列

# 1つ前の文字が等しい時は処理の必要なし
# (1) 変更: SとTが1文字以上あるとき (i,j>0)，Sの左上から1文字
# (2) 削除: Sが1文字以上あるとき(i>0)，Sの上側=dp[i-1][j]から1文字削除 (処理+1)
# (3) 挿入: Tが1文字以上あるとき(j>0)，Sの左側=dp[i][j-1]から1文字追加


def chmin(a, b):
    if a > b:
        return b
    else: return a

S = 'logistic'
T = 'algorithm'

inf = float('INF')
dp = [[inf for j in range(len(T)+1)] for i in range(len(S)+1)]
dp[0][0] = 0

for i in range(len(S)+1):
    for j in range(len(T)+1):

        # 1つ前の文字が等しい時は処理の必要なし
        if S[i - 1] == T[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        # 変更
        if i > 0 and j > 0:
            dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1] + 1)

        # 挿入
        if j > 0:
            dp[i][j] = chmin(dp[i][j], dp[i][j - 1] + 1)

        # 削除
        if i > 0:
            dp[i][j] = chmin(dp[i][j], dp[i - 1][j] + 1)


# 本に沿って解いてみたけど，一人で書けと言われたら厳しい


##############################################################
# 5章: p085
# 問題: 区間分割の最適化
# 日時: 2020/10/16
##############################################################

# N個の要素が1列に並んでいて，いくつかの区間に分割したい。
# 各区間[l, r)にはスコアc_lrがついている。
# 正の整数 K <= Nで，K+1個の整数t_0, t_1, ..., t_Kで区間を区切った時のスコアの最小値を求めたい。

N = 10
K = 4
t = [0, 3, 7, 8, 10]

# アイデア
# dp[i]: 区間 [0, i)について，いくつかの区間に分割する最小コスト
# 一番小さい区間のコストから考えてどんどん伸ばしていく，というDPの発想
# 最後に区切る位置がjであるとき，区間[0, i)の分割は，「区間[0, j)の分割に対して新たに区間[j, i)を追加したもの」


# とりあえず具体例がなくてやる気が起きないので写経

inf = float('INF')
dp = [inf]*(N-1)
dp[0] = 0

for i in range(N):
    for j in range(i, N):
        dp[i] = chmin(dp[i], dp[j] + cost[j][i])

# costが具体的にないので回せないが，こんな感じっぽい

##############################################################
# 5章: p088 - 章末問題 5.1
# 問題: AtCoder Educational DP Contest - C: Vacation
# URL: https://atcoder.jp/contests/dp/tasks/dp_c
# 日時: 2020/10/16
##############################################################

N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(max(abc[0]))
else:
    dp = [[-1 for j in range(3)] for i in range(N)]
    dp[0] = abc[0]

    # i日ごと選択肢jごとの幸福度を更新していく
    for i in range(1, N):
        for j in range(3):
            last = dp[i - 1].copy()
            last.pop(j)
            dp[i][j] = max(last) + abc[i][j]
    print(max(dp[N - 1]))


##############################################################
# 5章: p088 - 章末問題 5.2.1
# 問題: 部分和問題を再帰関数でかく
# 日時: 2020/10/17
##############################################################

# N個の正の整数からいくつか選んで総和を書房の整数Wに一致させることができるかどうか判定する問題をO(NW)で書け
N=4
a=(3, 2, 6, 5)
W=14

def partial_sum(i, W, a):
    if i == 0:
        if W == 0:
            return True
        else:
            return False

    if partial_sum(i - 1, W, a) or partial_sum(i - 1, W - a[i - 1], a):
        return True
    return False
partial_sum(N, W, a)

# ポイントは添字
# N=4で，引数のi=4のときa[i-1]は最後の要素を取り出す。a[i]じゃないことに注意


##############################################################
# 5章: p088 - 章末問題 5.2
# 問題: 部分和問題をメモ化再帰でかく
# 日時: 2020/10/17
##############################################################

# N個の正の整数からいくつか選んで総和を書房の整数Wに一致させることができるかどうか判定する問題をO(NW)で書け
N=4
a=(3, 2, 6, 5)
W=14

inf = float('INF')
dp = [[False for j in range(W)] for i in range(N)]
def partial_sum_dp(i, W, a):
    if i == 0:
        if W == 0:
            return True
        else:
            return False

    if dp[i - 1, W]:
        return True
    if dp[i - 1, W -a[i - 1]]:
        return True

    dp[i - 1, W] = partial_sum_dp(i - 1, W, a)
    dp[i - 1, W - a[i - 1]] = partial_sum_dp(i - 1, W - a[i - 1], a)

    return False
partial_sum(N, W, a)


##############################################################
# 5章: p088 - 章末問題 5.3
# 問題: AtCoder Typical DP Contest: A - コンテスト
# URL: https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
# 日時: 2020/10/17
##############################################################

N = int(input())
p = list(map(int, input().split()))
import numpy as np
history = np.array([0])
for i in range(N):
    history = np.unique(np.concatenate([history, history + p[i]]))

print(len(history))

# DPっぽくない解き方をしてしまった。

# DP使う模範解答はこれ
# https://atcoder.jp/contests/tdpc/submissions/17317766
# 最高点数×問題数のdpテーブルを作って，Falseのフラグを立てる。点数を取りうるならTrueを置く
# (i-1)問目の状態がわかってるときに，問題iを解かなければ同じ点数がTrue
# (i-1)問目の状態がわかってるときに，問題iを解けばp[i]点高いマスがTrueになる
# 天才の解答

sum_p = sum(p)
dp = [[False] * (sum_p + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(sum_p + 1):
        if dp[i - 1][j]:
            # i番目の問題を解かない
            dp[i][j] = True
            # i番目の問題を解く
            dp[i][j + p[i - 1]] = True



##############################################################
# 5章: p088 - 章末問題 5.8
# カテゴリ: DP分割問題
# 問題:  立命館大学プログラミングコンテスト 2018 - D:水槽
# URL: https://rippro.herokuapp.com/src/event/ritscamp2018/index.html
# 日時: 2020/10/17
##############################################################

# AORイカちゃんは縦 1 横 N の大きさの水槽をもらった。水槽は水を入れるのに十分な高さがある。
# 水槽には N−1 個の仕切りがあり N 個の区画に等間隔に区切られている。 ここに水を注いだところ、各区画の水の高さは ai になった。
# AORイカちゃんはいくつか仕切りを取り除き、区画の数を M 個以下にすることにした。
# 仕切りを取り除き終わった時、各区画の水の高さの総和の最大値を求めよ。 なお、仕切りの厚さは無視できるものとする。

# つまり，N個の整数をM個の区間に分割して，各区間の平均値を最大にすればいい

# 3重ループを回す O(N^3)
# 1重目: 区間[0, i]の部分
# 2重目: 区間[0, i]における仕切りの個数 = j (区画の個数はj+1)
# 3重目: 区間[0, i]におけるj個の仕切りの位置

def mean(vec): return sum(vec)/len(vec)

N, M = map(int, input().split())
a = list(map(int,input().split()))

inf = float('INF')
dp = [[inf for j in range(M)] for i in range(N+1)]
dp[0] = [0]*(M)

for i in range(1, N+1):
    for j in range(0, M):
        # print(f'(i, j) = ({i}, {j})')
        if j == 0:
            dp[i][j] = mean(a[0:i])
            continue
        if i <= j:
            dp[i][j] = dp[i][j-1]
            continue
        for k in range(j):

# ギブアップ
# 解答見てもわからん: https://rippro.herokuapp.com/src/event/ritscamp2018/D.pdf


##############################################################
# 6章: p094 - code6.1
# カテゴリ: 二分探索
# 問題: 数列にある要素が含まれているかを判定する単純な二分探索
# 日時: 2020/10/28
##############################################################

n = 8
a = [3, 5, 8, 10, 14, 17, 21, 39]

def binary_search(n, a):
    left = 0
    right = len(a)-1

    while left <= right:
        mid = int((left + right)/2)
        if a[mid] == n:
            return 'Yes'
        elif n < a[mid]:
            right = mid -1
        elif a[mid] < n:
            left = mid + 1
    return 'No'

binary_search(n, a)

# ポイントは2つ
# 1. whileの条件文をleft <= rightとする点: while Trueにしてif文を書くよりきれい
# 2. leftとrightの更新の際に1減らすor増やす点 (right = mid-1): midが含まれていないことが確認されているため

##############################################################
# 6章: p094 - code6.3
# カテゴリ: 二分探索
# 問題: 年齢当てゲーム
# 日時: 2020/10/28
##############################################################

def guess_age(age):
    left = 0
    right = 100

    while left <= right:
        mid = int((right+left)/2)
        print(f'Is the age less than {mid}?')
        if age == mid:
            print(f'The age is {mid}')
            break
        elif age < mid:
            print('Yes')
            right = mid - 1
        elif age > mid:
            print('No')
            left = mid + 1

guess_age(10)


##############################################################
# 6章: p094 - code6.4
# カテゴリ: 二分探索
# 問題: ペア和のK以上の中での最小値
# 日時: 2020/10/28
##############################################################
import bisect
n, k = 3, 10
a = sorted([8, 5, 4])
b = sorted([4, 1, 9])


def min_pair_sum(a, b):
    # a+bのうちk以上のもので最小値: k <= a+b
    # k-a <= b
    ans = float('INF')
    for i in range(len(a)):
        index = bisect.bisect_right(b, k-a[i])
        if ans > a[i] + b[index]:
            ans = a[i] + b[index]
    return ans

min_pair_sum(a, b)

# C++のstd::lower_bound()にあたるpythonの関数はbisect.bisect_right
# リストaとnを与えて，a[i] >= nとなる最小のインデックスを返してくれる
# AtCoderでも使えるのでbisectは必須

##############################################################
# 6章: p094 - code6.3
# カテゴリ: 二分探索
# 問題: 射撃王: ABC 023 - D
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
# 問題をクリアするための最小のxを
# 探す，という課題は，まさに二分探索が得意とする対象なので，上手く使う。
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
# 6章: p107 - 章末問題 6.1
# カテゴリ: 二分探索
# 問題: 1次元の座標圧縮
# 日時: 2020/10/29
##############################################################

# 1次元の座標(数列)が与えられた時に，位置情報だけほしい
# それぞれの要素は何番目に大きいか?

# 方針
# 1. aをソートしてvalsとする
# 2. aの各要素がvalsの何番目にあるかを二分探索で探す

a = [12, 43, 7, 15, 9]
n = len(a)
vals = sorted(a)

t = [-1]*n
for i in range(n):
    left = 0
    right = n-1

    while right - left > 1:
        mid = int((left+right)/2)
        if a[i] == vals[mid]: break
        elif a[i] < vals[mid]: right = mid
        elif a[i] > vals[mid]: left = mid
    t[i] = mid


# これだとバグる。二分探索がバグるのはあるあるらしい。
# バグるポイント1: 更新の際にmid+1なのかmidのままでいいのかわからん
# バグるポイント2: 終了条件が>=か>

# バグを解消するための書き方を参考にした

def is_ok(arg):
    return a[i] < vals[arg]

# OKが右側の場合
def bisect(ok, ng):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else: ng = mid
    return ok


t = [-1]*n
for i in range(n):
    t[i] = bisect(n, -1)
print(t)


##############################################################
# 6章: p107 - 章末問題 6.2
# カテゴリ: 二分探索
# 問題: ABC 077 - C: Snuke Festival
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

##############################################################
# 6章: p107 - 章末問題 6.3
# カテゴリ: 二分探索
# 問題: JOI 2007/2008 本選 問題3 - ダーツ
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

# 最初，こんな感じでp2のリストを作る祭にsetを使ったらMLE (メモリオーバー)になった
# 模範解答を参考にループで単純なリストを作ったら通った　(重複してるけど)

from itertools import product
p2 = sorted(list(set([i + j for i,j in product(p, p)])))

# Pypyでは通らないけどPythonでは通るという謎の問題だった
# 思いついた解答が公式の想定解答と同じで嬉しかった
# https://www.ioi-jp.org/joi/2007/2008-ho-prob_and_sol/2008-ho-review.pdf


##############################################################
# 6章: p107 - 章末問題 6.4
# カテゴリ: 二分探索
# 問題: POJ No. 2456 Aggressive cows
# http://poj.org/problem?id=2456
# 日時: 2020/10/31
##############################################################

import bisect
def getLI(): return list(map(int,input().split()))
def getX(n): return [int(input()) for i in range(n)]

n, m = getLI()
c = sorted(getX(n))

# 線形探索ならこう
# 「各2点でありうる最大間隔」が探索の終わりになる
d_max = (c[-1] - c[0])// (m-1)

ans = 0
for d in range(1, d_max+1):

    now = c[0]
    flag = True
    for i in range(1, m):
        idx = bisect.bisect_right(c, now+d-1)
        if idx >= n:
            flag = False
        else:
            now = c[idx]
    if flag:
        ans = d
print(ans)


# 二分探索で書いてみる
# 左がOKで，境界線含んでOKな二分探索

# OKが左側の場合
def is_ok(arg):
    now = c[0]
    flag = True
    for i in range(1, m):
        idx = bisect.bisect_right(c, now + arg - 1)
        if idx >= n:
            flag = False
        else:
            now = c[idx]
    return flag

def bisect_left(ok, ng):
    while (abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else: ng = mid
    return ok

d_max = (c[-1] - c[0])// (m-1)
bisect_left(-1, d_max+1)


# 北京大学のオンラインシステムがPython受け付けてないので，泣きそう
# 「最小値の最大値」みたいな問題は，「全ての要素がhogehogeを満たす必要があって，hogehogeを動かすことで最大値の閾値を探す」と言い換えられる
# この牛問題や射撃王はこの類の問題

##############################################################
# 6章: p107 - 章末問題 6.4
# カテゴリ: 二分探索
# 問題:
# http://poj.org/problem?id=2456
# 日時: 2020/10/31
##############################################################


import math
a, b, c = list(map(int,input().split()))
def cal(t):
    return a*t+b*math.sin(c*t*math.pi)

left = -1000
right = 1000

while abs(right - left) > 10**(-12):
    mid = (right+left) / 2

    if cal(mid) >= 100:
        right = mid
    else:
        left = mid
print(mid)


# 一発AC!!
# 実数の二分探索のポイントは，終了条件を> 1ではなく，> 10**(-12)にすること
# あとはmidの計算の祭に小数点を許すため // 2ではなく /2とすること


##############################################################
# 7章: p111
# カテゴリ: 貪欲法
# 問題: コイン問題
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0521
# 日時: 2020/10/31
##############################################################

# おつりの枚数の最小

total = int(input())
change = 1000 - total


coin = [500, 100, 50, 10, 5, 1]

def solve(change):
    ans = 0
    rest = change
    for c in coin:
        m = rest // c
        rest -= c*m
        ans += m
    return ans

while True:
    total = int(input())
    if total == 0:
        break
    else:
        change = 1000 - total
        print(solve(change))

##############################################################
# 7章: p119
# カテゴリ: 貪欲法
# 問題: AGC 009 - A - Multiple Array
# https://atcoder.jp/contests/agc009/tasks/agc009_a
# 日時: 2020/10/31
##############################################################

def getXY(n):
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]
    return x, y

n = int(input())
a, b = getXY(n)

ans = 0
add = 0
for j in [n-i-1 for i in range(n)]:
    a[j] += ans
    r = a[j] % b[j]
    if r != 0:
        add = b[j] - r
        ans += add
print(ans)

# ベクトルがでかいので，ループのなかで毎回全部を書き換えるのは大変
# iの次にi-1を更新するときは，ansを足すようにすれば計算量が減る


##############################################################
# 7章: p121
# カテゴリ: 貪欲法
# 問題: ARC 092 - C - 2D Plane 2N Points
# https://atcoder.jp/contests/arc092/tasks/arc092_a
# 日時: 2020/10/31
##############################################################


def getXY(n):
    xy = [[int(i) for i in input().split()] for _ in range(n)]
    return xy

def is_ok(arg, i, vals, vec):
    return vec[i] < vals[arg]

# OKが右側の場合
def bisect(ok, ng, i, vals, vec):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, i, vals, vec):
            ok = mid
        else: ng = mid
    return ok

def coordinate_compression(vec):
    n = len(vec)
    vals = sorted(vec)
    t = [-1]*n

    for i in range(n):
        t[i] = bisect(n, -1, i, vals, vec)

    t = [i-1 for i in t]
    return t


n = int(input())
ab = getXY(n)
cd = getXY(n)

# 方針
# a, bの組を小さい順に取っていって，c, dとのペアを貪欲に作っていく
# ソートしたほうが良いのか？ とりあえずソートせずにやってみる -> 入力例4でダメだった
# xとyの最小値でソートしてみる

ab_min = [min(i[0],i[1]) for i in ab]
cd_min = [min(i[0],i[1]) for i in cd]

ab_idx = coordinate_compression(ab_min)
cd_idx = coordinate_compression(cd_min)

ab_vec = [-1]*n
cd_vec = [-1]*n

i = 0
for j in ab_idx:
    ab_vec[j] = ab[i]
    i += 1

i = 0
for j in cd_idx:
    cd_vec[j] = cd[i]
    i += 1

ans = 0
for i in range(n):
    for j in range(n):
        if ab_vec[i][0] < cd_vec[j][0] and ab_vec[i][1] < cd_vec[j][1]:
            ans += 1
            cd_vec[j] = [-1, -1]
            break
print(ans)

# 提出したらREいくつかでた。解答みる
# https://img.atcoder.jp/arc092/editorial.pdf
# 青い点のうち，最も x 座標が小さいもの (bA とします) に注目します。
# この点と仲良しペアになれる点が存在した場合，そのような点のうち最も y 座標が大きいもの (rA とします) と仲良しペアにしてよいです。


def getXY(n):
    xy = [[int(i) for i in input().split()] for _ in range(n)]
    return xy

n = int(input())
ab = getXY(n)
cd = getXY(n)

cd = sorted(cd, key=lambda x: x[0])  #[1]に注目してソート

inf = -float('INF')
ans = 0
for j in range(n):
    t = [inf]*n
    for i in range(n):
        if ab[i][0] < cd[j][0] and ab[i][1] < cd[j][1]:
            t[i] = ab[i][1]
    if t != [inf]*n:
        idx = t.index(max(t))
        ans += 1
        ab[idx] = [inf, inf]
print(ans)

# 戦略が思いつかなかった
# こんなの思いつくか？


##############################################################
# 7章: p121
# カテゴリ: 貪欲法
# 問題: ABC 131: D - Megalomania
# https://atcoder.jp/contests/abc131/tasks/abc131_d
# 日時: 2020/10/31
##############################################################
def getN(): return int(input())
def getXY(n):
    xy = [[int(i) for i in input().split()] for _ in range(n)]
    return xy

n = getN()
ab = getXY(n)

ab = sorted(ab, key=lambda x: (x[1], x[0]))  #[1]に注目してソート

now = 0
for i in range(n):
    if now + ab[i][0] <= ab[i][1]:
        now += ab[i][0]
    else:
        print('No')
        exit()
print('Yes')


##############################################################
# 11章: p187 code 11.3
# カテゴリ: Union-find
# 問題: Union-findの全体の実装
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=ja
# 日時: 2020/11/12
##############################################################
# 参考: https://note.nkmk.me/python-union-find/

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

uf = UnionFind(5)
uf.unite(2, 3)
uf.par
uf.siz
uf.same(3, 2)
uf.all_group_members()

##############################################################
# 13章: p220 code 13.1
# カテゴリ: 深さ優先探索
# 問題: AOJ - ALDS1_11_B - Depth First Searchの入力例を参考に
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja
# 日時: 2020/11/01
##############################################################
from collections import deque

def getNest(n):
    xy = [[int(i) for i in input().split()] for _ in range(n)]
    return xy

n = int(input())
g = getNest(n)

# 始点
s = g[0][0]

# seenとtodoを初期化
seen = [False]*(n+1) # グラフの番号が1から始まるので，1つ多く要素を用意する
todo = deque([])

# seenとtodoに始点を追加する
seen[s] = True
todo.appendleft(s)

# todoが空になるまで繰り返す: dequeがemptyであればboolがFalseになるので，これを利用してPythonicに書く
while todo:
    v = todo.popleft() # todoの頭から1つ頂点を取り出す
    for w in g[v-1][2:]: # g(v)の各要素wに対して，
        if seen[w]: # seen[w]がTrueであれば何もしない
            continue
        seen[w] = True # そうでなかったらseen[w]にTrueを代入して, todoにwを追加
        todo.appendleft(w)
        print(seen, todo)


######################################################################
# 入力のリストの形をわかりやすく加工しながら受け取る方法で書き直す
# 参考) http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3182881#1
######################################################################

from collections import deque

n = int(input())
g = [None]*(n+1)
for _ in range(n):
    v, k, *e = list(map(int,input().split()))
    g[v] = e

# 始点
s = 1

# seenとtodoを初期化
seen = [False]*(n+1) # グラフの番号が1から始まるので，1つ多く要素を用意する
todo = deque([])

# seenとtodoに始点を追加する
seen[s] = True
todo.appendleft(s)

# todoが空になるまで繰り返す: dequeがemptyであればboolがFalseになるので，これを利用してPythonicに書く
while todo:
    v = todo.popleft() # todoの頭から1つ頂点を取り出す
    for w in g[v]: # g(v)の各要素wに対して，
        if seen[w]: # seen[w]がTrueであれば何もしない
            continue
        seen[w] = True # そうでなかったらseen[w]にTrueを代入して, todoにwを追加
        todo.appendleft(w)
        print(seen, todo)


##############################################################
# 13章: p220 code 13.2
# カテゴリ: 深さ優先探索
# 問題: 13.1を再帰関数を使って表現する
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja
# 日時: 2020/11/01
##############################################################

from collections import deque

n = int(input())
G = [None]*(n+1)
for _ in range(n):
    v, k, *e = list(map(int,input().split()))
    G[v] = e

seen = [False] * (n + 1)  # seenとtodoを初期化

# dfs関数: 頂点vからたどることのできる頂点のうち，まだ訪問していない頂点を全て訪問する
def dfs(v):
    seen[v] = True # vを訪問済みにする
    for w in G[v]: # vに隣接する頂点wを1つずつ巡る
        if seen[w]: # seen[w]がTrueであれば何もしない
            continue
        dfs(w) # 再帰的に探索

# もしGが連結グラフであれば，v=1だけで探索すれば全頂点を訪問できそう

# すべての頂点に対してdfs関数を使う
for v in range(1, n+1):
    if seen[v]: # もしcが訪問済みなら探索しない
        continue
    dfs(v)


##############################################################
# 13章: p220 code 13.3
# カテゴリ: 幅優先探索
# 問題: 13.1を再帰関数を使って表現する
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



##############################################################
# 14章: p251 code 14.2
# カテゴリ: 単一始点最短路問題 (負閉路あり)
# 問題: ベルマンフォード法の実装
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
# 日時: 2020/11/08
##############################################################
# 入力
n, m, s = map(int, input().split())
G = [[] for _ in range(n)]

# グラフは隣接リストで行き先と重みをセットに格納する
for i in range(m):
    v, e, w = map(int, input().split())
    G[v].append([e, w])

# 負閉路をもつかどうか
exist_negative_cycle = False

# 始点から各頂点までの最短距離をinfで初期化
inf = float('INF')
dist =  [inf] * n
dist[s] = 0 # 始点の設定


# n回更新を繰り返して，n-1回以内で収束するか，n回目でも更新するかを見る
# n回目で更新があれば負閉路があることになる。

for _ in range(n):
    update = False # 更新が発生したかどうかを表すフラグ

    for v in range(n):
        # dist[v]がinfのときは頂点vからの緩和を行わない
        if dist[v] == inf: continue

        # 頂点vの推移先を全て巡る
        for ew in G[v]:
            e = ew[0] # 行き先
            w = ew[1] # 重み
            # 緩和処理を行い，更新されたらupdateをtrueにする
            if dist[e] > dist[v]+ w:
                dist[e] = dist[v] + w
                update = True

    # 更新がなければ，すでに最短経路が求められている
    if not update: break

    # N回目の反復で更新が行われたならば，負閉路を持つ
    if iter == n-1 and update:
        exist_negative_cycle = True

if exist_negative_cycle:
    print('NEGATIVE CYCLE')
else:
    for i in dist:
        if i == inf:
            print('INF')
        else:
            print(i)


# ポイントは「たかがか|V|-1回の反復によってアルゴリズムが収束する」はずなのに，負閉路がある場合そうではなく，
# |V|回目の反復時に必ず更新が起こるということ


##############################################################
# 14章: p251 code 14.3
# カテゴリ: 単一始点最短路問題 (負閉路なし)
# 問題: 単純なダイクストラ法 (Dijkstra): 計算量はO(|V|^2)
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
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

    # ステップ3: 頂点min_vの推移先を全て巡る
    for ew in G[min_v]:
        e = ew[0]  # 行き先
        w = ew[1]  # 重み
        if dist[e] > dist[min_v]+ w:
            dist[e] = dist[min_v] + w

print(dist)


##############################################################
# 14章: p251 code 14.4
# カテゴリ: 単一始点最短路問題 (負閉路なし)
# 問題: ヒープを用いたダイクストラ法 (Dijkstra): 計算量はO(|E|*log|V|)
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
# 日時: 2020/11/08
##############################################################

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


##############################################################
# 14章: p266 code 14.5
# カテゴリ: 全点対間最短経路問題
# 問題: ワーシャルフロイド法
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja
# 日時: 2020/11/11
##############################################################

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
# 15章: p274 code 15.1
# カテゴリ: 最小全域木問題
# 問題: クラスカル木
# URL: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=ja
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



6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6