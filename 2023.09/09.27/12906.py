'''
https://school.programmers.co.kr/learn/courses/30/lessons/12906
같은 숫자는 싫어

배열 arr에서 "연속될 경우만" 중복 제거 해야하는데 원래 배열 순서 유지해야한다. (set사용 불가능?)

계획
arr를 for문으로 돌면서 현재 원소가 그 앞에 있는 원소랑 같지 않을 때만 answer 리스트에 추가하기
'''

def solution(arr):
    answer = []
    
    pre_a = None # 첫번째 원소 앞에는 아무것도 없으니까 처음엔 무조건 None

    for a in arr:
        if a != pre_a:
            answer.append(a)
        pre_a = a
        print(answer)

    return answer

arr = [1,1,3,3,0,1,1]
solution(arr)