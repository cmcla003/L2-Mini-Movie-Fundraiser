# Function goes here
# sting check indexes lists to asses input and tailor error message 
def string_check(question, num_letter, valid_list):

  error = "Please choose {} or {} ".format(valid_list[0],valid_list[1])
  if num_letter == 1:
    version = 1
  else: 
    version = 2
  
  while True:
    # Ask user if they have played before
    response = input(question).lower().strip()
    for item in valid_list: 
          if response == item[:version] or response == item:
            return item
    print(error)

# assesses input is not blank 
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print("This can't be blank please enter a name")

# main routine goes here
# initalise variables 

# initalise variables

# Lists and initialise variable 
yes_no = ["yes","no"]
payment = ["cash","credit"]

name = ""
count = 0
MAX_TICKETS = 5

# *** Main routine ***
# ask user if want instructions 
instructions = string_check("Please enter yes or no: ",1, yes_no)
if want_instructions == "yes":
  # print detailed instructions at a later date
  print("Instructions go here")


while name != "xxx" and count < MAX_TICKETS:
    # tells user how many tickets left
    if count < 4:
        print("You have {} places left".format(MAX_TICKETS-count))
    # one place left
    else:
        print("***You have ONE place left***")

    # get details
    name = not_blank("Name: ")
    count +=1
    age = int(input("Age: "))

    # calculate ticket price based on age
    if age < 16:
        ticket_price = 7.5
    
    elif age < 65:
        ticket_price = 10.5
    
    else:
        ticket_price = 6.5
  
if count == MAX_TICKETS:
    print("You have sold all available tickets.")