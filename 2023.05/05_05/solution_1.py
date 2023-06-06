'''
1. https://school.programmers.co.kr/learn/courses/30/lessons/120819
아이스 아메리카노
아메리카노 한 잔 5500원
최대로 마실 수 있는 아메리카노 잔 수 / 남는 돈
을 순서대로 담은 list를 return
'''

def solution(money):
    # answer = [] 이렇게 했을 때 IndexError발생. answer리스트가 비어있어서 그런 것 같다.
    answer = [0, 0] # 이렇게 초기값을 설정해서 해결
    cup = 5500
    # 가지고 있는 돈이 5500원보다 많은 동안
    while money >= cup:
            # 1잔을 사먹고
            money -= cup
            # answer에 기록함(반복)
            answer[0] += 1
    # 가지고 있는 돈이 5500원보다 적어지면
    else: 
          # 남은 돈을 answer리스트 1번째 자리에 넣어주고 끝
          answer[1] = money
    print(answer)
    return answer

solution(15000)

# 풀고나니까 그냥 //랑 %로 간단하게 풀 수 있는 문제였다. 
def solution(money):
      answer = [money // 5500, money % 5500]
      return answer

print(solution(15000))