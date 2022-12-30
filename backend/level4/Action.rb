class Rental_action
    attr_reader :actions
    def initialize(price,commission) 
        @price = price
        @commission = commission
        @actions = Rental_action.find_actions(@price.to_i,@commission)
    end
    #changes the presentation of the json file
    def self.find_actions(price,commission)
        #mapping the new values to the new dictionaries format
        actions = [
            ["driver", "debit", price],
            ["owner", "credit", price-commission.sum{|s,t| t}],
            ["insurance", "credit", commission[:insurance_fee]],
            ["assistance", "credit", commission[:assistance_fee]],
            ["drivy", "credit", commission[:drivy_fee]]].map {|who,type,amount| {"who" =>who, "type"=> type, "amount"=> amount}}
        return actions
    end
end