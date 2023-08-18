'''
https://school.programmers.co.kr/learn/courses/30/lessons/12943
콜라츠 추측

= 주어진 수가 1이 될 때까지 아래 작업을 반복하면 모든 수를 1로 만들 수 있다. 
1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

위 작업을 몇 번 반복해야 1이 되는지 구해서 반환
* 500번 반복해도 안되면 -1 반환

예상 풀이
1. if 짝수면 2로 나누고 answer += 1
2. if 홀수면 3을 곱하고 1을 더하고 answer += 1
3. while num > 1

실제 풀이
1. 그대로 ok
2. 500번 반복해도 안 될 경우 추가
'''

def solution(n):
    answer = 0

    while n > 1:
        if n % 2 == 0:
            n = n // 2
            answer += 1
            print(f"짝수 : {n, answer}")
        else:
            n = n * 3 + 1
            answer += 1
            print(f"홀수 : {n, answer}")

        if answer == 500:
            print("끝이 안남")
            return -1
            
    
    print(f"작업한 횟수 : {answer}")
    return answer

n = 626331
solution(n)