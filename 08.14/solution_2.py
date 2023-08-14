'''
https://school.programmers.co.kr/learn/courses/30/lessons/12918?itm_content=course14743
문자열 다루기 기본

문자열 s의 길이가 4 혹은 6일 때 + 숫자로만 되어있을 때 
-> True 반환
아니면 
-> False 반환

예상 풀이
1. answer = False로 초기화
2. if and연산자로 조건묶어서 해당하면 True반환

실제 풀이
그대로 ok
'''

def solution(s):
    answer = False

    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True

    print(answer)
    return answer

s = "a234"
solution(s)