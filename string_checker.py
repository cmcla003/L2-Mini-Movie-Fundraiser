# Function goes here
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

# Lists and initialise variable 
yes_no = ["yes","no"]
payment = ["cash","credit"]

valid = False
while not valid: 
  instructions = string_check("Please enter yes or no: ",1, yes_no)
  print(instructions)
  
  payment_method = string_check("Choose a payment method, cash or credit: ", 2 , payment)
  print(payment_method)