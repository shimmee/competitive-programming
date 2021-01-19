# ABC027C - 倍々ゲーム
# URL: https://atcoder.jp/contests/abc027/tasks/abc027_c
# 日付: 2020/12/22

# ---------- 思ったこと / 気づいたこと ----------
# grundy数ってやつ使いそう
# https://www.slideshare.net/yutakasai2/nimgrundy-84622339

# ------------------- 方針 --------------------
# grundy数: 必ず負ける状態ではgrundy数=0
# 今の状態から移行できる次の状態の全体のgrundy数の集合のうち，その集合に含まれない非負整数(mex)
# grundy数が0なら必ず負けるので，ゲーム開始時に高橋のターンにgrundy数が0なら，Aokiの勝ち
# grundy数が0より大きければTakahashiの勝ち


# ------------------- 解答 --------------------
code:python
    n = int(input())

    if n < 100:
        grundy = [-1]*(n+3)
        for x in reversed(range(1, n+3)):
            if 2*x > n:
                grundy[x] = 0
            else:
                next_grundy = set([grundy[2*x], grundy[2*x+1]])
                now_grundy = min(set([0,1,2])-next_grundy)
                grundy[x] = now_grundy

        if grundy[1] == 0: # 最初の高橋の手でgrundy数が0だったら高橋の負け
            print('Aoki')
        else:
            print('Takahashi')
    else:
        # Grundy数が求まった！
        # ただ，N<=10**18なので，TLEになる
        # 規則性がありそう! N=100のとき
        # x=51-100: grundy数=0
        # x=51-25: grundy=1or2
        # 2でどんどん割っていった商のリストを作って，長さの偶奇で決まったりしないかな？

        l = [n]
        while True:
            if n//2 < 1:
                break

            if n % 2:
                n = (n-1)//2
            else:
                n = n//2
            l.append(n)

        if len(l)%2:
            print('Aoki')
        else:
            print('Takahashi')

    # 85ケース中24ケースWAなので，嘘解法
    # 解説: https://www.slideshare.net/chokudai/abc027
    # 自分が解いた方法の2番目の方法が近かった: 樹形図の深さの偶奇で戦略が決まって，その戦略をもとにシミュレーションする
    # 偶奇だけでは勝ちは決まらない
    # 深さが奇数の時，先行は奇数だけを選ぶ戦略，後攻は偶数を選ぶ
    # 深さが偶数の時，先行は毎回偶数を選び，後攻は奇数を選ぶ
    n = int(input())
    depth = 1
    max_x = 1
    while True:
        if max_x >= n:
            break
        depth += 1
        max_x += 2**(depth-1)

    now_depth = 1
    x = 1
    if depth % 2: # 深さが奇数の時
        while True:
            if now_depth % 2: # 現在の深さが奇数のとき，高橋のターン(先行)
                x = 2*x+1
                now_depth += 1
                if x > n:
                    print('Aoki')
                    exit(); break
            else:
                x = 2 * x
                now_depth += 1
                if x > n:
                    print('Takahashi')
                    exit(); break
    else: # 深さが偶数の時
        while True:
            if now_depth % 2: # 現在の深さが奇数のとき，高橋のターン(先行)
                x = 2*x
                now_depth += 1
                if x > n:
                    print('Aoki')
                    exit(); break
            else:
                x = 2 * x + 1
                now_depth += 1
                if x > n:
                    print('Takahashi')
                    exit(); break


    # 超短い解答: https://atcoder.jp/contests/abc027/submissions/18513649
    # よくわからんな
    n = int(input())
    turn = 1 # 高橋のターンからスタート
    while 1 < n:
      if turn == 1:
          n = n // 2 - 1
      else :
          n = n // 2
      turn = 1 - turn
    print(['Takahashi','Aoki'][turn == 1])

# ------------------ 入力例 -------------------
1

5

7

10

123456789123456789

# ----------------- 解答時間 ------------------
# 2時間くらいかけてgrundy数を勉強して実装してTLE!!!

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc027
# 「樹形図の深さの偶奇で戦略が決まって，かつシミュレーションしてみる」というのが解答だった
# Nが小さければ，grundy数でも解ける問題ではあった。
# grundy数おもしろかったから勉強してよかった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#樹形図の深さ
#偶奇に注目
#同じ手段を選び続けるのが最善
#grundy数
