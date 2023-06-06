'''
* 5.3에서 못 푼 문제 
1. https://school.programmers.co.kr/learn/courses/30/lessons/12945 
피보나치 수
재귀함수로 해결X 영상을 보고 풀어보자
'''
# ver 1
def fib(num):
    # 2. 탈출 조건
    if num < 2:
        return num

    # 1. 기본 동작
    return fib(num - 1) + fib(num - 2)
num = int(input())
print(fib(num))

''' 
DP란? -> 기억하며 풀기
'''
# ver 2
def fib(num):
    # 2. 탈출 조건
    if dp[num] == -1 : # 한번도 연산된 적이 없다면
        dp[num] = fib(num - 1) + fib(num - 2)

    # 1. 기본 동작
    return dp[num]
num = int(input())
dp = [-1] * 100
dp[0] = 0
dp[1] = 1
print(fib(num))


# ver 3 (재귀함수 없이 DP배열만 사용)
num = int(input())
dp = [0] * 100
dp[1] = 1
for i in range(2, num + 1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[num])
