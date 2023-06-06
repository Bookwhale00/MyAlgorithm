'''
https://www.acmicpc.net/problem/2562
최댓값
'''
# numbers = list(input()) -> 하나만 들어감
# 모든 줄을 입력받아서 리스트 생성
numbers = []
count = 0
while True:
    line = input()
    # if not line: 
    #     break # 여기서 EOF Error (빈 문자열이 입력되어야 while문이 종료되는 구조)
    count += 1
    numbers.append(int(line)) # break문보다 앞에 있어야 한다.
    if count == 9:
        break

# 최댓값을 찾는다 : 출력 1
max_number = max(numbers)
print(f"최댓값:{max_number}")
# print(max_number)
# 찾은 최댓값이 리스트에서 몇 번째 수인지 찾는다 : 출력 2
find_max = numbers.index(max_number) + 1
print(f"최댓값의 자리:{find_max}")
# print(find_max)

'''
1번 시도
런타임에러(EOF Error) 발생
EOF Error : 입력의 끝(End of File)을 읽으려고 할 때 발생하는 오류
즉 입력이 더이상 없을 때 입력을 받으려고 해서 발생한다.
문제를 다시 보니 입력값은 9개로 고정이다.
line을 count해서 9가 될 때 while문을 종료시키면 해결될 것 같음

2번 시도
그냥 틀렸습니다 왜??
numbers.append(int(line)) 이게 break문보다 뒤에 있어서 마지막 값이 append되지 않고 break됨 -> break문 앞으로 옮겨서 해결
'''






