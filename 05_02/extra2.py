# 피보나치 수열을 재귀함수로 구현하기
# 먼저 팩토리얼처럼 써보기

# 0 1 1 2 3 5 8 ...

def fibonacci(n):
    if n <= 1: # 0이나 1이면 거기부터 시작해야하니까 n 리턴
        print(f"fibonacci({n}) = {n}")
        return n
    else:
        fibo = fibonacci(n-1) + fibonacci(n-2)
        print(f"fibonacci({n}) = {fibo}")
        return fibo
        # 이전항과 그 이전항을 더해서 리턴

answer = [] # 수열로 표시하기 위한 리스트
for i in range(5):
    answer.append(fibonacci(i))

print(answer)

# 출력해보니까 왜 스택오버플로우가 되는지 알 것 같다.
# 꼬리재귀 사용해서 중복호출을 해결할 수 있을까?? ok