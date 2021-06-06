import requests
import json
# Write your code here
class CoffeeMachine :
    # class attributes
    outlets = 0
    stock = None
    # def __init__(self, outlets) -> None:
    #     self.outlets = outlets

    def start(self, input_data):
        self.outlets = input_data['machine']['outlets']['count_n']
        total_quantity = input_data['machine']['total_items_quantity']
        beverages = input_data['machine']['beverages']
        self.stock = Stock(total_quantity)
        sol = []
        for beverage in beverages:
            result, msg = self.stock.available_check(beverages[beverage])
            if result:
                self.stock.deduct(beverages[beverage])
                result = f"{beverage} is prepared"
                sol.append({'result':result})
            else:
                result = f"{beverage} cannot be prepared because {msg}"
                sol.append({'result':result})
        return sol


class Stock:
    total_quantity = {}
    def __init__(self, total_quantity) -> None:
        self.total_quantity = total_quantity


    def deduct(self, requirements):
        for item in requirements:
            self.total_quantity[item] -= requirements[item]


    def available_check(self, requirements):
        """
            This method checks whether all the ingredients are present for that beverage.

        """
        for item in requirements:
            # print(item,'item')
            if self.total_quantity.get(item, None) is None:
                return False, f'{item} is not available'
            elif self.total_quantity[item] < requirements[item]:
                return False, f'item {item} is not sufficient'
        else:
            return True, 'Requirement Satisfied'




def test_working():
    f = open("test.json", "r")
    data = json.loads(f.read())
    f.close()
    for item in data:
        machine = CoffeeMachine()
        result = machine.start(item)
        print(result)


test_working()