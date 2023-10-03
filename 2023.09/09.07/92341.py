'''
https://school.programmers.co.kr/learn/courses/30/lessons/92341
주차 요금 계산

주차장의 요금표
입차, 출차 기록
-> 차량 별 주차 요금 계산

* 입차 후 출차 내역이 없으면 23:59에 출차된 것으로 간주

fees
[기본시간(분), 기본요금, 단위시간(분), 단위요금]

records
["시간 차량번호 IN", "시간 차량번호 OUT"]

요금 계산식
= 기본요금 + [(누적 주차 시간 - 기본시간) / 단위시간] * 단위요금

계획
1. 차량 별 누적주차시간을 구하기 (딕셔너리)
1-1. 짝맞추기? 출차가 없으면 마지막에 23:59 
1-2. 시간의 차이를 분단위로 반환하기 위해 datetime사용
2. 차량 별로 계산식 적용해서 값 구하기
3. 최종 결과는 차 번호 오름차순으로 정렬되어야 함
'''
from datetime import datetime
import math

def solution(fees, records):
    
    parking_time = {}
    temp = {}

    for i in records:
        print(f"기록 : {i}")
        time = i[:5]
        car = i[6:10]
        inout = i[11:]

        if car not in parking_time:
            parking_time[car] = 0

        print(f"자동차 별 누적 주차 시간 : {parking_time}")

        if inout == "IN":
            temp[car] = time
            print(f"임시 : {temp}")

        elif inout == "OUT":
            parking_time[car] += time_difference(temp[car], time)
            del temp[car]

            print(f"임시 : {temp}")
            print(f"자동차 별 누적 주차 시간 : {parking_time}")

    # 다 처리했는데 temp에 값이 남아있으면 그 차는 OUT이 없었다는 뜻 -> 23:59 강제 출차
    for car, in_time in temp.items():
        print(f"출차 안 한 차 : {car}")
        print(f"출차 안 한 차가 들어온 시간 : {in_time}")
        parking_time[car] += time_difference(in_time, "23:59")

    print(f"최종 자동차 별 누적 주차 시간 : {parking_time}")

    return calculate_fees(parking_time, fees)

# 출차 - 입차 시간 계산하는 함수
def time_difference(start, end):
    format_str = "%H:%M" 
    start_time = datetime.strptime(start, format_str) # 문자열->시간으로 변환
    end_time = datetime.strptime(end, format_str)

    result = end_time - start_time
    return int(result.total_seconds() // 60) # 분 단위

# 최종적으로 비용 계산하는 함수
# fees
# [기본시간(분), 기본요금, 단위시간(분), 단위요금]
# 요금 계산식
# = 기본요금 + [(누적 주차 시간 - 기본시간) / 단위시간] * 단위요금
def calculate_fees(parking_time, fees):
    answer = []
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    for car, time in sorted(parking_time.items()):
        if time <= base_time: # 주차시간이 기본시간보다 작거나 같으면
            answer.append(base_fee) # 기본요금
        else: # 주차시간이 기본시간을 오버하면 (계산식 사용)
            fee = base_fee + math.ceil((time - base_time) / unit_time) * unit_fee
            answer.append(fee)

    print(f"자동차 별 최종 주차 비용 : {answer}")
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees, records)

'''
334분 -> 14240원으로 나옴 
* 조건 "초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.""
-> import math해서 math.ceil사용
열심히 했지만 1점
'''