'''
아이스 아메리카노
https://school.programmers.co.kr/learn/courses/30/lessons/120819
'''

def solution(money):
    answer = [0, 0]
    cup = 5500
    while money >= cup:
            money -= cup
            answer[0] += 1
    else: 
          answer[1] = money
    return answer