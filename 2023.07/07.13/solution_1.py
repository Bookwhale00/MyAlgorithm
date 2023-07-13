'''
https://school.programmers.co.kr/learn/courses/30/lessons/181885
할 일 목록
Boolean Indexing!
'''

def solution(todo_list, finished):
    answer = []
    for todo, finish in zip(todo_list, finished):
        if finish == False:
            answer.append(todo)
            print(todo)
    print(answer)
    

todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False] 

solution(todo_list, finished)