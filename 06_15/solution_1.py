'''
https://school.programmers.co.kr/learn/courses/30/lessons/181858
무작위로 k개의 수 뽑기
'''


def solution(arr, k):
    # 서로 다른 수를 구해서 return
    # 중복 제거 set?
    # 리스트의 길이가 k보다 크면 슬라이싱
    # 리스트의 길이가 k보다 작으면 길이만큼 뺀 나머지 값을 -1로 채움
    answer = []
    num = set(arr)

    if len(num) > k:
        answer = list(num)[:k]
        # k까지만 자르기
    if len(num) < k:
        add = k - len(num)
        answer = list(num)
        for _ in range(add):
            answer.append(-1)
    # k - len(num) = 나오는 값 만큼 -1 추가 

    print(answer)
    return answer

arr = [0, 1, 1, 2, 2, 3]
k = 3
solution(arr, k)

# 테스트는 다 통과했는데 채점 다 실패..
# set는 순서가 없기 때문에 슬라이싱했을 때 틀린 값이 나올 수 있다고 함
