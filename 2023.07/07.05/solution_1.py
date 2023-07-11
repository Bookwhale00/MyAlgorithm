'''
https://school.programmers.co.kr/learn/courses/30/lessons/120871
저주의 숫자 3
3, 6, 9...를 쓰지않음 
3의 배수거나 3이 들어가면 skip 
음... 자리를 맞추면 될것같은데
3x마을의 법칙으로 1~100까지 수를 리스트로 만들어서
같은 index의 값을 가져오게하면 어떨까
for문 
'''

# 1차 시도 -> 테스트 4,5,6 런타임에러
# n이 1~100까지인거지 리스트에 들어갈 값은 제한이 없었다..!
# 그냥 범위를 200까지 늘려봤더니 통과했다! 

def solution(n):
    answer = 0
    # 3x마을 전용 리스트 만들기 
    sample_list = []
    sample = list(range(200))
    for x in sample:
        if x % 3 == 0:
            pass
        elif x % 3 != 0 and '3' not in str(x):
            sample_list.append(x)

    # n의 자리(-1)로 찾기
    answer = sample_list[n-1]
    return answer

n = 40
solution(n)