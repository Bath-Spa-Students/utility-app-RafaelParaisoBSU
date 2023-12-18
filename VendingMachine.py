Drinks = [
    {'Code': 'A1', 'Name': '     Water     ', 'Price': 1.00, 'Category': 'Drinks', 'Stock': 5},
    {'Code': 'A2', 'Name': '     Pepsi     ', 'Price': 3.50, 'Category': 'Drinks', 'Stock': 3},
    {'Code': 'A3', 'Name': '     Apple     ', 'Price': 2.50, 'Category': 'Drinks', 'Stock': 4},
]  # Makes a Dictionary for Drinks, includes the Code, Name, Category, and Stock
Chips = [
    {'Code': 'B4', 'Name': '    Ruffles    ', 'Price': 4.50, 'Category': 'Chips ', 'Stock': 4},
    {'Code': 'B5', 'Name': '    Doritos    ', 'Price': 5.50, 'Category': 'Chips ', 'Stock': 6},
    {'Code': 'B6', 'Name': '    Cheetos    ', 'Price': 6.50, 'Category': 'Chips ', 'Stock': 2},
]  # Makes a Dictionary for Chips, includes the Code, Name, Category, and Stock
Candy = [
    {'Code': 'C7', 'Name': '     Oreo      ', 'Price': 2.00, 'Category': 'Candy ', 'Stock': 4},
    {'Code': 'C8', 'Name': '     Mars      ', 'Price': 3.00, 'Category': 'Candy ', 'Stock': 5},
    {'Code': 'C9', 'Name': '     Twix      ', 'Price': 2.50, 'Category': 'Candy ', 'Stock': 1}
]  # Makes a Dictionary for Candy, includes the Code, Name, Category, and Stock
Sando = [
    {'Code': 'S1', 'Name': '    Rueben    ', 'Price': 20.00, 'Category': 'Sando ', 'Stock': 2},
    {'Code': 'S2', 'Name': '    Panini    ', 'Price': 15.00, 'Category': 'Sando ', 'Stock': 5},
    {'Code': 'S3', 'Name': '    Hoagie    ', 'Price': 10.50, 'Category': 'Sando ', 'Stock': 3}
]  # Makes a Dictionary for Sandwiches, includes the Code, Name, Category, and Stock
Meals = [
    {'Code': 'M1', 'Name': 'Chicken & Rice', 'Price': 15.00, 'Category': 'Meals ', 'Stock': 5},
    {'Code': 'M2', 'Name': 'Steak & Frites', 'Price': 25.00, 'Category': 'Meals ', 'Stock': 2},
    {'Code': 'M3', 'Name': 'Alfredo Pasta ', 'Price': 19.50, 'Category': 'Meals ', 'Stock': 1}
]  # Makes a Dictionary for Meals, includes the Code, Name, Category, and Stock

VendingMachine = ("""You have selected: 

      
     █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀ █
     ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄ ▄
   
           _______________________________________________
          |         _____________________________         | 
          |---------| Rafael's Vending Machine! |---------|
          |_______________________________________________|                   
          |    ---------------------------------------    |
          |    |   1. Drinks    |  A1  |  A2  |  A3  |    | 
          |    ---------------------------------------    |
          |    |   2. Chips     |  B4  |  B5  |  B6  |    |
          |    ---------------------------------------    | 
          |    |   3. Candy     |  C7  |  C8  |  C9  |    |
          |    ---------------------------------------    |
          |                                               | 
          |    ---------------------------------------    |
          |    | ----------------------------------- |    | 
          |    |  Water(A1) | Pepsi(A2) | Apple(A3)  |    | 
          |    | ----------------------------------- |    |
          |    _______________________________________    |
          |    ---------------------------------------    |
          |    | ----------------------------------- |    | 
          |    | Ruffles(B4)|Doritos(B5)|Cheetos(B6) |    | 
          |    | ----------------------------------  |    |
          |    _______________________________________    | 
          |    ---------------------------------------    |
          |    | ----------------------------------- |    | 
          |    |   Oreo(C7) |  Mars(C8) | Twix(C9)   |    | 
          |    | ----------------------------------  |    |
          |    _______________________________________    |
          |                                               | 
          |_______________________________________________|
         
           """)  # Displays a vending machine with its categories, items and codes.

FoodStand = ("""You have selected: 
    
                 █▀▀ █▀█ █▀█ █▀▄   █▀ ▀█▀ ▄▀█ █▄░█ █▀▄ █
                 █▀░ █▄█ █▄█ █▄▀   ▄█ ░█░ █▀█ █░▀█ █▄▀ ▄
                    
              ______________________________________________
             /           _____________________              \       
            /------------| Raf's Food Stand! |---------------\ 
           |__________________________________________________|        
           |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
           |--------------||                  ||--------------|
           | "Sandwiches" ||                  ||   "Meals"    |                              
           |--------------||                  ||--------------|
           |  Rueben(P1)  ||                  ||Chick&Rice(M1)|                                  
           |--------------||                  ||--------------|
           |  Panini(P2)  ||                  ||Steak&Frit(M2)|  
           |--------------||                  ||--------------|
           |  Hoagie(P3)  ||                  ||Carbonara (M3)|
           |--------------||                  ||--------------|
           |              ||                  ||              | 
           |              ||                  ||              |
           |/\/\/\/\/\/\/\||                  ||/\/\/\/\/\/\/\|
           |______________||__________________||______________|    
           |                                                  |
           |__________________________________________________|    
           |      ------------------                          |
           |     / /      |       \ \                         | 
           |    / /       |        \ \                        |
           |   / /        |         \ \                       |
           |  / /         |          \ \                      |
           | / /==========|===========\ \                     |
           | \ \          |           / /                     |
           |  \ \         |          / /                      |
           |---\ \        |         / /-----------------------|
                \ \       |        / /            \   /
                 --------------------              \_/
                                                 
      """)  # Similarly, this displays a food cart with its categories and items.

def process_category(selected_category, Wallet): # Uses a singular function to define the entire process of choosing categories and items, calculating the change, the stock system, and suggestions. This will make the code more efficient.
    
    print(f"\n   --------------------------------- {selected_category[0]['Category']} Menu ---------------------------------") # Uses an F-string to format the chosen category into a table.

    for item in selected_category:  # Uses a for loop to showcase the selected items in the category.
        print ("""   -------------------------------------------------------------------------------""")
        print(f'   |     {item["Code"]}     |     {item["Name"]}     |     ${item["Price"]:.2f}     |     {item["Stock"]}  available     |  ') # Uses an F-string to format the list of items.
    print("""   -------------------------------------------------------------------------------""") # Breakline

    choice = input("\nPlease enter an Item or 'Q' to go Back!: ") # Allows the user to input a code to select an item or go back to choosing a Category.


    if choice.lower() == 'q': # If the user enters 'q' or 'Q', goes back to selecting a category.
        return None, Wallet # Returns Wallet and item_choice values to be None.

    item_choice = None # Placeholder used to determine if the user inputs a valid code.
    for item in selected_category:  # Uses a for loop to determine if the "Code" is a valid key in the Dictionary.
        if item['Code'] == choice.upper() and item['Stock'] > 0: # If the key is found and is in stock then "item_choice" is updated to be the item in the dictionary.
            item_choice = item
            break
        elif item['Code'] == choice.upper() and item['Stock'] == 0: # If the item is not in stock, prints the error message.
            print("Item has run out of stock!")
            break

    if item_choice: # If the item the user choses is valid and in stock then the payment procedure ensues:
        amount_paid = float(input(f"Please insert your desired payment!: $ ")) # Asks the user to input their desired payment.
        Wallet += amount_paid # Increases the money in the Wallet (variable from earlier) to the users desired payment.

        if Wallet >= item_choice['Price']: # If the users money is more than the payment then:
            print(f"\n\nDispensing your '{item_choice['Name'].strip()}', Enjoy!\n") # Dispenses the item using an f-string. Since item_choice is now updated, this code can be used.

            change = Wallet - item_choice['Price'] # Calculates the change by subtracting the price of the item to your Wallet funds.
            if change > 0: # If your change is higher than 0, then;
                print(f"\nYour change is: ${change:.2f}!\n") # This prints. ".2f" which stands for 2 floats is used to print the next 2 decimals as well.

            item_choice['Stock'] -= 1
            print(f"\n'{item_choice['Name'].strip()}' Stock has decreased by 1!\n")  # A print statement that tells the user the item stock has been updated.

            Wallet = 0.0 # Resets your total balance in your Wallet.

            suggested_items = [item['Name'].strip() for item in selected_category if item['Stock'] > 0 and item['Code'] != item_choice['Code']]  # Suggests items on your selected category, ['Stock']>0 is used to make sure the code doesn't suggest an item with no stock and != item_choice is to make sure it does not include your selected item as a suggestion.
            if suggested_items:
                print(f"\nPlease consider buying {' & '.join(suggested_items)} as well! See you next time!\n") # Uses an F-string and .join to suggest the remaining items in the category.
            else:
                print("No more items available in this category. See you next time!\n")  # Prints if there is no more stock of every item in a category.
        else:
            print("\nInsufficient Funds! Please insert the right amount of money!") # If the user inputs insufficient funds, this prints.   

    else:
        print("\nError! Invalid Code or Out of Stock! Please Try Again!") # If the user inputs insufficient funds, this prints.   

    print ("--------------------------------------------------------------------------------------\n") # Breakline
    return item_choice, Wallet # Returns these 2 variables into their original values, being "None" and "0.00" respectively.

Wallet = 0.0  # Your Wallet, will be used for the payment process later.

while True: # Uses a while loop to loop throughout the entire code until the user says to quit.
    print("""\n
 ---------------------------------- Wᴇʟᴄᴏᴍᴇ ᴛᴏ ---------------------------------------
                        
                         ██████╗░░█████╗░███████╗██╗░██████╗
                         ██╔══██╗██╔══██╗██╔════╝╚█║██╔════╝
                         ██████╔╝███████║█████╗░░░╚╝╚█████╗░
                         ██╔══██╗██╔══██║██╔══╝░░░░░░╚═══██╗
                         ██║░░██║██║░░██║██║░░░░░░░░██████╔╝
                         ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═════╝░
           
       ███████╗░█████╗░░█████╗░██████╗░  ░█████╗░░█████╗░██╗░░░██╗██████╗░████████╗
       ██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝
       █████╗░░██║░░██║██║░░██║██║░░██║  ██║░░╚═╝██║░░██║██║░░░██║██████╔╝░░░██║░░░
       ██╔══╝░░██║░░██║██║░░██║██║░░██║  ██║░░██╗██║░░██║██║░░░██║██╔══██╗░░░██║░░░
       ██║░░░░░╚█████╔╝╚█████╔╝██████╔╝  ╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║░░░██║░░░
       ╚═╝░░░░░░╚════╝░░╚════╝░╚═════╝░  ░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░""")
    standchoice = input("\nWould you like to use the 'Vending Machine' or 'Food Stand'? (Type 'Q' to Quit): ").lower() # Asks the user to select between the Vending Machine or Food Stand using input.

    if standchoice == "vending machine": # If the user selects Vending machine then the procedure continues:
        print(VendingMachine) # Prints the Vending Machine variable, displaying the menu.
        while True: # Uses another while loop to loop through the code until the user wants to select a different food trip or exits.
            category_choice = input("\nSelect a Category (1-Drinks, 2-Chips, 3-Candy) or press 'Q' to Exit!: ") # Allows the user to select between Drinks, Chips and Candy, or else;
            if category_choice.lower() == 'q': # Stop the code and go back to selecting between Vending Machine and Food Stand.
                print("""\n
         ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗██╗
         ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██║
         ░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██║
         ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║╚═╝
         ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝██╗
         ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝
                            For using Raf's Vending Machine!
                      \n""")
                print("\n--------------------------------------------------------------------------------------\n")
                break

            if category_choice in ['1', '2', '3']: # 1 for Drinks, 2 for Chips, and 3 for Candy.
                category_choice = int(category_choice) # Forces the user to enter an Integer
            else:
                print("Invalid Category Code. Please Try Again!")  # If the user enters a string or float, this error code will be displayed.
                continue

            if category_choice == 1:  # If the user chooses 1 then;
                selected_category = Drinks  # Variable is updated to be used to determine which category prints later.
                print('\nYou have selected Drinks!') # This prints, same goes for the rest.
            elif category_choice == 2:
                selected_category = Chips
                print('\nYou have selected Chips!')
            elif category_choice == 3:
                selected_category = Candy
                print('\nYou have selected Candy!')

            item_choice, Wallet = process_category(selected_category, Wallet) # Returns the values of item_choice and Wallet to their original values.

    elif standchoice == "food stand": # If the user selects Food Stand then the procedure continues:
        print(FoodStand) # Prints the Food Stand Variable, Displaying the Menu.
        while True: # Uses another while loop to loop through the code until the user selects a different food trip or exits.
            category_choice = input("\nSelect a Category (1-Sandwiches, 2-Meals) or press 'Q' to Exit!: ") # Allows the user to select between Sandwiches or Meals.
            if category_choice.lower() == 'q': # If they input Q, they can exit the program.
                print("""\n
         ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗██╗
         ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██║
         ░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██║
         ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║╚═╝
         ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝██╗
         ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝
                            For using Raf's Food Stand!
                      \n""")
                print ("--------------------------------------------------------------------------------------\n")
                break

            if category_choice in ['1', '2']: # Allows the user to select 1 for Sandwiches, 2 for Meals.
                category_choice = int(category_choice) # Forces the user to input an Integer.
            else:
                print("Invalid Category Code. Please Try Again!") # Else, this prints.
                continue 

            if category_choice == 1: # If the user chooses 1 then;
                selected_category = Sando  # Variable is updated to be used to determine which category prints later. 
                print('\nYou have selected Sandwiches!')  # This prints, same goes for the rest.
            elif category_choice == 2:
                selected_category = Meals
                print('\nYou have selected Meals!')

            item_choice, Wallet = process_category(selected_category, Wallet)  # Returns the values of item_choice and Wallet to their original values.

    elif standchoice == 'q':
        print("\nThank you for using Rafael's Food Court! Goodbye!\n") # Exits the program if the user types Q.
        break 

    else:
        print("Invalid choice. Please enter 'Vending Machine' or 'Food Stand' or 'Q' to Quit.") # Error code when the user types something else.
