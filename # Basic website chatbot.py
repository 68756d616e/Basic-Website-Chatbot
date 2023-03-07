# Basic website chatbot - Without Natural Langauge Learning models
# In this the use will be a finance bot

# In the future I may include a Bot API, voice recognition and nlp

    # In the future - The below will display adjustable lists the owner can edit, to customise the information the users request
#   AdjustableListOfQuestionA = []
#   AdjustableListOfQuestionB = []
#   AdjustableListOfQuestionC = []
#   AdjustableListOfQuestionD = []

# Loop
while True:

    # Greet customers               
    print("Hello! I'm a Finance chatbot here to help. How can we assist you today?")
    
    # Converse reasoning
    print("We'd like to understand your reasons for communicating with us!")            

    # User question input
    user_question = input("""Please choose one of the following options so we can help assist you further!
A - Provide information about financial products and services   
B - Offer investment advice  
C - Provide educational resources  
D - service inquiries
Please enter the letter :          """)

    # User choice provided
    if user_question == 'a' or user_question == 'A':
        print("You chose A - Information about financial products and services")
        print("Please choose one of the following services!")
        print() # Space
        list_of_services = input("""List of Products and services!
A - Investment services
B - Financial planning services
C - Financial education
D - Accounting and tax service
- Back
""") # List of generic finance products and services
        
        print() # Space
        if list_of_services == 'a' or list_of_services == 'A':
            print("You chose Investment services")

        elif list_of_services == 'b' or list_of_services == 'B':
            print("You chose Financial planning services")

        elif list_of_services == 'c' or list_of_services == 'C':
            print("You chose Financial education")

        elif list_of_services == 'd' or list_of_services == 'D':
            print("You chose Accounting and tax service")
            
        elif list_of_services == 'Back' or list_of_services == 'back':
            print(user_question)
        
        else:
            print() # ...
            break

    elif a == 'b' or a == 'B':
        print("You chose B - Investment advice  ")
        a= input()
        
        if a == 'a' or a == 'A':
            print()

        elif a == 'a' or a == 'A':
            print()

        elif a == 'a' or a == 'A':
            print()

        elif a == 'a' or a == 'A':
            print()
            
        elif a == 'a' or a == 'A':
            print()
        
        else:
            print() # ...
            break
    
    elif b == 'c' or b == 'C':
        print("You chose C - Educational resources ")
        b = input()
        
        if b == 'a' or b == 'A':
            print()

        elif b == 'a' or b == 'A':
            print()

        elif b == 'a' or b == 'A':
            print()

        elif b == 'a' or b == 'A':
            print()
            
        elif b == 'a' or b == 'A':
            print()
        
        else:
            print() # ...
            break
    
    elif c == 'd' or c == 'D':
        print("You chose D - Service inquiries")
        c = input()

        if c == 'a' or c == 'A':
            print()

        elif c == 'a' or c == 'A':
            print()

        elif c == 'a' or c == 'A':
            print()

        elif c == 'a' or c == 'A':
            print()
            
        elif c == 'a' or c == 'A':
            print()
        
        else:
            print() # ...
            break

    else:
        print("Please choose A, B, C or D") # Repeat of initial question
        print(user_question)
