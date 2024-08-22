
# 
#   ______                                  _______             _             
#  |  ____|                                |__   __|           | |            
#  | |__  __  ___ __   ___ _ __  ___  ___     | |_ __ __ _  ___| | _____ _ __ 
#  |  __| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \    | | '__/ _` |/ __| |/ / _ \ '__|
#  | |____ >  <| |_) |  __/ | | \__ \  __/    | | | | (_| | (__|   <  __/ |   
#  |______/_/\_\ .__/ \___|_| |_|___/\___|    |_|_|  \__,_|\___|_|\_\___|_|   
#              | |                                                            
#              |_|     
#option 2 EXPENSE TRACKER 

import pprint # neater printing to the terminal. 

#! 1.  function to welcome user 
# gets users name
def name():
    return input("Please enter your name? ").strip()   
  
user_name = name()

def welcome(user_name):   
    print(f"Hello {user_name}, Welcome to your expense tracker!")   

   
# Defined spending categories
categories = ["travel","entertainment","food","home","clothing","other"]



#! 2. Ask for expense, category and description
#! 3. store data to the dictionary 
#! 5. Data validation: a) check for positive number b) Check category is valid 

# fucntion to add to expense lists 
def add_expense(expenses): # uses expense as argument 
    while True:
        try:
            amount = float(input("\nEnter the amount: £"))  
            if amount <=0:  
                print("You cannot enter 0 or a negative amount")
            else:
                break
        except ValueError:  #it must be an integer 
                print("You must enter a number!") 

    while True:    
        category = input("\nEnter the category: ").strip().lower()
        if category.strip().lower() not in categories:  # checks if the inputed category matches the one from the list 
                print("Pick from the following categories:\nTravel, Entertainment, Food, Home, Clothing or Other.")
        else:               
            break               
        
    desc = (input("\nEnter description: ")) # accepts any description 
    expenses[amount] = {"Category":category, "Description":desc} # insert variables in dictionary 
    print(f"\nThe amount £{amount} has been added to your expense list. \nCategory: {category}, \nDescription: {desc}")
    print("\nPlease see updated expenses:")
    pprint.pprint(expenses)      # shows list of all expenses   
            

#function to add more expenses 
def add_more_expenses(expenses):
    while True:
        response =input("\nWould you like to add another expense? YES or NO. ").strip().lower() # lower case and removes spaces
        if response == 'yes':
            add_expense(expenses)
        elif response == 'no':
            print("EXECUTION COMPLETE")

            break
        else:
            print("Invalid response. Please enter 'YES' or 'NO'.")
   
  
#! 4 Display Summary: a) show total spent, b)total spent per category  c)list of all expenses 


def sum_of_expense(expenses):    
    sum=0
    for amount in expenses.keys(): #iterate over the keys
        sum += float(amount) 
    return sum


def sum_expenses_by_category(expenses, category):  # function get sum by category 
    # Sum the amounts for the given category
    return sum(amount for amount, details in expenses.items() 
    if details['Category'].lower() == category.lower())   


#! Total amount spent in each category 
def display_summary(expenses):
    print("\nYour total amount spent: £",sum_of_expense(expenses))
    
    for category in categories:   # iterates through the each category and displays total 
        total = sum_expenses_by_category(expenses, category)
        print(f"Total amount for {category}: £{total}")


#! 6. Thank you message
def thank_you():
    print(f"\nThank you for using the expense tracker!")



#Run programme using all functions 
def main():
    welcome(user_name)

    expenses = {    # expense dictionary can be toggles on or off
    # 10.00:{"Category":"food","Description":"Subway"},
    # 59.75:{"Category":"food","Description":"Tesco"},
    # 79.99:{"Category":"Travel","Description":"Subway"},
    # 125.49:{"Category":"Clothing","Description":"Zara"},
    # 5.99:{"Category":"food","Description":"Greggs"},
    # 80.55:{"Category":"food","Description":"Asda"},
    # 110.50:{"Category":"travel","Description":"Virgin trains"},
    # 25.99:{"Category":"food","Description":"Nando"},
    # 40.99:{"Category":"clothing","Description":"selfridges"},
    # 9.99:{"Category":"Entertainment","Description":"netlfix"},
   }

    add_expense(expenses)   
    add_more_expenses(expenses)
    display_summary(expenses)
    thank_you()


main()


 



    
     


