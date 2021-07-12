# python3
import heapq

class Worker:
    def __init__(self, id, time=0):
        self.id = id
        self.time = time

    def __lt__(self, other):
        if self.time == other.time:
            return self.id < other.id
        return self.time < other.time

    def __gt__(self, other):
        if self.time == other.time:
            return self.id > other.id
        return self.time > other.time

class Job:
	def read_data(self):
		self.n_workers, m = map(int, input().split())
		self.jobs = list(map(int, input().split()))
		assert m == len(self.jobs)

	def response(self):
		for i in range(len(self.jobs)):
			print(self.ass_workers[i], self.start_times[i]) 

	def assign_jobs(self):
		# TODO: replace this code with a faster algorithm.		
		self.ass_workers = [None] * len(self.jobs)
		self.start_times = [None] * len(self.jobs)
		workers = [Worker(i) for i in range(self.n_workers)]
		for i in range(len(self.jobs)):
			worker = heapq.heappop(workers)
			self.ass_workers[i] = worker.id
			self.start_times[i] = worker.time
			worker.time += self.jobs[i]
			heapq.heappush(workers, worker)

	def solve(self):
		self.read_data()
		self.assign_jobs()
		self.response()

if __name__ == '__main__':
	job_queue = Job()
	job_queue.solve()
