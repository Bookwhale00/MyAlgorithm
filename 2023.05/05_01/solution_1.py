# ㅡㅡㅡㅡㅡ 1. https://school.programmers.co.kr/learn/courses/30/lessons/120815 ㅡㅡㅡㅡㅡ
# 피자나눠먹기(2)
import math

def solution(n):
    # n과 6의 최소공배수  유클리드 호제법 ? a * b // a, b의 최대공약수 -> 최소공배수 
    lcm = abs(n * 6) // math.gcd(n, 6) # -a, -b  -> 권장사항 
    return lcm//6 # lcm을 6으로 나눈다.