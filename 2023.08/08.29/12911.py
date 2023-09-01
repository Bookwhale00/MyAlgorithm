'''
https://school.programmers.co.kr/learn/courses/30/lessons/12911
다음 큰 숫자

n의 다음 큰 숫자는
1. n보다 큰 자연수
2. n과 n의 다음 큰 숫자는 2진수로 변환했을 때 1의 갯수가 같다. 
3. 조건 1, 2를 만족하는 수 중 가장 작은 수


예상 풀이
1. n을 이진수 변환 (bin_n)
2. bin_n에서 1의 갯수 세기
3. while문 -> n+1의 수와 1의 갯수가 일치할 때까지 += 1
'''

def solution(n):
    answer = 0
    # 1
    bin_n = bin(n)[2:]
    print(bin_n)

    # 2
    bin_n_count = bin_n.count("1")
    print(bin_n_count)

    next_n = n + 1

    # 4
    while True:
        bin_next = bin(next_n)[2:]
        bin_next_count = bin_next.count("1")
        if bin_n_count == bin_next_count:
            break
        next_n += 1
        print(next_n)
        print(bin_next)
        print(bin_next_count)
    
    answer = next_n
    print(answer)

    return answer

n = 15
solution(n)