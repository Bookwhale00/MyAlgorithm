# ㅡㅡㅡㅡㅡ 2. https://school.programmers.co.kr/learn/courses/30/lessons/120816 ㅡㅡㅡㅡㅡ

def solution(slice, n):
    i = 1
    # slice * 1, 2, 3... 하다가 n 이상이 될 때 스탑하기 -> while문?
    while slice * i < n:
        i += 1
    return i