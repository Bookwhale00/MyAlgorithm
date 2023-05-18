'''
https://school.programmers.co.kr/learn/courses/30/lessons/181936
공배수
* 공배수 구하는 방법
1. for문 돌면서 범위 안의 값을 공배수를 구할 값으로 나눴을 때 둘 다 0이 나오면 list에 append하기.
2. math함수 사용. 두 수의 곱을 두 수의 최대공약수로 나누면 최소공배수를 구할 수 있다. range의 3번째 인자로 최소공배수를 넘어서(step) 공배수를 찾아서 list로 반환한다. 
'''

def solution(number, n, m):
    answer = 0
    # number가 n으로도 나눠지고 m으로도 나눠지면 n과 m의 공배수
    if number % n == 0 and number % m == 0:
        answer += 1
    print(answer)
    return answer

solution(60, 2, 3)
