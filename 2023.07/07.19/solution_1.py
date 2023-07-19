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

# 1차 시도 
# 1번 테스트 통과 2번 테스트 실패(중복신고)

from collections import Counter

def solution(id_list, report, k):
    # report에서 신고당한 유저 이름만 뽑기
    # reported_users = {repo.split()[0] : repo.split()[1] for repo in report}
    # 기대값 = {'muzi' : 'frodo', 'apeach' : 'frodo', 'frodo' : 'neo', 'muzi' : 'neo', 'apeach' : 'muzi'}
    # 실제 나온 값 = {'muzi': 'neo', 'apeach': 'muzi', 'frodo': 'neo'}
    # 이유 : 딕셔너리 value의 유일성 때문에 마지막으로 신고한 유저 또는 신고당한 유저만을 저장했기 때문

    report_list = [(repo.split()[0], repo.split()[1]) for repo in report]
    # 이렇게 튜플로 해서 해결
    print(f"신고내역: {report_list}")

    # count
    reported_users = [reported[1] for reported in report_list]
    report_counts = Counter(reported_users)
    print(f"신고당한 횟수: {report_counts}")

    # k번 이상 신고된 유저 리스트
    k_reported_users = [user for user, count in report_counts.items() if count >= k]
    print(f"정지된 유저: {k_reported_users}")

    # k_reported_users를 신고한 유저 리스트
    reporters = []
    for reported in report_list:
        if reported[1] in k_reported_users:
            reporters.append(reported[0])
    print(f"정지시킨 유저: {reporters}")

    answer = []
    for id in id_list:
        answer.append(reporters.count(id))
    print(f"받은 메일 수: {answer}")

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

solution(id_list, report, k)

# 2차 시도 
# 중복 받지를 위해 set사용
# 정확성 3번만 시간초과로 실패
from collections import Counter

def solution(id_list, report, k):

    # report에서 신고당한 유저 이름만 뽑기
    # set추가해서 중복 방지!
    report_list = set((repo.split()[0], repo.split()[1]) for repo in report)
    print(f"신고내역: {report_list}")

    # count
    reported_users = [reported[1] for reported in report_list]
    report_counts = Counter(reported_users)
    print(f"신고당한 횟수: {report_counts}")

    # k번 이상 신고된 유저 리스트
    # 3차 시도에서 수정 
    # 리스트에서 in 연산은 O(n) 이지만 집합에서 in 연산은 0(1)이다. 
    # 리스트 -> 집합으로 수정
    # k_reported_users = [user for user, count in report_counts.items() if count >= k]
    k_reported_users = {user for user, count in report_counts.items() if count >= k}
    print(f"정지된 유저: {k_reported_users}")

    # k_reported_users를 신고한 유저 리스트
    reporters = []
    for reported in report_list:
        if reported[1] in k_reported_users:
            reporters.append(reported[0])
    print(f"정지시킨 유저: {reporters}")

    answer = []
    for id in id_list:
        answer.append(reporters.count(id))
    print(f"받은 메일 수: {answer}")

    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

solution(id_list, report, k)
