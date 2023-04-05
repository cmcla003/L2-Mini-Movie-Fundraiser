import pandas 
from random import choice

# currency formatting 
def currency(x):
  return "${:.2f}".format(x)

#dictionaries hard coded for testing
all_names = ["Albie", "Brian", "Carrie", "Daniel", "Ellie"]
all_ticket_costs = [7.50,7.50,10.50,10.50,6.50]
surcharge = [0,0,0.53,0.53,0]

mini_movie_dict = {"Name": all_names, "Ticket Price": all_ticket_costs, "Surcharge": surcharge}
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

# lucky ticket raffle
winner = choice(all_names)
print(winner)
locate = all_names.index(winner)
print(locate)
print("Raffle winner {} You have won ${:.2f} your ticket is free. ".format(winner,all_ticket_costs[locate]))