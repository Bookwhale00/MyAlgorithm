"""
https://school.programmers.co.kr/learn/courses/30/lessons/120898
편지
한 글자 당 2cm
편지지의 최소 가로길이를 return
공백도 하나의 문자로 취급
"""


def solution(message):
    num = len(message)

    answer = num * 2
    print(answer)
    return answer


message = "I love you~"
solution(message)
