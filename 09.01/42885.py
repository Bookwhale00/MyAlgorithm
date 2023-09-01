'''
https://school.programmers.co.kr/learn/courses/30/lessons/42885
구명보트

탐욕법?
-> 현재 상황에서 가장 좋아보이는 선택을 하면서 해답을 찾는 방법

구명보트는 한번에 2명씩 밖에 탈 수 없고 무게제한도 있음
최대한 적은 구명보트로 모든 사람을 구출하려고 할 때 필요한 최소 구명보트 갯수를 return 

계획
1. people 오름차순 정렬
2. 앞에서부터 pop해서 합이 limit를 넘어서면 멈추고 answer += 1
'''
# from collections import deque

# def solution(people, limit):
#     answer = 0
#     weight_sum = 0
#     # 1
#     people.sort()
#     people_deque = deque(people)
#     print(f"먼저 오름차순 정렬 : {people_deque}")

#     # 2
#     while people_deque:
#         weight = people_deque.popleft()
#         weight_sum += weight
#         print(f"{limit}넘었나? : {weight_sum}")

#         if weight_sum > limit:
#             answer += 1
#             print(f"보트 {answer}대 사용함")
#             weight_sum = weight
#             print(f"다음 보트에 이미 탄 무게 : {weight_sum}")
#             print(f"무인도에 남은 사람 : {people_deque}")

#     if weight_sum > 0:
#         answer += 1
#         print(f"보트 {answer}대 사용함")
        
#     print(f"최종 사용한 보트 {answer}")
#     return answer

# people = [70, 50, 80, 50]
# limit = 100
# solution(people, limit)

'''
정확성 2, 8, 14, 15 효율성 4, 5 빼고 다 실패

가장 가벼운 사람과 가장 무거운 사람을 같이 보내야 하는데 둘을 합했을 때 limit를 넘어간다면 가장 무거운 사람을 먼저 보내야 한다고 함.
-> Two Pointers 기법 (단순 arr[0] + arr[-1] 과는 다르다. )

1. 일단 오름차순 정렬
2. 배열의 양 끝 값을 더해서 limit를 초과하면 오른쪽 끝만 보내고 초과하지 않으면 둘 다 보내기
3. 결과에 따라 포인터 이동 (pop 안해도됨!)
'''

def solution(people, limit):
    answer = 0
    # 1
    people.sort()
    
    # 인덱스로 포인터 설정
    left = 0
    right = len(people) - 1

    while left <= right: 
        weight_sum = people[left] + people[right]
        print(f"현재 포인터 : {left}, {right}")
        print(f"두 사람의 무게 : {weight_sum}")
        
        if weight_sum > limit: # 제한 초과
            answer += 1
            right -= 1
            print("더 무거운 사람만 타고")
            print(f"{answer}번 보트 출발")

        elif weight_sum <= limit:
            answer += 1
            left += 1
            right -= 1
            print("두 사람 다 타고")
            print(f"{answer}번 보트 출발")

    print(f"총 사용된 보트 갯수 : {answer}")
    return answer

people = [70, 80, 50]
limit = 100
solution(people, limit)