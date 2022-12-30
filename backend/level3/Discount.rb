class Rental_discount 
    attr_reader :discount

    def initialize(days,price_per_day)
        @days = days
        @price_per_day = price_per_day
        @discount = Rental_discount.calculate_discounts(@days,@price_per_day)
    end
    
    def self.calculate_discounts(days,price_per_day)
        #calculating the price based of the number of days
        #first we see what formula we need to use based on the days
        #next find the difference between the last threshold ie 10,4 or 1
        #add this to a fixed price created
        if days > 10
            between = days-10
            result = between*(price_per_day*0.5) + 6*(price_per_day*0.7) + 3*(price_per_day*0.9) + price_per_day
        elsif days > 4
            between = days-4
            result = between*(price_per_day*0.7) + 3*(price_per_day*0.9) + price_per_day
        elsif days > 1
            between = days-1
            result = between*(price_per_day*0.9) + price_per_day
        else
            result = price_per_day
        return result
        end
    end
end