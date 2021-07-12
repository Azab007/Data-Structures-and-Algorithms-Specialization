# python3
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[]] * self.bucket_count
        self.solution = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, ind, query):
        for i in self.elems[ind]:
            if i == query.s:          
                self.solution.append('yes')
                return True
        self.solution.append('no')
        return False
    def write_search_result1(self, ind, query):
        for i, s in enumerate(self.elems[ind]):
            if s == query.s:          
                return i
        return -1
    def write_chain(self, chain):
        self.solution.append(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems[query.ind]))
        else:
            ind = self._hash_func(query.s)
            if query.type == 'find':
                self.write_search_result(ind, query)
            elif query.type == 'add':
                if self.write_search_result1(ind, query) == -1:
                    self.elems[ind].append(query.s)
            else:
                index = self.write_search_result1(ind, query)
                if index != -1:
                    self.elems[ind].pop(index)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
    for i in proc.solution:
        print(i)
