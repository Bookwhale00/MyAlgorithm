'''
https://school.programmers.co.kr/learn/courses/30/lessons/12954
x만큼 간격이 있는 n개의 숫자

x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트 반환

예상 풀이
1. 리스트의 길이는 len(n+1)
2. 첫번째 값은 x
3. x씩 step -> range함수의 3번째 인자?

실제 풀이
1. range함수를 쓰려면 마지막 값을 정확히 알아야 하기 때문에 이 조건에서는 쓰기 어렵다. -> while 루프로 변경
2. answer 리스트의 길이가 n보다 작으면 루프한다. 
'''

def solution(x, n):
    step = x
    answer = []

    while len(answer) < n:
        answer.append(x)
        x += step

    print(answer)
    return answer

x = -4
n = 2
solution(x, n)