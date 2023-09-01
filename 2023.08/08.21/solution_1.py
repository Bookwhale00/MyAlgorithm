'''
https://school.programmers.co.kr/learn/courses/30/lessons/82612
부족한 금액 계산하기

놀이기구를 n번째 이용하면 원래 이용료의 n배를 받는다.
ex) 1번 100원, 2번 200원, 3번 300원...
놀이기구를 count번 타면 현재 가지고 있는 금액에서 얼마가 모자라는지 return
+ 금액이 부족하지 않으면 0 return 

예상 풀이
1. range(a, b, step) 사용 (08.16 1번 문제 참고)
2. list로 형변환
3. 리스트 합산
4. answer = 0으로 초기화
5. if 소지 금액이 모자라면 모자란 금액 반환

실제 풀이
그대로 ok
'''

def solution(price, money, count):
    answer = 0

    play_attraction = list(range(price, price*count+1, price))
    need_money = sum(play_attraction)

    if need_money > money:
        answer += need_money - money

    print(f"부족한 금액 : {answer}")

    return answer

price = 3
money = 20
count = 4
solution(price, money, count)