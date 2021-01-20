# ABC011C - 123引き算
# URL: https://atcoder.jp/contests/abc011/tasks/abc011_3
# 日付: 2020/12/14

# ---------- 思ったこと / 気づいたこと ----------
# 貪欲に大きい数字から引いていく

# ------------------- 方針 --------------------
# 使った数字のカウントを行うリストを作る
# now_use = 3として，3を使い切ったら2を使い，2と使い切ったら1を使う
# 次の数字が無事にNGでなかったら，nからnow_useをどんどん引いていく
# NGだったらnow_useの次の数字を引いてみる

# ------------------- 解答 --------------------
#code:python
n = int(input())
ng = [int(input()) for _ in range(3)]
if n in ng:
    print('NO')
    exit()

count = [0]*3
now_use = 3
while n > 0:
    if n == 1 and count[0] < 100:
        count[0] += 1
        break
    if n == 2 and count[1] < 100:
        count[1] += 1
        break
    if n == 3 and count[2] < 100:
        count[2] += 1
        break
    if not(count[now_use-1] <= 100): # 使おうとしている数字が100回以上使ってたら1減らす
        now_use -= 1
    if not(n - now_use in ng): # 次の数がNG数でなかったらnow_use分減らして，countを増やす
        n -= now_use
        count[now_use-1] += 1
    else: # NG数だったら
        if (now_use in [3,2]) and not(n - (now_use-1) in ng): # 次の数を使う
            n -= (now_use-1)
            count[(now_use-1) - 1] += 1
        else:
            print('NO')
            exit()


if sum(count) <= 100:
    print('YES')
else:
    print('NO')


# 短い書き方: https://atcoder.jp/contests/abc011/submissions/18664552
n, *ng=[int(input()) for _ in range(4)]
cnt = 100

if n in ng: print('NO'); exit()

while cnt > 0:
    cnt -= 1
    for i in range(3, 0, -1):
        if n-i >= 0 and n-i not in ng: # n-i >= 0はマイナスにならないようにしてる, # n-i not in ngはngじゃないかどうかの確認
            n -= i
            break
print('YNEOS'[n>0::2]) # この書き方わろた



# ------------------ 入力例 -------------------
143
142
141
140


2
1
7
15

5
1
4
2

300
57
121
244

1
1
2
3


# ----------------- 解答時間 ------------------
# 29分

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc011
# 例外処理が大変だった
# 短いコードが神がかってるので復習したい

# ----------------- カテゴリ ------------------
#AtCoder #abc
#例外処理
#貪欲法
#復習したい
