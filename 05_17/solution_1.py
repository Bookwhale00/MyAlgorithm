'''
https://school.programmers.co.kr/learn/courses/30/lessons/120824
짝수 홀수 개수
'''
def solution(num_list):
    answer = [0, 0]
    # for문돌려서 짝수면 answer[0] += 1
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        elif i % 2 == 1:
            answer[1] += 1

    print(answer)
    return answer

num_list = [1,3,5,7]
solution(num_list)

# 감탄한 풀이

def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer