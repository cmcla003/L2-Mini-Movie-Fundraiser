import pandas 

# Function goes here
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print("This can't be blank please enter a name")

def number_check(question):
    error = "Please enter a whole number"

    valid = False
    while not valid:

        try:
            response = int(input(question))
            return response
            valid = True

        except ValueError:
            print(error)

def calc_ticket_price(var_age):
   if age < 16:
     price = 7.5
   elif age < 65:
     price = 10.5
   else:
     price = 6.5
   return price
  
def string_check(question, num_letter, valid_list):
  error = "Please choose {} or {} ".format(valid_list[0],valid_list[1])

  while True:
    # Ask user if they have played before
    response = input(question).lower().strip()
    for item in valid_list: 
          if response == item[:num_letter] or response == item:
            return item
    print(error)

# assesses input is not blank 
def instructions ():
  print("Instructions go here.... to be completed ")

# currency formatting 
def currency(x):
  return "${:.2f}".format(x)
  
# Lists and initialise variables
yes_no = ["yes","no"]
payment = ["cash","credit"]
all_names = []
all_ticket_costs = []
all_surcharge = []

name = ""
tickets_sold = 0
MAX_TICKETS = 5

# set up dictionary to populate from list data 
mini_movie_dict = {"Name": all_names, "Ticket Price": all_ticket_costs, "Surcharge": all_surcharge}

# *** Main routine ***
# ask user if want instructions 
want_instructions = string_check("Do you want instructions enter yes or no: ",1, yes_no)
if want_instructions == "yes":
  # print detailed instructions at a later date
  instructions()
  
while name != "xxx" and tickets_sold < MAX_TICKETS:
  # tells user how many tickets left
  if tickets_sold < 4:
      print("You have {} places left".format(MAX_TICKETS-tickets_sold))
  # one place left
  else:
      print("***You have ONE place left***")
  # get user details check age and calculate ticket price
  name = not_blank("Name: ")
  age = number_check("Age: ")
  if age >=12 and age <=120:
    pass
  elif age < 12:
    print("Sorry you are too young for this movie")
    continue
  else: 
    print("Looks like a typo, please try again")
    continue  
  # calculate ticket price based on age
  ticket_cost= calc_ticket_price(age)

  # payment method
  payment_method = string_check("Choose a payment method, cash or credit: ", 2 , payment)

  if payment_method == "cash":
    surcharge = 0 
  else: 
    surcharge = ticket_cost * 0.05
  tickets_sold += 1
  # populate values into correct list 
  all_names.append(name)
  all_ticket_costs.append(ticket_cost)
  all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index("Name")

# calcuate total cost incl surcharge
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# calcualte total profit 
mini_movie_frame ["Profit"] = mini_movie_frame["Ticket Price"] - 5

# calculate ticket and profit totals 
total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()

# currency formatting 
add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
  mini_movie_frame [var_item]= mini_movie_frame[var_item].apply(currency)
  
# display totals on screen 
print("--- Ticket Data ---")
print()
print(mini_movie_frame)
print()
print("--- Ticket Sales & profit ---")
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))
print()

#if ALL tickets sold
if tickets_sold == MAX_TICKETS:
  print("You have sold all available tickets.")