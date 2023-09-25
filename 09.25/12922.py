'''
https://school.programmers.co.kr/learn/courses/30/lessons/12922
수박

itertools사용

'''

from itertools import repeat, chain, islice

def solution(n):
    answer = ''
    water = ["수"]
    melon = ["박"]

    repeated_list = chain.from_iterable(repeat(water + melon))

    answer = ''.join(islice(repeated_list, n))

    print(answer)

    return answer

n = 5
solution(n)