'''
https://school.programmers.co.kr/learn/courses/30/lessons/181893
배열 조각하기
* 문제 이해하기
짝수 인덱스 [0,2,4...] 의 값 뒷부분을 잘라서 버리고
홀수 인덱스 [1,3,5...] 의 값 앞부분을 잘라서 버린다.
이것을 반복해서 남는 arr를 return해라.
'''

def solution(arr, query):

    # query의 길이만큼 자르기를 반복한다. 
    for i in range(len(query)):
        print(i) # 0 1 2 
        # 슬라이싱
        if i % 2 == 0: # 짝수 인덱스
            arr = arr[:query[i]+1] # 남기기
            print(arr)
        else: # 홀수 인덱스
            arr = arr[query[i]:] # 남기기
            print(arr)

    print(arr)
    return arr

arr = [3,2,4,5,1,6]
query = [4,1,2]

solution(arr, query)