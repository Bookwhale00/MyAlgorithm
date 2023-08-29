'''
https://school.programmers.co.kr/learn/courses/30/lessons/12924
숫자의 표현

자연수 n이 주어질 때 "연속된 자연수"로 n을 표현하는 방법의 수를 return

ex) n = 15
1+2+3+4+5 = 15
4+5+6 = 15
7+8 = 15
15 = 15
방법의 수 = 4개

예상 풀이 
1. 1부터 돌면서 다음 수를 더하다가 n이 되면 answer += 1하고 넘어감
2. n을 넘어가면 그냥 pass

실제 풀이
1. range(n+1)
2. ..?
'''

def solution(n):
    answer = 0

    for a in range(1, n+1):
        sum = 0
        for b in range(a, n+1):
            sum += b
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
            print(sum)
    print(answer)

    return answer

n = 15
solution(n)