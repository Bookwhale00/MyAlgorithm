'''
분수의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/120808
전에 한 번 풀었던 문제
'''

from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = (numer1/denom1) + (numer2/denom2)
    fraction = Fraction(answer).limit_denominator()
    numer = fraction.numerator
    denom = fraction.denominator
    return numer, denom