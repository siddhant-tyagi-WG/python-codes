


class book:
    def __init__(self,key,title,genre):
        self.key=key
        self.title=title
        self.genre=genre



class library:
    def login(self,verify):
        pass
    def signup(self,verify):
        pass


class admin(book):
    def add_to_database(self,verification_bool):
        pass

    def change_in_database(self,verification_bool):
        pass
    def generate_report(self):
        pass
    def details_of_user(self):
        pass

class user(book,admin):
    def filter_functionality(self,mylist):
        pass
    def show_my_data(self,mylist):
        pass
    def book_taken(self,mylist,secured_verification):
        pass
    def fine_paid(self,mylist,check_verify):
        pass


