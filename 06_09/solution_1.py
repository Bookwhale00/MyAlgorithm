'''
https://school.programmers.co.kr/learn/courses/30/lessons/120864
숨어있는 숫자의 덧셈(2)
자연수가 있으면
-> 자연수들의 합 return
자연수가 없으면
-> 0 return
'''
# 1번 시도 실패
# def solution(my_string):
#     answer = 0
#     num_list = []
#     # 먼저 for문으로 리스트형변환 (index필요해서 enumerate사용)
#     for i, n in enumerate(my_string):
#         # if type(n) == int: # 문자열의 각 문자는 str이기 때문에 항상 False가 됨
#         if n.isdigit() and not n[i+1].isdigit:
#         # n이 숫자 + n 바로 다음 값이 숫자가 아닐 때 
#             num_list.append(n)
        
#     return answer

# 2번 시도
# 연속된 수를 각각이 아니고 하나의 수로 보는 게 관건일 것 같다.
# 정규표현식 모듈 re를 쓸 수 있다는 힌트를 얻었음
import re 

def solution(my_string):
    
    str_list = re.findall(r'[0-9]+', my_string)
    '''
    re.findall() : 정규식 패턴과 일치하는 모든 문자열 찾아서 리스트로 반환
    r : raw string. \를 이스케이프 문자x 문자열 그대로 처리함
    [0-9] : 0부터 9까지의 숫자
    + : 앞에 있는 [0-9]가 하나 이상 반복되는 패턴을 찾는 meta character
    '''
    int_list = list(map(int, str_list))
    answer = sum(int_list)

    return answer

my_string = "aAbBcCoOp"

solution(my_string)