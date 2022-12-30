import json
from Rental import Rental_functions

# initialising the array that is going to be written at the answer in the output
answer = []

# opening the input file and retrieving the cars and rentals dictionaries as two separate variables
with open('data\input.json') as data_file:
    data_details = json.load(data_file)


car_data = data_details["cars"]
rental_data = data_details["rentals"]


''' looping through to find the price of each car_id
    We retrieve the dictionary in cars which has the same id as the car_id from rentals
    here we also initialising the variables to be able to access Rental_functions class
    we use this class to call functions and append the answers array
'''
for i in range(len(rental_data)):
    dictionary = list(filter(lambda car_data: car_data['id'] == rental_data[i]["car_id"], car_data))[0]
    rentals = Rental_functions(dictionary,rental_data[i])
    answer.append({"id": rentals.id, "price": int(rentals.price())})


#writing the result in a JSON file called output
with open('data\output.json', 'w') as outfile:
    json.dump({'rentals': answer}, outfile, indent=2)
