'''
https://school.programmers.co.kr/learn/courses/30/lessons/12948
핸드폰 번호 가리기

전화번호 뒷 4자리를 제외한 나머지를 전부 *으로 가린 문자열 리턴

예상 풀이 과정
1. 뒤에서 4번째 자리까지의 값 잘라내서 answer에 저장
2. 나머지 전부 *로 replace해서 answer에 추가

실제 풀이 과정
1. 뒤에서 4번째 자리까지의 값을 제외한 부분을 star로 정의
2. star를 그 길이만큼의 "*" 로 대체 (replace)
'''

def solution(phone_number):
    answer = ''
    # 1
    star = phone_number[:-4]

    # 2
    answer = phone_number.replace(star, "*" * len(star))

    print(f"실제 번호 : {phone_number}")
    print(f"가릴 번호 : {star}")
    print(f"최종 번호 : {answer}")

    return answer

phone_number = "01033334444"

solution(phone_number)