import task1input as t1
import time

def pizza_count(price, pizza_no):
    '''Calculates price for total pizzas'''
    
    new_price = price * pizza_no
    return new_price

# def day_check(price, day = "yes" if time.localtime()[6] == 1 else "no"):
def day_check(price, day = "no"):
    '''Checking if it's Tuesday for discount'''
        
    if day == "y" or day == "yes":
        price = price - (50/100) * price
        
    elif day == "n" or day =="no":
        pass

    else:
        print("y or n only")
    
    return price

def app_check(price, app_order = "n"):
    '''Check if ordered by app for discount'''
    
    if app_order == "y" or app_order == "yes":
        price  = price - (25/100) * price

    elif app_order == "n" or app_order == "no":
        pass

    else:
        print("y or n only")
        
    return price
    
def delivery_check(price, delivery, pizza_no):
    '''Check if delivery is required or not, add price for small orders'''
    
    if delivery == "y" or delivery == "yes":
        if pizza_no < 5:
            price = price + 2.5

    elif delivery == "n" or delivery == "no":
        pass

    else:
        print("y or n only")
    
    return price

print()    
print("BPP Pizza Price Calculator")
print("=" * 30)
print()

price = 12

pizza_no, delivery, day, app_order = t1.user_input()

if not day:
    if time.localtime()[6] == 1:
        day = "yes"
    else:
        day = "no"
    
new_price = pizza_count(price, pizza_no)
delivery_price = delivery_check(new_price, delivery, pizza_no)
day_price = day_check(delivery_price, day)
app_price = app_check(day_price, app_order)

print()
print(f"Total Price of the pizza is: £{app_price:.2f}.")
print()
