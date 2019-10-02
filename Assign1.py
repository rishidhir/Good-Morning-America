#Assigning Prices to the Items in the Menu
EGG = 0.99
BACON = 0.49
SAUSAGE = 1.49
HASH_BROWN = 1.19
TOAST = 0.79
COFFEE = 1.09
TEA = 0.89

#Deriving the breakfast options from individual options
SMALL_BREAKFAST = EGG + HASH_BROWN + (TOAST*2) + (BACON*2) + SAUSAGE
REGULAR_BREAKFAST = (EGG*2) + HASH_BROWN + (TOAST*2) + (BACON*4) + (SAUSAGE*2)
BIG_BREAKFAST = (EGG*3) + (HASH_BROWN*2) + (TOAST*4) + (BACON*6) + (SAUSAGE*3)

#Initializing a price variable and assigning it a value to keep track of the customer's total cost of breakfast
price = 0

#Declaring a boolean in order to run the loop until customer finishes the order
q = True

#The formatInput function is used to allow the input to be read including spaces
def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine

#Using a loop to obtain the customer's response while calculating the total cost for breakfast.
while q: #The loop will run until the boolean value is changed to False (will happen when user enters q)
    userInput = input("Enter Item (q to terminate): small breakfast, regular breakfast,"
                      " big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    #Formating user input by removing case sensitivity and the spaces sensitivity
    userInput = userInput.casefold()
    userInput = formatInput(userInput)

    #Declaring a boolean to run a second loop until the user inputs a valid quantity
    x = True

    #Checking if the user input is valid
    if userInput.isnumeric():
        print("Enter a valid input")

    #If the user input matches one of the described items, the user is given the option to enter a quantity
    elif userInput == "egg":
        while x:
            #User will input a quantity for the option selected
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput) #Converting the input from a string to an integer
                price = price + (quantityInput * EGG) #Adding the user's cost
                quantityInput = 0 #Setting the variable back to 0, so it can be reused again for other user inputs
                x = False #setting the condition false to exit the loop (so it doesn't ask the user for the quantity again)
            else:
                print("Enter a valid input")

    elif userInput == "bacon":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * BACON)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "sausage":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * SAUSAGE)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "hash brown":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * HASH_BROWN)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "toast":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * TOAST)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "coffee":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * COFFEE)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "tea":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * TEA)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "small breakfast":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * SMALL_BREAKFAST)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "regular breakfast":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * REGULAR_BREAKFAST)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "big breakfast":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * BIG_BREAKFAST)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "q":
        q = False #If the user enters q, the program will exit out of the first loop as the user has finished with the order

    else:
        print("Enter a valid input")

tax = 0.13
taxPrice = 0.13 * price #Multiply tax by the Price the user has to pay

#Printing out the cost, tax, and total cost in a formatted form that is rounded to 2 decimal places
print("\nCost  : ", "$%.2f" % round(price, 2))
print ("Tax   : ", "$%.2f" % round(taxPrice, 2))
print("Total : ","$%.2f" % round((taxPrice+price), 2))










