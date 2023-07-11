'''
0 떼기
https://school.programmers.co.kr/learn/courses/30/lessons/181847
'''

def solution(n_str):
    answer = ''
    # for문을 돌면서 0이 안나오는 순간 해당 값부터 끝까지 answer에 저장 
    for n in n_str:
        if n == '0':
            continue
        else:
            answer = n_str[n_str.index(n):]
            break
    return answer

n_str = "0010"
solution(n_str)