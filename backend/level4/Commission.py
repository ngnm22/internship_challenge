class Rental_commission:
    def __init__(self,numberofdays,price):
        self.commission = Rental_commission.calculate_commission(price,numberofdays)

    #calculates the commission based on the given formulas
    def calculate_commission(price,days):
        commission = 0.3*price
        insurance_fee = commission*0.5
        assistance_fee = days*100
        drivy_fee = commission - insurance_fee - assistance_fee
        return {"insurance_fee": int(insurance_fee),"assistance_fee": int(assistance_fee),"drivy_fee": int(drivy_fee)}