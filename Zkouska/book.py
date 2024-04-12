class Book:
    
    
    def __init__(self, book_info):  
        self.id = 0
        self.name = ""
        self.author = ""
        self.available = False

        book_info = book_info.split(';')
        self.id = int(book_info[0])
        self.name = book_info[1]
        self.author = book_info[2]
        if book_info[3] == "Available":
            self.available = True
    
    def __lt__(self, other) -> bool:        
        return self.author < other.author
        
    
    def __eq__(self, other) -> bool:    
        return self.id == other.id
        
    
    def repr(self) -> str:         
        return f"{self.id};{self.name};{self.author};{self.available}"
    
    def __str__(self):            
        return f"ID: {self.id}, Title: {self.name}, Author: {self.author}, Available: {'Yes' if self.available else 'No'}"
    
    def set_id(self, new_id):     
        self.id = new_id
        print("Kniha přidána s ID: " + str(new_id))
        
    def is_available(self):         
        return self.available

    def borrow_book(self):
        if self.available:
            self.available = False
        else:
            print(f"Tato kniha neni dostupna")
        
