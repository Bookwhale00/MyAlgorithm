'''
https://school.programmers.co.kr/learn/courses/30/lessons/181854
배열의 길이에 따라 다른 연산하기
'''

def solution(arr, n):
    answer = []
    # arr의 길이가 홀수라면
    if len(arr) % 2 == 1:
        # 짝수 인덱스에 +n
        for i, x in enumerate(arr):
            if i % 2 == 0:
                answer.append(x + n)
            else:
                answer.append(x)
        print(answer)
        return answer
    # arr의 길이가 짝수라면
    else:
        # 홀수 인덱스에 +n
        for i, x in enumerate(arr):
            if i % 2 == 1:
                answer.append(x + n)
            else:
                answer.append(x)
        print(answer)
        return answer

arr = [49, 12, 100, 276, 33]
arr2 = [444, 555, 666, 777]
n = 100

solution(arr2, n)