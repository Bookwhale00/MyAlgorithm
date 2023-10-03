'''
https://school.programmers.co.kr/learn/courses/30/lessons/77484
로또의 최고 순위와 최저 순위

알아볼 수 없는 번호 = 0
로또 번호 6개
당첨이 가능했던 최고 순위와 최저 순위를 배열에 담아서 return

1 - 6개 일치
2 - 5개 일치
3 - 4개 일치
4 - 3개 일치
5 - 2개 일치
6 - 그 외

계획
1. 1 ~ 45까지 win_nums에 있는데 lottos에 없는 번호 찾아서 0을 대체한 뒤 두 리스트 일치하는 숫자 찾기 -> 최고순위
2. 1 ~ 45까지 win_nums에 없고 lottos에도 없는 번호 찾아서 0을 대체한 뒤 두 리스트 일치하는 숫자 찾기 -> 최저순위
-> 그냥 대체안하고 0으로 둬도 최저점수 나오지않을까? 

'''
def solution(lottos, win_nums):
    answer = []
    zero_count = lottos.count(0)
    max_num = 0
    max_rank = 0
    min_num = 0
    min_rank = 0

    # 2 최저순위 (lottos값 대체하기 전에 미리 최저점수 뽑기)
    for i in lottos:
        if i in win_nums:
            min_num += 1
    print(f"최저일 때 lottos : {lottos}")
    print(f"최저일 때 맞춘 번호 갯수 : {min_num}")

    # 1 최고순위
    for i in range(1, 46):
        # win_nums에 있으면서 lottos에 없는 번호
        if i in win_nums and i not in lottos: 
            # zero_count가 0이 될 때까지 i를 0 대신 집어넣기
            if zero_count > 0:
                lottos[lottos.index(0)] = i
                zero_count -= 1
            else:
                break
    
    print(f"최대일 때 lottos : {lottos}")

    # win_nums 안에 lottos 숫자가 들어있다면 max_num += 1
    for i in lottos:
        if i in win_nums:
            max_num += 1
    print(f"최대일 때 맞춘 번호 갯수 : {max_num}")

    # 로또번호 맞춘 갯수에 따라 순위 결정 (줄일 수 없을까)
    # if max_num < 2:
    #     max_rank += 6
    # elif max_num == 2:
    #     max_rank += 5
    # elif max_num == 3:
    #     max_rank += 4
    # elif max_num == 4:
    #     max_rank += 3
    # elif max_num == 5:
    #     max_rank += 2
    # elif max_num == 6:
    #     max_rank += 1

    # if min_num < 2:
    #     min_rank += 6
    # elif min_num == 2:
    #     min_rank += 5
    # elif min_num == 3:
    #     min_rank += 4
    # elif min_num == 4:
    #     min_rank += 3
    # elif min_num == 5:
    #     min_rank += 2
    # elif min_num == 6:
    #     min_rank += 1

    # 딕셔너리로 줄임
    rank_dict = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    max_rank = rank_dict[max_num]
    min_rank = rank_dict[min_num]

    answer = [max_rank, min_rank]
    print(f"최대 순위, 최저 순위 : {answer}")

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
solution(lottos, win_nums)