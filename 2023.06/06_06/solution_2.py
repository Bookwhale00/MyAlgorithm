"""
https://school.programmers.co.kr/learn/courses/30/lessons/120854
배열원소의 길이
"""


def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    print(answer)
    return answer


strlist = ["We", "are", "the", "world!"]
solution(strlist)
