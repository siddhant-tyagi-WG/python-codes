


class book():

    def __init__(self,key,title,author,genre,count):
        self.key=key
        self.title=title
        self.author=author
        self.genre=genre
        self.count=count




class library():

    def __init__(self):
        self.my_list=[]
        self.key_val=0
        self.user_dict={}
        self.my_unique_books = set()
    def check(self):
        self.my_list.append(book(self.key_val,'fundamentals of wavelets','goswami','signal_processing',1))
        self.my_unique_books.add('fundamentals of wavelets'+'goswami')
        self.key_val=self.key_val+1

        self.my_list.append(book(self.key_val,'data smart','foreman','data_science',1))
        self.my_unique_books.add('data smart'+'foreman')
        self.key_val = self.key_val + 1

        self.my_list.append(book(self.key_val, 'birth of theorm', 'vilani', 'mathematics',1))
        self.my_unique_books.add('birth of theorm'+'vilani')
        self.key_val = self.key_val + 1



    def print_my_list(self):
        for obj in self.my_list:
            print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}')


    def login_signup(self):
        ans=input("press 1 to log in and 2 to sign up")

        if(ans=='1'):
            input1 = input('Enter your email id')
            input2 = input('Enter your password')
            if (input1 in self.user_dict.keys() and self.user_dict[input1] == input2):
                return 'v' + ' ' + input1
            else:
                print("user not found or  you have entered the wrong credentials")
                return 'NA'
        else:
            input1 = input('enter your email id')
            input2 = input('enter your password')
            input3 = input('enter the password again')
            if (input2 == input3 and input1.count('@') == 1):
                print('account created')
                self.user_dict[input1] = input2
                return 'NAC' + ' ' + input1

            else:
                print('you have entered the wrong email id or password not match')
                print('retry')
                return 'fk'


class admin():

    def __init__(self):
        self.user_data_dict={}
        self.admin_id='sid@gmail.com'
        self.admin_password='hashcode1.'
        self.user_list=[]


    def verify(self,i1,i2):
        if(i1==self.admin_id and i2==self.admin_password):
            return True
        else:
            return False

    #This function is used to add books to the database
    def add_to_database(self,library):
        title_of_book=input('enter the name of the book')
        author_of_book=input('enter the author of the book')
        genre_of_book=input('enter the genre of the book')
        s=title_of_book+author_of_book
        if s not in library.my_unique_books:
            library.my_list.append(book(library.key_val,title_of_book,author_of_book,genre_of_book,1))
            library.my_unique_books.add(s)
            library.key_val=library.key_val+1
        else:
            for itr in library.my_list:
                if(itr.title==title_of_book and author_of_book==itr.author):
                    itr.count=itr.count+1
                    break
        print('book added succesfully')


#this function is used to add book to a particular user
    def change_in_database(self,library,email,key):
        for itr in  library.my_list:
            if(itr.key==key):
                if(itr.count==0):
                    print('book not available')
                    break
                else:
                    self.user_data_dict.setdefault(email, []).append(itr)
                    itr.count=itr.count-1
                    print('book added')
                    break


    def generate_report_of_all_books(self, library):
        for obj in library.my_list:
            print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}')
    def generate_report_of_all_users(self):
        alpha=1
        for key in self.user_data_dict:
            print(f'User no. {alpha}')
            print(f"email: {key}")
            for itr in self.user_data_dict[key]:
                print(f"books taken: key={itr.key} title={itr.title} author={itr.author} genre={itr.genre}")
            print('----------------------------')
            alpha=alpha+1

    def details_of_particular_user(self,email):
        kp=False
        for itr in self.user_data_dict.get(email, []):
            print(f"books taken: key={itr.key} title={itr.title} author={itr.author} genre={itr.genre}")
            kp=True
        if(kp==False):
            print('No data is available for this email id')




class user():

    def show_me_the_books(self,library):
        for obj in library.my_list:
            if(obj.count>0):
                print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}')

    def filter_functionality(self,library):

        filter_input=input('Enter the basis on which you want the filter \n press 1 for title \n press 2 for author \n press 3 for genre')
        if(filter_input=='1'):
            title_filter_input=input('enter the title you want to filter for')
            kp=False
            for obj in library.my_list:
                if (obj.count>0 and obj.title==title_filter_input):
                    print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}')
                    kp=True
            if (kp == False):
                library.print_my_list()

        elif (filter_input == '2'):
            author_filter_input = input('enter the author you want to filter for')
            kp=False
            for obj in library.my_list:
                if (obj.count>0 and obj.author == author_filter_input):
                    print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}')
                    kp=True
            if (kp == False):
                library.print_my_list()
        elif(filter_input=='3'):
            genre_filter_input=input('enter the genre you want to filter for')
            kp=False
            for obj in library.my_list:
                if (obj.count>0 and obj.genre == genre_filter_input):
                    print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}')
                    kp=True
            if (kp == False):
                library.print_my_list()


    def show_my_data(self,admin,email):
        flag = False
        for obj in admin.user_data_dict.get(email, []):
            flag = True
            print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}')
        if flag==False:
            print('NO books are issued  for this user')




if __name__=="__main__":
    lc=library()
    lc.check()
    lc.print_my_list()
    print('----------------')
    ad=admin()
    lc.print_my_list()
    user_obj = user()
    print('----------------')
    #ad.generate_report_of_all_books(lc)
    print('-----------------------')
    print('check complete')
    print('---------------------------------------------\n\n')
    print('Welcome to my library')
    print('please Login/Signup for the account')
    while 1:
        admin_person=input('press 1 if you want to log in for admin else press any key')
        if(admin_person=='1'):
            input1=input('Enter your email')
            input2=input('enter your password')
            check_admin=ad.verify(input1,input2)
            if(check_admin==True):
                print('admin login successfully')
                while 1:
                    admin_input=input('press 1 for add a book a database \n  press 2 to generate a report of all books \n press 3 to see details of a particular user \n press 4 to generate report of all users \n press 5 to generate  a complete report \n press 6 to log out')
                    if(admin_input=='1'):
                        ad.add_to_database(lc)
                    elif(admin_input=='2'):
                        ad.generate_report_of_all_books(lc)
                    elif(admin_input=='3'):
                        email_input=input('enter the email of the user that you want the info for :')
                        ad.details_of_particular_user(email_input)
                    elif(admin_input=='4'):
                        ad.generate_report_of_all_users()

                    elif(admin_input=='5'):
                        pass
                    elif(admin_input=='6'):
                        break
            else:
                print('Incorrect Details')
        else:

            k = lc.login_signup()
            if(k=='NA' or k=='fk'):
                continue
            kk = k.split()
            if (kk[0] == 'NAC'):
                print('user portal shown up')
                user_obj = user()
                while True:
                    user_input = input(
                        'press 1 for seeing the available books : \n press 2 for filter: \n press 3 for show my data \n  press 4 to add book \n press 5 for end portal')
                    if (user_input == '1'):
                        user_obj.show_me_the_books(lc)
                    elif (user_input == '2'):
                        user_obj.filter_functionality(lc)
                    elif (user_input == '3'):
                        # print(kk[1])
                        user_obj.show_my_data(ad, kk[1])
                    elif (user_input == '4'):
                        key_to_add_in_database = int(input('Enter the key number of book to add in database'))
                        ad.change_in_database(lc, kk[1], key_to_add_in_database)
                    elif (user_input == '5'):
                        break
            elif (kk[0] == 'v'):
                print('user portal shown up')

                while True:
                    user_input = input(
                        'press 1 for seeing the available books : \n press 2 for filter: \n press 3 for show my data \n  press 4 to add book \n press 5 for end portal')
                    if (user_input == '1'):
                        user_obj.show_me_the_books(lc)
                    elif (user_input == '2'):
                        user_obj.filter_functionality(lc)
                    elif (user_input == '3'):
                        # print(kk[1])
                        user_obj.show_my_data(ad, kk[1])
                    elif (user_input == '4'):
                        key_to_add_in_database = int(input('Enter the key number of book to add in database'))
                        ad.change_in_database(lc, kk[1], key_to_add_in_database)
                    elif (user_input == '5'):
                        break























