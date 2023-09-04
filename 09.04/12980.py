'''
https://school.programmers.co.kr/learn/courses/30/lessons/12980
점프와 순간이동

1. 1번에 K 칸을 앞으로 점프 -> K 만큼 건전지 사용 
2. (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동 
-> 건전지 사용 x

거리가 N 만큼 떨어진 장소로 가는 게 목적
사용해야 하는 건전지 사용량의 최솟값을 return

Key Point
1. 순간이동을 최대한 활용하자.
2. 거꾸로 목표지점에서 시작점으로 간다고 생각해보자. (n = 0이 될 때까지)
'''

def solution(n):
    battery = 0

    while n > 0:
        if n % 2 == 0:
            n = n // 2
            print(f"순간이동 : {n}")
        elif n % 2 != 0:
            n -= 1
            print(f"점프 : {n}")
            battery += 1
            print(f"배터리 사용 : {battery}")

    return battery

n = 5000
solution(n)


'''
bin(n)[2:].count('1') 로도 풀린다고 함. 
'''

# def solution(n):
#     answer = bin(n)[2:].count('1')

#     print(answer)
#     return answer

# n = 5000
# solution(n)