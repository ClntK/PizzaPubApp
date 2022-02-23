
# Filename: pubMenu.py
# created Date: 2/15/2022
# Author: Clint Kline
# Purpose: learn the pizza pub menu


# ****************************************************************************************************************************************************************
#  NOTES
# ****************************************************************************************************************************************************************

# Future Functions:
#     - Choose toppings- check
#     - Show Menu
#     - Remove ingredients
#     - Back function ???
#     - Remove Item
#     - Print Reciept

# ****************************************************************************************************************************************************************

print("Welcome to the Pizza Pub!")

# ****************************************************************************************************************************************************************
#  FUNCTIONS
# ****************************************************************************************************************************************************************
# *************************
#  MENU ITEMS
# *************************

def apps(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nAppetizers: ")
    print(
        " 1. Homemade Breadsticks\n", 
        "2. Garlic Toast\n", 
        "3. Pizza Roll\n", 
        "4. Taco Nacho Supreme\n", 
        "5. Buffalo Wings\n", 
        "6. Mozzarella Sticks\n", 
        "7. Cinnamon Toasties\n", 
        "8. Bacon & Cheddar Fries\n", 
        "9. Side of Fries\n"
    )

    appOption = input("What would you like to order? >> ")
    appOption = int(appOption)

    if appOption == 0:
        finalize(orderNum, ticket, orderTotal)

    elif appOption == 1:
        # breadsticks
        print(
            " 1. 6 stix\n",
            "2. 12 stix\n"
        )
        
        size = input("Which size order would you like? >> ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)

        elif size == 1:
            # add cost to total
            orderTotal = orderTotal + 2.95
            #  add item to order list
            ticket.append("B6\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            orderTotal = orderTotal + 4.95
            ticket.append("B12\n")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif appOption == 2:
        # Garlic Toast
        print(
            " 1. Cheese\n",
            "2. No Cheese\n"
        )
        
        cheese = input("Cheese? >> ")
        cheese = int(cheese)

        if cheese == '0':
            finalize(orderNum, ticket, orderTotal)

        elif cheese == 1:
            # add cost to total
            orderTotal = orderTotal + 3.95
            #  add item to order list
            ticket.append("GT w/ch\n")
            order(orderNum, ticket, orderTotal)

        elif cheese == 2:
            orderTotal = orderTotal + 3.50
            ticket.append("GT\n")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif appOption == 3:
        # Pizza Roll
        ticket.append("Proll\n")
        orderTotal = orderTotal + 4.75
        order(orderNum, ticket, orderTotal)

    elif appOption == 4:
        # Taco Nacho Supreme
        ticket.append("T.nacho\n")
        orderTotal = orderTotal + 6.95
        order(orderNum, ticket, orderTotal)

    elif appOption == 5:
        # Buffalo Wings
        print(
            " 1. Plain\n",
            "2. Buffalo\n",
            "3. BBQ\n"
        )
    
        sauce = input("Sauce?")
        sauce = int(size)

        if sauce == '0':
            finalize(orderNum, ticket, orderTotal)

        elif sauce == 1:
            # add cost to total
            orderTotal = orderTotal + 9.95
            #  add item to order list
            ticket.append("PW Wgs\n")
            order(orderNum, ticket, orderTotal)

        elif sauce == 2:
            # add cost to total
            orderTotal = orderTotal + 9.95
            #  add item to order list
            ticket.append("Buff Wgs\n")
            order(orderNum, ticket, orderTotal)
        
        elif sauce == 3:
            # add cost to total
            orderTotal = orderTotal + 9.95
            #  add item to order list
            ticket.append("BBQ Wgs\n")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif appOption == 6:
        # Mozzarella Sticks
        ticket.append("Mozz\n")
        orderTotal = orderTotal + 5.95
        order(orderNum, ticket, orderTotal)

    elif appOption == 7:
        # Cinnamon Toasties
        ticket.append("Cinn\n")
        orderTotal = orderTotal + 3.95
        order(orderNum, ticket, orderTotal)

    elif appOption == 8:
        # Bacon Cheddar Fries
        ticket.append("BCF\n")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif appOption == 9:
        # Fries
        ticket.append("FF\n")
        orderTotal = orderTotal + 2.95
        order(orderNum, ticket, orderTotal)
                        
    else:
        print("Please select a valid option.")

def salads(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nSalads:\n")
    print(
        " 1. Garden Salad\n",
        "2. 1/2 Chef Salad\n",
        "3. Chef Salad\n",
        "4. Taco Salad\n",
        "5. Antipasto Salad\n",
        "6. Steak Salad\n",
        "7. Chicken Salad\n",
        "8. Buffalo Chicken Salad\n"
    )

    salad = input("What would you like to order? >> ")
    salad = int(salad)

    if salad == 0:
        finalize(orderNum, ticket, orderTotal)

    elif salad == 1:
        # Garden Salad
        ticket.append("GSal\n")
        orderTotal = orderTotal + 3.75
        order(orderNum, ticket, orderTotal)

    elif salad == 2:
        # 1/2 Chef Salad
        ticket.append("HCfSal\n")
        orderTotal = orderTotal + 5.50
        order(orderNum, ticket, orderTotal)

    elif salad == 3:
        # Chef Salad
        ticket.append("CfSal\n")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 4:
        # Taco Salad
        ticket.append("TSal\n")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 5:
        # Antipasto Salad
        ticket.append("APSal\n")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 6:
        # Steak Salad
        ticket.append("SSal\n")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 7:
        # Chicken Salad
        ticket.append("CxSal\n")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 8:
        # Chef Salad
        ticket.append("BCxSal\n")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)
                     
    else:
        print("Please select a valid option.")

def sammies(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nSandwiches:\n")
    print(
        " 1. Ham & Cheese\n",
        "2. Reuben\n",
        "3. Rachel\n",
        "4. Chicken\n",
        "5. Pub Burger w/ Fries\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        # Ham & Cheese
        ticket.append("HC\n")
        orderTotal = orderTotal + 5.50
        order(orderNum, ticket, orderTotal)

    elif option == 2:
        # Reuben
        ticket.append("RbS\n")
        orderTotal = orderTotal + 6.75
        order(orderNum, ticket, orderTotal)

    elif option == 3:
        # Rachel
        ticket.append("RcS\n")
        print(orderNum, ticket)
        orderTotal = orderTotal + 6.75
        order(orderNum, ticket, orderTotal)

    elif option == 4:
        # Chicken 
        ticket.append("CxS\n")
        orderTotal = orderTotal + 6.75
        order(orderNum, ticket, orderTotal)

    elif option == 5:
        # Pub Burger
        print(
            " 1. Fries\n",
            "2. No Fries\n"
        )
    
        fries = input("Fries?")
        fries = int(fries)

        if fries == '0':
            finalize(orderNum, ticket, orderTotal)

        elif fries == 1:
            # add cost to total
            orderTotal = orderTotal + 8.50
            #  add item to order list
            ticket.append("PB w/f\n")
            order(orderNum, ticket, orderTotal)

        elif fries == 2:
            # add cost to total
            orderTotal = orderTotal + 5.95
            #  add item to order list
            ticket.append("PB\n")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")
                   
    else:
        print("Please select a valid option.")

def bolis(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nStromboli:\n")
    print(
        " 1. Meatballboli\n",
        "2. Pizzaboli\n",
        "3. Veggieboli\n",
        "4. Italianboli\n",
        "5. Hawaiianboli\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        # Meatballboli
        ticket.append("Mboli\n")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif option == 2:
        # Pizzaboli
        ticket.append("Pboli\n")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif option == 3:
        # Veggieboli
        ticket.append("Vboli\n")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif option == 4:
        # Italianboli
        ticket.append("Itboli\n")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif option == 5:
        # Hawaiianboli
        ticket.append("Hboli\n")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)
                      
    else:
        print("Please select a valid option.")

def custZahs(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nCustom Pizzas:\n")
    print(
        " 1. Blend of Cheese\n",
        "2. 1 Topping\n",
        "3. 2 Toppings\n",
        "4. 3 Toppings\n",
        "5. 4 Toppings\n",
        "6. Additional Toppings\n",
        "7. Exxtra Cheese\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        # blend of cheese
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 3.90
            ticket.append("Mini BOC\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 5.95
            ticket.append("Sm BOC\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 8.25
            ticket.append("Med BOC\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 12.95
            ticket.append("Lg BOC\n")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")
        
        crustType(orderNum, ticket, orderTotal)

    elif option == 2:
        # 1 topping
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)
        tops = toppings(orderNum, ticket, orderTotal, 1)        

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.15
            ticket.insert(1, "Mini")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 6.95
            ticket.insert(1, "Sm")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 9.75
            ticket.insert(1, "Med")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 14.70
            ticket.insert(1, "Lg")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")
        

    elif option == 3:
        # 2 topping
        size = pizzaSize(orderNum, ticket, orderTotal)
        crustType(orderNum, ticket, orderTotal)
        tops = toppings(orderNum, ticket, orderTotal, 2)     

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.40
            ticket.insert(1, "Mini")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 7.95
            ticket.insert(1, "Sm")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 11.25
            ticket.insert(1, "Med")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 16.45
            ticket.insert(1, "Lg")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")


    elif option == 4:
        # 3 topping
        size = pizzaSize(orderNum, ticket, orderTotal)
        crustType(orderNum, ticket, orderTotal)
        tops = toppings(orderNum, ticket, orderTotal, 3)     

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.65
            ticket.insert(1, "Mini")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 8.95
            ticket.insert(1, "Sm")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 12.75
            ticket.insert(1, "Med")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 18.20
            ticket.insert(1, "Lg")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")
        

    elif option == 5:
        # 4 topping
        size = pizzaSize(orderNum, ticket, orderTotal)
        crustType(orderNum, ticket, orderTotal)
        tops = toppings(orderNum, ticket, orderTotal, 4)     

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.90
            ticket.insert(1, "Mini")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.insert(1, "Sm")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.insert(1, "Med")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.insert(1, "Lg")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    else:
        print("Please select a valid option.")
        

def specZahs(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nSpecialty Pizzas:\n")
    print(
        " 1. Pub Special\n",
        "2. Taco Pizza\n",
        "3. Vegetarian Pizza\n",
        "4. White Pizza\n",
        "5. Hawaiian Pizza\n",
        "6. Ranch Pizza\n",
        "7. Buffalo Pizza\n",
        "8. Pete\'s Pizza\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        #  Pub Special
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Spec\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Spec\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Spec\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Spec\n")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 2:
        #  Taco Pizza
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Taco\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Taco\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Taco\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Taco\n")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 3:
        #  Vegetarian Pizza
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Veg\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Veg\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Veg\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Veg\n")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please select a valid option.")

    elif option == 4:
        #  White Pizza
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.50
            ticket.append("Mini White\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 7.50
            ticket.append("S White\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 11.50
            ticket.append("M White\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 17.95
            ticket.append("L White\n")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please select a valid option.")

    elif option == 5:
        #  Hawaiian Pizza
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Haw\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 8.75
            ticket.append("S Haw\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 12.50
            ticket.append("M Haw\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 17.95
            ticket.append("L Haw\n")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please select a valid option.")

    elif option == 6:
        #  Ranch Pizza
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Ranch\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Ranch\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Ranch\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Ranch\n")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please select a valid option.")

    elif option == 7:
        #  Buffalo Chicken Pizza
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Buff\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Buff\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Buff\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Buff\n")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please select a valid option.")

    elif option == 8:
        #  Pete's Pizza
        crustType(orderNum, ticket, orderTotal)
        size = pizzaSize(orderNum, ticket, orderTotal)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.75
            ticket.append("Mini Pete\n")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 8.25
            ticket.append("S Pete\n")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 12.50
            ticket.append("M Pete\n")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 18.25
            ticket.append("L Pete\n")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please select a valid option.")
                      
    else:
        print("Please select a valid option.")

def harrys(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nOld Style \"Harry\'s\" Pizza:\n")
    print(
        " 1. per Slice\n",
        "2. Whole Tray (28 slices)\n",
        "3. 1/2 Tray\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        # by the slice
        sliceCost = numSlices(ticket)     
        orderTotal = orderTotal + sliceCost
        order(orderNum, ticket, orderTotal)

    elif option == 2:
        # whole tray
        orderTotal = orderTotal + 22.95
        ticket.append("Tray Harry\'s\n")
        order(orderNum, ticket, orderTotal)

    elif option == 3:
        orderTotal = orderTotal + 11.95
        ticket.append("1/2 Tray Harry\'s\n")
        order(orderNum, ticket, orderTotal)
                       
    else:
        print("Please select a valid option.")

def wedgies(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nWedgies:\n")
    print(
        " 1. Reuben\n",
        "2. Italian\n",
        "3. Veggie\n",
        "4. B.L.T.\n",
        "5. Ham, Roast Beef, or Turkey\n",
        "6. Combo\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        #  Rueben Wedgie
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.95
            ticket.append("1/2 Reggie")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.95
            ticket.append("Reggie")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 2:
        #  Italian Wedgie
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.75
            ticket.append("1/2 ITW")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.75
            ticket.append("ITW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 3:
        #  Veggie Wedgie
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.75
            ticket.append("1/2 VW")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.75
            ticket.append("VW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 4:
        #  B.L.T. Wedgie
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.95
            ticket.append("1/2 BLTW")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.95
            ticket.append("BLTW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 5:
        #  Ham, RB, Turkey Wedgie
        print("Meats: ")
        print(
            " 1. Ham\n",
            "2. Roast Beef\n",
            "3. Turkey\n"
        )

        meat = input("Choose your meat: ")
        meat = int(meat)

        if meat == 0:
            finalize(orderNum, ticket, orderTotal)

        elif meat == 1:
            # Ham
            print("Sizes: ")
            print(
                " 1. Half\n",
                "2. Whole\n"
            )

            size = input("Choose a size: ")
            size = int(size)

            if size == 0:
                finalize(orderNum, ticket, orderTotal)
            
            elif size == 1:
                # half
                orderTotal = orderTotal + 4.75
                ticket.append("1/2 HW")
                order(orderNum, ticket, orderTotal)

            elif size == 2:
                # whole
                orderTotal = orderTotal + 7.75
                ticket.append("HW")
                order(orderNum, ticket, orderTotal)

            else:
                print("Please select a valid option.")

        elif meat == 2:
            # Roast Beef
            print("Sizes: ")
            print(
                " 1. Half\n",
                "2. Whole\n"
            )

            size = input("Choose a size: ")
            size = int(size)

            if size == 0:
                finalize(orderNum, ticket, orderTotal)
            
            elif size == 1:
                # half
                orderTotal = orderTotal + 4.75
                ticket.append("1/2 RBW")
                order(orderNum, ticket, orderTotal)

            elif size == 2:
                # whole
                orderTotal = orderTotal + 7.75
                ticket.append("RBW")
                order(orderNum, ticket, orderTotal)

            else:
                print("Please select a valid option.")

        elif meat == 3:
            # Turkey
            print("Sizes: ")
            print(
                " 1. Half\n",
                "2. Whole\n"
            )

            size = input("Choose a size: ")
            size = int(size)

            if size == 0:
                finalize(orderNum, ticket, orderTotal)
            
            elif size == 1:
                # half
                orderTotal = orderTotal + 4.75
                ticket.append("1/2 TW")
                order(orderNum, ticket, orderTotal)

            elif size == 2:
                # whole
                orderTotal = orderTotal + 7.75
                ticket.append("TW")
                order(orderNum, ticket, orderTotal)

            else:
                print("Please select a valid option.")

        else:
            print("Please choose a valid option.")

    elif option == 6:
        #  Combo Wedgie
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.75
            ticket.append("1/2 CW")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.75
            ticket.append("CW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")
    
    else:
        print("Please choose a valid option.")

def hoagies(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nHoagies:\n")
    print(
        " 1. Meatball\n",
        "2. Hoagie\n",
        "3. Buff Chix\n",
        "4. The Clarion Cheesesteak\n",
        "5. Italian\n",
        "6. Deli\n",
        "7. Combo\n",
        "8. Veggie\n",
        "10. B.L.T.\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        # meatball
        orderTotal = orderTotal + 6.75
        ticket.append("MBS")
        order(orderNum, ticket, orderTotal)

    elif option == 2:
        # hoagie
        orderTotal = orderTotal + 6.75
        ticket.append("Hoag")
        order(orderNum, ticket, orderTotal)

    elif option == 3:
        # buff chix
        orderTotal = orderTotal + 6.95
        ticket.append("Buff S")
        order(orderNum, ticket, orderTotal)

    elif option == 4:
        # cheesesteak
        orderTotal = orderTotal + 7.25
        ticket.append("Buff S")
        order(orderNum, ticket, orderTotal)

    elif option == 5:
        # italian
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.95
            ticket.append("1/2 Ital S")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.95
            ticket.append("Ital S")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 6:
        #  deli == roast beef, ham, or turkey
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            meat = meatChoice()

            if meat == 0:
                finalize(orderNum, ticket, orderTotal)

            elif meat == 1:
            # roast beef
                orderTotal = orderTotal + 4.95
                ticket.append("1/2 RBS")
                order(orderNum, ticket, orderTotal)

            elif meat == 2:
                # ham
                orderTotal = orderTotal + 4.95
                ticket.append("1/2 HS")
                order(orderNum, ticket, orderTotal)

            elif meat == 3:
                # turkey
                orderTotal = orderTotal + 4.95
                ticket.append("1/2 TS")
                order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            meat = meatChoice()
            
            if meat == 0:
                finalize(orderNum, ticket, orderTotal)

            elif meat == 1:
            # roast beef
                orderTotal = orderTotal + 7.95
                ticket.append("RBS")
                order(orderNum, ticket, orderTotal)

            elif meat == 2:
                # ham
                orderTotal = orderTotal + 7.95
                ticket.append("HS")
                order(orderNum, ticket, orderTotal)

            elif meat == 3:
                # turkey
                orderTotal = orderTotal + 7.95
                ticket.append("TS")
                order(orderNum, ticket, orderTotal)
        
        else:
            print("Please pick a valid option")

    elif option == 7:
        # combo
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.95
            ticket.append("1/2 CS")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.95
            ticket.append("CS")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 8:
        #  veggie
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.95
            ticket.append("1/2 VS")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.95
            ticket.append("VS")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 9:
        #  BLT
        print("Sizes: ")
        print(
            " 1. Half\n",
            "2. Whole\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize(orderNum, ticket, orderTotal)
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.95
            ticket.append("1/2 BLTS")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.95
            ticket.append("BLTS")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")
                        
    else:
        print("Please select a valid option.")

def drinks(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nBeverages:\n")
    print(
        " 1. Soft Drink\n",
        "2. Bottle a' H2O\n"
    )

    option = input("What would you like to drink? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        # soft drinks
        print("Soft Drinks: ")
        print(
            " 1. Pepsi\n",
            "2. Mtn Dew\n",
            "3. Sprite\n" #,
            # "4. Root Beer\n",
            # "5. Orange soda\n",
            # "6. Dr Pepper\n",
            # "7. Diet Pepsi\n"
        )

        soda = input("Choose your soft drink: >> ")
        soda = int(soda)

        if soda == 0:
            finalize(orderNum, ticket, orderTotal)

        elif soda == 1:
            orderTotal = orderTotal + 2.95
            ticket.append("Pepsi")
            order(orderNum, ticket, orderTotal)
        
        elif soda == 2:
            orderTotal = orderTotal + 2.95
            ticket.append("Mtn Dew")
            order(orderNum, ticket, orderTotal)

        elif soda == 3:
            orderTotal = orderTotal + 2.95
            ticket.append("Sprite")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please select a valid option.")

    elif option == 2:
        # bottled water
        orderTotal = orderTotal + 1.95
        ticket.append("Bottled water") 
        order(orderNum, ticket, orderTotal)
                    
    else:
        print("Please select a valid option.")


# *************************
#  OPTIONS
# *************************

#  record the customers crust selection
def crustType(orderNum, ticket, orderTotal):
    print(
        " 1. Homestyle\n",
        "2. Traditional\n"
    )

    crust = input("Choose your favorite crust: >> ")
    crust = int(crust)

    if crust == 0:
        finalize(orderNum, ticket, orderTotal)
    
    elif crust == 1:
        ticket.append("H) ")

    elif crust == 2:
        ticket.append("T) ")

    elif crust == 3:
        print("Please select a valid option.")

#  record the customers meat selection
def meatChoice(orderNum, ticket, orderTotal):
    print("Choose your meat: ")
    print(
        " 1. Roast Beef\n",
        "2. Ham\n",
        "3. Turkey\n"
    )
    meat = input("Roast Beef, Ham, or Turkey? >> ") 
    meat = int(meat)
    if meat == 0:
        finalize(orderNum, ticket, orderTotal)

    elif meat == 1:
        # roast beef
        return 1

    elif meat == 2:
        # ham
       return 2

    elif meat == 3:
        # turkey
        return 3

    else:
        print("Please select a valid option.")

#  record a list of selected pizza toppings
def toppings(orderNum, ticket, orderTotal, num):
        
    toppings = ["P", "S", "H", "G", "M", "Ba", "B", "O", "HP", "T", "A", "Pa"]
    selectedTops = []
    count = 1
    
    print("\n\nToppings: ")
    print(
        "  1. Pepperoni\n",
        " 2. Spicy Sausage\n",
        " 3. Ham\n",
        " 4. Green Peppers\n",
        " 5. Mushrooms\n",
        " 6. Bacon\n",
        " 7. Black Olives\n",
        " 8. Onions\n",
        " 9. Hot Peppers\n",
        "10. Tomatoes\n",
        "11. Anchovies\n",
        "12. Pineapple\n"
    )

    while count <= num:
        topping = input("Please choose your toppings: >> ")
        topping = int(topping)
    
        # print("topping: ", toppings[topping - 1])
        # print("num: ", num)

        if topping == 0:
            finalize(orderNum, ticket, orderTotal)
    
        elif topping in range(0, len(toppings) + 1):
            selectedTops.append(toppings[topping - 1])
            count = count + 1

        else:
            print("Please select a valid option.")

    for i in selectedTops:
        ticket.append(i)

#  record the customers pizza size selection
def pizzaSize(orderNum, ticket, orderTotal):
    
    print("Sizes: ")
    print(
        " 1. Mini (4 cut)\n",
        "2. Small (6 cut)\n",
        "3. Medium (8 cut)\n",
        "4. Large (12 cut)\n"
    )

    size = input("Choose a size: ")
    size = int(size)

    return size

#  record the number of pizza slices the customer wants to order
def numSlices(ticket):    
        
        sliceCount = input("How many slices would you like? >> ")

        if sliceCount.isdigit():
            sliceCount = int(sliceCount)
            sliceCost = .9 * sliceCount
            ticket.append(str(sliceCount) + " Harry\'s")
        else:
            print("Please select a number.")
            numSlices(ticket)

        return sliceCost


# *************************
#  UTILITY FUNCTIONS
# *************************

#  finalize the order
def finalize(orderNum, ticket, orderTotal):

    print("\nYour total comes to: $" + str('{:.2f}'.format(orderTotal)) + "\n")

    # accept payment

    # print ticket
    print("****************")
    print("*    TICKET    *")
    print("****************")

    for i in ticket:
        print(i)
    
    print("\n\n")

# record the order
def order(orderNum, ticket, orderTotal):
    print("\nTotal: $" + str('{:.2f}'.format(orderTotal)))
    print("\nWhat would you like to order?\n")
    print(" 1. Appetizers\n 2. Salads\n 3. Sandwiches\n 4. Stromboli\n 5. Custom Pizzas\n 6. Specialty Pizzas\n 7. Old Style \"Harry\'s\" Pizza\n 8. Wedgies\n 9. Hoagies\n 10. Drinks\n")
    print("** Enter a number to select the corresponding option. **")
    # print("** Type \'b\' or \'B\' at any time to go back. **")
    print("** Type \'0\' at any time to complete your order. **\n")

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize(orderNum, ticket, orderTotal)

    elif option == 1:
        apps(orderNum, ticket, orderTotal)

    elif option == 2:
        salads(orderNum, ticket, orderTotal)

    elif option == 3:
        sammies(orderNum, ticket, orderTotal)

    elif option == 4:
        bolis(orderNum, ticket, orderTotal)

    elif option == 5:
        custZahs(orderNum, ticket, orderTotal)

    elif option == 6:
        specZahs(orderNum, ticket, orderTotal)

    elif option == 7:
        harrys(orderNum, ticket, orderTotal)

    elif option == 8:
        wedgies(orderNum, ticket, orderTotal)

    elif option == 9:
        hoagies(orderNum, ticket, orderTotal)

    elif option == 10:
        drinks(orderNum, ticket, orderTotal)                        
    else:
        print("Please select a valid option.")


#*****************
# MAIN
#*****************
def main():
    orderNum = 0
    ticket = []
    orderTotal = 0

    orderNum = orderNum + 1

    order(orderNum, ticket, orderTotal)

if __name__ == "__main__":
    main()
