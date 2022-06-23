from math import ceil
from collections import defaultdict


def get_time(time):
    h, m = map(int, time.split(':'))
    return h*60 + m


def calc_fee(time, b_time, b_cost, s_time, s_cost):
    extra_time = max(0, time - b_time)
    extra_fee = ceil(extra_time / s_time) * s_cost
    return b_cost + extra_fee


def solution(fees, records):
    answer = []
    p_record = defaultdict(int)
    p_lot = dict()
    b_time, b_cost, s_time, s_cost = fees

    for record in records:
        event_time, car_num, in_out = record.split()
        time = get_time(event_time)

        if in_out == 'IN':
            p_lot[car_num] = time
        else:
            p_record[car_num] += (time - p_lot[car_num])
            del p_lot[car_num]  # 지워버리는 건 생각도 못했다.

    for car in p_lot:  # 남은 차
        p_record[car] += (get_time('23:59') - p_lot[car])

    for car in p_record:
        fee = calc_fee(p_record[car], b_time, b_cost, s_time, s_cost)
        answer.append([car, fee])
    answer.sort()
    answer = [x[1] for x in answer]

    return answer
