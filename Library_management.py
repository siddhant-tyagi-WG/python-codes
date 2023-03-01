


class book():

    def __init__(self,key,title,author,genre):
        self.key=key
        self.title=title
        self.author=author
        self.genre=genre




class library():

    def __init__(self):
        self.my_list=[]
        self.key_val=0
    def check(self):
        self.my_list.append(book(self.key_val,'Fundamentals of Wavelets','Goswami, Jaideva','signal_processing'))
        self.key_val=self.key_val+1
        self.my_list.append(book(self.key_val,'Data Smart','Foreman, John','data_science'))
        self.key_val = self.key_val + 1


    def print_my_list(self):
        for obj in self.my_list:
            print(obj.key,obj.title,obj.author,obj.genre)


    def login(self,verify):
        pass
    def signup(self,verify):
        pass



class admin():

    # def __init__(self):
    #     super().__init__()
    def add_to_database(self,library, verification_bool):
        library.my_list.append(book(library.key_val,'birth of theorm','vilani','mathematics'))
        library.key_val=library.key_val+1


    def change_in_database(self,verification_bool):
        pass

    def generate_report_of_all_users(self, library):
        for obj in library.my_list:
            print(obj.key, obj.title, obj.author, obj.genre)


    def details_of_user(self):
        pass

class user():
    def filter_functionality(self):
        pass
    def show_my_data(self):
        pass
    def book_taken(self):
        pass
    def fine_paid(self):
        pass

if __name__=="__main__":
    lc=library()
    lc.check()
    lc.print_my_list()
    print('----------------')
    ad=admin()
    ad.add_to_database(lc,True)
    lc.print_my_list()
    print('----------------')
    ad.generate_report_of_all_users(lc)








