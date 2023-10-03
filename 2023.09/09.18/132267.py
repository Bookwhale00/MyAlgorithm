'''
https://school.programmers.co.kr/learn/courses/30/lessons/132267
콜라 문제

콜라 2병을 가져다주면 1병을 받는다. 단 보유 중인 병이 2개 미만이면 받을 수 없다.

마트에 주는 병 수 a
a를 줬을 때, 마트한테 받을 수 있는 병 수 b
가지고 있는 빈 병의 개수 n

받을 수 있는 콜라의 병 수 return

계산식
quotient = n // a (몫)

n = n - (a * quotient) + (quotient * b)
'''

def solution(a, b, n):
    answer = 0
    print(f"처음에 {n}개 가지고 있었는데")

    while n >= a: # 가능한 만큼 마트에 병을 갖다줄 때까지 반복
        quotient = n // a
        answer += quotient * b # 마트에서 받을때마다 answer에 저장
        n = n - (a * quotient) + (quotient * b) # 가져다 준 병을 빼고 새롭게 얻은 병을 더해서 다시 n을 계산한다.
        print(f"{a * quotient}개 주고")
        print(f"{quotient * b}개 받아서")
        print(f"남은 병 {n}개")

    print(f"그래서 마트에서 총 {answer}개 받음")
    return answer

a = 3
b = 1
n = 20
solution(a, b, n)
