# Basic website chatbot - Without Natural Langauge Learning models
# In this the use will be a finance bot

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
        print("You chose")

    elif user_question == 'b' or user_question == 'B':
        print("You chose")
    
    elif user_question == 'c' or user_question == 'C':
        print("You chose")
    
    elif user_question == 'd' or user_question == 'D':
        print("You chose")

    else:
        print("Please choose A, B, C or D")
        print(user_question)