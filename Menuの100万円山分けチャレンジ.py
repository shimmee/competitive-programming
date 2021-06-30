# Menuの100万円山分けチャレンジ
# URL:
# Date: 2021/06/09

# ---------- Ideas ----------
# 辞書でいろいろ管理する


# ------------------- Answer --------------------
#code:python
import sys
from collections import deque, defaultdict

# lines = [input() for _ in range(198)]

def main(lines):
    n = int(lines[0])
    num_input = len(lines) - 1

    book_list_reserve = defaultdict(deque) # 各本を予約してるユーザー
    book_list_borrow = defaultdict(deque)  # 各本を借りているユーザー
    user_list_reserve = defaultdict(set)  # 各ユーザーが予約してる本
    user_list_borrow = defaultdict(set) # 各ユーザーが借りている本

    shelf = defaultdict(bool)
    shelf_keep = defaultdict(bool)

    for i in range(num_input):
        info = list(lines[i+1].split())
        if info[0] == 'open':
            print('open')
        elif info[0] == 'close':
            print('close')
        elif info[0] == 'borrow':

            user_id = info[1]
            if user_id not in user_list_reserve: # 初めての人
                user_list_reserve[user_id] = set()
                user_list_borrow[user_id] = set()

            book_ids = []
            if len(info) > 2:  # 予約以外にも本がある
                book_ids = info[2:]
            reserved_books = list(user_list_reserve[user_id])  # このユーザーが予約している本一覧

            # 初めての予約本の初期化
            for reserved_book_id in reserved_books:
                if reserved_book_id not in book_list_reserve:
                    book_list_reserve[reserved_book_id] = deque([])
                    book_list_borrow[reserved_book_id] = deque([])
                    shelf[reserved_book_id] = True
                    shelf_keep[reserved_book_id] = False

            # 初めての本の初期化
            for book_id in book_ids:
                if book_id not in book_list_reserve:
                    book_list_reserve[book_id] = deque([])
                    book_list_borrow[book_id] = deque([])
                    shelf[book_id] = True
                    shelf_keep[book_id] = False

            # まずは貸し出せる本をカウントする
            cnt = len(user_list_borrow[user_id])  # すでに借りている本の数
            # 予約本の貸し出し
            if reserved_books:  # 予約がある場合
                for reserved_book_id in reserved_books:
                    # 取り置き棚にあって，かつ待ち順が一番最初なら貸せる
                    if shelf_keep[reserved_book_id] and book_list_reserve[reserved_book_id][0] == user_id:
                        cnt += 1
            # 貸し出しが予約以外にある場合: 書架にあったら貸せる
            if book_ids:
                for book_id in book_ids:
                    if shelf[book_id]:  # 書架にある場合
                        cnt += 1

            # もし貸し出し希望の本の数がn以下なら行ける
            if n >= cnt:
                ans = []
                # 予約本の貸し出し
                if reserved_books:  # 予約がある場合
                    for reserved_book_id in reserved_books:
                        # 取り置き棚にあって，かつ待ち順が一番最初なら貸せる
                        if shelf_keep[reserved_book_id] and book_list_reserve[reserved_book_id][0] == user_id:
                            ans.append(reserved_book_id)
                            shelf_keep[reserved_book_id] = False
                            book_list_reserve[reserved_book_id].popleft()
                            book_list_borrow[reserved_book_id].append(user_id)
                            user_list_reserve[user_id].remove(reserved_book_id)
                            user_list_borrow[user_id].add(reserved_book_id)

                # 貸し出しが予約以外にもある場合: 書架にあったら貸せる
                if book_ids:
                    for book_id in book_ids:
                        if shelf[book_id]:  # 書架にある場合
                            shelf[book_id] = False
                            book_list_borrow[book_id].append(user_id)
                            user_list_borrow[user_id].add(book_id)
                print('can', *sorted(ans))
            else:
                print('cannot', cnt-n)

        #######################################
        # 返却 #################################
        #######################################
        elif info[0] == 'return':
            book_ids = info[1:]
            ans = []
            for book_id in book_ids:
                # 返却した人を把握して，借りたリストから除いてあげる
                user_id = book_list_borrow[book_id].popleft()
                user_list_borrow[user_id].remove(book_id)

                if book_list_reserve[book_id]:  # 誰かが予約していれば取り置きだなに置く
                    ans.append(book_list_reserve[book_id][0])
                    shelf_keep[book_id] = True
                else:  # 誰も予約してなければ書庫に戻す
                    ans.append('return')
                    shelf[book_id] = True

            print(*ans)

        #######################################
        # 予約 #################################
        #######################################
        elif info[0] == 'reserve':
            user_id = info[1]
            book_ids = info[2:]

            # 初めての人
            if user_id not in user_list_reserve:
                user_list_reserve[user_id] = set()
                user_list_borrow[user_id] = set()

            # 初めての本の初期化
            for book_id in book_ids:
                if book_id not in book_list_reserve:
                    book_list_reserve[book_id] = deque([])
                    book_list_borrow[book_id] = deque([])
                    shelf[book_id] = True
                    shelf_keep[book_id] = False

            cannot_list = []
            cannot_flag = False
            for book_id in book_ids:
                if shelf[book_id]:  # 書架にある場合cannot
                    cannot_flag = True
                    cannot_list.append('s' + book_id)
                elif book_id in user_list_reserve[user_id]:  # 現在すでに予約してる場合cannot
                    cannot_flag = True
                    cannot_list.append('r' + book_id)
                elif book_id in user_list_borrow[user_id]:  # すでに借りてる場合cannot
                    cannot_flag = True
                    cannot_list.append('b' + book_id)

            num_reverse = len(user_list_reserve[user_id]) + len(book_ids)
            if num_reverse > n: # 予約可能冊数を超える場合
                print('cannot', num_reverse - n)
            elif cannot_flag:
                print('cannot', *cannot_list)
            else:  # 予約できる場合
                print('can')
                for book_id in book_ids:
                    book_list_reserve[book_id].append(user_id)
                    user_list_reserve[user_id].add(book_id)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)



# ------------------ Sample Input -------------------
5
open
borrow 1234567 12345678 23456789
borrow 1234567 11111111 22222222 33333333 44444444
reserve 2345678 12345678
reserve 2345678 55555555
reserve 1234567 12345678
reserve 2345678 12345678 55555555
return 12345678 23456789
borrow 1234567 11111111 22222222 33333333 44444444
borrow 2345678
close
return 11111111

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
