dict={3044: ["ram","12-04-2000",25000,678908], 3089:["shyam","10-03-1990",100000,345678], 1505:["shyam","12-12-1995",50000,654321] , 6782:["raj","14-12-1996",200000,126730]}
secure={"shyam@bankxx.com":'alpha@2021'}
print(dict)
bank_amount=int(100000000)
while(1):
    x1=int(input("enter the account number of a person: "))
    x2=input("enter the DOB of the person in the format dd/mm/yyyy")
    x3=input("enter the name of the person")
    x10=input("press EMP if you are employee of the company and want to check the bank balance")
    if(x10=='EMP'):
        x11=input("enter your mail and password")
        x12=input()
        if(x11 in secure.keys() and secure[x11]==x12):
            print("bank has amount Rs",bank_amount)


    if x1 in dict.keys():
        if(x2==dict[x1][1] and x3==dict[x1][0]):
            print("verified \n you have amount RS",dict[x1][2],"in your account")
            x4=input("do you want to withdraw or add money to your account \n type Y for YES and N for NO")
            if(x4=='Y'):
                x5=input("type W for withdraw and A to ADD money")
                if(x5=='W'):
                    x8=int(input("enter your secret  pin to withdraw the money"))
                    if(x8==dict[x1][3]):
                     x6=int(input("Enter the amount to withdraw"))
                     if(x6>dict[x1][2]):
                         print("Your account don't have that much amount")
                     else:
                         dict[x1][2]=dict[x1][2]-x6
                         print("your bank balance is: Rs",dict[x1][2])
                         bank_amount=bank_amount-x6
                else:
                    x7 = int(input("Enter the amount to add to your account"))
                    bank_amount=bank_amount+x7
                    dict[x1][2]=dict[x1][2]+x7
                    print("your bank balance is: Rs", dict[x1][2])


        else:
            print("user not found")
    else:
        print("user not found")