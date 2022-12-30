from datetime import datetime
class Rental_functions:
    ''' NEWEST UPDATE: 
        1. adding the actions function
        2. this is called in main.py as .actions()


        Attributes
        -------------
        rental_data: dict
        id: int
        start_date: str
        end_date: str
        price_per_km: int
        price_per_day: int
        distance: int
    '''

    def __init__(self,dictionary,rental_data):
        self.rental_data = rental_data
        self.id = rental_data["id"]
        self.start_date = rental_data["start_date"]
        self.end_date = rental_data["end_date"]
        self.price_per_km = dictionary["price_per_km"]
        self.price_per_day = dictionary["price_per_day"]
        self.distance = rental_data["distance"]



    def price(self):
        #   INPUT: discounted price (based on days and price per day), distance, price per km
        #   OUTPUT: total price

        ''' calculating the price based on formula given in READ.me '''

        return int(self.discounts()) + (self.distance* self.price_per_km)



    def days(self):
        #   INPUT: start date, end date
        #   OUTPUT: number of days difference

        ''' calculating the number of days difference between the start date and end date
            initialising the current format of the date
            using the datetime library to find the difference in days
            use this and price per day to calculate'''
        
        date = "%Y-%m-%d"
        a = datetime.strptime(self.start_date, date)
        b = datetime.strptime(self.end_date, date)
        delta = b - a
        return delta.days + 1
    


    def discounts(self):
        #   INPUT: number of days, price per day
        #   OUTPUT: discounted price (not based on distance and km yet)

        ''' calculating the price based of the number of days (call the days function)
            first we see what formula we need to use based on the days (from READ.me file)
            next find the difference between the number of days and the last threshold ie 10,4 or 1
            use this and price per day to calculate'''
        
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
    


    def commission(self):
        #   INPUT: total price, number of days
        #   OUTPUT: dictionary of insurance_fee, assistance fee and druvy_fee

        ''' calculating the commission as 30% of the total price
            finding the difference fees based on the instructions in READ.me
            creating a dictionary for these values'''
        
        commission = 0.3*self.price()
        insurance_fee = commission*0.5
        assistance_fee = self.days()*100
        drivy_fee = commission - insurance_fee - assistance_fee
        return {"insurance_fee": int(insurance_fee),"assistance_fee": int(assistance_fee),"drivy_fee": int(drivy_fee)}
        


    def actions(self):
        #   INPUT: total price, commission
        #   OUTPUT: array of dictionaries

        ''' create an array for each owner, debit or credit and the price assigned
            calculates the owner credit from the total price - sum of all values in the commission dictionary
            map these out into the dictionary structure wanted'''
        
        actions = [["driver", "debit", self.price()],
        ["owner", "credit", self.price() -sum(self.commission().values())],
        ["insurance", "credit",self.commission()["insurance_fee"]],
        ["assistance", "credit", self.commission()["assistance_fee"]],
        ["drivy", "credit", self.commission()["drivy_fee"]]]
        keys = ["who","type","amount"]
        action = [dict(zip(keys,i)) for i in actions]
        return action
    
