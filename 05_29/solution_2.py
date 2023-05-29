"""
https://school.programmers.co.kr/learn/courses/30/lessons/120830
양꼬치
10인분 이상이면 -> n을 10으로 나눈 몫(서비스 음료)을 k에서 뺀 다음 계산한다.
10인분 미만이면 -> 그냥 제 값
"""


def solution(n, k):
    answer = 0
    if n >= 10:
        k = k - (n // 10)
        answer += (n * 12000) + (k * 2000)
        print(answer)
    else:
        answer += (n * 12000) + (k * 2000)
        print(answer)
    return answer


solution(10, 3)
