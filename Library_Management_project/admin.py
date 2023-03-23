import json

from datetime import datetime
from datetime import date

from book import Book

class admin():

    def __init__(self):
        self.user_data_dict={}
        self.admin_id='sid@gmail.com'
        self.admin_password='hashcode1.'
        self.user_list=[]
        self.day=1
        self.book_issue_dict={}


    def verify(self,id,password):
        """

        :param i1:admin id
        :param i2:admin password
        :return: admin is authenticated or not
        """
        file = open("my_file.json", "r")
        x = file.read()
        final_data = json.loads(x)
        for itr in final_data['admin_list']:
            if(itr['admin_id']==id and itr['admin_password']==password):
                return True
        return False


    def add_new_member_to_admins(self):
        input_mailid=input("Enter the mail id of the new member")
        input_password=input("Enter the password")
        if(input_mailid.count('@')!=1 or input_password==''):
            print('input parameters not right \nplease retry')

        data={"admin_id":input_mailid, "admin_password":input_password}

        with open('my_file.json', 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["admin_list"].append(data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=3)

        print("member added successfully\n\n")

    #This function is used to add books to the database
    def add_to_database(self,library):
        """

        :param library:
        :return: none
        """
        title_of_book=input('enter the name of the book')
        author_of_book=input('enter the author of the book')
        genre_of_book=input('enter the genre of the book')
        s=title_of_book+author_of_book
        if s not in library.my_unique_books:
            library.my_list.append(Book(library.key_val,title_of_book,author_of_book,genre_of_book,1))
            library.my_unique_books.add(s)
            library.key_val=library.key_val+1
        else:
            for itr in library.my_list:
                if(itr.title==title_of_book and author_of_book==itr.author):
                    itr.count=itr.count+1
                    break
        print('book added succesfully\n')


    def change_in_database(self,library,email,key):
        """
        Used to add book to a particular user.

        :param library:
        :param email:
        :param key:
        :return: None
        """
        for itr in  library.my_list:
            if(itr.key==key):
                if(itr.count==0):
                    print('book not available\n')
                    break
                else:
                    self.user_data_dict.setdefault(email, []).append(itr)
                    itr.count=itr.count-1
                    print('book added\n')
                    break


    def generate_report_of_all_books(self, library):
        """

        :param library:
        :return: none
        """
        for obj in library.my_list:
            print(f'key={obj.key} title= {obj.title} genre={obj.genre} author={obj.author} count={obj.count}\n')
    def generate_report_of_all_users(self):

        cnt=1
        for key in self.user_data_dict:
            print(f'User no. {cnt}')
            print(f"email: {key}")
            for itr in self.user_data_dict[key]:
                print(f"books taken: key={itr.key} title={itr.title} author={itr.author} genre={itr.genre}")
            print('----------------------------')
            cnt=cnt+1

    def details_of_particular_user(self,email):
        kp=False
        for itr in self.user_data_dict.get(email, []):
            print(f"books taken: key={itr.key} title={itr.title} author={itr.author} genre={itr.genre} \n")
            kp=True
        if(kp==False):
            print('No data is available for this email id \n')

    def book_issue_reissue_status(self,title_of_the_book):
        """

        :param title_of_the_book:
        :return: none
        """

        self.book_issue_dict.setdefault(title_of_the_book, []).append("{:%B %d, %Y}".format(datetime.now()))



    def check_status_of_the_book(self,give_me_the_title):
        """
        function use: book issue-reissue when
        :param give_me_the_title:
        :return:
        """
        for itr in self.book_issue_dict[give_me_the_title]:
            print(f'book issued on {itr} \n')


    def login_signup(self,library):
        """

        :param library:
        :return: account created(NAC) , login successfull(v), !login successfull(NA) ,password not match(fk)
        """
        ans=input("press 1 to log in and 2 to sign up :")

        if(ans=='1'):
            input1 = input('Enter your email id :')
            input2 = input('Enter your password :')
            if (input1 in library.user_dict.keys() and library.user_dict[input1] == input2):
                return 'v' + ' ' + input1
            else:
                print("user not found or  you have entered the wrong credentials")
                print('---------------------------------------------------------------------------------------------')
                print('\n\n')
                return 'NA'
        else:
            input1 = input('enter your email id :')
            input2 = input('enter your password :')
            input3 = input('enter the password again :')
            if (input2 == input3 and input1.count('@') == 1):
                print('account created\n')
                library.user_dict[input1] = input2
                return 'NAC' + ' ' + input1

            else:
                print('you have entered the wrong email id or password not match :')
                print('retry')
                print('---------------------------------------------------------------------------------------------')
                print('\n\n')
                return 'fk'