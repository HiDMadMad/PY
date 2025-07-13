from emoji import emojize

class library():
    books = {}
    book_counter = 0

    def __init__(self, library_name):
        self.library_name = library_name
        print("\nyour library was created!")
    
    def add_book(self, title, author):
        self.title = title
        self.author = author
        library.books.update({library.book_counter:[self.title,self.author]})
        library.book_counter += 1
        return emojize(f"\n:inbox_tray: your book named '{self.title}' by '{self.author}' was added.")
    
    def delete_book(self, title):
        self.title = title
        book_to_del_list = []
        for book_to_del in library.books.items():
            if(book_to_del[1][0] == self.title):
                want_to_del = input(emojize(f"\n:magnifying_glass_tilted_right: {book_to_del[1][0]} by {book_to_del[1][1]} was founded, do you want to delete it? (Y/N)\n"))
                if(want_to_del.upper() in ["Y", "YES", "ARE", "BALE"]):
                    book_to_del_list.append(book_to_del[0])
        
        for deletes in book_to_del_list:
            library.books.pop(deletes)
            library.book_counter -=1                   
        
        return emojize(f"\n:outbox_tray: delete was successfully!")
    
    def search_book(self, title):
        self.title = title
        founded_cnt = 0
        for infos in library.books.values():
            if(infos[0] == self.title):
                founded_cnt+=1
                print(f"{founded_cnt}.{infos[0]} by {infos[1]}")
        return emojize(':index_pointing_up: they were founded :index_pointing_up:')

    def __str__(self):
        print(emojize("\n:books: your books are :"))
        book_cnt = 0
        for infos in library.books.values():
            book_cnt+=1
            print(f"{book_cnt}.{infos[0]} by {infos[1]}")
        return ''

    first_time_showing = True
    def show_menu(self):
        if(library.first_time_showing):
            print(f"\nwelcome to {self.library_name} library!!!")
            library.first_time_showing=False
        else:
            print(f"\nwhat do you want to do ?")
        print("1.show my books")
        print("2.add a new book")
        print("3.delete a book")
        print("4.search")
        
    def what_to_do(self):
        what = input(">> ")
        match what:
            case '1' | 'show' | 'show my books':
                print(self)
            case '2' | 'add' | 'add a new book':
                title_to_add = input("\nenter your book title : ")
                auth_to_add = input("enter your book author name : ")
                print(self.add_book(title_to_add, auth_to_add))
            case '3' | 'delete' | 'delete a book':
                title_to_del = input("\nenter the title of the book you want to delete it : ")
                print(self.delete_book(title_to_del))
            case '4' | 'search':
                title_to_search = input("\nenter the title of the book : ")
                print(self.search_book(title_to_search))




if __name__ == "__main__":
    lib = library(input("enter your library name : "))
    want_to_lib = True
    while want_to_lib :
        lib.show_menu()
        lib.what_to_do()
#MadMad_87