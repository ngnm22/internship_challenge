from datetime import datetime
class Rental_price:
    def __init__(self,car_data,rental_data):
        #retrieving the dictionary in cars which has the same id as the car_id from rentals
        dictionary = list(filter(lambda car_data: car_data['id'] == rental_data["car_id"], car_data))[0]
        print(dictionary)
        self.id = rental_data["id"]
        #finding the next set of values needed in the price formula
        self.price_per_km = dictionary["price_per_km"]
        self.price_per_day = dictionary["price_per_day"]
        self.distance = rental_data["distance"]
        self.numberofdays = Rental_price.count_days(rental_data["start_date"],rental_data["end_date"])
        #calculating the price
        self.price = (self.numberofdays*self.price_per_day) + (self.distance* self.price_per_km)

    def count_days(start_date,end_date):
        date = "%Y-%m-%d"
        a = datetime.strptime(start_date, date)
        b = datetime.strptime(end_date, date)
        delta = b - a
        return delta.days + 1