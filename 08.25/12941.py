'''
https://school.programmers.co.kr/learn/courses/30/lessons/12941
최솟값 만들기

길이가 같은 배열 A, B(자연수)
배열에서 각각 한 개의 숫자를 뽑아 두 수를 곱한다.
배열의 길이만큼 위 과정을 반복해서 두 수를 곱한 값을 누적해서 더한다.
최종적으로 "누적된 값이 최소가 되도록" 하는게 목표.
한 번 뽑은 숫자는 다시 쓸 수 없다.

예상 풀이
1. 모든 조합을 곱해서 더 작은 수 찾기...? 다른 방법이 있을 것 같다

2. A 배열의 가장 작은 값 x B 배열의 가장 큰 값
그다음 작은 값 X 그 다음 큰 값....
A 배열은 오름차순 B 배열은 내림차순 한 다음에
앞에서부터 차례로 곱하면 되겠다. 

실제 풀이
2번 방법에 + zip()
'''

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    print(f"A 재정렬 : {A}")
    print(f"B 재정렬 : {B}")

    result = [a * b for a, b in zip(A, B)]
    print(f"차례대로 곱함 : {result}")

    answer = sum(result)
    print(f"최솟값 : {answer}")

    return answer


A = [1, 4, 2]
B = [5, 4, 4]
solution(A, B)