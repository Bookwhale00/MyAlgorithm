'''
https://school.programmers.co.kr/learn/courses/30/lessons/12947
하샤드 수
x = 양의 정수
x의 자릿수의 합으로 x가 나누어진다면 x는 하샤드 수 이다.
x가 하샤드 수인지 아닌지 검사해서 true나 false로 반환할 것

예상 풀이
1. 자릿수의 합 구하기
1-1. for문으로 문자열로 분리 -> int 변환 -> 합치기
1-2. divmod?
2. if문으로 나눠지는 지 판별

실제 풀이
1-1 방법으로 ㄱㄱ
'''

def solution(x):
    answer = False
    number = sum(int(n) for n in str(x))
    print(f"x : {x}")
    print(f"x의 자릿수 합 : {number}")

    if x % number == 0:
        answer = True

    print(f"x는 하샤드 수인가? : {answer}")
    return answer

x = 10000
solution(x)