# Name: lukka ayres
# Period:uh PM?
# Disneyland Trip Budget Calculator
print("Welcome to your DisneyLand trip calculator!")
print("I'm going to help you calculate the total cost of your trip based on some simple questions i will ask you.")
print("Let's get started!")
#my greetings to the user
name = input("What is your name? ")
print(f"Hello, {name}! Let's calculate the cost of your trip.")
#ALLLLL of my variables besides the name to calculate the total cost
party_size = int(input("How many people are in your party? "))
days = int(input("How many days will you be staying at DisneyLand? "))
hotel_cost_per_night = float(input("What is the cost for one room per night at your hotel? "))
hotel_rooms = int(input("How many hotel rooms will you need? "))
total_hotel_cost = hotel_cost_per_night * days * hotel_rooms
ticket_cost_per_person = float(input("What is the cost of a ticket per person? "))
total_ticket_cost = ticket_cost_per_person * party_size
food_budget = float(input("how much will each person spend on food for the trip? "))
food_budget_total = food_budget * party_size
souvenir_budget = float(input("how much will each person spend on souvenirs for the trip? "))
souvenir_budget_total = souvenir_budget * party_size
distance_to_disneyland_oneway = float(input("What is the distance to DisneyLand in miles? "))
round_trip_distance = distance_to_disneyland_oneway * 2
vehicle_mpg = float(input("What is your vehicles MPG? "))
current_gas_price = float(input("What is the current price of gas per gallon? "))
gallons_needed = round_trip_distance / vehicle_mpg
gas_cost = gallons_needed * current_gas_price
Disneyland_parking_cost = float(input("What is the cost of parking at DisneyLand? "))
parking_price_per_day = Disneyland_parking_cost * days
Total_trip_budget = total_hotel_cost + total_ticket_cost + food_budget_total + souvenir_budget_total + gas_cost + parking_price_per_day
total_cost_per_person = Total_trip_budget / party_size
total_cost_per_day = Total_trip_budget / days
trip_budget = float(input("What is your budget for the trip? "))
trip_budget_difference = trip_budget - Total_trip_budget
#finished all my calculations and thank the user for the info
#display a full report of the trip cost
print(f"Thank you for providing the information, {name}.")
print()
#very nicelly formatted with supa cool spacing and catagorys
print("----DISNEYLAND TRIP COST SUMMARY----")
print()
print("-------TRAVLER INFO-------")
print(f"name: {name}")
print(f"Number of people: {party_size}")
print(f"Number of park days: {days}")
print(f"Number of hotel nights: {days}")
print(f"Total hotel cost: ${total_hotel_cost:.2f}")
print()
print("-------TICKET INFO-------")
print(f"Park Hopper ticket price: ${ticket_cost_per_person:.2f}")
print(f"Total Park Hopper cost: ${total_ticket_cost:.2f}")
print()
print("-------FOOD & SOUVENIR INFO-------")
print(f"Total food cost: ${food_budget_total:.2f}")
print(f"Total souvenir cost: ${souvenir_budget_total:.2f}")
print()
print("-------DRIVING INFO-------")
print(f"One-way driving distance: {distance_to_disneyland_oneway} miles")
print(f"Round-trip driving distance: {round_trip_distance} miles")
print(f"Vehicle MPG: {vehicle_mpg}")
print(f"Gas price: ${current_gas_price:.2f}")
print(f"Gallons of gas needed: {gallons_needed:.2f}")
print(f"Total gas cost: ${gas_cost:.2f}")
print(f"Total parking cost: ${parking_price_per_day:.2f}")
print()
#final cost info and totals
print("-------FINAL COST INFO-------")
print(f"Final Disneyland trip cost: ${Total_trip_budget:.2f}")
print(f"Cost per person: ${total_cost_per_person:.2f}")
print(f"Cost per park day: ${total_cost_per_day:.2f}")
print()
#show the user if they are over or under budget

print("-------BUDGET INFO-------")
print(f"Trip budget: ${trip_budget:.2f}")
print(f"Budget difference: ${trip_budget_difference:.2f}")
print()
#thank user and give a farewell mesage to the user with final cost and savings
print("Thank you for using the Disneyland trip calculator! Have a magical trip!")
print(f"you have a budget difference of ${trip_budget_difference:.2f} for your trip and the total cost is ${Total_trip_budget:.2f}!")