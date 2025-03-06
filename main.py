def odd_or_even():
    print("___________________________________")
    print("\n            ODD OR EVEN            ")
    print("___________________________________")
    while True:
        try:
            num = input("\nEnter a number: ")
            print("___________________________________")
            if num.lower() == 'exit':
                print("Exiting the Odd or Even checker.")
                break
            num = int(num)
            if num % 2 == 0:
                print(f"\nThe number {num} is even")
                print("___________________________________")
            else:
                print(f"\nThe number {num} is odd")
                print("___________________________________")
                
            print("\ntype 'exit' to quit")
            print("___________________________________")
        except ValueError:
            print("Invalid input! Please enter a number or type 'exit' to quit.")

def info_data_Entry():
    print("___________________________________")
    print("\n      INFORMATION DATA ENTRY       ")
    print("___________________________________")
    while True:
        try:
            # Prompt for data entry
            name = input("\nWhat is your name? ")
            age = int(input("\nHow old are you? "))
            height = float(input("\nEnter your height (in meters): "))
            weight = float(input("\nEnter your weight (in kg): "))
            fav_color = input("\nWhat is your favorite color? ")

            # Display the entered data
            print("___________________________________")
            print("\nData entered successfully! Here is the information:")
            print(f"\nName: {name}")
            print(f"Age: {age}")
            print(f"Height: {height}")
            print(f"Weight: {weight}")
            print(f"Favorite Color: {fav_color}")
            print("___________________________________")

            # Ask if the user wants to exit or continue
            exit_option = input("\nDo you want to enter more data? (Yes/Exit): ").strip().lower()
            if exit_option == 'exit':
                print("Exiting the Information Data Entry.")
                break
            elif exit_option != 'yes':
                print("Invalid option! Please type 'Yes', 'No', or 'Exit'.")
                
        except ValueError:
            print("Invalid input! Please try again.")


def calculator():
    print("___________________________________")
    print("\n        SIMPLE CALCULATOR          ")
    print("___________________________________")
    while True:
        try:
            operator = input("\nEnter the operator (+, -, /, *), or type 'exit' to quit: ")
            print("___________________________________")
            if operator.lower() == 'exit':
                print("Exiting the calculator.")
                break
            
            num1 = float(input("\nEnter the first number: "))
            print("___________________________________")
            num2 = float(input("\nEnter the second number: "))
            print("___________________________________")
            
            if operator == "+":
                print("\nResult: ", num1 + num2)
                print("___________________________________")
            elif operator == "-":
                print("\nResult: ", num1 - num2)
                print("___________________________________")
            elif operator == "*":
                print("\nResult: ", num1 * num2)
                print("___________________________________")
            elif operator == "/":
                if num2 != 0:
                    print("\nResult: ", num1 / num2)
                    print("___________________________________")
                else:
                    print("\nSyntax Error! Division by zero.")
            else:
                print("\nInvalid operator!")
        except ValueError:
            print("Invalid input! Please enter valid numbers or type 'exit' to quit.")

def temp_converter():
    print("___________________________________")
    print("\n       TEMPERATURE CONVERTER       ")
    print("___________________________________")
    while True:
        try:
            unit = input("\nEnter the unit (C/F/K) to convert: ").strip().upper()
            print("___________________________________")
            
            if unit not in ["C", "F", "K"]:
                print("\nInvalid unit! Please enter C, F, or K.")
                continue  # Skip the rest of the loop if invalid unit

            temperature = float(input("\nEnter the temperature: "))
            print("___________________________________")
            
            # Perform the conversion based on the chosen unit
            if unit == "C":
                f_temp = (temperature * 9/5) + 32
                k_temp = temperature + 273.15
                print(f"\n{temperature} degrees Celsius = {f_temp:.2f} degrees Fahrenheit")
                print("___________________________________")
                print(f"\n{temperature} degrees Celsius = {k_temp:.2f} Kelvin")
                print("___________________________________")
            elif unit == "K":
                c_temp = temperature - 273.15
                f_temp = (c_temp * 9/5) + 32
                print(f"\n{temperature} Kelvin = {c_temp:.2f} degrees Celsius")
                print("___________________________________")
                print(f"\n{temperature} Kelvin = {f_temp:.2f} degrees Fahrenheit")
                print("___________________________________")
            elif unit == "F":
                c_temp = (temperature - 32) * 5/9
                k_temp = c_temp + 273.15
                print(f"\n{temperature} degrees Fahrenheit = {c_temp:.2f} degrees Celsius")
                print("___________________________________")
                print(f"\n{temperature} degrees Fahrenheit = {k_temp:.2f} Kelvin")
                print("___________________________________")
            
        except ValueError:
            print("\nError! Please enter valid numbers.")

        # Ask if the user wants to proceed or exit after conversion
        proceed = input("\nDo you want to perform another conversion? (Yes/No): ").strip().lower()
        
        if proceed == "no":
            print("___________________________________")
            print("\nExiting the temperature converter.")
            break
        elif proceed != "yes":
            print("___________________________________")
            print("\nInvalid option! Please type 'Yes' to continue or 'No' to exit.")



def weather_app():
    print("_____________________________________")
    print("\n          WEATHER CHECKER          ")
    print("\n___________________________________")
    while True:
        try:
            print("\n1. Check weather")
            print("2. Exit")
            print("___________________________________")
            choice = input("\nChoose an option (1-2): ")
            print("___________________________________")

            if choice == '2':
                print("Exiting the weather app.")
                break
            if choice == "1":
                temperature = float(input("\nWhat is the temperature outside? ( in Celsius) "))
                print("___________________________________")
                
                if temperature >= 38:
                    print("\nIt's too hot outside!")
                elif temperature >= 20:
                    print("\nThe weather is good!")
                else:
                    print("\nIt's cold outside!")
                print("___________________________________")
            else:
                print("\nInvalid choice! Please choose a valid option.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def english_to_metric_converter():
    print("___________________________________")
    print("\n     ENGLISH TO METRIC SYSTEM    ")
    print("___________________________________")
    while True:
        try:
            print("\n1. Miles to Kilometers")
            print("2. Yards to Meters")
            print("3. Feet to Meters")
            print("4. Inches to Meters")
            print("5. Pounds to Kilograms")
            print("6. Ounces to Kilograms")
            print("7. Gallons (UK) to Liters")
            print("8. Quarts to Liters")
            print("9. Pints to Liters")
            print("10. Fluid Ounces to Liters")
            print("11. Exit")
            print("\n___________________________________")
            choice = input("\nChoose an option (1-11): ")
            print("___________________________________")

            if choice == '11':
                print("Exiting the English to Metric converter.")
                break
            if choice == '1':
                miles = float(input("\nEnter miles: "))
                print("___________________________________")
                km = miles * 1.60934
                print(f"\n{miles} miles = {km:.2f} kilometers")
                print("___________________________________")
            elif choice == '2':
                yards = float(input("\nEnter yards: "))
                print("___________________________________")
                meters = yards * 0.9144
                print(f"\n{yards} yards = {meters:.2f} meters")
                print("___________________________________")
            elif choice == '3':
                feet = float(input("\nEnter feet: "))
                print("___________________________________")
                meters = feet * 0.3048
                print(f"\n{feet} feet = {meters:.2f} meters")
                print("___________________________________")
            elif choice == '4':
                inches = float(input("\nEnter inches: "))
                print("___________________________________")
                meters = inches * 0.0254
                print(f"\n{inches} inches = {meters:.2f} meters")
                print("___________________________________")
            elif choice == '5':
                pounds = float(input("\nEnter pounds: "))
                kg = pounds * 0.453592
                print(f"\n{pounds} pounds = {kg:.2f} kilograms")
            elif choice == '6':
                ounces = float(input("\nEnter ounces: "))
                print("___________________________________")
                kg = ounces * 0.0283495
                print(f"\n{ounces} ounces = {kg:.2f} kilograms")
                print("___________________________________")
            elif choice == '7':
                gallons = float(input("\nEnter gallons (UK): "))
                print("___________________________________")
                liters = gallons * 4.54609
                print(f"\n{gallons} gallons = {liters:.2f} liters")
                print("___________________________________")
            elif choice == '8':
                quarts = float(input("\nEnter quarts: "))
                print("___________________________________")
                liters = quarts * 1.13652
                print(f"\n{quarts} quarts = {liters:.2f} liters")
                print("___________________________________")
            elif choice == '9':
                pints = float(input("\nEnter pints: "))
                print("___________________________________")
                liters = pints * 0.568261
                print(f"\n{pints} pints = {liters:.2f} liters")
                print("___________________________________")
            elif choice == '10':
                fluid_ounces = float(input("\nEnter fluid ounces: "))
                print("___________________________________")
                liters = fluid_ounces * 0.0295735
                print(f"\n{fluid_ounces} fluid ounces = {liters:.2f} liters")
                print("___________________________________")
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
def shopping_management():
    print("___________________________________")
    print("\n       SHOPPING MANAGEMENT         ")
    print("___________________________________")
    
    while True:
        cart_item = []
        prices = []
        total_price = 0.0
        discount = 0.0  # Initialize discount to 0
        
        while True:
            cart = input("\nEnter the items that you want to buy (type 'done' to finish or 'exit' to quit): ").lower()
            print("___________________________________")
            
            if cart == "done":
                break
            elif cart == "exit":
                print("Exiting the shopping management.")
                return  # Exit the function and return to the main menu
            else:
                try:
                    item_price = float(input(f"\nEnter the price of {cart}: "))
                    print("___________________________________")
                    cart_item.append(cart)
                    prices.append(item_price)
                    total_price += item_price  
                except ValueError:
                    print("Please enter a valid price.")  

        # Show shopping cart summary
        print("\nShopping Cart Summary:")
        print("___________________________________")
        for i in range(len(cart_item)):
            print(cart_item[i], ": $" ,prices[i])  

        # Display the total amount before discount
        print("___________________________________")
        print(f"\nTotal Amount: ${total_price:.2f}")
        print("___________________________________")

        # Ask the user if they want to apply a discount
        apply_discount = input("\nDo you want to apply a discount? (Yes/No): ").strip().lower()
        print("___________________________________")

        if apply_discount == 'yes':
            try:
                # Let the user input their discount percentage
                discount_percentage = float(input("\nEnter your discount percentage (e.g., 10 for 10%): "))
                # Validate the discount percentage
                print("___________________________________")
                if 0 <= discount_percentage <= 100:
                    discount = (discount_percentage / 100) * total_price
                else:
                    print("___________________________________")
                    print("Invalid discount percentage! Please enter a value between 0 and 100.")
                    discount = 0
            except ValueError:
                print("Invalid input! Please enter a valid number for the discount.")
                discount = 0
        else:
            # Calculate the discount based on total_price if no manual discount entered
            if total_price >= 100:
                discount = total_price * 0.1  # 10% discount for prices above 100
            elif total_price >= 50:
                discount = total_price * 0.05  # 5% discount for prices between 50 and 100
            else:
                print("Total amount did not reach the minimum spend, no discount: $", total_price)

        # Apply discount to the total price
        discounted_price = total_price - discount

        # Show the total amount with discount
        print(f"\nTotal Amount with Discount: ${discounted_price:.2f}")
        print("___________________________________")

        # Ask if the user wants to make another purchase or exit
        final_action = input("\nDo you want to make another purchase or exit? (Enter 'purchase' for another purchase or 'exit' to quit): ").strip().lower()
        print("___________________________________")
        
        if final_action == "exit":
            print("\nExiting the shopping management.")
            print("___________________________________")
            break  # Exit the loop and return to the main menu
        elif final_action == "purchase":
            continue  # Continue shopping and repeat the loop for a new transaction
        else:
            print("Invalid option! Exiting the shopping management.")
            break  # Exit the loop and return to the main menu

    
    
def color_game():
    import random
    print("___________________________________")
    print("\n         COLOR GAME APP            ")
    print("___________________________________")
    
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
    print("\nWelcome to the Color Bet Game!")
    
    while True:
        # Step 1: User selects 6 colors
        print("___________________________________")
        print("\nAvailable colors: ", ", ".join(colors))
        selected_colors = []
        for i in range(3):
            color = input(f"\nChoose color {i+1} (type a color from the list): ").strip().lower()
            print("___________________________________")
            while color not in colors or color in selected_colors:
                print("Invalid choice or color already selected. Please choose a different color.")
                color = input(f"Choose color {i+1} (type a color from the list): ").strip().lower()
            selected_colors.append(color)
        
        # Step 2: User enters their bet
        try:
            bet_amount = float(input("\nEnter your bet amount: $"))
            print("___________________________________")
        except ValueError:
            print("Invalid input! Please enter a valid amount.")
            continue
        
        # Step 3: Draw 3 random colors
        drawn_colors = random.sample(colors, 3)
        print(f"\nDrawn colors: {', '.join(drawn_colors)}")
        print("___________________________________")
        
        # Step 4: Check how many colors match
        matching_colors = set(selected_colors).intersection(drawn_colors)
        num_matches = len(matching_colors)
        
        # Step 5: Determine the result
        if num_matches == 3:
            multiplier = 4
            print(f"\nCongratulations! You got all 3 colors right! Your bet is multiplied by {multiplier}.")
            print("___________________________________")
        elif num_matches == 2:
            multiplier = 3
            print(f"\nGood job! You got 2 colors right! Your bet is multiplied by {multiplier}.")
            print("___________________________________")
        elif num_matches == 1:
            multiplier = 2
            print(f"\nNice try! You got 1 color right! Your bet is multiplied by {multiplier}.")
            print("___________________________________")
        else:
            multiplier = 0
            print("\nSorry, no matches. Better luck next time!")
            print("___________________________________")
        
        # Step 6: Calculate the final result
        total_winnings = bet_amount * multiplier
        print(f"\nYour total winnings are: ${total_winnings:.2f}")
        print("___________________________________")
        
        # Step 7: Ask if they want to play again
        play_again = input("\nDo you want to play again? (Yes/No): ").strip().lower()
        print("___________________________________")
        if play_again != "yes":
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    while True:
        print("___________________________________")
        print("\nMY PYTHON APPLICATION MENU")
        print("___________________________________")
        print("\nPlease select an option:")
        print("___________________________________")
        print("A. Odd or Even")
        print("B. Information Data Entry")
        print("C. Calculator")
        print("D. Temperature Converter")
        print("E. Weather Checker")
        print("F. English to Metric System Conversion")
        print("G. Shopping Management")
        print("H. Color Game")
        print("I. Exit")
        
        print("___________________________________")
        choice = input("\nEnter your choice (A-I): ").upper()
        print("___________________________________")

        if choice == "A":
            odd_or_even()
        elif choice == "B":
            info_data_Entry()
        elif choice == "C":
            calculator()
        elif choice == "D":
            temp_converter()
        elif choice == "E":
            weather_app()
        elif choice == "F":
            english_to_metric_converter()
        elif choice == "G":
            shopping_management()
        elif choice == "H":
            color_game()
        elif choice == "I":
            print("\nExiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")


        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        