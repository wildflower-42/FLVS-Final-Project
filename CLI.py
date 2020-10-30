#This function creates a block of pre-formated menu text for our program:
def menu():
    print('''\n                                                           
        88b           d88   ad88888ba         db         88888888ba  
        888b         d888  d8"     "8b       d88b        88      "8b 
        88`8b       d8'88  Y8,              d8'`8b       88      ,8P 
        88 `8b     d8' 88  `Y8aaaaa,       d8'  `8b      88aaaaaa8P'  
        88  `8b   d8'  88    `"""""8b,    d8YaaaaY8b     88""""""'    
        88   `8b d8'   88          `8b   d8""""""""8b    88         
        88    `888'    88  Y8a     a8P  d8'        `8b   88         
        88     `8'     88   "Y88888P"  d8'          `8b  88 
    ''')
    print("1. Find Your Major")
    print("2. Register your major")
    print("3. Learn About Majors")
    print("4. About")
    print("5. Quit")

#This function creates the main menu loop:
def mainMenu():
    menu()
    menuInput = input(">")
mainMenu()