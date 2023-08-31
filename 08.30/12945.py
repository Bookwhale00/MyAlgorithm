'''
https://school.programmers.co.kr/learn/courses/30/lessons/12945
피보나치 수

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
-> 0 1 1 2 3 5 8 ...

예상 풀이
1. 재귀 안쓰고 해보기
'''

def solution(n):

    MOD = 1234567 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # 조건이 n = 2이상이라서 없어도 됨
    
    a = 0
    b = 1
    for _ in range(2, n+1):
        a, b = b % MOD, (a + b) % MOD
        # a = b
        # b = a + b 
        # 로 하면 X 위에서 이미 a = b라고 했기 때문에 아래 연산에서 b = b + b가 되버린다.
        print(b)
    return b

n = 47
solution(n)

'''
테스트 7~14 실패
n이 매우 큰 경우 n번째 피보나치 수는 언어가 표현할 수 있는 자료형의 범위를 넘어가서 오버플로우가 발생한다. 
-> 각 연산마다 % 연산 사용해서 오버플로우를 방지할 것
'''