class OnlineShoppingCart:
     def __init__(self):
        self.cart={}
        self.products={
            "Laptop":95000,
            "Mobile":50000,
            "Headphone":5000,
            "Tablet":7000,
            "keyword":3000
        }
        print("Welcome to online Shopping")
        self.start()

     def start(self):
         print(f'''1. View Products\n
                  2. Add to Cart\n
                  3. Remove to Cart\n
                  4. view cart\n
                  5.Checkout\n
                  6.Exit\n
                    ''')
         choice = input("Enter your choice")
         if choice == '1':
           self.View_Product()
         elif choice == '2':
           self.Add_to_Cart()
         elif choice == '3':
           self.Remove_to_Cart()
         elif choice == '4':
           self.View_Cart()
         elif choice == '5':
           self.Checkout()
         elif choice == '6':
           print("Thank you for visiting")
         else:
           print("Invalid Choice")
     def View_Product(self):
         print("\n---------VIEW PRODUCT---------")
         for product,price in self.products.items():
            print(f"{product}:Rs{price}")
         self.start()
     def Add_to_Cart(self):
      while True:
        product_name=input("enter Product_name").title()
        if product_name in self.products:
          qty=int(input("enter your quantity:"))
          self.cart[product_name]=self.cart.get(product_name,0)+qty
          print("product adde to Cart successfully")
          print("your total product",self.cart)
        else:
          print("product_name is invalid")
        more_items=input("Do you add more items ? (yes/no):")
        if more_items.lower() != "yes":
            break
      self.start()
     def Remove_to_Cart(self):
        item = input("enter product name to remove").title()
        if item in self.cart:
            remove_qty=int(input("enter qty to remove"))
            if remove_qty == self.cart[item]:
               del self.cart[item]
               print("product is remove from cart")
            elif remove_qty > self.cart[item]:
               print("invalid qty please try again")
            else:
               self.cart[item] -= remove_qty
               print("Quantity updated soccessfully ")
            print("updated cart:",self.cart)
        else:
           print("product not found in cart")
        self.start()
     def View_Cart(self):
        print("\n--------VIEW CART----------")
        if not self.cart:
           print("cart is empty")
        else:
            for item, qty in self.cart.items():
               print(f"{item} , {qty}")
        self.start()
     def Checkout(self):
        total = 0
        print("\n--------BILL-------")
        for item , qty in self.cart.items():
           price=self.products[item]*qty
           print(f"{item} ({qty}) = RS{price}")
           total += price
        print("Total Amount = ",total)
        self.start()











