'''
https://school.programmers.co.kr/learn/courses/30/lessons/86051
없는 숫자 더하기

0-9
numbers 리스트에 없는 숫자를 모두 더한 수 return

예상 풀이
1. 비교할 리스트 origin 생성 (0-9까지 다 있는 리스트)
2. numbers 오름차순 정렬
3. origin - numbers 차집합 구하기 (순서 중요하지 않으니까)
4. 차집합 합산

실제 풀이
1. 그대로
2. 오름차순 정렬 안하고 filter(lambda문 사용)
'''

def solution(numbers):
    answer = 0
    # 1
    origin = [0,1,2,3,4,5,6,7,8,9]

    # 2
    result = list(filter(lambda x: x not in numbers, origin))

    # 3
    answer = sum(result)

    print(answer)
    return answer

numbers = [5,8,4,0,6,7,9]
solution(numbers)

# 신기한 답안
def solution(numbers):
    return 45 - sum(numbers)