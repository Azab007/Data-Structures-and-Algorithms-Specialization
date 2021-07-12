# python3
def compute_min_refills(Fulldistance, tank, stops):
    refills = 0
    cur_refill = 0
    dis = 0
    stops.insert(0, int(0))
    stops.append(Fulldistance)
    while dis < Fulldistance:
        last_refill = cur_refill
        while dis < Fulldistance and (stops[cur_refill+1] - stops[last_refill]) <= tank:
            cur_refill+=1
            dis = stops[cur_refill]
        if cur_refill == last_refill:
            return -1
        if dis < Fulldistance:
            refills+=1
    return refills
d = int(input())   
m = int(input())
_ = int(input())
stops = list(map(int, input().split()))
print(compute_min_refills(d, m, stops))
