require_relative "Discount"
require_relative "Commission"
class Rental_price
    attr_reader :id, :price, :commission
    def initialize(car_data,rental_data) 
        #retrieving the dictionary in cars which has the same id as the car_id from rentals
        @dictionary = car_data.select {|k| k["id"] == rental_data["car_id"]}[0]
        @id = rental_data["id"]
        #finding the next set of values needed in the price formula
        @price_per_km = @dictionary["price_per_km"]
        @price_per_day = @dictionary["price_per_day"]
        @distance = rental_data["distance"]
        @numberofdays = Rental_price.days(rental_data["start_date"],rental_data["end_date"])
        #calculating the price
        @discounted_rental = Rental_discount.new(@numberofdays,@price_per_day)
        @price = @discounted_rental.discount + (@distance* @price_per_km)
        @commission_rental = Rental_commission.new(@numberofdays,@price)
        @commission = @commission_rental.commission
    end
    # creating a function to find the number of days between the start and end date
    def self.days(start_date,end_date)
        a = Date.parse(start_date)
        b = Date.parse(end_date)
        delta = b - a
        return delta.to_i + 1
    end 
end