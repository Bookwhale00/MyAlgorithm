'''
https://school.programmers.co.kr/learn/courses/30/lessons/42628
이중우선순위큐

I 숫자 -> 주어진 숫자를 인큐
D 1 -> 최댓값 디큐
D -1 -> 최솟값 디큐

연산 operations는 배열로 주어진다
ex) ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
연산이 끝난 후 큐가 비어있으면 [0, 0] 반환
비어있지 않으면 [최댓값, 최솟값] 반환

* 파이썬에서 큐 쓰려면?
1. 그냥 리스트 쓰기 -> 시간복잡도 O(n) 
2. from collections import deque -> 시간복잡도 O(1) but 인덱스 접근은 O(n)
3. from queue import Queue -> 시간복잡도 O(1) 인덱스 접근 불가
4. heapq 기본적으로 최소힙 -> 음수 붙여서 최대힙 구현 ★ 

예상 풀이
1. operations (key, value) 형태로 분리하기
2. if로 명령어 구분해서 임시리스트 temp에 적용
3. temp에 값이 있는지 없는지 체크해서 answer 반환

실제 풀이
그대로 했는데 value가 기본 문자열이라 에러 발생 -> int로 감싸줌
'''

def solution(operations):
    temp = []
    answer = []

    # 1
    for op in operations:
        key, value = op.split()
        value = int(value)
        
        # 2
        if key == "I":
            temp.append(value)
            print(f"인큐 : {temp}")

        elif key == "D" and temp:
            if value == 1:
                temp.remove(max(temp))
                print(f"최댓값 디큐 : {temp}")
            elif value == -1:
                temp.remove(min(temp))
                print(f"최솟값 디큐 : {temp}")
    
    # 3
    if temp:
        answer = [max(temp), min(temp)]
    else:
        answer = [0, 0]    

    print(f"최종 결과 : {answer}")

    return answer

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
solution(operations)

'''
+3점
'''

'''
import heapq

# 빈 최소 힙 생성
min_heap = []

# 원소 추가
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)
print(f"min_heap: {min_heap}")

# 최소 값 얻기
min_value = heapq.heappop(min_heap)
print(f"min_value: {min_value}")

# 빈 최대 힙 생성
max_heap = []

# 원소 추가 (음수로 변환하여 최대 힙처럼 활용)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)
print(f"min_heap: {max_heap}")

# 최대 값 얻기 (원래 값으로 변환)
max_value = -heapq.heappop(max_heap)
print(f"max_value: {max_value}")
'''