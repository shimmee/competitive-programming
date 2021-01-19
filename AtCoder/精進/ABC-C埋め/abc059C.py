# ABC059C - Sequence
# URL: https://atcoder.jp/contests/abc059/tasks/arc072_a
# 日付: 2020/12/18

# ---------- 思ったこと / 気づいたこと ----------
# 手前から貪欲にやっていく
# 0があるとやっかい

# ------------------- 方針 --------------------
# 累積和のうち，最初の項が正なら次の項を負に，その次の項を正に，と交互に正負になるように調整する

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))
ans = 0
# 第1項 a1が0のときがやっかい: というか初めて0以外が出てくるまでがやっかい
# 最初に0以外が出てくる場所を探す: 0は-1とか1に置き換えればいいから，もう数列から消し去りながらansをインクリメントする
while True:
    if len(a) == 0: break
    if a[0] == 0:
        a.pop(0)
        ans += 1
    else: break

if len(a) == 0:
    print(ans)
    exit()

l = [a[0]]

for i in range(1, len(a)):
    cum = sum(l) # 累積和

    # okな場合: 0じゃないし符号も異なる: 前後の累積和をかけたら負になる
    if cum * (cum + a[i]) < 0 :
        l.append(a[i])
        cum += a[i]
    elif cum + a[i] == 0: # 新しい要素を足して0になるとき，1か-1にする
        ans += 1
        if cum < 0: # これまでが負なら，cum+a[i]は正であるべき
            l.append(1)
        else:
            l.append(-1)
    else: # 新しい要素を足して，符号が同じ場合:
        k = abs(cum + a[i]) + 1
        ans += k
        if cum < 0:  # これまでが負なら，cum+a[i]は正であるべき
            l.append(a[i] + k)
        else:
            l.append(a[i] - k)
print(ans)

# TLEです!!! popやらappendやらでO(N^2)になってる
# リストの操作をやめて，第i項までの累積和だけで管理する

n = int(input())
a = list(map(int, input().split()))

# aが全部0だったとき
if all([i == 0 for i in a]):
    print(1+(n-1)*2)

ans = 0
# a1が0のときがやっかい: というか初めて0以外が出てくるまでがやっかい。
# 初めて0以外が出現するindexを探す
# (0,0,0,0,5) だったら，(1,0,0,0,5)にしたいし，(0,0,0,5)だったら(-1,0,0,5)にしたい
if a[0] == 0:
    for i in range(n):
        if a[i] != 0:
            idx = i
            break
    if idx % 2:
        a[0] = -1
    else: a[0] = 1
    ans += 1

cum = a[0] # i項までの累積和

for i in range(1, len(a)):

    # okな場合: 0じゃないし符号も異なる: 前後の累積和をかけたら負になる
    if cum * (cum + a[i]) < 0 :
        cum += a[i]
    else: # 新しい要素を足して，符号が同じ場合:
        if cum >= 0:  # これまでが負なら，cum+a[i]は正であるべき
            x = cum + a[i] + 1
            ans += x
            cum = -1
        else:
            x = 1 - cum - a[i]
            ans += x
            cum = 1
print(ans)

# 18ケース中10AC，8WA
# たぶん解き方が間違ってる
# 解説: https://img.atcoder.jp/arc072/editorial.pdf
# インデックスの偶奇に注目して，「偶数番目の累積和は正にして，奇数番目を負にする」もしくはその逆で決め打ちして，足りない数をインクリメント

n = int(input())
a = list(map(int, input().split()))

########################################
# 偶数番目を正, 奇数番目を負に
ans_even = 0
cum = 0 # i番目までの累積和

for i in range(n):
    if i % 2 == 0: # 偶数番目
        if cum + a[i] > 0: # 偶数番目が正ならOK
            cum += a[i]
            pass
        else: # 偶数番目が0以下なら，1に変更するまでインクリメント
            ans_even += abs(cum + a[i]) + 1
            cum = 1
    else: # 奇数番目
        if cum + a[i] < 0: # 奇数番目が負ならOK
            cum += a[i]
            pass
        else: # 奇数番目が0以上なら，-1に変更するまでインクリメント
            ans_even += abs(cum + a[i]) + 1
            cum = -1

########################################
# 偶数番目を負，奇数番目を正に
ans_odd  = 0
cum = 0 # i番目までの累積和

for i in range(n):
    if i % 2 == 0: # 偶数番目
        if cum + a[i] < 0: # 偶数番目が負ならOK
            cum += a[i]
            pass
        else: # 偶数番目が0以上なら，-1に変更するまでインクリメント
            ans_odd += abs(cum + a[i]) + 1
            cum = -1
    else: # 奇数番目
        if cum + a[i] > 0: # 奇数番目が正ならOK
            cum += a[i]
            pass
        else: # 奇数番目が0以下なら，-1に変更するまでインクリメント
            ans_odd += abs(cum + a[i]) + 1
            cum = 1

print(min(ans_even, ans_odd))



# ------------------ 入力例 -------------------
6
1 0 0 0 0 0 -1

5
0 0 5 0 0

5
0 0 0 0 3

4
1 -3 1 0

5
3 -6 4 -5 7

6
-1 4 3 2 -5 4

# ----------------- 解答時間 ------------------
# 1時間30分以上つかった気がする。結局解説AC

# -------------- 解説 / 感想 / 反省 -------------
# 解説をみるとこんな単純な貪欲法なのに！と思ってしまう。とても悔しい
# 本番は正答率13.6%!! 低い！！ https://ichijyo.at-ninja.jp/ABC_C.htm
# 最初の自分の解答が半分間違えていたのは，偶奇に注目せず，
# 最初に出てきた要素の正負だけで暗黙的に「偶奇どちらを正にするか」を勝手に決め打ちしてしまっていたから



# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#偶奇に注目
#貪欲法
