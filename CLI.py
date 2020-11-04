def majorInformation(infoType,rating):
    #This section of this function deals with information that has to do with majors and their intensity:
    if infoType == "intensity":
        if rating =="1":
            return ["Buisness Adminstraton","Lesuire Studies", "Physical Education", "Marketing"]
        elif rating =="2":
            return ["Finnance","Pychology","Economics","Socioology","Political Science"]
        elif rating =="3":
            return ["Computer Science","History","Accounting","Elementary Education","English","Theater"]
        elif rating =="4":
            return ["Anthropology","Philosophy","Mathmatics","Biology","Music"]
        elif rating =="5":
            return ["Nursing","Art","Chemistry","Physics","Arcitecture"]
    #This section of this function deals with information that has to do with majors and their average starting salaries
    elif infoType == "salary":
        if rating == "y":
            return ["Computer Science","Pychology","Economics","Marketing","Physics","Chemistry"]
        elif rating == "n":
            return ["Buisness Adminstraton","Lesuire Studies", "Physical Education", "Marketing","Finnance","Pychology","Economics","Socioology","Political Science",["Computer Science","History","Accounting","Elementary Education","English","Theater","Anthropology","Philosophy","Mathmatics","Biology","Music","Nursing","Art","Chemistry","Physics","Arcitecture"]
    #This section of this function deals with information that has to do with majors and their realtive popularity/size
    elif infoType == "popularity":
        if rating == "1":
            return ["Buisness Adminstraton","Marketing","Physical Education","Elementary Education","English","Nursing","Art","Socioology","Political Science","Arcitecture"]
        elif rating == "2":
            return ["Buisness Adminstraton","Lesuire Studies", "Physical Education", "Marketing","Finnance","Pychology","Economics","Socioology","Political Science",["Computer Science","History","Accounting","Elementary Education","English","Theater","Anthropology","Philosophy","Mathmatics","Biology","Music","Nursing","Art","Chemistry","Physics","Arcitecture"]
        elif rating == "3": 
            return ["Physics","Chemistry","Lesuire Studies","Anthropology","Mathmatics","Biology"]
#This function asks the user for an input, and then based on that input returns the proper results from another function that indexes the results this function is trying to fraw from:
def intensityFunction():
    intensity=input("On a scale of 1-5, how intense do you wish your classes to be?")
    if intensity == "1":
        return majorInformation("intensity","1")
    elif intensity == "2":
        return majorInformation("intensity","2")
    elif intensity == "3":
        return majorInformation("intensity","3")
    elif intensity == "4":
        return majorInformation("intensity","4")
    elif intensity == "5":
        return majorInformation("intensity","5")
#This function asks the user for an input, and then based on that input returns the proper results from another function that indexes the results this function is trying to fraw from:
def salaryFunction():
    salary=input("Do you care if you have a high starting salary?(y/n)")
    if salary == "y":
        return majorInformation("salary","y")
    elif salary == "n":
        return majorInformation("salary","n")
def popularityFunction():
    popularity=input("Do you want a major that has a large number of people in it?\n1. Yes\n2. Don't Care\n3. No")
    if popularity == "1":
        return majorInformation("popularity","1")
    elif popularity == "2":
        return majorInformation("popularity","2")
    elif popularity == "3":
        return majorInformation("popularity","3")

def majorDecision():
    intensity = intensityFunction()
    salary = salaryFunction()
    popularity = popularityFunction()
    print(intensity)









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
    #This line opens up the display for our main menu:
    menu()
    #This section of code creates inputs for each option displayed in the above menu:
    menuInput = input(">")
    #Each menu item returns a specic string value (which is a number in this case) to the function.
    #This is so we can call this main menu function and figure out what we selected.
    #We can then use those responses in diffrent functions later on!
    if menuInput == "1":
        return "1"
    elif menuInput == "2":
        return "2"
    elif menuInput == "3":
        return "3"
    elif menuInput == "4":
        return "4"
    elif menuInput == "5":
        return "5"
def menuLoop():
    #This section creates an indefinte loop for our main menu:
    x = 1 
    while x == 1: 
        state = mainMenu()
        if state == "1":
            pass
        elif state == "2":
            pass
        elif state == "3":
            pass
        elif state == "4":
            pass
        #Instead of calling a function, this "elif(xyz)" statement breaks the main menu loop, and thus ends the program:
        elif state == "5":
            break
menuLoop()