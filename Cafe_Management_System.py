import time
class Cafe:
  def __init__(self):
    self.order={}
    self.Total_bil=None
    self.order_time=None
    self.menu_items={
        "-----Foods-----": {
           "Burger":100,
           "Pizza":250,
           "Pasta":110,
           "Roll":120
        },
        "-----Drinks-----":{
           "Water Bottel":20,
           "Tea":50,
           "Coffee":90,
           "Coldrink":50
         },
        "-----Desserts-----":{
            "Ice Cream":80,
            "Cake":200,
            "Pastry":90,
            "Milk Cake":600

         }


    }
    print("Welcome to my cafe, How may i  assist you")
    self.menu()
  def menu(self):
     print('''\n1.view_menu
               \n2.order_food
               \n3.view_bill
               \n4.cancel_order
               to press anything to exit''')
     cust_input=input("Enter your choice")
     if cust_input == '1':
      self.view_menu()
     elif cust_input == '2':
      self.order_food()
     elif cust_input == '3':
      self.view_bill()
     elif cust_input == '4':
       self.cancel_order()
     else:
      print("thank you")
  def view_menu(self):
     print("\n--------Menu---------")
     for item_types,items in self.menu_items.items():
       print(f'\n{item_types}')
       for food,price in items.items():
         print(f'{food} : Rs{price}')
     self.order_food()
     self.menu()
  def order_food(self):
    while True:
      user_item_type=input("enter item_types (Foods / Drinks / Desserts):").title()
      if user_item_type == "Foods":
        item_types = "-----Foods-----"
      elif user_item_type == "Drinks":
        item_types = "-----Drinks-----"
      elif user_item_type == "Desserts":
        item_types = "-----Desserts-----"
      else:
        print("items not found")
        continue
      food_name=input("enter items name").title()
      if food_name in self.menu_items[item_types]:
             qty=int(input("enter your quantity: "))
             self.order[food_name]=self.order.get(food_name,0) + qty
             print("your food added successfully:")
             print(f"your current order : {food_name},{qty}")
             print("your total order",self.order)
             if self.order_time is None: # Set order time only if it's the first item added
                 self.order_time = time.time()
      else :
             print("food is not available:")
      more_items=input("do you want to add more items (yes/no)")
      if more_items == 'no':
        break
    self.menu()
  def view_bill(self):
      if not self.order:
        print("no order placed")
      else:
        self.Total_bil=0
        print('\n----------Total_bil---------')
        for food,qty in self.order.items():
          for item_types in self.menu_items:
            if food in self.menu_items[item_types]:
               price=self.menu_items[item_types][food] * qty
               self.Total_bil += price
               print(f'{food} * {qty} = {price}')
          print('------------------------------')
          print(f'Total_bil : {self.Total_bil}')
      self.menu()
  def cancel_order(self):
    if not self.order:
      print("no order cancel")
      return
    # Check if order_time is set before performing operations
    if self.order_time is None:
        print("Cannot cancel: Order time was not recorded. Please place an order first.")
        return
    current_time=time.time()
    if current_time - self.order_time <= 600:
        self.order.clear()
        self.order_time = None
        print("your order cancelled successfully")
    else:
       print("sorry! you can cancel order ")
