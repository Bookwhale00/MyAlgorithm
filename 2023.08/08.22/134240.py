'''
https://school.programmers.co.kr/learn/courses/30/lessons/134240
푸드 파이트 대회

1:1
한 명은 왼쪽부터 다른 한 명은 오른쪽부터 먹어서 중앙의 물을 먼저 먹는 선수가 승리
음식의 종류, 양, 먹는 순서는 같다.
칼로리가 낮은 음식부터 먼저 배치
몇 개는 못먹을 수도 있음
물은 0

음식의 양을 칼로리가 적은 순서대로 나타낸 배열 food
대회를 위한 음식 배치를 나타내는 "문자열" return

예상 풀이
1. 각 값을 2로 나눈 몫만 취해서 배열구하기 [1,3,4,6] -> [1,2,3]
2. 배열을 갯수만큼 문자열로 변환 [1,2,3] -> "122333"
3. 끝에 + "0"
4. 2번에서 구한 문자열 뒤집어서 0 뒤에 붙여주기
'''

def solution(food):
    answer = ''
    a_list = []
    
    
    return answer

food = [1,3,4,6]
solution(food)