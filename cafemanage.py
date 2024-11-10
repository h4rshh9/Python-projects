#cafe management system 
def order(str):
    # cafe menu
    menu={
        "coffee" : 30,
        "cold coffee" : 60,
        "cold coffee with icecreame" : 80,
        "pasta" : 70,
        "momos" : 60,
        "pizza" : 120,
        "burger" : 40,
    }
    if(str=="menu"):
        return menu
    
    if item in menu:
        print(f"Your item {str} has been added to your order ")
        return menu[item]
    else:
        print(f"Order item {str} is not avaialable yet")
        return 0


print("Welcome To KV cafe...!")
print("HELLO ^.^")


bill = 0
menu = order("menu")
print(menu)

while True:
    if(bill==0):
        item = input("Please enter your order: ").strip()
        price = order(item)
        bill += price
      
    elif(bill!=0)  :
        item = input("Please enter your order & get bill to type bill: ").strip()
        if item == "bill":
            break
        
        price = order(item)
        bill += price

print(f"Your total bill is :) {bill}")

print("Thanks for  come \n\tPleace come back^,^ :)")
