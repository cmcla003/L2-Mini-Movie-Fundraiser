# Function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If  yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no output 'display instructions'
        elif response == "no" or response == "n":
            response= "no"
            return response

        else:
            print("Please enter yes or no")

# start of loop

# intialise variables

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
name = ""
count = 0
MAX_TICKETS = 5

# *** Main routine ***
# ask user if want instructions 
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
  # print detailed instructions at a later date
  print("Instructions go here")


while name != "xxx" and count < MAX_TICKETS:
    # tells user how many tickets left
    if count < 4:
        print("You have {} places left".format(MAX_TICKETS-count))
    #  on place left
    else:
        print("***You have ONE place left***")

    # get details
    name = not_blank("Name: ")
    count +=1

if count == MAX_TICKETS:
    print("You have sold all available tickets.")