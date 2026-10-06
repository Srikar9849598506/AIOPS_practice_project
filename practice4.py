def home():
    while True:
        choice=input("press start :")
        if choice.lower() == "start":
            print("welcome to costa coffee")
            break
    
        else :
            print("please press start to continue")
            
            
coffee_price={"latte":2,"cappicuno":3,"espresso":4}
coffee_choice={1:"Latte",2:"cappicuno",3:"espresso"}

for (coffee,price),(coffee,choice) in zip(coffee_choice.items(),coffee_choice.items()):
    if price == 3:
        print("coffee",coffee)
        print("price",price)
        print("choice",choice)
        
        
data={}

def select_coffee():
    print("1.latte")
    print("2.cappicuno")
    print("3.espresso")
    choice=int(input("enter your choice"))
    if choice == 1:
        print("you have selected latte")
        return choice
    if choice == 2:
        print("you have selected cappicuno")
        return choice
    if choice ==3:
        print("you have selected espresso")
        return choice
                    
def quantity():
    choice=int(input("enter the quantity"))
    print(f"you selected {choice} quantity")
    data["quantity"]=choice
    return choice

def coffee_name(choice):
    coffee=coffee_choice[choice]
    data['coffee']=coffee
    
def total(choice):
    for key,value in coffee_price.items():
        if value == choice:
            print(value)
            data['value']=value
        
        
# def menu():
#     home()
#     choice=select_coffee()
#     quantity()
#     coffee_name(choice)
#     total(choice)
#     print(data)
    
    
    
# menu()