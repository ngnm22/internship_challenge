class Rental_commission
    attr_reader :commission
    def initialize(numberofdays,price) 
        @commission = Rental_commission.calculate_commission(price,numberofdays)
    end

    #calculates the commission based on the given formulas
    def self.calculate_commission(price,days)
        commission = 0.3*price
        insurance_fee = commission*0.5
        assistance_fee = days*100
        drivy_fee = commission - insurance_fee - assistance_fee
        return {"insurance_fee": insurance_fee.to_i,"assistance_fee": assistance_fee,"drivy_fee": drivy_fee.to_i}
    end
end