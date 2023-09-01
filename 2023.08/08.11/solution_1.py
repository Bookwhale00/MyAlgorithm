'''
https://school.programmers.co.kr/learn/courses/30/lessons/12912
두 정수 사이의 합

예상 풀이
1. 중복허용x -> 집합사용
2. 주어진 값 a에서 b까지 집합으로 묶어서 값 전부 더하기

실제 풀이
1. a < b일때는 되지만 a > b일때는 빈 집합이 반환됨
-> 조건문 사용

'''

def solution(a, b):
    answer = 0

    if a <= b:
        result = set(range(a, b+1))
    else:
        result = set(range(b, a+1))

    answer = sum(result)
    
    print(f"범위 내 정수 : {result}")
    print(f"합 : {answer}")
    
    return answer

a = 3
b = 3
solution(a, b)