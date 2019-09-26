#Assigning Prices to Names of Items in the Menu
egg = 0.99
bacon = 0.49
sausage = 1.49
hashBrown = 1.19
toast = 0.79
coffee = 1.09
tea = 0.89

#Deriving the breakfast options from individual options
smallBreakfast = egg + hashBrown + (toast*2) + (bacon*2) + sausage
regularBreakfast = (egg*2) + hashBrown + (toast*2) + (bacon*4) + (sausage*2)
bigBreakfast = (egg*3) + (hashBrown*2) + (toast*4) + (bacon*6) + (sausage*3)

#Assigning a price variable to keep track of the customer's cost
price = 0

#Declaring a boolean in order to loop until the condition is met
q = True

#The formatInput function is used to allow the input to be read including spaces
def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine

#Using a loop to obtain the customer's response while calculating the total cost for breakfast
while q:
    userInput = input("Enter Item (q to terminate): small breakfast, regular breakfast,"
                      " big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")

    #Formating user input by removing case sensitivity and the spaces sensitivity
    userInput = userInput.casefold()
    userInput = formatInput(userInput)

    #Declaring a boolean in order to create a second loop that will keep going until the user inputs a valid quantity
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
                quantityInput = int(quantityInput) #Converting the input from a string to an int
                price = price + (quantityInput * egg) #Adding the user's cost
                quantityInput = 0 #Setting the variable back to 0, so it can be reused again for other user inputs
                x = False #setting the condition false to exit the loop (so it doesn't ask the user for the quantity again)
            else:
                print("Enter a valid input")

    elif userInput == "bacon":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * bacon)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "sausage":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * sausage)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "hash brown":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * hashBrown)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "toast":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * toast)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "coffee":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * coffee)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "tea":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * tea)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "small breakfast":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * smallBreakfast)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "regular breakfast":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * regularBreakfast)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "big breakfast":
        while x:
            quantityInput = input("Enter the Quantity: ")
            if quantityInput.isnumeric():
                quantityInput = int(quantityInput)
                price = price + (quantityInput * bigBreakfast)
                quantityInput = 0
                x = False
            else:
                print("Enter a valid input")

    elif userInput == "q":
        q = False #If the user enters q, the program will exit out of the first loop, and calculate the total cost for breakfast

    else:
        print("Enter a valid input")

tax = 0.13
taxPrice = 0.13 * price #Multiply tax by the Price the user has to pay

#Printing out the cost, tax, and total cost in a formatted form that is rounded to 2 decimal places
print("Cost  : ", "$%.2f" %round(price,2))
print ("Tax   : ", "$%.2f" %round(taxPrice, 2))
print("Total : ","$%.2f" %round((taxPrice+price),2))










