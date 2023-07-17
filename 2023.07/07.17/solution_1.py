'''
https://school.programmers.co.kr/learn/courses/30/lessons/92334
신고 결과 받기

불량이용자 신고하고 처리결과를 메일로 발송
1. 각 유저는 한 번에 한 명의 유저만 신고 가능
(여러번 신고할 수 있지만 신고 횟수는 1회로 처리)

2. k번 이상 신고되면 이용정지. 

3. 이용정지된 유저를 신고한 모든 유저에게 정지사실을 메일로 발송

4. 각 유저별로 처리 결과 메일을 받은 횟수를 배열로 return
'''

def solution(id_list, report, k):
    answer = []
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2