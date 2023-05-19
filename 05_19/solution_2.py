'''
https://www.acmicpc.net/problem/20499
다리우스님 한타 안 함?
K + A < D이거나, 
D = 0이면 그는 「가짜」이고, 그렇지 않으면 「진짜」이다.
입력 : 0/5/3
'''
kda = list(map(int, input().split("/")))
k = kda[0]
d = kda[1]
a = kda[2]

if k + a < d or d == 0:
    print("hasu")
else:
    print("gosu")

