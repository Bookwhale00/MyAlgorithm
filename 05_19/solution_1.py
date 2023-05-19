'''
https://www.acmicpc.net/problem/10039
평균점수
입력값 - 5줄
점수가 40점 이상 -> 그 점수 그대로
점수가 40점 미만 -> 항상 40점
5명의 점수가 주어졌을 때 평균 점수를 구해라.
'''

scores = []
for _ in range(5):
    score = int(input())
    if score < 40 :
        scores.append(40)
    else:
        scores.append(score)
    # 5줄의 값을 입력받아서 scores 리스트에 append
    # 입력받을 때 40미만이면 40으로 바꿔서 가져오기

print(scores)
print(f"평균점수 : {round(sum(scores)/5)}")