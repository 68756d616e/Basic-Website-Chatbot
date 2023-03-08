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
            print("Here is a list of our financial services")
            list_of_financial_services = int(input("""
1 - Brokerage services: Brokerage services are provided by firms that help investors buy and sell stocks, bonds, mutual funds, and other securities.

2 - Robo-advisory services: These are online investment platforms that use algorithms to provide investment advice and portfolio management services.

3 - Investment banking services: Investment banks provide services such as underwriting, mergers and acquisitions, and financial advisory services.

4 - Wealth management services: Wealth management firms provide services to high net worth individuals and families, including financial planning, investment management, and tax planning.

5 - Financial planning services: Financial planners help individuals and families create financial plans, set investment goals, and make investment decisions.

6 - Exchange-traded funds (ETFs): ETFs are a type of investment fund that trades on an exchange like a stock and provides exposure to a basket of securities.

7 - Mutual funds: Mutual funds pool money from investors to invest in a diversified portfolio of securities.

8 - Hedge funds: Hedge funds are private investment funds that use a variety of strategies to generate high returns for investors.

9 - Real estate investment trusts (REITs): REITs are investment vehicles that own and operate income-producing real estate properties.

10 - Venture capital services: Venture capital firms provide financing to startup companies and early-stage businesses with high growth potential.

Please enter a number here :"""))
            
            if list_of_financial_services == '1':
                print()
            
            elif list_of_financial_services == '2':
                print()

            elif list_of_financial_services == '3':
                print()

            elif list_of_financial_services == '3':
                print()

            elif list_of_financial_services == '4':
                print()

            elif list_of_financial_services == '5':
                print()

            elif list_of_financial_services == '6':
                print()

            elif list_of_financial_services == '7':
                print()

            elif list_of_financial_services == '8':
                print()
                
            elif list_of_financial_services == '9':
                print()

            elif list_of_financial_services == '10':
                print()

            else:
                print("Please choose a number from 1 - 10")

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
