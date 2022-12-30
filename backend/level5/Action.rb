class Rental_action
    #decided to add options to the actions class as a lot of variables needed, overlap.
    attr_reader :actions, :options
    def initialize(price,commission,option_data,rental_data,numberofdays) 
        #find all the dictionaries with matching ids and loop through these and add the 'tyoe' value to an array
        @dictionary_options = option_data.select {|k| k["rental_id"] == rental_data["id"]}
        #initialising arrays so we can build up the options, owners as we go
        @options = []
        @owner = []
        @getaround = []
        @dictionary_options.each {|option| Rental_action.options(option["type"],numberofdays,@options,@owner,@getaround)}
        @actions = Rental_action.find_actions(price.to_i,commission,@owner,@getaround)
    end
    #changes the presentation of the json file
    def self.find_actions(price,commission,owner,drivy)
        #mapping the new values to the new dictionaries format
        actions = [
            ["driver", "debit", price + owner.sum + drivy.sum],
            ["owner", "credit", price-commission.sum{|s,t| t} + owner.sum],
            ["insurance", "credit", commission[:insurance_fee]],
            ["assistance", "credit", commission[:assistance_fee]],
            ["drivy", "credit", commission[:drivy_fee]+ drivy.sum]].map {|who,type,amount| {"who" =>who, "type"=> type, "amount"=> amount}}
        return actions

    end

    def self.options(type,days,arr,owner,getaround)
        #set dictionaries for the price and section of each option
        fees = {"gps"=> 500, "baby_seat"=> 200, "additional_insurance" => 1000}
        owned = {"gps"=> "owner", "baby_seat"=> "owner", "additional_insurance"=> "getaround"}
        price = fees[type] * days
        #accumulating the prices
        if owned[type] == "owner"
            owner.push(price)
        elsif owned[type] == "getaround"
            getaround.push(price)
        end
        arr.push(type)
    end
end