'''
https://school.programmers.co.kr/learn/courses/30/lessons/12939
최댓값과 최솟값

문자열 s
공백으로 구분된 숫자
숫자 중 최댓값 최솟값 찾아서
"(최솟값) (최댓값)" 으로 return

예상 풀이
1. s -> 리스트
2. "min(s)  max(s)" -> f스트링?

실제 풀이
1. 리스트 변환할 때 split()써서 공백 기준으로 변환하기
+ 마이너스 값이 있으니까 int도 써야함(마이너스 기호는 숫자보다 작은 값)
'''


def solution(s):
    answer = ''

    # 1
    new_s = list(map(int, s.split()))
    print(f"공백 기준으로 리스트변환 : {new_s}")

    # 2
    answer = f"{min(new_s)} {max(new_s)}"
    print(f"최소 최대 : {answer}")

    return answer

s = "-1 -1"
solution(s)