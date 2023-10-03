'''
https://school.programmers.co.kr/learn/courses/30/lessons/181932
코드 처리하기

주어진 문자열 code
앞에서부터 읽는다
"1"이 등장하면 mode 변경 (mode는 0과 1이 있음)
시작 mode는 0

mode 0
code의 인덱스가 짝수인 문자만 answer에 추가

mode 1
code의 인덱스가 홀수인 문자만 answer에 추가
'''

def solution(code):
    answer = ''
    mode = 0

    for i, char in enumerate(code):
        if char == "1":
            mode = 1 - mode # 1<->0 전환시키기
        elif mode == 0 and i % 2 == 0: # 짝수만 추가
            answer += char
        elif mode == 1 and i % 2 == 1: # 홀수만 추가
            answer += char
        print(f"문자 : {char}")
        print(f"모드 : {mode}")
        print(f"처리결과 : {answer}")

    return answer

code = "abc1abc1abc"
solution(code)

'''
테스트 12, 13 실패
-> answer가 빈 문자열이라면 "EMPTY"를 return! 
'''

def solution(code):
    answer = ''
    mode = 0

    for i, char in enumerate(code):
        if char == "1":
            mode = 1 - mode # 1<->0 전환시키기
        elif mode == 0 and i % 2 == 0: # 짝수만 추가
            answer += char
        elif mode == 1 and i % 2 == 1: # 홀수만 추가
            answer += char
        print(f"문자 : {char}")
        print(f"모드 : {mode}")
        print(f"처리결과 : {answer}")

    # 추가
    if answer:
        return answer
    else:
        return "EMPTY"

code = "abc1abc1abc"
solution(code)