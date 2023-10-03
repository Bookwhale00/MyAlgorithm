'''
https://school.programmers.co.kr/learn/courses/30/lessons/42862
체육복

hint : 정렬

여벌 체육복이 있는 학생이 다른 학생에게 체육복을 빌려주려고 한다.
학생들의 번호는 체격 순이라 바로 앞번호나 뒷번호의 학생에게만 체육복을 빌려줄 수 있다. 
최대한 많은 학생이 체육복을 입고 수업을 들어야 한다.

전체 학생의 수 n
체육복이 없는 학생들의 배열 lost
여벌 체육복이 있는 학생들의 배열 reserve
* 여벌 체육복을 가져왔는데 도난당했으면 체육복을 빌려줄 수 없다.

체육 수업을 들을 수 있는 학생 수의 최댓값을 return

계획
1. 여벌 가져왔는데 도난당했을 경우 -> set사용
두 리스트에 진짜 빌려줄 수 있는 사람하고 진짜 빌려야 하는 사람이 섞여있어서 확실히 분리해야함
2. 왜 그리디?
'''

def solution(n, lost, reserve):
    answer = 0

    set_lost = set(lost) - set(reserve)
    # 체육복 잃어버리고 여벌 없는 학생
    print(f"체육복 잃어버렸는데 여벌 없는 학생 : {set_lost}")

    set_reserve = set(reserve) - set(lost)
    # 여벌 체육복이 있고 잃어버리지 않은 학생 (=빌려줄 수 있음)
    print(f"여벌 체육복 다른 사람한테 빌려줄 수 있는 학생 : {set_reserve}")

    # 이제 set_reserve가 set_lost한테 빌려주면 됨 -> 이 부분이 가장 그리디스럽다.
    for student in set_reserve:
        print(f"빌려주기 전에 체크 : {student}")
        if student - 1 in set_lost: # 만약 student(빌려줄 수 있는 학생) 앞 번호가 체육복을 잃어버렸다면
            set_lost.remove(student - 1) # 빌려주고 set_lost에서 삭제
            print(f"아직 못 빌린 학생 : {set_lost}")
        elif student + 1 in set_lost: # 만약 student 뒷 번호가 체육복을 잃어버렸다면
            set_lost.remove(student + 1) # 빌려주고 set_lost에서 삭제
            print(f"아직 못 빌린 학생 : {set_lost}")

    # 그럼 이제 set_lost에 남은 학생은 끝까지 체육복을 빌리지 못해서 수업에 참가하지 못하는 학생
    # 전체 학생 수에서 수업에 참가하지 못하는 학생 수를 빼면 
    # 수업에 참가할 수 있는 학생 수가 나옴

    answer = n - len(set_lost)
    print(f"끝까지 못 빌린 학생 : {set_lost}")
    print(f"수업 들을 수 있는 학생 : {answer}")

    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
solution(n, lost, reserve)