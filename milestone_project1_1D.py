def check(my_list):
    for itr in my_list:
        if (itr == '_'):
            return False
    return True


def func(list1, list2, list3, str, str2, checker0, checker1):
    if (list1[0] == list2[0] and list2[0] == list3[0] and list1[0] == str):
        checker0 = True
        return
    if (list1[0] == list1[1] and list1[0] == list1[2] and list1[0] == str):
        checker0=True
        return
    if (list1[0] == list2[1] and list2[1] == list3[2] and list1[0] == str):
        checker0=True
        return
    if (list2[0] == list2[1] and list2[1] == list2[2] and list2[0] == str):
        checker0=True
        return
    if (list3[0] == list3[1] and list3[1] == list3[2] and list3[0] == str):
        checker0=True
        return
    if (list1[2] == list2[1] and list3[0] == list2[1] and list3[0] == str):
        checker0=True
        return
    if (list1[1] == list2[1] and list2[1] == list3[1] and list2[1] == str):
        checker0=True
        return
    if (list1[2] == list2[2] and list3[2] == list2[2] and list1[2] == str):
        checker0=True
        return




    if (list1[0] == list2[0] and list2[0] == list3[0] and list1[0] == str2):
        checker1 = True
        return
    if (list1[0] == list1[1] and list1[0] == list1[2] and list1[0] == str2):
        checker1=True
        return
    if (list1[0] == list2[1] and list2[1] == list3[2] and list1[0] == str2):
        checker1=True
        return
    if (list2[0] == list2[1] and list2[1] == list2[2] and list2[0] == str2):
        checker1=True
        return
    if (list3[0] == list3[1] and list3[1] == list3[2] and list3[0] == str2):
        checker1=True
        return
    if (list1[2] == list2[1] and list3[0] == list2[1] and list3[0] == str2):
        checker1=True
        return
    if (list1[1] == list2[1] and list2[1] == list3[1] and list2[1] == str2):
        checker1=True
        return
    if (list1[2] == list2[2] and list3[2] == list2[2] and list1[2] == str2):
        checker1=True
        return



list1 = ['_', '_', '_']
list2 = ['_', '_', '_']
list3 = ['_', '_', '_']

user0 = 0  # '0'
user1 = 1  # 'X'
k = False
while (1):
    for itr in list1:
        print(itr, end=" ")
    print('\n')
    for itr in list2:
        print(itr, end=" ")
    print('\n')
    for itr in list3:
        print(itr, end=" ")
    print('\n')
    k1 = False
    if (check(list1) == True):
        if (check(list2) == True):
            if (check(list3) == True):
                k1 = True

    if (k1 == True):
        print("GAME OVER")
        break
    if (user0 == 1):
        while (1):
            row = int(input("enter the row user0 : "))
            col = int(input('enter the col user0 :'))
            if (row == 0):
                list1[col] = '0'
                user0 = 0
                user1 = 1
                break
            elif (row == 1):
                list2[col] = '0'
                user0 = 0
                user1 = 1
                break
            elif (row == 2):
                list3[col] = '0'
                user0 = 0
                user1 = 1
                break

            else:
                if (check(list1) == True):
                    print("Game Over \nNo one wins")
                    k = True
                    break
                elif (check(list2) == True):
                    print("Game Over \nNo one wins")
                    k = True
                    break
                elif (check(list3) == True):
                    print("Game Over \nNo one wins")
                    k = True
                    break
                else:
                    print("invalid move \ntry again")
        if (k == True):
            break

    elif user1 == 1:
        while (1):
            row = int(input("enter the row user1: "))
            col = int(input('enter the col user1: '))
            if (row == 0):
                list1[col] = 'X'
                user0 = 1
                user1 = 0
                break
            elif (row == 1):
                list2[col] = 'X'
                user0 = 1
                user1 = 0
                break
            elif (row == 2):
                list3[col] = 'X'
                user0 = 1
                user1 = 0
                break
            else:
                if (check(list1) == True):
                    print("Game Over \nNo one wins")
                    k = True
                    break
                elif (check(list2) == True):
                    print("Game Over \nNo one wins")
                    k = True
                    break
                elif (check(list3) == True):
                    print("Game Over \nNo one wins")
                    k = True
                    break
                else:
                    print("invalid move \ntry again")
        if (k == True):
            break
    print("after the move the list looks like")
    # print(my_list)
    checker0 = False
    checker1 = False
    func(list1, list2, list3, '0', 'x', checker0, checker1)

    if checker0 == True:
        print('player wins =USER0')
        break
    if checker1 == True:
        print('player wins = USER1')
        break
