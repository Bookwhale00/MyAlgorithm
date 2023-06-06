'''
https://www.acmicpc.net/problem/10817
세 수
세 정수를 입력받아 두 번째로 큰 정수를 출력하라.
입력 : 20 30 10
'''
num_list = list(map(int, input().split()))

print(sorted(num_list, reverse=True)[1])





