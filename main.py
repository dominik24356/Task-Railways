import os

class Rail:

    def __init__(self, num_of_cities, sitting_places, requests, file):

        if num_of_cities < 1 or num_of_cities > 60000:
            raise Exception("Incorrect amount of cities")
        self.__num_of_cities = num_of_cities

        if sitting_places < 1 or sitting_places > 60000:
            raise Exception("Incorrect amount of sitting places")
        self.__sitting_places = sitting_places

        if requests < 1 or requests > 60000:
            raise Exception("Incorrect amount of requests")
        self.__requests = requests

        # destinations includes starting station, destination station, number of passengers
        self.__destinations = []

        self.__people_inside = 0

        self.__requests_in_progress = []

        self.__file = file

    def get_number_of_cities(self):
        return self.__num_of_cities

    def get_number_of_requests(self):
        return self.__requests

    # adding all requests to database
    def add_requests(self):
        for i in range(self.__requests):

            request = [int(e) for e in self.__file.readline().split(" ")]

            # validation of request
            if len(request) != 3:
                raise Exception("Incorrect length of request")
            else:
                if request[0] < 1 or request[0] >= request[1]:
                    raise Exception("Incorrect start station")
                elif request[1] > self.__num_of_cities:
                    raise Exception("Incorrect destination station")
                elif 1 > request[2] or request[2] > self.__sitting_places:
                    raise Exception("Incorrect numbers of requests for seats")

            # adding single request to database
            self.__destinations.append(request)

    def entry_permit(self, request, current_station):
        if self.__destinations[request][0] == current_station and self.__destinations[request][2]+self.__people_inside \
                <= self.__sitting_places:
            return True
        else:
            return False

    def accept_request(self, request):
        self.__people_inside += self.__destinations[request][2]
        self.__requests_in_progress.append(request)

    def update_seats(self, current_station):
        for e in self.__requests_in_progress:
            if self.__destinations[e][1] == current_station:
                self.__people_inside -= self.__destinations[e][2]


def seats_reservation_system(rail):
    requests_answer = ["N"] * rail.get_number_of_requests()

    rail.add_requests()

    for s in range(1, rail.get_number_of_cities()+1):
        rail.update_seats(s)
        for r in range(rail.get_number_of_requests()):
            if rail.entry_permit(r, s):
                rail.accept_request(r)
                requests_answer[r] = "T"

    result_output = ""
    for i in requests_answer:
        result_output += i+"\n"
    return result_output


folder_path = "inputs"

list_of_files = os.listdir(folder_path)


count_file = 1
for file_name in list_of_files:
    with open("inputs/"+file_name, 'r') as f:
        f_content = f.readline()
        inf = [int(e) for e in f_content.split(" ")]
        rail_1 = Rail(inf[0], inf[1], inf[2], f)

        with open("outputs/output"+str(count_file)+".txt", 'w') as output_file:
            output_file.write(seats_reservation_system(rail_1))

        count_file += 1





