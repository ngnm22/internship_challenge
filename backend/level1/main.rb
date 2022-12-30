require "json"
require "date"
require_relative "Rental"
# initialising the array that is going to be written at the answer in the output
answer = []

# opening the input file and retrieving the cars and rentals dictionaries as two separate variables
file = File.read('data\input.json')
data_details = JSON.parse(file)
car_data = data_details["cars"]
rental_data = data_details["rentals"]

# looping through to find the price of each car_id
for i in 0...rental_data.length() do
    rentals = Rental.new(car_data,rental_data[i])
    #appending the answers array for the result of this loop
    answer.push({"id" => rentals.id, "price"=> rentals.price.to_i})
end

#writing the result in a JSON file called output
File.write('data\output.json', JSON.pretty_generate({'rentals': answer}))

