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

# Lists and initialise variables
yes_no = ["yes","no"]
payment = ["cash","credit"]
name = ""
count = 0
MAX_TICKETS = 5

# *** Main routine ***
# ask user if want instructions 
want_instructions = string_check("Do you want instructions enter yes or no: ",1, yes_no)
if want_instructions == "yes":
  # print detailed instructions at a later date
  instructions()
  
while name != "xxx" and count < MAX_TICKETS:
  # tells user how many tickets left
  if count < 4:
      print("You have {} places left".format(MAX_TICKETS-count))
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
  count += 1
  # print for testing 
  print("Name: {} Age: {} Ticket price ${}".format(name,age,ticket_cost))
  # payment method
  payment_method = string_check("Choose a payment method, cash or credit: ", 2 , payment)
  
  # print for testing
  print("You have chosen to pay {}".format(payment_method))
  
  #if ALL ticekts sold
  if count == MAX_TICKETS:
    print("You have sold all available tickets.")