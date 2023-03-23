# Function goes here
def cash_credit(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If cash
        if response == "cash" or response == "ca":
            response = "cash"
            return response

        # If credit
        elif response == "credit" or response == "cr":
            response= "credit"
            return response

        else:
            print("Sorry that is not a valid payment method")

# Main routine goes here ...valid = Falsewhile not valid:
valid = False
while not valid:
  payment_method = cash_credit("Choose a payment method, cash or credit: ")
  print(payment_method)

