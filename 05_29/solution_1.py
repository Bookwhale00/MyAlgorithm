"""
https://school.programmers.co.kr/learn/courses/30/lessons/120831
짝수의 합
"""


def solution(n):
    answer = 0
    for n in range(n + 1):
        if n % 2 == 0:
            answer += n
        else:
            pass
    return answer
