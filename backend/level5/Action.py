class Rental_action:
    def __init__(self,price,commission):
        self.action = Rental_action.find_actions(price,commission)

    #changes the presentation of the json file
    def find_actions(price,commission):
        print(commission)
        actions = [["driver", "debit", price],
        ["owner", "credit", price-sum(commission.values())],
        ["insurance", "credit", commission["insurance_fee"]],
        ["assistance", "credit", commission["assistance_fee"]],
        ["drivy", "credit", commission["drivy_fee"]]]
        keys = ["who","type","amount"]
        action = [dict(zip(keys,i)) for i in actions]
        return action