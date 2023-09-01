'''
https://school.programmers.co.kr/learn/courses/30/lessons/12951
JadenCase 문자열 만들기

JadenCase 
= 모든 단어의 첫 문자는 대문자. 그 외의 알파벳은 소문자.
첫 문자가 알파벳이 아닐 때는 그냥 소문자
입력받은 s를 JadenCase로 바꿔서 return해라

예상 풀이
1. 공백 바로 다음 문자는 대문자
2. 공백 기준으로 split해서 첫 문자만 대문자로 바꾸고 나머지는 소문자로 바꿔서 다시 합치기
'''

# def solution(s):
#     result = []
#     answer = ''
#     step1 = s.split(' ')
#     print(f"일단 분리 : {step1}")

#     for word in step1:
#         change = word[0].upper() + word[1:].lower()
#         result.append(change)
#     print(f"대소문자 정리 : {result}")
        
#     answer = ' '.join(result)
#     print(f"다시 문자열로 : {answer}")

#     return answer

# s = "3people unFollowed me"
# solution(s)

'''
테스트케이스 통과
2, 4, 5, 8, 9, 11, 12, 13, 14, 17 런타임 에러
반례 뭐지 
공백이 연속될 때?
'''

def solution(s):
    result = []
    answer = ''
    step1 = s.split(' ')
    print(f"일단 분리 : {step1}")

    for word in step1:
        if word:
            change = word[0].upper() + word[1:].lower()
            result.append(change)
        else: # word가 공백이면
            result.append('')

    print(f"대소문자 정리 : {result}")

    answer = ' '.join(result)
    print(f"다시 문자열로 : {answer}")

    return answer

s = "3people  unFollowed me"
solution(s)

'''
.title() -> 그냥 JadenCase만들어버리기
.capitalize() -> .upper()랑 같음
.isalpha() -> 알파벳 판별
.isspace() -> 빈칸 판별
'''