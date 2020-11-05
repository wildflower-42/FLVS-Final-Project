studentMajor = ""
def majorInformation(infoType,rating):
    #This section of this function deals with information that has to do with majors and their intensity:
    if infoType == "intensity":
        if rating =="1":
            return ["Business Adminstraton","Leisure Studies", "Physical Education", "Marketing"]
        elif rating =="2":
            return ["Finnance","Psychology","Economics","Sociology","Political Science"]
        elif rating =="3":
            return ["Computer Science","History","Accounting","Elementary Education","English","Theater"]
        elif rating =="4":
            return ["Anthropology","Philosophy","Mathematics","Biology","Music"]
        elif rating =="5":
            return ["Nursing","Art","Chemistry","Physics","Architecture"]
    #This section of this function deals with information that has to do with majors and their average starting salaries
    elif infoType == "salary":
        if rating == "y":
            return ["Computer Science","Psychology","Economics","Marketing","Physics","Chemistry"]
        elif rating == "n":
            return ["Business Adminstraton","Leisure Studies", "Physical Education", "Marketing","Finnance","Psychology","Economics","Sociology","Political Science","Computer Science","History","Accounting","Elementary Education","English","Theater","Anthropology","Philosophy","Mathematics","Biology","Music","Nursing","Art","Chemistry","Physics","Architecture"]
    #This section of this function deals with information that has to do with majors and their relative popularity/size
    elif infoType == "popularity":
        if rating == "1":
            return ["Business Adminstraton","Marketing","Physical Education","Elementary Education","English","Nursing","Art","Sociology","Political Science","Architecture"]
        elif rating == "2":
            return ["Business Adminstraton","Leisure Studies", "Physical Education", "Marketing","Finnance","Psychology","Economics","Sociology","Political Science","Computer Science","History","Accounting","Elementary Education","English","Theater","Anthropology","Philosophy","Mathematics","Biology","Music","Nursing","Art","Chemistry","Physics","Architecture"]
        elif rating == "3": 
            return ["Physics","Chemistry","Leisure Studies","Anthropology","Mathematics","Biology"]
#This function asks the user for an input, and then based on that input returns the proper results from another function that indexes the results this function is trying to draw from:
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
#This function asks the user for an input, and then based on that input returns the proper results from another function that indexes the results this function is trying to draw from:
def salaryFunction():
    salary=input("Do you care if you have a high starting salary?(y/n)")
    if salary == "y":
        return majorInformation("salary","y")
    elif salary == "n":
        return majorInformation("salary","n")
def popularityFunction():
    popularity=input("Do you want a major that has a large number of people in it?\n1. Yes\n2. Don't Care\n3. No\n>")
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
    majorsList = set(intensity) & set(salary) & set(popularity)
    return majorsList
def majorSelect(majorsList):
    print("Please select your major of choice:\n(Please type the full name of the major that you are selecting)\n\n")
    for n in majorsList:
        print(n)
def majorRecord(majorOfChoice):
    studentMajor == majorOfChoice
def registerMajor():
    majorsList = ["Business Adminstraton","Leisure Studies", "Physical Education", "Marketing","Finnance","Psychology","Economics","Sociology","Political Science","Computer Science","History","Accounting","Elementary Education","English","Theater","Anthropology","Philosophy","Mathematics","Biology","Music","Nursing","Art","Chemistry","Physics","Architecture"]
    print("Please select a major from the list:\n(Please type the full name of the major that you are selecting)\n\n")
    for n in majorsList:
        print(n)
    studentMajor = input(">")
def salaryTable1():
    print("""
+--------------------------------------+------------------------+--------------------------+---------------------------------------------------+
|         Undergraduate Major          | Starting Median Salary | Mid-Career Median Salary | Percent change from Starting to Mid-Career Salary |
+--------------------------------------+------------------------+--------------------------+---------------------------------------------------+
| Religion                             |                  34100 |                    52000 |                                              52.5 |
| Education                            |                  34900 |                    52000 |                                                49 |
| Spanish                              |                  34000 |                    53100 |                                              56.2 |
| Interior Design                      |                  36100 |                    53200 |                                              47.4 |
| Music                                |                  35900 |                    55000 |                                              53.2 |
| Nutrition                            |                  39900 |                    55300 |                                              38.6 |
| Criminal Justice                     |                  35000 |                    56300 |                                              60.9 |
| Drama                                |                  35900 |                    56900 |                                              58.5 |
| Hospitality & Tourism                |                  37800 |                    57500 |                                              52.1 |
| Sociology                            |                  36500 |                    58200 |                                              59.5 |
| Graphic Design                       |                  35700 |                    59800 |                                              67.5 |
| Psychology                           |                  35900 |                    60400 |                                              68.2 |
| Health Care Administration           |                  38800 |                    60600 |                                              56.2 |
| Anthropology                         |                  36800 |                    61500 |                                              67.1 |
| Forestry                             |                  39100 |                    62600 |                                              60.1 |
| English                              |                  38000 |                    64700 |                                              70.3 |
| Biology                              |                  38800 |                    64800 |                                                67 |
| Art History                          |                  35800 |                    64900 |                                              81.3 |
| Geography                            |                  41200 |                    65500 |                                                59 |
| Journalism                           |                  35600 |                    66700 |                                              87.4 |
| Nursing                              |                  54200 |                    67000 |                                              23.6 |
| Film                                 |                  37900 |                    68500 |                                              80.7 |
| Communications                       |                  38100 |                    70000 |                                              83.7 |
| History                              |                  39200 |                    71000 |                                              81.1 |
| Agriculture                          |                  42600 |                    71900 |                                              68.8 |
| Business Management                  |                  43000 |                    72100 |                                              67.7 |
| Information Technology (IT)          |                  49100 |                    74800 |                                              52.3 |
| Architecture                         |                  41600 |                    76800 |                                              84.6 |
| Accounting                           |                  46000 |                    77100 |                                              67.6 |
| Political Science                    |                  40800 |                    78200 |                                              91.7 |
| Geology                              |                  43500 |                    79500 |                                              82.8 |
| Marketing                            |                  40800 |                    79600 |                                              95.1 |
| Chemistry                            |                  42600 |                    79900 |                                              87.6 |
| International Relations              |                  40900 |                    80900 |                                              97.8 |
| Philosophy                           |                  39900 |                    81200 |                                             103.5 |
| Management Information Systems (MIS) |                  49200 |                    82300 |                                              67.3 |
| Finance                              |                  47900 |                    88300 |                                              84.3 |
| Construction                         |                  53700 |                    88900 |                                              65.5 |
| Civil Engineering                    |                  53900 |                    90500 |                                              67.9 |
| Physician Assistant                  |                  74300 |                    91700 |                                              23.4 |
| Math                                 |                  45400 |                    92400 |                                             103.5 |
| Mechanical Engineering               |                  57900 |                    93600 |                                              61.7 |
| Industrial Engineering               |                  57700 |                    94700 |                                              64.1 |
| Computer Science                     |                  55900 |                    95500 |                                              70.8 |
| Physics                              |                  50300 |                    97300 |                                              93.4 |
| Economics                            |                  50100 |                    98600 |                                              96.8 |
| Aerospace Engineering                |                  57700 |                   101000 |                                                75 |
| Electrical Engineering               |                  60900 |                   103000 |                                              69.1 |
| Computer Engineering                 |                  61400 |                   105000 |                                                71 |
| Chemical Engineering                 |                  63200 |                   107000 |                                              69.3 |
+--------------------------------------+------------------------+--------------------------+---------------------------------------------------+
        """)
def salaryTable2():
    print("""
    
+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
| Mid-Career 10th Percentile Salary | Mid-Career 25th Percentile Salary | Mid-Career 75th Percentile Salary | Mid-Career 90th Percentile Salary |
+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
|                             29700 |                             36500 |                             70900 |                             96400 |
|                             29300 |                             37900 |                             73400 |                            102000 |
|                             31000 |                             40000 |                             76800 |                             96400 |
|                             35700 |                             42600 |                             72500 |                            107000 |
|                             26700 |                             40200 |                             88000 |                            134000 |
|                             33900 |                             44500 |                             70500 |                             99200 |
|                             32200 |                             41600 |                             80700 |                            107000 |
|                             36700 |                             41300 |                             79100 |                            153000 |
|                             35500 |                             43600 |                             81900 |                            124000 |
|                             30700 |                             40400 |                             81200 |                            118000 |
|                             36000 |                             45500 |                             80800 |                            112000 |
|                             31600 |                             42100 |                             87500 |                            127000 |
|                             34600 |                             45600 |                             78800 |                            101000 |
|                             33800 |                             45500 |                             89300 |                            138000 |
|                             41000 |                             49300 |                             78200 |                            111000 |
|                             33400 |                             44800 |                             93200 |                            133000 |
|                             36900 |                             47400 |                             94500 |                            135000 |
|                             28800 |                             42200 |                             87400 |                            125000 |
|                             40000 |                             50000 |                             90800 |                            132000 |
|                             38400 |                             48300 |                             97700 |                            145000 |
|                             47600 |                             56400 |                             80900 |                             98300 |
|                             33900 |                             45500 |                            100000 |                            136000 |
|                             37500 |                             49700 |                             98800 |                            143000 |
|                             37000 |                             49200 |                            103000 |                            149000 |
|                             36300 |                             52100 |                             96300 |                            150000 |
|                             38800 |                             51500 |                            102000 |                            147000 |
|                             44500 |                             56700 |                             96700 |                            129000 |
|                             50600 |                             62200 |                             97000 |                            136000 |
|                             42200 |                             56100 |                            108000 |                            152000 |
|                             41200 |                             55300 |                            114000 |                            168000 |
|                             45000 |                             59600 |                            101000 |                            156000 |
|                             42100 |                             55600 |                            119000 |                            175000 |
|                             45300 |                             60700 |                            108000 |                            148000 |
|                             38200 |                             56000 |                            111000 |                            157000 |
|                             35500 |                             52800 |                            127000 |                            168000 |
|                             45300 |                             60500 |                            108000 |                            146000 |
|                             47200 |                             62100 |                            128000 |                            195000 |
|                             56300 |                             68100 |                            118000 |                            171000 |
|                             63400 |                             75100 |                            115000 |                            148000 |
|                             66400 |                             75200 |                            108000 |                            124000 |
|                             45200 |                             64200 |                            128000 |                            183000 |
|                             63700 |                             76200 |                            120000 |                            163000 |
|                             57100 |                             72300 |                            132000 |                            173000 |
|                             56000 |                             74900 |                            122000 |                            154000 |
|                             56000 |                             74200 |                            132000 |                            178000 |
|                             50600 |                             70600 |                            145000 |                            210000 |
|                             64300 |                             82100 |                            127000 |                            161000 |
|                             69300 |                             83800 |                            130000 |                            168000 |
|                             66100 |                             84100 |                            135000 |                            162000 |
|                             71900 |                             87300 |                            143000 |                            194000 |
+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
    """)
def dataAppendix(Query):
    
    if Query == "salaries":
        x=1
        while x == 1:
            salaryTable1()
            input("1. Next Page\n>")
            salaryTable2()
            turnPage = input("1. Next Page\n2. Back\n>")
            if turnPage == "1":
                break
            elif turnPage == "2":
                pass
    elif Query == "popularity":
        print(r"""
        
+----------------------------------------------------+-------------------+
|                       Major:                       | % of US Students: |
+----------------------------------------------------+-------------------+
| Business                                           | 26.1%             |
| Education                                          | 9.4%              |
| Humanities and Liberal Arts                        | 8.6%              |
| Architecture and Engineering                       | 8.3%              |
| Health                                             | 7.5%              |
| Social Sciences                                    | 6.9%              |
| Computer Sciences, statistics and Mathematics      | 5.6%              |
| Psychology and Social Work                         | 5.2%              |
| Communications and Journalism                      | 5.2%              |
| Arts                                               | 4.8%              |
| Biology and Life Sciences                          | 3.3%              |
| Industrial Arts, Consumer services, and recreation | 2.7%              |
| Law and Public Policy                              | 2.6%              |
| Physical Sciences                                  | 2.5%              |
| Agriculture and Natural Resources                  | 1.5%              |
+----------------------------------------------------+-------------------+
        """)
        input("Press any key to continue:\n>")
    elif Query == "difficulty":
        print("""
+-------------------------+--------------------------------------------------+
|         Major:          | Average Number of Hours Spent Studying Per Week: |
+-------------------------+--------------------------------------------------+
| Speech                  |                                             10.8 |
| Leisure Studies         |                                             11.1 |
| Physical Education      |                                             11.8 |
| Marketing               |                                             12.1 |
| Business Administration |                                             13.2 |
| Finance                 |                                             13.3 |
| Sociology               |                                             13.8 |
| Psychology              |                                             13.9 |
| Economics               |                                             14.4 |
| Political Science       |                                             14.6 |
| Computer Science        |                                             14.7 |
| History                 |                                               15 |
| Accounting              |                                             15.1 |
| Elementary Education    |                                             15.2 |
| English                 |                                             15.9 |
| Theater                 |                                               16 |
| Anthropology            |                                               16 |
| Philosophy              |                                             16.2 |
| Mathematics             |                                             16.4 |
| Biology                 |                                             16.7 |
| Music                   |                                             17.5 |
| Nursing                 |                                               18 |
| Art                     |                                             18.1 |
| Chemistry               |                                             18.4 |
| Physics                 |                                             19.7 |
| Chemical Engineering    |                                             21.6 |
| Architecture            |                                             23.7 |
+-------------------------+--------------------------------------------------+
        """)
def majorExplorationSubmenu():
    print("""
    Explore our major options:\n
    1. Explore major salaries\n
    2. Explore major popularity\n
    3. Explore major difficulty\n

    4. Back\n
    """)
    menuResponse = input(">")
    if menuResponse == "1":
        dataAppendix("salaries")
    elif menuResponse == "2":
        dataAppendix("popularity")
    elif menuResponse == "3":
        dataAppendix("difficulty")
    elif menuResponse == "4":
        pass
def calculatorSubmenu():
    print("""
    Please choose a function:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Summation
    6. Find the average of a set of data
    7. Back
    """)
    menuInput = input(">")
    if menuInput == "1":
        num1 = input("n1:\n")
        num2 = input("n2:\n")
        print(float(num1)+float(num2))
    elif menuInput == "2":
        num1 = input("n1:\n")
        num2 = input("n2:\n")
        print(float(num1)-float(num2))
    elif menuInput == "3":
        num1 = input("n1:\n")
        num2 = input("n2:\n")
        print(float(num1)*float(num2))
    elif menuInput == "4":
        num1 = input("n1:\n")
        num2 = input("n2:\n")
        print(float(num1)/float(num2))
    elif menuInput == "5":
        summationVector = []
        n = input("How many numbers would you like to summate?\n>")
        x=0
        while x != int(n):
            x+1
            num = input("n"+str(n)+":")
            summationVector.append(num)
        print(sum(float(summationVector)))
    elif menuInput == "6":
        summationVector = []
        n = input("How many numbers would you like to Average?\n>")
        x=0
        while x != int(n):
            x+1
            num = input("n"+str(x)+":")
            summationVector.append(num)
        vectorSize = len(int(summationVector))
        summation = sum(float(summationVector))
        print(summation/vectorSize)
    elif menuInput == "7":
        pass
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
    print("5. Calculator")
    print("6. Quit")

#This function creates the main menu loop:
def mainMenu():
    #This line opens up the display for our main menu:
    menu()
    #This section of code creates inputs for each option displayed in the above menu:
    menuInput = input(">")
    #Each menu item returns a specific string value (which is a number in this case) to the function.
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
    elif menuInput == "6":
        return "6"
def menuLoop():
    #This section creates an indefinite loop for our main menu:
    x = 1 
    while x == 1: 
        state = mainMenu()
        if state == "1":
            process = majorDecision()
            majorSelect(process)
            majorOfChoice = input(">")
            majorRecord(majorOfChoice)
            print("Thank you for selecting your new major!\nYou have officially been recorded as being a "+studentMajor+" major!!!!")
            input("Press any key to continue:\n>")
        elif state == "2":
            registerMajor()
            print("Thank you for selecting your new major!\nYou have officially been recorded as being a "+studentMajor+" major!!!!")
            input("Press any key to continue:\n>")
        elif state == "3":
            majorExplorationSubmenu()
        elif state == "4":
            about()
        elif state == "5":
            calculatorSubmenu()
        #Instead of calling a function, this "elif(xyz)" statement breaks the main menu loop, and thus ends the program:
        elif state == "6":
            break
menuLoop()