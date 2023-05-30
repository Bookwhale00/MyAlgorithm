"""
https://school.programmers.co.kr/learn/courses/30/lessons/120849
모음 제거
[a, e, i, o, u]를 문자열에서 제외하기
translate, str.maketrans 함수 사용
"""


# 1번 풀이
def solution(my_string):
    vowel = my_string.maketrans(
        {
            "a": "",
            "e": "",
            "i": "",
            "o": "",
            "u": "",
        },
    )
    print(my_string.translate(vowel))
    return my_string.translate(vowel)


my_string = "nice to meet you"
solution(my_string)


# 2번 풀이
def solution(my_string):
    vowel = my_string.maketrans("", "", "aeiou")

    return my_string.translate(vowel)


my_string = "nice to meet you"
solution(my_string)
