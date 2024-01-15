if __name__ != "__main__":
    
    def user_input():
        '''Takes in fully processed user input'''
        
        while True:
            try:
                pizza_no = int(input("How many pizzas ordered? "))
                
                if pizza_no == 0:
                    print("\nPlease enter a valid value.\n")
                    
                elif pizza_no < 0:
                    print("\nCannot be a negative value\n")
                    
                elif pizza_no >= 1 and pizza_no <= 100:
                    break
                
                elif pizza_no > 100:
                    print("\nToo many pizzas, make separate orders!\n")
                    
            except TypeError:
                print("\nPositive integers only\n")
                
            except ValueError:
                    pizza_no = 1
                    break
        
        while True:
            delivery = input("\nIs delivery required? ")
            delivery = delivery.strip().lower()
            
            if delivery == "y" or delivery == "yes" or delivery == "n" or delivery == "no":
                break
            
            elif delivery == '':
                delivery = "n"
                break
            
            else:
                print("\nPlease enter yes or no only (y/n)\n")
        
        while True:
            day = input("\nIs it Tuesday? ")
            day = day.strip().lower()
            
            if day == "y" or day == "yes" or day == "n" or day == "no":
                break
            
            elif day == '':
                break
            
            else:
                print("\nPlease enter yes or no only (y/n)\n")
        
        while True:
            app_order = input("\nDid the customer use the app? ")
            app_order = app_order.strip().lower()
            
            if app_order == "y" or app_order == "yes" or app_order == "n" or app_order == "no":
                break
            
            elif app_order == '':
                app_order = "n"
                break
            
            else:
                print("\nPlease enter yes or no only (y/n)\n")
        
        return pizza_no, delivery, day, app_order
