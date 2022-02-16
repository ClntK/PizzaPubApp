
# Filename: pubMenu.py
# created Date: 2/15/2022
# Author: Clint Kline
# Purpose: learn the pizza pub menu


# ****************************************************************************************************************************************************************
#  NOTES
# ****************************************************************************************************************************************************************

# apps = []
# salads = []
# sammies = []
# bolis = []
# customZahs = []
# specZahs = []
# harrys = []
# wedgies = []
# hoagies = []
# drinks = []

# menu = [apps, salads, sammies, bolis, customZahs, specZahs, harrys, wedgies, hoagies, drinks]
# menu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ****************************************************************************************************************************************************************



# ****************************************************************************************************************************************************************
#  FUNCTIONS
# ****************************************************************************************************************************************************************

print("Welcome to the Pizza Pub!")

def apps(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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
            ticket.append("B6")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            orderTotal = orderTotal + 4.95
            ticket.append("B12")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")

    elif appOption == 2:
        # Garlic Toast
        print(
            " 1. Cheese\n",
            "2. No Cheese\n"
        )
        
        cheese = input("Cheese?")
        cheese = int(size)

        if cheese == '0':
            finalize(orderNum, ticket, orderTotal)

        elif cheese == 1:
            # add cost to total
            orderTotal = orderTotal + 3.95
            #  add item to order list
            ticket.append("GT w/ch")
            order(orderNum, ticket, orderTotal)

        elif cheese == 2:
            orderTotal = orderTotal + 3.50
            ticket.append("GT")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")

    elif appOption == 3:
        # Pizza Roll
        ticket.append("Proll")
        orderTotal = orderTotal + 4.75
        order(orderNum, ticket, orderTotal)

    elif appOption == 4:
        # Taco Nacho Supreme
        ticket.append("T.nacho")
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
            ticket.append("PW")
            order(orderNum, ticket, orderTotal)

        elif sauce == 2:
            # add cost to total
            orderTotal = orderTotal + 9.95
            #  add item to order list
            ticket.append("BuffW")
            order(orderNum, ticket, orderTotal)
        
        elif sauce == 3:
            # add cost to total
            orderTotal = orderTotal + 9.95
            #  add item to order list
            ticket.append("BBQW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")

    elif appOption == 6:
        # Mozzarella Sticks
        ticket.append("Mozz")
        orderTotal = orderTotal + 5.95
        order(orderNum, ticket, orderTotal)

    elif appOption == 7:
        # Cinnamon Toasties
        ticket.append("Cinn")
        orderTotal = orderTotal + 3.95
        order(orderNum, ticket, orderTotal)

    elif appOption == 8:
        # Bacon Cheddar Fries
        ticket.append("BCF")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif appOption == 9:
        # Fries
        ticket.append("FF")
        orderTotal = orderTotal + 2.95
        order(orderNum, ticket, orderTotal)
                        
    else:
        print("Please select a valid option.")

def salads(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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
        finalize()

    elif salad == 1:
        # Garden Salad
        ticket.append("GSal")
        orderTotal = orderTotal + 3.75
        order(orderNum, ticket, orderTotal)

    elif salad == 2:
        # 1/2 Chef Salad
        ticket.append("HCfSal")
        orderTotal = orderTotal + 5.50
        order(orderNum, ticket, orderTotal)

    elif salad == 3:
        # Chef Salad
        ticket.append("CfSal")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 4:
        # Taco Salad
        ticket.append("TSal")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 5:
        # Antipasto Salad
        ticket.append("APSal")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 6:
        # Steak Salad
        ticket.append("SSal")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 7:
        # Chicken Salad
        ticket.append("CxSal")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)

    elif salad == 8:
        # Chef Salad
        ticket.append("BCxSal")
        orderTotal = orderTotal + 8.95
        order(orderNum, ticket, orderTotal)
                     
    else:
        print("Please select a valid option.")

def sammies(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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
        finalize()

    elif option == 1:
        # Ham & Cheese
        ticket.append("HC")
        orderTotal = orderTotal + 5.50
        order(orderNum, ticket, orderTotal)

    elif option == 2:
        # Reuben
        ticket.append("RbS")
        orderTotal = orderTotal + 6.75
        order(orderNum, ticket, orderTotal)

    elif option == 3:
        # Rachel
        ticket.append("RcS")
        print(orderNum, ticket)
        orderTotal = orderTotal + 6.75
        order(orderNum, ticket, orderTotal)

    elif option == 4:
        # Chicken 
        ticket.append("CxS")
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
            ticket.append("PB w/f")
            order(orderNum, ticket, orderTotal)

        elif fries == 2:
            # add cost to total
            orderTotal = orderTotal + 5.95
            #  add item to order list
            ticket.append("PB")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")
                   
    else:
        print("Please select a valid option.")

def bolis(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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
        finalize()

    elif option == 1:
        # Meatballboli
        ticket.append("Mboli")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif option == 2:
        # Pizzaboli
        ticket.append("Pboli")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif option == 3:
        # Veggieboli
        ticket.append("Vboli")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif option == 4:
        # Italianboli
        ticket.append("Itboli")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)

    elif option == 5:
        # Hawaiianboli
        ticket.append("Hboli")
        orderTotal = orderTotal + 7.95
        order(orderNum, ticket, orderTotal)
                      
    else:
        print("Please select a valid option.")

def custZahs(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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
        finalize()

    elif option == 1:
        apps()

    elif option == 2:
        salads()

    elif option == 3:
        sammies()

    elif option == 4:
        bolis()

    elif option == 5:
        custZahs()

    elif option == 6:
        specZahs()

    elif option == 7:
        harrys()
                    
    else:
        print("Please select a valid option.")

def specZahs(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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
        finalize()

    elif option == 1:
        #  Pub Special
        print("Sizes: ")
        print(
            " 1. Mini (4 cut)\n",
            "2. Small (6 cut)\n",
            "3. Medium (8 cut)\n",
            "4. Large (12 cut)\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize()
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Spec")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Spec")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Spec")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Spec")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")



    elif option == 2:
        #  Taco Pizza
        print("Sizes: ")
        print(
            " 1. Mini (4 cut)\n",
            "2. Small (6 cut)\n",
            "3. Medium (8 cut)\n",
            "4. Large (12 cut)\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize()
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Taco")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Taco")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Taco")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Taco")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")

    elif option == 3:
        #  Vegetarian Pizza
        print("Sizes: ")
        print(
            " 1. Mini (4 cut)\n",
            "2. Small (6 cut)\n",
            "3. Medium (8 cut)\n",
            "4. Large (12 cut)\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize()
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Veg")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Veg")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Veg")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Veg")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please enter a valid option.")

    elif option == 4:
        #  White Pizza
        print("Sizes: ")
        print(
            " 1. Mini (4 cut)\n",
            "2. Small (6 cut)\n",
            "3. Medium (8 cut)\n",
            "4. Large (12 cut)\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize()
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.50
            ticket.append("Mini White")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 7.50
            ticket.append("S White")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 11.50
            ticket.append("M White")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 17.95
            ticket.append("L White")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please enter a valid option.")

    elif option == 5:
        #  Hawaiian Pizza
        print("Sizes: ")
        print(
            " 1. Mini (4 cut)\n",
            "2. Small (6 cut)\n",
            "3. Medium (8 cut)\n",
            "4. Large (12 cut)\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize()
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Haw")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 8.75
            ticket.append("S Haw")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 12.50
            ticket.append("M Haw")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 17.95
            ticket.append("L Haw")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please enter a valid option.")

    elif option == 6:
        #  Ranch Pizza
        print("Sizes: ")
        print(
            " 1. Mini (4 cut)\n",
            "2. Small (6 cut)\n",
            "3. Medium (8 cut)\n",
            "4. Large (12 cut)\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize()
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Ranch")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Ranch")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Ranch")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Ranch")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please enter a valid option.")

    elif option == 7:
        #  Buffalo Chicken Pizza
        print("Sizes: ")
        print(
            " 1. Mini (4 cut)\n",
            "2. Small (6 cut)\n",
            "3. Medium (8 cut)\n",
            "4. Large (12 cut)\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize()
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.95
            ticket.append("Mini Buff")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 9.95
            ticket.append("S Buff")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 14.25
            ticket.append("M Buff")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 19.95
            ticket.append("L Buff")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please enter a valid option.")

    elif option == 8:
        #  Pete's Pizza
        print("Sizes: ")
        print(
            " 1. Mini (4 cut)\n",
            "2. Small (6 cut)\n",
            "3. Medium (8 cut)\n",
            "4. Large (12 cut)\n"
        )

        size = input("Choose a size: ")
        size = int(size)

        if size == 0:
            finalize()
        
        elif size == 1:
            # mini
            orderTotal = orderTotal + 4.75
            ticket.append("Mini Pete")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # small
            orderTotal = orderTotal + 8.25
            ticket.append("S Pete")
            order(orderNum, ticket, orderTotal)

        elif size == 3:
            # medium
            orderTotal = orderTotal + 12.50
            ticket.append("M Pete")
            order(orderNum, ticket, orderTotal)

        elif size == 4:
            # large
            orderTotal = orderTotal + 18.25
            ticket.append("L Pete")
            order(orderNum, ticket, orderTotal)
            
        else:
            print("Please enter a valid option.")
                      
    else:
        print("Please select a valid option.")

def harrys(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
    print("\nOld Style \"Harry\'s\" Pizza:\n")
    print(
        " 1. per Slice\n",
        "2. Whole Tray (28 slices)\n",
        "3. 1/2 Tray\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize()

    elif option == 1:
        apps()

    elif option == 2:
        salads()

    elif option == 3:
        sammies()
                       
    else:
        print("Please select a valid option.")

def wedgies(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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
        finalize()

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
            finalize()
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.95
            ticket.append("HReggie")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.95
            ticket.append("Reggie")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")

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
            finalize()
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.75
            ticket.append("HITW")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.75
            ticket.append("ITW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")

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
            finalize()
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.75
            ticket.append("HVW")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.75
            ticket.append("VW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")

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
            finalize()
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.95
            ticket.append("HBLTW")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.95
            ticket.append("BLTW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")

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
            finalize()

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
                finalize()
            
            elif size == 1:
                # half
                orderTotal = orderTotal + 4.75
                ticket.append("HHW")
                order(orderNum, ticket, orderTotal)

            elif size == 2:
                # whole
                orderTotal = orderTotal + 7.75
                ticket.append("HW")
                order(orderNum, ticket, orderTotal)

            else:
                print("Please enter a valid option.")

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
                finalize()
            
            elif size == 1:
                # half
                orderTotal = orderTotal + 4.75
                ticket.append("HRBW")
                order(orderNum, ticket, orderTotal)

            elif size == 2:
                # whole
                orderTotal = orderTotal + 7.75
                ticket.append("RBW")
                order(orderNum, ticket, orderTotal)

            else:
                print("Please enter a valid option.")

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
                finalize()
            
            elif size == 1:
                # half
                orderTotal = orderTotal + 4.75
                ticket.append("HTW")
                order(orderNum, ticket, orderTotal)

            elif size == 2:
                # whole
                orderTotal = orderTotal + 7.75
                ticket.append("TW")
                order(orderNum, ticket, orderTotal)

            else:
                print("Please enter a valid option.")

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
            finalize()
        
        elif size == 1:
            # half
            orderTotal = orderTotal + 4.75
            ticket.append("HCW")
            order(orderNum, ticket, orderTotal)

        elif size == 2:
            # whole
            orderTotal = orderTotal + 7.75
            ticket.append("CW")
            order(orderNum, ticket, orderTotal)

        else:
            print("Please enter a valid option.")
    
    else:
        print("Please choose a valid option.")



def hoagies(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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
        finalize()

    elif option == 1:
        apps()

    elif option == 2:
        salads()

    elif option == 3:
        sammies()

    elif option == 4:
        bolis()

    elif option == 5:
        custZahs()

    elif option == 6:
        specZahs()

    elif option == 7:
        harrys()

    elif option == 8:
        wedgies()

    elif option == 9:
        hoagies()

    elif option == 10:
        drinks()                        
    else:
        print("Please select a valid option.")

def drinks(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
    print("\nBeverages:\n")
    print(
        " 1. Soft Drink\n",
        "2. Fountain Drink\n",
        "3. Bottle a' H2O\n"
    )

    option = input("What would you like to order? >> ")
    option = int(option)

    if option == 0:
        finalize()

    elif option == 1:
        apps()

    elif option == 2:
        salads()

    elif option == 3:
        sammies()
                       
    else:
        print("Please select a valid option.")

def finalize(orderNum, ticket, orderTotal):

    print("\nYour total comes to: $", orderTotal, "\n")

    # accept payment

    # print ticket
    print("****************")
    print("*    TICKET    *")
    print("****************")

    for i in ticket:
        print(i)
    
    print("\n\n")
    
    # print receipt


def order(orderNum, ticket, orderTotal):
    print("\nTotal: $", orderTotal)
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