'''
https://school.programmers.co.kr/learn/courses/30/lessons/155652
둘만의 암호

규칙
1. 문자열 s의 각 알파벳을 index 만큼 뒤의 알파벳으로 바꿔준다. 
2. index 만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아간다.
3. skip에 있는 알파벳은 제외하고 건너뛴다.
* skip에 포함되는 알파벳은 s에 포함되지 않는다 *

계획
1. 알파벳이 전부 있는 리스트 alphabet
2. alphabet에서 skip 제거
3. s 반복 돌면서 자릿수 찾아서 리스트에 저장
4. map써서 index만큼 더하기
5. 더한 자릿수를 alphabet에서 찾아서 문자열로 리턴
* IndexError: list index out of range 발생 (z를 넘어가서)
-> if문써서 처리
'''
import string

def solution(s, skip, index):
    answer = ''

    # 1
    alphabet = list(string.ascii_lowercase)

    # 2
    for skip_str in skip:
        if skip_str in alphabet:
            alphabet.remove(skip_str)
    
    # 3
    index_list = []
    for original_str in s:
        if original_str in alphabet:
            index_list.append(alphabet.index(original_str))

    # 4
    convert_list = list(map(lambda x: x + index, index_list))

    # 5
    for i in convert_list:
        if i >= len(alphabet): # z를 넘어가면
            i %= len(alphabet) # alphabet 길이로 나눈 나머지로 바꿔주기 (a부터 시작)
        answer += alphabet[i]
    
    print(f"skip 제외한 알파벳 : {alphabet}")
    print(f"s 문자열의 자릿수 : {index_list}")
    print(f"위에다가 index {index} 더하기 : {convert_list}")
    print(f"새로 찾은 자릿수를 문자열로 바꾸면? : {answer}")
    
    return answer

s = "aukks"
skip = "wbqd"
index = 5
solution(s, skip, index)