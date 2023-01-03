
class Rail:

    def __init__(self, num_of_cities, sitting_places, requests):
        if num_of_cities < 1 or num_of_cities > 60000:
            raise Exception("Incorrect amount of cities")
        self.num_of_cities = num_of_cities

        if num_of_cities < 1 or num_of_cities > 60000:
            raise Exception("Incorrect amount of sitting places")
        self.sitting_places = sitting_places

        if num_of_cities < 1 or num_of_cities > 60000:
            raise Exception("Incorrect amount of requests")
        self.requests = requests




