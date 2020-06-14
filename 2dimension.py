import pprint

n = int(input())
S = [[0 for j in range(n)] for i in range(n)]

S[0]=["A","B","C","D"]
S[1]=["A","B","D","C"]
S[2]=["A","D","B","C"]
S[3]=["A","C","D","B"]
#
# for x in range(n):
#     row = list(map(str,input().split()))
#     S[x] = row



def main():
    global n
    a_change()
    b_change()
    c_change()


def check_char(s, char):
    where_char = []
    for i in range(s):
        for j in range(s):
            if S[i][j] == char:
                k = [i, j]
                where_char.append(k)

    return where_char


def check(S,x,y):
    c = []
    print(S)
    for i in range(len(S)):
        if S[i][0] != x or S[i][1] != y:
            c.append(S[i])
    return c


def a_change():
    global S
    where_a = check_char(n, "A")
    print(where_a)

    # (0,0)にAを置く
    move_tate(where_a[0][1],0 - where_a[0][0])  # (0,0)において、where_a[0]における行のずれ。　動かし方は縦で動かす
    move_yoko(0, 0 - where_a[0][1])  # (0,0)において、where_a[0]における 列のずれ。　動かし方は横で動かす
    #pprint.pprint(S, width=n * 10)


    where_a = check_char(n, "A")
    where_a = check(where_a,0,0)
    print(where_a)
    # (0,1)にAを置く
    if where_a[0][1] == 0:    # 0列目にある場合、縦の移動ができないのでいったん横にずらす
        move_yoko(where_a[0][0], 1)  # 1列目に移動
        move_tate(1, 0 - where_a[0][0])  # (0,1)において、where_a[1]における行のずれ。　縦に動かす

    elif where_a[0][0] == 0:  # 0行目にある場合、横の移動ができないのでいったん縦にずらす
        move_tate(where_a[0][1], 1)  # いったん縦に回避
        move_yoko(0, where_a[0][1]-1)  # (0,1)において、where_a[1]における列のずれ。1行目にいるため、1行目において、横移動し(1,1)へ
        move_tate(where_a[0][1], -1) # 1行目の1列目にいるため、縦移動1回
        move_yoko(0, -(where_a[0][1] - 1))
    else:
        move_yoko(where_a[0][0], 1 - where_a[0][1])# (0,1)において、where_a[0]における 列のずれ。　動かし方は横で動かす
        move_tate(1, 0 - where_a[0][0])# (0,1)において、where_a[0]における行のずれ。　動かし方は縦で動かす

    where_a = check_char(n, "A")
    where_a = check(where_a,0,0)
    where_a = check(where_a,0,1)
    print(where_a)
    pprint.pprint(S, width=n * 10)

    # (1,0)にAを置く
    if where_a[0][1] == 0 or where_a[0][1] == 1:   # 0列目,1列目にある場合、縦の移動ができないのでいったん横にずらす
        move_yoko(where_a[0][0], 2-where_a[0][1])  # 2列目に移動
        move_tate(2, 1 - where_a[0][0])    # (1,0)において、where_a[1]における行のずれ . 2列目における縦移動
        move_yoko(1, -2)  # 1行目における横移動
    else:
        move_tate(where_a[0][1], 1 - where_a[0][0])# (1,0)において、where_a[0]における行のずれ。　動かし方は縦で動かす
        move_yoko(1, 0 - where_a[0][1])# (1,0)において、where_a[0]における 列のずれ。　動かし方は横で動かす

    where_a = check_char(n, "A")
    where_a = check(where_a,0,0)
    where_a = check(where_a,0,1)
    where_a = check(where_a,1,0)
    print(where_a)
    pprint.pprint(S, width=n * 10)


    # (1,1)にAを置く
    if where_a[0][1] == 0 or where_a[0][1] == 1:  # 0列目,1列目にある場合、縦の移動ができないのでいったん横にずらす
        move_yoko(where_a[0][0], 2 - where_a[0][1])  # 2列目に移動
        move_yoko(1, 1)  # 1行目の+1列ずらす
        move_tate(2, 1 - where_a[0][0])  # # (1,1)において、where_a[1]における行のずれ。　縦に動かす2列目における縦移動
        move_yoko(1, -1)  # 1行目をもとに戻す　# ー1横移動

    elif where_a[0][0] == 0:  # 0行目、横の移動ができないので揃えると同時に動かす。
        move_yoko(1, where_a[0][1] - 1)  # (1,1)において、where_a[1]における列のずれ , 1行目におけるyoko移動
        move_tate(where_a[0][1], 1)  # 1行目に移動
        move_yoko(1, -(where_a[0][1] - 1)) # 1行目におけるyoko移動 ずらした分、もとに戻す
    else:
        move_yoko(1, where_a[0][1] - 1)  #  (1,1)において、where_a[1]における列のずれ1行目におけるyoko移動
        row_far = 1 - where_a[0][0]  # (1,0)において、where_a[0]における行のずれ。　動かし方は縦で動かす
        move_tate(where_a[0][1], row_far)
        move_yoko(1, -(where_a[0][1] - 1))

    pprint.pprint(S, width=n * 10)


def b_change():
    global S
    where_b = check_char(n, "B")

    # (2,0)にBを置く
    if where_b[0][1] == 0 or where_b[0][1] == 1:  # 0列目,1列目にある場合、縦の移動ができないのでいったん横にずらす
        print("hiatta")
        move_yoko(where_b[0][0], 2-where_b[0][1])  # 2列目に移動
        move_tate(2, 2-where_b[0][0])  # 2行目に移動
        move_yoko(2,  -2)  # 2列目まで動かした分をもとに戻す

    elif where_b[0][0] == 0 or where_b[0][0] == 1:  # 0行目,1行目にある場合、横の移動ができないのでいったん縦にずらす
        move_tate(where_b[0][1], 2-where_b[0][0])  # 2行目に縦移動
        move_yoko(2,  0-where_b[0][1])  # (2,0)へ移動

    else:
        move_tate(where_b[0][1], 2-where_b[0][0])  # 2行目に縦移動
        move_yoko(2,  0-where_b[0][1])  # (2,0)へ移動

    where_b = check_char(n, "B")
    where_b = check(where_b, 2, 0)
    print(where_b)

    # (3,0)にBを置く
    move_tate(where_b[0][1], 3 - where_b[0][0])  # 3行目に縦移動
    move_yoko(3, 0 - where_b[0][1])  # (3,0)へ移動
    move_tate(where_b[0][1], -(3 - where_b[0][0]))

    where_b = check_char(n, "B")
    where_b = check(where_b, 2, 0)
    where_b = check(where_b, 3, 0)
    print(where_b)
    pprint.pprint(S, width=n * 10)



    # (2,1)にBを置く
    if where_b[0][1] == 1 and where_b[0][0] == 3:  # 1列目にある場合、縦の移動ができないのでいったん横にずらす
        print("入った")
        move_yoko(3, 1)  # 3列目を移動
        move_yoko(2, 1)  # 2列目を移動
        move_tate(2, -1)  # 2列目をー1移動
        move_yoko(2, -1)# 2列目まで動かした分をもとに戻す
        move_yoko(3, -1) # 3列目まで動かした分をもとに戻す
        pprint.pprint(S, width=n * 10)

    elif where_b[0][0] == 2 and (where_b[0][1] == 2 or where_b[0][1] == 3):  # 2行目にある場合、横の移動ができないのでいったん縦にずらす
        move_tate(where_b[0][1], 1)  # いったん縦にずらす
        move_yoko(2, where_b[0][1] - 1)  # (2,1)を# 移動
        move_tate(where_b[0][1], -1)  # 2行目に縦移動
        move_yoko(2, -(where_b[0][1] - 1))  # (2,0)へ移動

    else:
        move_yoko(2, where_b[0][1]-1)  # (2,1)を# 移動
        move_tate(where_b[0][1], 2 - where_b[0][0])  # 2行目に縦移動
        move_yoko(2, -(where_b[0][1]-1))# (2,0)へ移動


    where_b = check_char(n, "B")
    where_b = check(where_b, 2, 0)
    where_b = check(where_b, 3, 0)
    where_b = check(where_b, 2, 1)
    pprint.pprint(S, width=n * 10)
    print(where_b)

    # (3,1)にBを置く
    if where_b[0][0] == 3: #3行目にいる場合
        move_tate(where_b[0][1], -1)  # 2行目に縦移動
        move_yoko(3, where_b[0][1]-1)
        move_tate(where_b[0][1], 1)
        move_yoko(3, -(where_b[0][1] - 1))
    else:
        move_yoko(3, where_b[0][1] - 1)
        move_tate(where_b[0][1], 3-where_b[0][0])
        move_yoko(3, -(where_b[0][1] - 1))

    pprint.pprint(S, width=n * 10)


def c_change():
    global S
    where_c = check_char(n, "C")

    # (0,2)をC
    if where_c[0][1] == 2:  # 2列目2があれば　縦移動
        move_tate(2, 0-where_c[0][0])  # (0.2)に移動
    elif where_c[0][0] == 0:  #0行目にある場合
        move_tate(3, 1)
        move_yoko(0,1)
        move_tate(3, -1)
        move_yoko(0, -1)
    else:
        move_yoko(0, 1)
        move_tate(3, 0-where_c[0][0])
        move_yoko(0, -1)

    where_c = check_char(n, "C")
    where_c = check(where_c, 0, 2)

    # (0,3)にC
    if where_c[0][1] == 3:  # 3列目Cがある　縦の移動
        move_tate(3, 0 - where_c[0][0])  # (0.3)に移動
    else:
        move_yoko(where_c[0][0], 1)
        move_tate(3, 0 - where_c[0][0])
        move_yoko(where_c[0][0], -1)

    where_c = check_char(n, "C")
    where_c = check(where_c, 0, 2)
    where_c = check(where_c, 0, 3)


    # (1,2)にCを置く
    if where_c[0][1] == 2:  # 2列目にある場合、左にずらす
        move_yoko(where_c[0][0], -1)  # 2列目に移動
        move_tate(2, where_c[0][0]-1)
        move_yoko(where_c[0][0], 1)
        move_tate(2, -(where_c[0][0]-1))

    elif where_c[0][0] == 1:
        move_tate(3, -1)
        move_yoko(1, 1)
        move_tate(3, 1)
        move_yoko(1, -1)
    else:
        move_yoko(1, 1)
        move_tate(3, 1-where_c[0][0])
        move_yoko(1, -1)
        move_tate(3, -(1 - where_c[0][0]))

    where_c = check_char(n, "C")
    where_c = check(where_c, 0, 2)
    where_c = check(where_c, 0, 3)
    where_c = check(where_c, 1, 2)


    # (1,3)にCを置く
    if where_c[0][1] == 2: #2列目にある場合
        move_tate(3, where_c[0][0]-1)
        move_yoko(where_c[0][0],1)
        move_tate(3, -(where_c[0][0]-1))
        move_yoko(where_c[0][0], -1)
    else:
        move_yoko(where_c[0][0], 1)
        move_tate(3, where_c[0][0]-1)
        move_yoko(where_c[0][0], -1)
        move_tate(3, -(where_c[0][0] - 1))

    pprint.pprint(S, width=n * 10)


def move_yoko(row_num, mv):
    global S

    if mv > 0:
        for _ in range(abs(mv)):
            wk = S[row_num][0]
            S[row_num][0] = S[row_num][3]
            S[row_num][3] = S[row_num][2]
            S[row_num][2] = S[row_num][1]
            S[row_num][1] = wk

    else:
        for _ in range(abs(mv)):
            wk = S[row_num][0]
            S[row_num][0] = S[row_num][1]
            S[row_num][1] = S[row_num][2]
            S[row_num][2] = S[row_num][3]
            S[row_num][3] = wk
            mv += 1


def move_tate(line_num, mv):
    global S
    if mv > 0:
        for _ in range(abs(mv)):
            wk = S[3][line_num]
            S[3][line_num] = S[2][line_num]
            S[2][line_num] = S[1][line_num]
            S[1][line_num] = S[0][line_num]
            S[0][line_num] = wk
    else:
        for _ in range(abs(mv)):
            wk = S[0][line_num]
            S[0][line_num] = S[1][line_num]
            S[1][line_num] = S[2][line_num]
            S[2][line_num] = S[3][line_num]
            S[3][line_num] = wk


if __name__ == '__main__':
    main()



'''
アルゴリズムの説明


'''