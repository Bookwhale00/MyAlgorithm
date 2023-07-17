'''
https://school.programmers.co.kr/learn/courses/30/lessons/178871
달리기 경주
선수들이 
"자기 바로 앞의 선수를 추월할 때" 
"추월한 선수의 이름"을 부른다. 
=> 이름을 부르면 등수가 바뀐다. 
이름이 불린 선수 <-> 해당 선수 앞에 있던 선수

경주가 끝났을 때 1등부터 순서대로 이름 배열 return
hint : 딕셔너리
'''

def solution(players, callings):
    p_i = {player: i for i, player in enumerate(players)}
    # 선수(index) : 등수(value)
    i_p = {i: player for i, player in enumerate(players)}
    # 등수(index) : 선수(value)

    for call in callings:
        current_i = p_i[call]
        # 이름을 불린 선수의 현재 등수
        pre_i = current_i - 1
        # 이름 불린 선수 바로 앞에 있는 선수의 등수(???헷갈려)
        current_p = call
        # 이름을 불린 선수의 이름
        pre_p = i_p[pre_i]
        # 이름을 불린 선수 바로 앞에 있는 선수의 이름

        p_i[current_p] = pre_i
        # 현재 선수(index) : 등수(value) => 앞 선수의 등수로 바뀜
        p_i[pre_p] = current_i 
        # 앞 선수(index) : 등수(value) => 뒷 선수의 등수로 바뀜

        i_p[current_i] = pre_p
        # 현재 등수(index) : 선수(value) => 앞 선수 이름으로 바뀜
        i_p[pre_i] = current_p 
        # 앞 선수 등수(index) : 선수(value) => 뒷 선수 이름으로 바뀜
    
    answer = list(i_p.values())
    return answer
    

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

solution(players, callings)