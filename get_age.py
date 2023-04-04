def int_check (question):
    error = "Please enter a whole number"

    valid = False
    while not valid:

        try:
            response = int(input(question))
            return response
            valid = True
        except ValueError:
            print(error)

valid = False
while not valid: 
  
  age = int_check("Age: ")
  if age >=12 and age <=120:
    print("Age: {} test ".format(age))
  elif age <12:
    print("Sorry you are too young for this movie")

  else: 
    print("Looks like a typo, please try again")
