# python3

from collections import namedtuple
from queue import Queue
Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finished_time = [] 
    def process(self, request):
        while self.finished_time:
            if self.finished_time[0] <= request.arrived_at:
                self.finished_time.pop(0)
            else:
                break
        if len(self.finished_time) == self.size:
            return Response(True, -1)
        if not self.finished_time:
            self.finished_time = [request.arrived_at + request.time_to_process]
            return Response(False, request.arrived_at)
        lst_element = self.finished_time[-1]
        self.finished_time.append(lst_element + request.time_to_process)
        return Response(False, lst_element)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
