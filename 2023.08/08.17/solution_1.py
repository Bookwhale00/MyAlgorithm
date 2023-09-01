'''
https://school.programmers.co.kr/learn/courses/30/lessons/12910
나누어 떨어지는 숫자 배열

arr의 값을 divisor로 나눴을 때 나누어 떨어지는 값(=나머지가 0인 값)을 배열에 담아서 오름차순으로 반환.
나누어 떨어지는 값이 없다면 배열에 -1을 담아서 반환

예상 풀이
1. 맵 사용 
2. if 값이 없으면 -1 append
3. 오름차순 정렬

실제 풀이
1. 맵x 필터 사용 (맵은 [True, False, False, True] 반환)
2. sorted()로 정렬 (list.sort() 썼더니 None 반환)
3. 조건문으로 분기
'''

def solution(arr, divisor):
    answer = []

    # 1, 2
    answer = sorted(list(filter(lambda x: x % divisor == 0, arr)))

    # 3
    if answer:
        print(f"나누어 떨어지는 수가 존재 : {answer}")
        return answer
    
    answer.append(-1)
    print(f"나누어 떨어지는 수가 없음 : {answer}")
    return answer

arr = [2, 36, 1, 3]
divisor = 1
solution(arr, divisor)