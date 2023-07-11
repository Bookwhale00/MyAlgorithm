"""
https://school.programmers.co.kr/learn/courses/30/lessons/120826
특정 문자 제거하기
"""


def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    print(answer)
    return answer


my_string = "BCBdbe"
letter = "B"

solution(my_string, letter)
