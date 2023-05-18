'''
* 5.3에서 못 푼 문제 
2. https://www.acmicpc.net/problem/25304
영수증
hint : 어디에 어떤 값이 입력되는 지 정확히 파악하기, map함수
첫째 줄 : 영수증에 적힌 총 금액 x
둘째 줄 : 영수증에 적힌 구매한 물건의 종류의 수 n
이후 n개의 줄 : 각 물건의 가격 a 개수 b가 "공백"을 기준으로 주어진다.
둘째 줄 이후의 값으로 계산한 총 금액 = 첫째 줄의 총 금액 
-> Yes 
일치하지 않는다면
-> No
260000
4
20000 5
30000 2
10000 6
5000 8
'''
# 총금액 x
x = int(input())
# 구매한 종류의 수 n 
n = int(input())
# 각 물건의 가격과 개수
# price = list(map(int, input().split()))
# 이러면 하나만 입력받는데??

amount = []

for price in range(n):
    a, b = map(int, input().split())
    amount.append(a * b)
    # n번만큼 입력받아서 가격 * 개수 계산해서 amount리스트에 집어넣기

total_amount = sum(amount)

print(f"영수증에 적힌 총금액 : {x}")
print(f"구매한 종류의 수 : {n}")
print(f"금액 리스트 : {amount}")
print(f"계산한 총 금액 : {total_amount}")

if x == total_amount:
    print("Yes")
else:
    print("No")

