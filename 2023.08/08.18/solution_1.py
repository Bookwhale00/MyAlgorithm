'''
https://school.programmers.co.kr/learn/courses/30/lessons/81301
숫자 문자열과 영단어

네오->프로도 : 일부 자릿수는 영단어로 바꾼 카드
프로도 -> 원래 숫자를 찾아서 return

예상 풀이
1. 일단 대응되는 단어를 정의해놓고 문자열안에서 마주치면 바꾸는 함수가 있었던거 같은데 -> replace

실제 풀이
1. 다중 replace
2. 문자열로 반환되서 int로 형변환
'''

def solution(s):
    answer = 00
    
    # 1 
    answer = s.replace("zero", "0").replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")

    print(int(answer))
    return int(answer)

s = "2three45sixseven"
solution(s)