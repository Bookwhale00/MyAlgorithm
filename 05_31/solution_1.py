"""
https://school.programmers.co.kr/learn/courses/30/lessons/120889
삼각형의 완성조건 (1)
: 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다.
sides = [1, 2, 3]
삼각형을 만들 수 있다면 
= 가장 큰 값이 다른 값들의 합보다 작다면 -> 1
아니라면 2를 return
"""


def solution(sides):
    answer = 0
    max_num = max(sides)  # 최대값 구해서
    sides.remove(max_num)  # 리스트에서 제거하고
    sum_num = sum(sides)  # 남은 값의 합을 구함

    if max_num < sum_num:
        answer = 1
    else:
        answer = 2

    print(answer)
    return answer


sides = [199, 72, 222]
solution(sides)
