'''
https://school.programmers.co.kr/learn/courses/30/lessons/12909
올바른 괄호

'('로 열렸으면 반드시 ')'로 닫혀야 한다.
문자열 s가 올바른 괄호면 true, 올바르지 않은 괄호면 false 반환

스택 활용 -> 문자열을 순회하며 '('을 만나면 push ')'을 만나면 pop 순회가 끝나고 스택이 비어있다면 올바른 괄호이다.

예상 풀이
1. 임시리스트를 만들어서 for문으로 문자열을 돌면서 ')'을 만나면 1을 push, ')'을 만나면 pop한다.
2. 순회가 끝났을 때 임시리스트가 비어있으면 괄호가 전부 짝이 맞다는 뜻 -> True 반환
임시리스트에 값이 있으면 괄호가 짝이 안맞다는 뜻 -> False 반환

실제 풀이
그대로했는데 answer = True로 초기화시킨다음에 False인 경우만
if문으로 처리 (if result: )
'''

# def solution(s):
#     answer = True
#     result = []

#     for c in s:
#         if c == '(':
#             result.append(1)
#             print(result)
#         elif c == ')':
#             result.pop()
#             print(result)
    
#     if result:
#         answer = False

#     print(answer)
#     return answer

# s = ")()("
# solution(s)

'''
처음부터 ")"이 나올 경우 IndexError: pop from empty list 에러 발생
-> 이 경우 무조건 False니까 if로 거를까? 
'''

def solution(s):
    answer = True
    result = []

    for c in s:
        if c == '(':
            result.append(1)
            print(result)
        elif c == ')':
            # 처음에 ')'가 나올 경우 추가
            # -> 풀이를 보니까 try-except로 처리!!
            if not result:
                answer = False
                break
            result.pop()
            print(result)
    
    if result:
        answer = False

    print(answer)
    return answer

s = ")()("
solution(s)
