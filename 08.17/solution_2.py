'''
https://school.programmers.co.kr/learn/courses/30/lessons/12950
행렬의 덧셈

같은 자리끼리 더하기, 2차원 배열

예상 풀이
1. 이중 for문
2. arr가 2개니까 zip

실제 풀이
그대로 ok
'''

def solution(arr1, arr2):
    answer = []

    # for num1, num2 in zip(arr1, arr2):
    #     temp = []
    #     for a, b in zip(num1, num2):
    #         temp.append(a+b)
    #     answer.append(temp)
    #     print(answer)
        
    # 리팩토링
    answer = [[a+b for a, b in zip(num1, num2)] for num1, num2 in zip(arr1, arr2)]

    print(answer)
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
solution(arr1, arr2)
