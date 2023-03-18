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
            
            if list_of_financial_services == 1:
                print("You chose Brokerage services\n")
                print("""A brokerage is a financial intermediary that facilitates the buying and selling of financial assets, such as stocks, bonds, 
commodities, currencies, and derivatives, on behalf of clients. A brokerage firm typically employs licensed professionals known as brokers or 
financial advisors who are authorized to buy and sell these assets on behalf of their clients. \n""")
                # Create services and list them below
            
            elif list_of_financial_services == 2:
                print("You chose Robo-advisory services")
                print("""Robo-advisory services are a type of financial advisory service that use algorithms and technology to 
provide automated investment advice and portfolio management to clients. Robo-advisors typically use computer algorithms to 
analyze client data, such as investment goals, risk tolerance, and financial situation, and then recommend a diversified investment 
portfolio that is tailored to the client's needs. \n""")

            elif list_of_financial_services == 3:
                print("You chose Investment banking services")
                print("""Investment banking is a type of financial service that provides various services to clients such as companies, 
governments, and institutional investors. Investment banks help clients to raise capital, make financial decisions, and carry out complex financial transactions.\n """)

            elif list_of_financial_services == 4:
                print("You chose Wealth management services")
                print(""" Wealth management is a specialized financial advisory service that helps individuals and families with significant wealth to manage 
their assets and achieve their financial goals. Wealth management services are typically offered by banks, investment firms, and specialized wealth management companies.

The primary goal of wealth management is to provide comprehensive financial planning and investment management services to high 
net worth individuals (HNWI) and ultra-high net worth individuals (UHNWI). Wealth management services typically include \n""")

            elif list_of_financial_services == 5:
                print("You chose Financial planning services")
                print("""Financial planning is the process of setting and achieving financial goals through the management of one's financial resources. 
It involves assessing one's current financial situation, identifying goals, and developing a plan to achieve those goals. Financial planning is essential 
for individuals and families to ensure that they are making the most of their financial resources, and that they are prepared for future financial needs. \n""")
    
            elif list_of_financial_services == 6:
                print("You chose Exchange-traded funds (ETFs)")
                print(""" Exchange-traded funds (ETFs) are investment funds that are traded on stock exchanges like individual stocks. 
ETFs are designed to track the performance of an underlying index, such as the S&P 500, or a specific sector, commodity, or currency. 
ETFs allow investors to diversify their portfolio and gain exposure to a wide range of assets with lower costs than traditional mutual funds.

ETFs are similar to mutual funds in that they pool money from investors to invest in a portfolio of assets, but they differ in how they are bought and sold.
ETFs trade on an exchange like individual stocks, and their prices fluctuate throughout the trading day, while mutual funds are priced at the end of each trading day. 
Additionally, ETFs typically have lower management fees and expenses than mutual funds. \n""")

            elif list_of_financial_services == 7:
                print("You chose Mutual funds")
                print(""" Mutual funds are a type of investment vehicle that pools money from many investors to invest in a portfolio of assets, such as stocks, 
bonds, and other securities. The portfolio is managed by professional money managers who make investment decisions on behalf of the investors. \n""")

            elif list_of_financial_services == 8:
                print("You chose Hedge funds")
                print(""" Hedge funds are private investment funds that are typically open only to a limited number of accredited or institutional investors. 
Hedge funds aim to generate high returns through a variety of investment strategies, including long and short positions in equities, bonds, derivatives, and other assets.

Hedge funds are managed by professional portfolio managers who use a range of investment techniques, such as leverage, short-selling, and derivatives, to achieve their investment goals. 
Hedge funds are known for their flexibility and can invest in a wide range of assets and markets, including stocks, bonds, commodities, and currencies.\n """)
                
            elif list_of_financial_services == 9:
                print("You chose Real estate investment trusts (REITs)")
                print(""" Real estate investment trusts (REITs) are investment vehicles that allow investors to invest in a portfolio of income-producing 
real estate properties, such as apartment buildings, office buildings, shopping centers, and other commercial properties. REITs are typically publicly traded 
companies that own and manage a diversified portfolio of real estate assets. \n """)

            elif list_of_financial_services == 10:
                print("You chose Venture capital services")
                print(""" Venture capital services involve the provision of financing, support, and strategic guidance to early-stage or high-growth companies with 
high potential for growth and profitability. Venture capital firms provide equity financing to companies in exchange for an ownership stake and involvement in their 
management and decision-making processes. \n """)     

            else:
                print("Please choose a number from 1 - 10")
                print(list_of_financial_services) # The services may be provided later

        elif list_of_services == 'b' or list_of_services == 'B':
            print("You chose Financial planning services")
            print("""Please find a list of our Financial Services
Retirement Planning
Investment Planning
Tax Planning
Estate Planning
Insurance Planning
Debt Management
Cash Flow Planning
College Planning
Risk Management
Business Planning
Wealth Management
Budgeting and Savings Planning
Charitable Giving Planning
Real Estate Planning
Special Needs Planning
Financial Counseling and Coaching
Asset Protection Planning. 
Each service is unavailable at the moment!""") # Create additional if etc functions for the services
            
        elif list_of_services == 'c' or list_of_services == 'C':
            print("You chose Financial education")
            print("""Please find the following
Budgeting and Personal Finance Management
Credit and Debt Management
Investing Basics
Retirement Planning
Understanding the Stock Market
Real Estate Investing
Insurance and Risk Management
Tax Planning and Preparation
Small Business Finance
Financial Planning for Families
Estate Planning
Financial Literacy for Children and Young Adults
Financial Fraud Awareness and Prevention
Understanding Economic Indicators and Trends
International Finance and Currency Exchange
Behavioral Finance and Decision Making
Financial Markets and Trading
Cryptocurrency and Blockchain Technology.""") # Create additional if etc functions for the services
            
        elif list_of_services == 'd' or list_of_services == 'D':
            print("You chose Accounting and tax service")
            print("""
Bookkeeping
Tax Preparation
Financial Statements
Payroll Processing
Audit Services
Financial Planning and Analysis
Tax Consulting
Forensic Accounting """) # Create the answers for the questions
            
        elif list_of_services == 'Back' or list_of_services == 'back':
            print(user_question)
        
        else:
            print() # ...
            break

    elif user_question == 'b' or user_question == 'B':
        print("You chose B - Investment advice  ")
        print("""
1 - Define your investment goals: Before making any investment, it's essential to know what you want to achieve from it. 
Set clear and realistic investment objectives that are aligned with your financial goals and risk appetite.

2 - Diversify your portfolio: Diversification is key to reducing investment risk. 
Spread your investment across different asset classes, such as stocks, bonds, real estate, and commodities.

3 - Consider your risk tolerance: Understand your risk tolerance level and invest accordingly. 
If you're risk-averse, invest in less volatile assets like bonds, while if you're more risk-tolerant, you may consider investing in high-growth stocks.

4 - Invest for the long-term: Investing is a long-term game. 
Don't get swayed by short-term market volatility and focus on your long-term investment goals.

5- Keep fees low: High fees can eat into your investment returns over time. 
Be mindful of fees and expenses associated with your investments and opt for low-cost investment options.

6- Seek professional advice: Consider seeking professional financial advice from a qualified financial advisor or investment 
professional to help you make informed investment decisions. """)
        
        a = 0 # Placeholder
        
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
