'''
2. https://school.programmers.co.kr/learn/courses/30/lessons/150370
개인정보 수집 유효기간
hint : terms는 딕셔너리, 모든 달은 28일. 우선 terms로 월을 더한 뒤 today와 비교 ...
type도 주의... privacies에서 index+1로 구하면 될듯
날짜를 더하고 빼는 함수 -> timedelta
'''
from datetime import datetime

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"] # 슬라이스해서 딕셔너리로 만들어야하나?
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def solution(today, terms, privacies):
    answer = []
    # 먼저 terms와 privacies 전부 딕셔너리로 변환하자.
    terms_dict = {}
    privacies_dict = {}
    for i in terms:
        key, value = i.split()
        terms_dict[key] = value
    for i in privacies:
        key, value = i.split()
        privacies_dict[key] = value
    # terms로 privacies의 월을 더함 (timedelta사용?) 막혔다...
    


    # 더해서 나온 날짜와 today를 비교해서 초과면 폐기해야되는 개인정보임

    # 폐기해야하는 정보의 index+1해서 answer리스트에 넣는다.
    
    


solution(today, terms, privacies)