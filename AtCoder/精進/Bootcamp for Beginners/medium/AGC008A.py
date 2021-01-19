# AGC008A - Simple Calculator
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc008/tasks/agc008_a
# Date: 2021/01/04

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# 場合分け

# ------------------- Answer --------------------
code:python

    x, y = map(int, input().split())

    if x >= 0 and y >= 0:
        if y >= x:
            print(y-x)
        else:
            print(x-y+2)

    elif x >= 0 and y <= 0:
        print(abs(x + y) + 1)

    elif x <= 0 and y >= 0:
        print(abs(x + y) + 1)
    elif x <= 0 and y <= 0:
        if x >= y:
            print(x-y+2)
        else:
            print(y-x)



        if x >= -y:
            print(abs(x+y)+1)
        else:
            print(abs(x+y)+1)


        if -x <= y:
            print(x+y+1)
        else:
            print(x + y + 1)




    # This results in 2WA
    x, y = map(int, input().split())

    if x >= 0 and y >= 0 or x <= 0 and y <= 0:
        if y > x: print(y-x)
        else: print(x-y+2)
    else:
        print(abs(abs(x) - abs(y)) + 1)


    # But this AC. What's difference??????????
    x, y = map(int, input().split())

    if (x >= 0 and y >= 0 and x < y) or (x <= 0 and y <= 0 and x < y):
        print(y - x)
    elif (x > 0 and y > 0 and x > y) or (x < 0 and y < 0 and x > y):
        print(x - y + 2)
    else:
        print(abs(abs(x) - abs(y)) + 1)

# ------------------ Sample Input -------------------
-100 -190
10 9
0 -10

10 20
20 10

20 -10
10 -20

-10 20
-20 10

-10 -20
-20 -10


10 20

10 -10

-10 -20






# ----------------- Length of time ------------------
# 26分解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc008/editorial.pdf
# if文の挙動が謎すぎてもう辛い。なんで自分のコードはWAなの？？？

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#AC_with_editorial #解説AC
#wanna_review #medium復習
#場合分け