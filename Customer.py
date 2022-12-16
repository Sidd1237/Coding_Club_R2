class Customer:
    def __init__(self,name="",id_no="",room_no="",cart_balance=0,total_disc=0.0):
        self.name = name
        self.id_no = id_no
        self.room_no = room_no
        self.swd = 100000
        self.cart_balance = cart_balance
        self.total_disc = total_disc
        self.cart = []

    def __str__(self):
        return f"Name: {self.name} \nID No: {self.id_no} \nRoom: {self.room_no}"

    def placeOrder(self, item):
        for obj in self.cart:
            if item.name == obj.name:
                obj.setQuantity(obj.getQuantity()+item.getQuantity())
                self.cart_balance+=item.getQuantity()*obj.getPrice()
                return

        self.cart.append(item)
        self.cart_balance+=item.getQuantity()*item.getPrice()
        self.cart.sort(key=lambda x: x.sector,)

    def displayCart(self):
        if len(self.cart)==0:
            print("Your cart is empty :(")
            return
        for item in self.cart:
            print(item)
            print("\n\n")
            print(f"Amount to be paid: {self.cart_balance}")

    def removeItem(self,item,quantity=0):
        quantity = item.getQuantity()
        
        for obj in self.cart:
            if item.name == obj.name and (obj.getQuantity()==quantity or quantity==0):
                quantity = obj.getQuantity()
                self.cart.remove(obj)
                self.cart_balance-=quantity*obj.getPrice()
                
            elif item.name == obj.name and not obj.quantity==quantity:
                obj.setQuantity(obj.getQuantity()-quantity)
                self.cart_balance-=quantity*obj.getPrice()

                
            else:
                print(f"Your cart doesn't contain {item.name}")

    def checkout(self):
        print(f"Your total balance: {self.cart_balance}")
        print("Enter the mode of payment\n")
        choice = int(input("1.SWD\n2.UPI"))
        if choice ==1:
            self.swd-=self.cart_balance
            temp = self.cart_balance
            self.cart_balance=0
            self.cart=[]
            print(f"{temp} has been deducted from your SWD successfully")
            print(f"{self.swd} left in your SWD")
            return
        
        elif choice ==2:
            print(f"{self.cart_balance} to be paid with UPI")
            self.cart_balance=0
            self.cart=[]
            return





class Store: 
    def __init__(self,name):
        self.name = name

    inventory={
            1:'Orange',
            2:'Apple',
            3:'Onion',
            4:'Loreal Conditioner',
            5:'Dove soap',
            6:'Tresseme Lotion',
            7:'Laptop',
            8:'Smartphone',
            9:'Watch',
            10:'Shirt',
            11:'Jeans',
            12:'Hat'

        }

    def displayInventory(self):

        for i in range(12):
            print(i+1,Store.inventory[i+1],": Rs.",Item.prices[Store.inventory[i+1]])

    def addToCart(self, cust:Customer()):
        n = int(input("Enter the item number you would like to buy: "))
        quantity = int(input(f"Enter the quantity of {Store.inventory[n]} you would like to buy: "))
        item = Item(Store.inventory[n],quantity)
        cust.placeOrder(item)
        print("Item added successfully")

    def removeFromCart(self,cust:Customer()):
        cust.displayCart()
        if len(cust.cart)==0:
            return
        name = input("Enter the name of the item you would like to remove (Case sensitive): ")
        quantity = int(input(f"Enter the quantity of {name} you would like to remove: "))
        item = Item(name,quantity)
        cust.removeItem(item)
        print(f"{quantity} {name} removed successfully")

    def searchInventory(self,cust:Customer(),name:str):
        if name in Store.inventory.values():
            choice = input("Found!! Would you like to buy this item?")
            if choice.lower()=="yes":
                quantity = int(input("Enter the quantity: "))
                cust.placeOrder(Item(name,quantity))

            else:
                print("Un Bruh momento")
            
        else:
            print("Item not found")
class Item:
    prices = {
            'Orange':10,
            'Apple':10,
            'Onion':40,
            'Loreal Conditioner':100,
            'Dove soap':80,
            'Tresseme Lotion':120,
            'Laptop':40000,
            'Smartphone':13000,
            'Watch':2000,
            'Shirt':400,
            'Jeans': 1000,
            'Hat':200

        }
    sector = {
            'Orange':"Fruits and Vegetables",
            'Apple':"Fruits and Vegetables",
            'Onion':"Fruits and Vegetables",
            'Loreal Conditioner':"Toiletries",
            'Dove soap':"Toiletries",
            'Tresseme Lotion':"Toiletries",
            'Laptop':"Electronics",
            'Smartphone':"Electronics",
            'Watch':"Electronics",
            'Shirt':"Clothing",
            'Jeans': "Clothing",
            'Hat':"Clothing"
        }

    discount = {
            'Orange':0.2,
            'Apple':0.2,
            'Onion':0.3,
            'Loreal Conditioner':0.1,
            'Dove soap':0.1,
            'Tresseme Lotion':0.1,
            'Laptop':0.15,
            'Smartphone':0.15,
            'Watch':0.20,
            'Shirt':0.40,
            'Jeans': 0.40,
            'Hat':0.50

        }

    profits = {
            'Orange':2,
            'Apple':2,
            'Onion':10,
            'Loreal Conditioner':30,
            'Dove soap':30,
            'Tresseme Lotion':40,
            'Laptop':10000,
            'Smartphone':2000,
            'Watch':300,
            'Shirt':80,
            'Jeans': 200,
            'Hat':10

        }
          
    def __init__(self,name="",quantity=0,price=0,sector="",disc=0.0):

        self.name = name
        self.quantity = quantity
        self.price=Item.prices[name]
        self.sector = Item.sector[name]
        self.disc = Item.discount[name]

    def __str__(self):
        return f"Name: {self.name} \nQuantity: {self.quantity} \nSector: {self.sector}"

    def setQuantity(self,n=0):
        self.quantity =n

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price
    
    def getSector(self):
        return self.sector

    def getDiscount(self):
        return self.disc

        

class Admin:
    def __init__(self,user,password):
        self.user = user
        self.password = password

    def viewItems(self, store:Store("")):
        store.displayInventory()

    def viewProfits(self):
        profits = Item.profits
        
        print("Profits:")
        for item in profits.keys():
            print(f"{item}: Rs.{profits[item]}")
        print()

cust1 = Customer("Siddharth","2022A7PS0070P","SR-236")
store = Store("Akshay")
choice = int(input(f"Choose method of logging in:\n1.Customer\n2.Admin\n"))

username = "akshay123"
password = "akshay_is_mid"

if choice ==1:
    name = input("Enter your name: ")
    id_no = input("Enter your id_no:")
    room_no = input("Enter your room no:")
    cust = Customer(name,id_no,room_no)
    print(f"Welcome {cust.name}!")
    print("How would you like to procede?")
    
    while(choice!=-1):


        ch = int(input("\n1.View cart\n2.Add to cart\n3.Remove from cart\n4.Checkout\n5.Exit"))
        if(ch==1):
            cust.displayCart()

        elif(ch==2):
            store.displayInventory()
            store.addToCart(cust)

        elif(ch==3):
            store.removeFromCart(cust)

        elif(ch==4):
            cust.checkout()

        elif(ch==5):
            break
    
elif choice==2:
    admin = Admin(username,password)
    user=input("Enter the username: ")
    pass_=input("Enter the password: ")

    if user==username and pass_==password:
        print("Successfully logged in!")

        while(True):
            ch=int(input("1.Check prices\n2.Check profits\n3.Exit\n"))

            if ch==1:
                admin.viewItems(store)

            elif ch==2:
                admin.viewProfits()

            elif ch==3:
                break

    











