print("Welcome to your DisneyLand trip calculator!")
print("I'm going to help you calculate the total cost of your trip based on some simple questions i will ask you.")
print("Let's get started!")

name = input("What is your name? ")
print(f"Hello, {name}! Let's calculate the cost of your trip.")
party_size = float(input("How many people are in your party? "))
days = float(input("How many days will you be staying at DisneyLand? "))
hotel_cost_per_night = float(input("What is the cost for one room per night at your hotel? "))
hotel_rooms = float(input("How many hotel rooms will you need? "))
total_hotel_cost = hotel_cost_per_night * days * hotel_rooms
ticket_cost_per_person = float(input("What is the cost of a ticket per person? "))
total_ticket_cost = ticket_cost_per_person * party_size
food_budget = float(input("how much will each person spend on food for the trip? "))
food_budget_total = food_budget * party_size
souvenir_budget = float(input("how much will each person spend on souvenirs for the trip? "))
souvenir_budget_total = souvenir_budget * party_size
distance_to_disneyland = float(input("What is the distance to DisneyLand in miles? "))
vehicle_mpg = float(input("What is your vehicles MPG? "))
current_gas_price = float(input("What is the current price of gas per gallon? "))
Disneyland_parking_cost = float(input("What is the cost of parking at DisneyLand? "))
Total_trip_budget = total_hotel_cost + total_ticket_cost + food_budget_total + souvenir_budget_total + (distance_to_disneyland / vehicle_mpg * current_gas_price) + Disneyland_parking_cost

print(f"Thank you for providing the information, {name}.")
print(f"The total cost of your trip to DisneyLand will be: ${Total_trip_budget:.2f}")