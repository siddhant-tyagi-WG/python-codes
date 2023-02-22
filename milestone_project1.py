def func(my_list, help):
    if my_list[0][0] == my_list[0][1] and my_list[0][2] == my_list[0][1] and my_list[0][0] == help:
        return True
    if my_list[0][0] == my_list[1][0] and my_list[2][0] == my_list[1][0] and my_list[0][0] == help:
        return True
    if my_list[0][0] == my_list[1][1] and my_list[1][1] == my_list[2][2] and my_list[0][0] == help:
        return True
    if my_list[0][1] == my_list[1][1] and my_list[1][1] == my_list[2][1] and my_list[0][1] == help:
        return True
    if my_list[0][2] == my_list[1][1] and my_list[1][1] == my_list[2][0] and my_list[0][2] == help:
        return True
    if my_list[1][0] == my_list[1][1] and my_list[1][1] == my_list[1][2] and my_list[1][0] == help:
        return True
    if my_list[2][0] == my_list[2][1] and my_list[2][1] == my_list[2][2] and my_list[2][0] == help:
        return True
    if(my_list[0][2]==my_list[1][2] and my_list[2][2]==my_list[0][2] and my_list[0][2]==help):
        return True
    else:
        return False
def check(my_list):
    for itr in my_list:
        for val in itr:
            if(val==' '):
                return False
    return True


my_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

user0 = 0  # '0'
user1 = 1  # 'X'
k=False
while (1):
    for itr in my_list:
        print(itr)
    if(check(my_list)==True):
        print("Game Over")
        break
    if (user0 == 1):
        while (1):
            row = int(input("enter the row user0 : "))
            col = int(input('enter the col user0 :'))
            if (my_list[row][col] == ' '):
                my_list[row][col] = '0'
                user0 = 0
                user1 = 1
                break
            else:
                if (check(my_list) == True):
                    print("Game Over \nNo one wins")
                    k=True
                    break
                else:
                    print("invalid move \ntry again")
        if (k == True):
            break

    elif user1 == 1:
        while (1):
            row = int(input("enter the row user1: "))
            col = int(input('enter the col user1: '))
            if (my_list[row][col] == ' '):
                my_list[row][col] = 'X'
                user1 = 0
                user0 = 1
                break
            else:
                if (check(my_list) == True):
                    print("Game Over \nNo one wins")
                    k = True
                    break
                else:
                    print("invalid move \ntry again")
        if(k==True):
            break
    print("after the move the list looks like")
    #print(my_list)
    checker0 = func(my_list, '0')
    checker1 = func(my_list, 'X')
    if checker0 == True:
        print('player wins =USER0')
        break
    if checker1 == True:
        print('player wins = USER1')
        break
