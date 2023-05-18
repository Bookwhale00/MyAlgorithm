# ㅡㅡㅡㅡㅡ 2. https://school.programmers.co.kr/learn/courses/30/lessons/120813 ㅡㅡㅡㅡㅡ
# 예전에 풀었던 문제

def solution(n):
    answer = [] # answer는 리스트
    numbers = list(range(n+1)) 
    # n+1의 범위만큼 수를 리스트로 만들어라
    for num in numbers : # numbers를 하나씩
        if num % 2 == 1: 
            # 2로 나눠서 나머지 = 1이면 홀수
            answer.append(num) 
            # 홀수면 answer에 넣고
        else:
            pass # 건너뛸 때는 continue
            # 아니면 지나가라.
            # else문 자체가 없어도 ok! 
    return answer