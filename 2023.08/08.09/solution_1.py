'''
https://school.programmers.co.kr/learn/courses/30/lessons/17681
비밀지도
공백" " 
벽 "#"
2장의 지도를 겹쳐서 전체 지도를 획득
하나라도 벽인 부분은(#) 전체 지도에서도 벽이다. (or)
두 지도에서 모두 공백("")인 부분은 전체 지도에서도 공백이다. (and)
벽 = 1 공백 = 0 (이진수)
ex) 9 = 01001 = 공백/벽/공백/공백/벽
arr1과 arr2는 정수 배열로 주어짐 -> [9, 20, 28, 18, 11]

예상 풀이 과정
1. arr1과 arr2의 정수를 이진수로 변환(문자열로) -> bin함수 사용+zfill사용
2. 두 arr를 자리별로 각각 비교해서 새로운 arr3 생성 -> zip사용
    1) 둘 다 0이면 -> 0 
    2) 그 외에는 모두 -> 1
3. arr3의 값을 0이면 공백(" ") 1이면 #으로 대체 -> replace (첫번째 메소드가 값을 반환하면 반환된 값에서 또다시 함수를 호출하는 식으로 연속해서 여러 번 호출하는 것 -> method chaining)
4. 대체한 배열을 반환
'''

def solution(n, arr1, arr2):
    answer = []
    after_arr1 = []
    after_arr2 = []
    result = []

    # 1
    for num in arr1:
        after_arr1.append(bin(num)[2:].zfill(n))
    for num in arr2:
        after_arr2.append(bin(num)[2:].zfill(n))
    print(f"arr1 이진수 : {after_arr1}")
    print(f"arr2 이진수 : {after_arr2}")

    # 2
    for str1, str2 in zip(after_arr1, after_arr2):
        comparison = ''.join(['0' if c1 == '0' and c2 == '0' else '1' for c1, c2 in zip(str1, str2)])
        result.append(comparison)
    print(f"병합 : {result}")

    # 3
    answer = [s.replace('1', '#').replace('0', ' ') for s in result]
    print(f"최종출력 : {answer}")

    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

solution(n, arr1, arr2)
