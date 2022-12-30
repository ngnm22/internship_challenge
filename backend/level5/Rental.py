from datetime import datetime
class Rental_functions:
    def __init__(self,dictionary,rental_data,option_data):
        self.option_data = option_data
        self.rental_data = rental_data
        self.id = rental_data["id"]
        self.start_date = rental_data["start_date"]
        self.end_date = rental_data["end_date"]
        #finding the next set of values needed in the price formula
        self.price_per_km = dictionary["price_per_km"]
        self.price_per_day = dictionary["price_per_day"]
        self.distance = rental_data["distance"]
        self.new_action = self.actions()



    def price(self):
        #calculating the price
        return int(self.discounts()) + (self.distance* self.price_per_km)



    def days(self):
        date = "%Y-%m-%d"
        a = datetime.strptime(self.start_date, date)
        b = datetime.strptime(self.end_date, date)
        delta = b - a
        return delta.days + 1
    


    def discounts(self):
        #calculating the price based of the number of days
        #first we see what formula we need to use based on the days
        #next find the difference between the last threshold ie 10,4 or 1
        #add this to a fixed price created
        if self.days() > 10:
            between = self.days()-10
            result = between*(self.price_per_day*0.5) + 6*(self.price_per_day*0.7) + 3*(self.price_per_day*0.9) + self.price_per_day
        elif self.days() > 4:
            between = self.days()-4
            result = between*(self.price_per_day*0.7) + 3*(self.price_per_day*0.9) + self.price_per_day
        elif self.days() > 1:
            between = self.days()-1
            result = between*(self.price_per_day*0.9) + self.price_per_day
        else:
            result = self.price_per_day
        return result
    


    #calculates the commission based on the given formulas
    def commission(self):
        commission = 0.3*self.price()
        insurance_fee = commission*0.5
        assistance_fee = self.days()*100
        drivy_fee = commission - insurance_fee - assistance_fee
        return {"insurance_fee": int(insurance_fee),"assistance_fee": int(assistance_fee),"drivy_fee": int(drivy_fee)}
        


    #changes the presentation of the json file
    def actions(self):
        actions = [["driver", "debit", self.price()],
        ["owner", "credit", self.price() -sum(self.commission().values())],
        ["insurance", "credit",self.commission()["insurance_fee"]],
        ["assistance", "credit", self.commission()["assistance_fee"]],
        ["drivy", "credit", self.commission()["drivy_fee"]]]
        keys = ["who","type","amount"]
        action = [dict(zip(keys,i)) for i in actions]
        return action
    


    def options(self):
        #retrieving the dictionary in options which has the same id as the car_id from rentals
        dictionary_options = list(filter(lambda x: x['rental_id'] == self.rental_data["id"], self.option_data))
        #initialising arrays so we can build up the options, owners as we go
        option = []
        #set dictionaries for the price and section of each option
        fees = {"gps": 500, "baby_seat": 200, "additional_insurance": 1000}
        owned = {"gps": "owner", "baby_seat": "owner", "additional_insurance": "getaround"}
        for i in dictionary_options:
            type = i["type"]
            price = fees[type] * self.days()
            #accumulating the prices
            self.new_action[0]["amount"] += price
            if owned[type] == "owner":
                self.new_action[1]["amount"] += price
            elif owned[type] == "getaround":
                self.new_action[4]["amount"] += price
            option.append(type)
        return option
