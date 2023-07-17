'''
https://school.programmers.co.kr/learn/courses/30/lessons/181885
할 일 목록
불리안배열
-> Python에서는 불리안값은 대문자로 시작해야 한다.
프로그래머스 입력값이 소문자라 헷갈렸음
'''

def solution(todo_list, finished):
    answer = []
    for todo, finish in zip(todo_list, finished):
        if finish == False:
            answer.append(todo)
    return answer 
    
todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False] 

solution(todo_list, finished)