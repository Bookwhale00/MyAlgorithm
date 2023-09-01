'''
https://school.programmers.co.kr/learn/courses/30/lessons/70129
이진 변환 반복하기

문자열 x
1. x의 모든 0을 제거한 후
2. "x의 길이"를 이진법으로 표현한 문자열 = x 
ex) 처음에 x = "0111010" 
0 모두 제거하면 x = "1111" 길이는 4
4를 이진수로 바꾸면 100 
x = "100"
3. 위 과정을 x = "1" 이 될 때까지 반복
4. ["이진 변환한 횟수", "변환 과정에서 제거된 모든 0의 개수"] 반환

예상 풀이
1. while문
2. ["이진 변환한 횟수", "변환 과정에서 제거된 모든 0의 개수"] 
초기화 시켜놓기
3. while문 안에서 변환 과정 차근차근 쓰기

실제 풀이
1. while s is not "1" -> while s != "1"로 수정 (SyntaxWarning: "is not" with a literal) 
is 연산자는 주로 'None'과 비교할 때 사용된다고 함.
'''

def solution(s):
    answer = []
    change_count = 0
    zero_count = 0

    while s != "1":
        zero_count += s.count("0")
        change_count += 1

        # s = s.replace("0", "") # 0 제거
        # s = len(s) # 길이
        # s = bin(s)[2:] # 이진수로 변환
        
        s = bin(len(s.replace("0", "")))[2:] # 한줄로 압축

        print(f"변환 {change_count}회차")
        print(f"제거한 0의 누적 갯수 : {zero_count}")
        print(f"변환된 문자열 s : {s}")

    answer = [change_count, zero_count]
    print(f"최종 결과 : {answer}")

    return answer

s = "110010101001"
solution(s)