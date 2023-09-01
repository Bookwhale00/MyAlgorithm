'''
https://school.programmers.co.kr/learn/courses/30/lessons/12982
예산

부서별로 물건 사줘야함
부서별 신청 금액 d
예산 budget
최대 몇 개의 부서에 물품을 지원할 수 있는지?

예상 풀이
1. 오름차순 정렬
2. 왼쪽부터 더하면서 budget을 넘으면 자르기

실제 풀이
2. if check > budget 으로 했더니 budget을 처음 넘은 금액까지 포함이 되서
check + n > budget으로 변경
'''

def solution(d, budget):
    check = 0
    n_list = []
    d.sort()
    
    for n in d:
        if check + n > budget: 
            break

        n_list.append(n)
        check += n
        
    print(f"구입 리스트 : {n_list}")
    print(f"금액 합 : {check}")
    print(f"부서 수 : {len(n_list)}")

    return len(n_list)


d = [1,3,2,5,4]
budget = 9
solution(d, budget)