
class Rail:

    def __init__(self, num_of_cities, sitting_places, requests):
        if num_of_cities < 1 or num_of_cities > 60000:
            raise Exception("Incorrect amount of cities")
        self.__num_of_cities = num_of_cities

        if num_of_cities < 1 or num_of_cities > 60000:
            raise Exception("Incorrect amount of sitting places")
        self.__sitting_places = sitting_places

        if num_of_cities < 1 or num_of_cities > 60000:
            raise Exception("Incorrect amount of requests")
        self.__requests = requests

        # destinations includes starting station, destination station, number of passengers
        self.__destinations = []

    # adding all requests to database
    def add_requests(self):
        for i in range(self.__requests):

            request = [int(e) for e in input("request number "+str(i)+" : ").split(" ")]

            # validation of request
            if len(request) != 3:
                raise Exception("Incorrect length of request")
            else:
                if request[0] < 1 or request[0] >= request[1]:
                    raise Exception("Incorrect start station")
                elif request[1] > request[2]:
                    raise Exception("Incorrect destination station")
                elif request[2] > self.__sitting_places:
                    raise Exception("Incorrect numbers of requests for seats")

            # adding single request to database
            self.__destinations.append(request)


    def check_request(self):
        pass
    def accept_request(self):
        pass
    def update_seats(self):
        pass


def seats_reservation_system(rail):
    rail.add_requests()




inf = [int(e) for e in input("cities | sitting places | requests : ").split(" ")]

rail_1 = Rail(inf[0], inf[1], inf[2])

seats_reservation_system(rail_1)




