'''
3. https://school.programmers.co.kr/learn/courses/30/lessons/133502
햄버거 만들기

아래->위로 쌓임
빵-야채-고기-빵
[야채, 빵, 빵, 야채, 고기 빵, 야채, 고기, 빵] 일 때
빵야채고기빵을 빼고, 또 빼고 또 빼서 뺀 횟수를 return
1 = 빵
2 = 야채
3 = 고기
따라서 [1, 2, 3, 1] 을 빼내야함
'''

# 파이썬 리스트에서 리스트 빼는 방법
# 1. for문 -> pop쓰니까 순서대로 제거가 안됨. remove쓰니까 ok
# 2. 집합 -> 중복제거때문에 이 문제에서는 못씀

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

# while hamburger in ingredient: -> 안됨 
# set에서 <=를 쓰면 부분집합 여부를 True, False로 반환할 수 있다.
# but 부분집합은 순서가 없다.......
# hamburger리스트의 순서까지! 일치하는 부분집합이 있을 때만 삭제하도록 해보자
# del 을 쓰면 특정 인덱스의 요소를 삭제할 수 있다. (복구X)

# 통과 못한 코드
# def solution(ingredient):
#     answer = 0
#     hamburger = [1, 2, 3, 1]
#     while set(hamburger) <= set(ingredient):
#         answer += 1 # 부분집합이 있으면 +1
#         for h in hamburger:
#             ingredient.remove(h)
#             print(ingredient)
#         print(answer)
# solution(ingredient)

# 재시도
# hint : pop이나 del를 써보자
def solution(ingredient):
    hamburger = []
    answer = 0
    for i in ingredient:
        hamburger.append(i)
        # 하나씩 넣으면서 슬라이싱으로 끝에서부터 비교하기
        print(hamburger)
        if hamburger[-4:] == [1,2,3,1]:
            # [-4:] -> 마지막 4개의 원소
            answer += 1
            print(f"햄버거완성 : {hamburger[-4:]} 삭제")
            del hamburger[-4:]
            # for p in range(4):
            #     hamburger.pop()
    print(f"만든 햄버거 : {answer}개")
    return answer
    
solution(ingredient)