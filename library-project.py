'''
    Project: Wizard Librarian
    Program Description: simulating a digital library site with properties
    like sort, search, exit
'''




import sys
class Book:
    def __init__(self,wizard_file=None):
        self.wizard_file=wizard_file
      
    def get_wiz(self):
        '''initializing function to open books file'''
        
        try:
            with open('wizard_books.txt', 'r') as file:
                self.wizard_file=file.readlines()
        except FileNotFoundError:
            self.wizard_file=[]
            print(self.wizard_file)
            print('We are sorry, the Hogwarts security deems you unfit to access this Library. Try again')
            main_menu()

    def get_title(self):
        '''function that sorts the book file based on title'''
        
        new=open('wizard_books_TITLE.txt','w')
        self.get_wiz() 
        self.wizard_file.sort()
        for a in self.wizard_file:    
            new.write(f'{a}')
        new.close()
        print('*** Books were sorted by title and exported to wizard_books_TITLE.txt ***')
        
  
    def get_author(self):
        '''function that sorts the book file based on author last name'''
        Auth=open('wizard_books_AUTHOR.txt','w')
        self.get_wiz()
        self.wizard_file.sort(key=lambda x: x.split()[-1])
        for b in self.wizard_file:
            Auth.write(b)
        Auth.close()
        print('*** Books were sorted by author and exported to wizard_books_AUTHOR.txt ***')

    def searching(self, r, ind=0):
        '''function search for keywords or phrases entered by user'''
        
        self.get_wiz()
        A=[]
        for a in self.wizard_file:
            o=a.split('-')[ind].lower()
            A.append(o)
        B=''.join(A)
        if r.lower() in B:
            print(f'=== MATCHES FOR [{r}] ===')
            for found in self.wizard_file:
                tit=found.split('-')[ind]
                if r.lower() in tit.lower():
                    print(found)
                else:
                    pass
            print('=========================================')
            A.clear()
            
        elif r.lower() not in B:
            print(f'===== NO MATCHES FOUND FOR THE SEARCH [{r}] =====')
            A.clear()    
        
    def defaulter(self, crit):
        '''function that resorts to searching the original books file if both title and author sorted files do not exist.'''
        
        print("[homenum revelio] Enter your search keyphrase or type 'back' to return")
        dee=input('>')
        if dee.lower()=='back':
            search()
        if crit=='title':
            self.searching(dee, 0)
            self.defaulter(crit)
        elif crit=='author':
            self.searching(dee,1)
            self.defaulter(crit)
        elif crit=='either':
            self.get_wiz()
            A=[]
            for a in self.wizard_file:
                o=a.lower()
                A.append(o)
            B=''.join(A)
            if dee.lower() in B:
                print(f'=== MATCHES FOR [{dee}] ===')
                for found in self.wizard_file:
                    
                    if dee.lower() in found.lower():
                        print(found)
                    else:
                        pass
                print('=========================================')
                A.clear()
                
            elif dee.lower() not in B:
                print(f'===== NO MATCHES FOUND FOR THE SEARCH [{dee}] =====')
                A.clear() 
            self.defaulter(crit)
        elif crit=='back':
            search()
            
    def get_search_auth_title(self, criteria):
        '''function that searches the sorted books if they exist'''
        
        with open('wizard_books_%s.txt' % criteria,'r') as fiel:
                a_t_search=fiel.readlines()
        if criteria=='AUTHOR':
            name=input('[homenum revelio] Enter your search keyphrase or type \'back\' to return\n>')
            if name.lower()=='back':
                search()
            else:
                A=[]
                for a in a_t_search:
                    o=a.split('-')[1].lower()
                    A.append(o)
                B=''.join(A)
                if name.lower() in B:
                    print(f'=== MATCHES FOR [{name}] ===')
                    for found in a_t_search:
                        tit=found.split('-')[1]
                        if name.lower() in tit.lower():
                            print(found)
                        else:
                            pass
                    print('=========================================')
                    A.clear()
                    self.get_search_auth_title(criteria)
                elif name.lower() not in B:
                    print(f'===== NO MATCHES FOUND FOR THE SEARCH [{name}] =====')
                    A.clear()
                    self.get_search_auth_title(criteria)
        elif criteria=='TITLE':
            name=input('[homenum revelio] Enter your search keyphrase or type \'back\' to return\n>')
            if name.lower()=='back':
                search()
            else:
                A=[]
                for a in a_t_search:
                    o=a.split('-')[0].lower()
                    A.append(o)
                B=''.join(A)
                if name.lower() in B:
                    print(f'=== MATCHES FOR [{name}] ===')
                    for found in a_t_search:
                        tit=found.split('-')[0]
                        if name.lower() in tit.lower():
                            print(found)
                        else:
                            pass
                    print('=========================================')
                    A.clear()
                    self.get_search_auth_title(criteria)
                elif name.lower() not in B:
                    print(f'===== NO MATCHES FOUND FOR THE SEARCH [{name}] =====')
                    A.clear()
                    self.get_search_auth_title(criteria)   
        
def sort():
    '''sorting function that calls from the book class to sort the books.'''
    
    print('[Wingardium Leviosa] How would you like to sort the catalog? [title, author, back]')
    sorter=input('>').lower()
    if sorter=='title':
        book.get_title()
        main_menu()
    elif sorter=='author':
        book.get_author()
        main_menu()
    elif sorter=='back':
        main_menu()
    else:
        pass
    
        
        
      
def search():
    '''searching function that calls from the book class to search the books'''
      
    print('[Aparecium] How would you like to search by? [title, author, either, back]')
    searcher= input('>').lower()
    if searcher=='author':
        try:
            book.get_search_auth_title(searcher.upper())  
        except FileNotFoundError:
            print("Reparo!: Book file [wizard_books_AUTHOR.txt] not found! Defaulting to 'wizard_books.txt'")
            book.defaulter(searcher)
    elif searcher=='title':
        try:
            book.get_search_auth_title(searcher.upper())   
        except FileNotFoundError:
            print("Reparo!: Book file [wizard_books_TITLE.txt] not found! Defaulting to 'wizard_books.txt'")
            book.defaulter(searcher)      
    elif searcher=='either':
        book.defaulter(searcher)
    elif searcher=='back':
        main_menu()
    else:
        pass
    
def main_menu():
    '''main menu function that controls the whole system'''
    
    print('[Alohomora] Welcome, to the Wizard Library! What would you like to do? [sort, search, exit]')
    entry=input('>').lower()
    while True:
        if entry=='sort':
            while True:
                sort()
                break
        elif entry=='search':
            while True:
                search()
                break
        
        elif entry=='exit':
            print(f'Fare thee well, seeker of knowledge! A great pleasure t\'was to grace thine walls. Evanesco ')
            sys.exit()
        else:
            print('unknown input')
            main_menu()
         
            

if __name__=="__main__":
    book=Book()
    main_menu()































