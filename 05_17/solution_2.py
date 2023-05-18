'''
https://school.programmers.co.kr/learn/courses/30/lessons/120825
문자 반복 출력하기
'''

def solution(my_string, n):
    answer = ''
    # my_string을 리스트로 형변환해서 lambda함수를 써보자
    string_list = []
    for i in my_string:
        string_list.append(i)
    answer = "".join(map(lambda x : x * n, string_list))
    # lambda로 계산한 뒤 .join을 써서 문자열로 합쳐줌
    print(answer)
    return answer

my_string = "hello"
solution(my_string, 5)


    