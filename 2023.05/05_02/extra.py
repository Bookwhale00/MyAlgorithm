'''재귀함수'''

# 문제 n 값이 주어졌을때 n의 팩토리얼을 구하라!
# 반복문으로 구하기
n = 5
# 5 * 4 * 3 * 2 * 1
result = n
while True:
    n -= 1
    if n == 0:
        break
    result *= n

print(result)

#####################################################
# 팩토리얼 재귀 함수로 구하기

def solution(n):
    if n == 1:
        return 1
    else:
        return n * solution(n -1)

# 5 * solution(n-1)
# 4 * solution(n-1)  : 3
# 3 * solution(n-1)  : 2
# 2 * solution(n-1)  : 1
# 1 일때는 1을 리턴!

print(solution(n))

# 팩토리얼 이해하면 피보나치로!

#####################################################
'''
재귀함수(Recursive Function)란?
자기 자신을 호출하는 함수
종료 조건이 충족될때까지 반복적으로 스스로를 불러내면서 주어진 작업을 수행한다. 항상 종료조건을 정의해야 한다. (안그럼 무한루프에 빠짐)

재귀함수로 짜여진 코드는 for, while 등 반복문으로 대체 가능하다.
but 반복문을 중첩해서 써야 하는 경우라면 
재귀함수가 더 효율적일 수 있다. 

재귀함수의 성능이슈
재귀함수는 호출될 때마다 메모리의 스택에 쌓이고 스택이 넘치면 스택오버플로우 에러가 발생한다. 
* 스택오버플로우(Stack Overflow) = Buffer Overflow
그리고 jump가 잦아서 반복문에 비해 시간이 더 많이 걸린다. 
-> 이를 해결하기 위해 프로그래밍 언어들에서는 꼬리 재귀 최적화라는 기능을 제공

꼬리 재귀 최적화(Tail Call Optimization)
: 재귀함수를 컴퓨터가 재해석하여 선형 알고리즘으로 만들어 실행하는 것. 이를 이용해 스택의 크기를 줄일 수 있다.
-> 무슨 말인지 모르겠다! 일단 패스
'''
def canTailRecurse():
    return canTailRecurse()
'''함수 자체만 return : 꼬리재귀 가능'''

def canNotTailRecurse():
    n = 2
    return n * canNotTailRecurse()
'''다른 것이 섞여서 return : 꼬리재귀 불가능'''

'''하노이의 탑 : 완전 어렵다'''