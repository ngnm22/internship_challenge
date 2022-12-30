import json
import Rental

# initialising the array that is going to be written at the answer in the output
answer = []

# opening the input file and retrieving the cars and rentals dictionaries as two separate variables
with open('data\input.json') as data_file:
    data_details = json.load(data_file)
car_data = data_details["cars"]
rental_data = data_details["rentals"]

# looping through to find the price of each car_id
for i in range(len(rental_data)):
    rentals = Rental.Rental_price(car_data,rental_data[i])
    #appending the answers array for the result of this loop
    answer.append({"id": rentals.id, "price": int(rentals.price)})

#writing the result in a JSON file called output
with open('data\output.json', 'w') as outfile:
    json.dump({'rentals': answer}, outfile, indent=2)