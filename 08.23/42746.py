'''
https://school.programmers.co.kr/learn/courses/30/lessons/42746
가장 큰 수 (정렬 알고리즘)

numbers의 정수를 이어붙여 만들 수 있는 가장 큰 수를 구하기
[6, 10, 2] -> "6210"

예상 풀이
1. 배열 안의 값들을 전부 이어붙인 문자열로 바꾸기 -> join 
[6, 10, 2] -> "6102"
2. 문자열을 1자리 씩 리스트로 변환
3. 내림차순 정렬하고 다시 문자열로 바꾸기

실제 풀이
1. ok
2-3. ''.join(sorted(reverse=True)) 를 써서 리스트변환->정렬->문자열변환까지 한번에 ok
'''

# def solution(numbers):
#     answer = ''
    
#     # 1
#     num_str = ''.join(map(str, numbers))
#     print(f"1차 문자열 변환 : {num_str}")

#     # 2-3
#     answer = ''.join(sorted(num_str, reverse=True))
#     print(f"2차 문자열 변환 : {answer}")

#     return answer


# numbers = [3, 30, 34, 5, 9]
# solution(numbers)

'''
9534330이 나와야하는데 9543330이 나와서 실패
기존 숫자 조합 상관없이 그냥 숫자를 나열해서 가장 큰 값을 만드는 거로 착각함

3과 30을 비교했을 때 3이 먼저 나와야함... 303보다 330이 크니까
sort나 sorted에 key인자를 사용하면 정렬 기준을 사용자정의 할 수 있다고 함
각 원소는 1~1000이니까 최대 3번 반복한 값을 기준으로 비교해서 내림차순정렬
-> str_list.sort(key=lambda x: x*3, reverse=True)
'''

# def solution(numbers):
#     answer = ''
    
#     str_list = list(map(str, numbers))
#     print(f"1차 문자열 리스트 변환 : {str_list}")

#     str_list.sort(key=lambda x: x*3, reverse=True)
#     print(f"3번 반복해서 비교한 뒤 내림차순 정렬 : {str_list}")

#     answer = ''.join(str_list)
#     print(f"문자열로 변환 : {answer}")

#     return answer


# numbers = [0, 0, 0]
# solution(numbers)

'''
11번 케이스 실패
아마 [0, 0, 0] 이라는 배열이 있을 때 
0이 나와야하는데 000이 나오는 게 문제같음
'''

def solution(numbers):
    answer = ''
    
    str_list = list(map(str, numbers))
    print(f"1차 문자열 리스트 변환 : {str_list}")

    str_list.sort(key=lambda x: x*3, reverse=True)
    print(f"3번 반복해서 비교한 뒤 내림차순 정렬 : {str_list}")

    answer = str(int(''.join(str_list))) # 정수로 변환했다가 다시 문자열로 변환함
    print(f"문자열로 변환 : {answer}")

    return answer


numbers = [0, 0, 0]
solution(numbers)

'''
얻은 것
1. sort 사용자정의 기준 key인자 (다중조건 정렬도 가능!)
2. 원소 최대 값이 1000일 경우 값을 3번 반복해서 비교하면 good
3. [0, 0, 0]일 때 0을 뽑아내려면 정수로 한번 변환하면 가능
'''