from datetime import datetime
import Discount
import Commission
class Rental:
    def __init__(self,car_data,rental_data):
        #retrieving the dictionary in cars which has the same id as the car_id from rentals
        dictionary = list(filter(lambda car_data: car_data['id'] == rental_data["car_id"], car_data))[0]
        self.id = rental_data["id"]
        #finding the next set of values needed in the price formula
        self.price_per_km = dictionary["price_per_km"]
        self.price_per_day = dictionary["price_per_day"]
        self.distance = rental_data["distance"]
        self.numberofdays = Rental.count_days(rental_data["start_date"],rental_data["end_date"])
        #calculating the price
        self.discounted_rental = Discount.Rental_discount(self.numberofdays,self.price_per_day)
        self.price = int(self.discounted_rental.discount) + (self.distance* self.price_per_km)
        commission_rental = Commission.Rental_commission(self.numberofdays,self.price)
        self.commission = commission_rental.commission

    def count_days(start_date,end_date):
        date = "%Y-%m-%d"
        a = datetime.strptime(start_date, date)
        b = datetime.strptime(end_date, date)
        delta = b - a
        return delta.days + 1