def calc_ticket_price(var_age):
   if age < 16:
     price = 7.5
   elif age < 65:
     price = 10.5
   else:
     price = 6.5
   return price

  
profit = 0
while True: 
  age=int(input("Age: "))

  ticket_price = calc_ticket_price(age)
  print("{} : ${:.2f}". format(age, ticket_price))

  print("Profit made from tickets: ${:.2f}".format(profit))