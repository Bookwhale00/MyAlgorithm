# ㅡㅡㅡㅡㅡ 1. https://school.programmers.co.kr/learn/courses/30/lessons/120818 ㅡㅡㅡㅡㅡ
# 옷가게 할인 받기

# 100000 >= price : * 0.95
# 300000 >= price : * 0.9
# 500000 >= price : * 0.8

def solution(price):
    answer = price * 0.8

    if 499999 >= price >= 300000:
        answer = price * 0.9
    elif 299999 >= price >= 100000:
        answer = price * 0.95

    return answer
# 보기 불편....

def solution(price):
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price

    return int(answer)
# 1차 수정 

def solution(price):
    return int(price * (0.8 if price >= 500000 else 0.9 if price >= 300000 else 0.95 if price >= 100000 else 1))
# 중첩된 삼항연산자 사용해서 팍 줄여버리기
# 했더니 테스트 13, 14 실패 
# 제한사항 "소수점 이하를 버린 정수를 return" 
# int()로 정수변환해주고 통과!