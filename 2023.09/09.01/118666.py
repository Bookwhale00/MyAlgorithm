'''
https://school.programmers.co.kr/learn/courses/30/lessons/118666
성격 유형 검사하기
문제가 이해하기 어렵다

1번 - RT
2번 - CF
3번 - JM
4번 - AN

* AN이면 동의가 N 비동의가 A *
* NA이면 동의가 A 비동의가 N *

* choices
1 = 매우 비동의 (앞 3점)
2 = 비동의
3 = 약간 비동의
4 = 모르겠음 (0점)
5 = 약간 동의
6 = 동의
7 = 매우 동의 (뒤 3점)

AN 지표에서 5번(약간 동의) -> N형 1점
CF 지표에서 3번(약간 비동의) -> C형 1점
MJ 지표에서 2번(비동의) -> M형 2점
RT 지표에서 7번(매우 동의) -> T형 3점
NA 지표에서 5번(약간 동의) -> A형 1점

1번 지표 -> T
2번 지표 -> C
3번 지표 -> M
4번 지표 -> 각각 1점씩 -> 사전순으로 A

->> TCMA형

풀이 과정
1. 답변 리스트 생성
2. 
choices가 1이면 "survey[i][0] 3"
choices가 2이면 "survey[i][0] 2"
choices가 3이면 "survey[i][0] 1"
choices가 4이면 "0 0"
choices가 5이면 "survey[i][1] 1"
choices가 6이면 "survey[i][1] 2"
choices가 7이면 "survey[i][1] 3"

3. answer 결과를 kakao 딕셔너리에 넣어서 정리
4. 짝지어서 value를 비교해서 더 큰 key 뽑고, value가 같으면 알파벳순으로 넣기. 
'''

def solution(survey, choices):

    kakao = {
        "R" : 0,
        "T" : 0,
        "C" : 0,
        "F" : 0,
        "J" : 0,
        "M" : 0,
        "A" : 0,
        "N" : 0
    }
    
    # 1
    answer = []

    # 2
    for a, b in zip(survey, choices):
        if b == 1:
            answer.append(a[0] + str(3))
        elif b == 2:
            answer.append(a[0] + str(2))
        elif b == 3:
            answer.append(a[0] + str(1))
        elif b == 4:
            answer.append(str(0) + str(0))
        elif b == 5:
            answer.append(a[1] + str(1))
        elif b == 6:
            answer.append(a[1] + str(2))
        elif b == 7:
            answer.append(a[1] + str(3))

    # 3
    for i in answer:
        key = i[0]
        value = int(i[1])
        if key in kakao:
            kakao[key] += value

    # 4
    result = ""
    keys = list(kakao.keys())

    for i in range(0, len(keys), 2):
        key1 = keys[i]
        key2 = keys[i+1]

        # kakao가 이미 2개씩 잘랐을 때 사전순이기 때문에 값이 같으면 key1 뽑으면 됨
        if kakao[key1] >= kakao[key2]:
            result += key1
        else:
            result += key2
        
    
    print(f"답변 : {answer}")
    print(f"유형별 점수 : {kakao}")
    print(f"최종 결과 : {result}")
    return result

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
solution(survey, choices)