'''
https://school.programmers.co.kr/learn/courses/30/lessons/12940
최대공약수와 최대공배수

두 수를 입력받아서
[최대공약수, 최소공배수] 를 반환

예상 풀이
1. 최대공약수는 math.gcd 사용
2. 최소공배수는 유클리드 호제법 사용
* 유클리드 호제법 : (a * b // a, b의 최대공약수) = a, b의 최소공배수 

실제 풀이
그대로 ok
'''

import math

def solution(n, m):
    answer = []

    gcd = math.gcd(n, m)
    print(f"최대공약수 : {gcd}")

    lcm = n * m // gcd
    print(f"최소공배수 : {lcm}")

    answer = [gcd, lcm]
    print(f"결과 : {answer}")
    return answer

n = 3
m = 12
solution(n, m)
