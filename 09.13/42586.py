'''
https://school.programmers.co.kr/learn/courses/30/lessons/42586
기능개발

progresses -> 작업의 진도
speeds -> 각 작업의 개발 속도
*뒤에 있는 기능은 앞의 기능이 배포될 때 함께 배포된다. 

각 배포마다 몇 개의 기능이 배포되는지 return 

계획
1. 각 작업마다 며칠 걸려야 100% 되는지 배열로 만들기
1-1. day [] - 100 - progresses[i] / speeds[i] 
* 나머지가 0이 아니면 +1 -> 그냥 올림하자

2. [7, 3, 9] -> [2, 1]로 만들기
2-1. 뒤의 값이 현재 값보다 작은 동안 count해서 append하기 
2-2. 앞에서부터 빼야하니까 덱(큐) 사용
'''
import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days_list = []

    # 1
    for progress, speed in zip(progresses, speeds):
        days = math.ceil((100 - progress) / speed)
        days_list.append(days)

    print(days_list)

    # 2
    days_queue = deque(days_list)  

    print(days_queue)

    while days_queue: # 큐 안에 값이 모두 제거될때까지
        current = days_queue.popleft()
        count = 1 
        while days_queue and days_queue[0] <= current:
            count += 1
            days_queue.popleft()

        print(days_queue)
            
        answer.append(count)

    print(answer)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
solution(progresses, speeds)
