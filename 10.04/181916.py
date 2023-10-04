'''
https://school.programmers.co.kr/learn/courses/30/lessons/181916
주사위 게임

1 - 6 주사위 네 개
1. 4개 숫자가 모두 p로 같다면 1111 x p 
2. 3개 숫자가 p로 같고 다른 하나가 q라면 (10 x p + q)2 
3. 2개씩 같다면 (p + q) x |p - q| (절댓값)
4. 2개는 같고(p) 나머지는 각각 다르면(q, r) -> q * r
5. 숫자가 모두 다르다면 가장 작은 숫자

경우에 따라 값을 return

'''

def solution(a, b, c, d):
    dice = [a, b, c, d]
    # 중복 제거
    numbers = set(dice)

    # case 1 : numbers의 길이가 1
    if len(numbers) == 1:
        print("case 1")
        return 1111 * a
    
    # case 2 : numbers의 길이가 2면서 어떤 한 숫자가 3개일 때
    elif len(numbers) == 2 and dice.count(dice[0]) == 3 or dice.count(dice[1]) == 3:
        print("case 2")
        if dice.count(dice[0]) == 3:
            p = dice[0]
        else:
            p = dice[1]
        q = list(numbers - {p})[0] # 차집합
        return (10 * p + q) ** 2

    # case 3 : numbers의 길이가 2일 때 (2개씩)
    elif len(numbers) == 2:
        print("case 3")
        p, q = list(numbers) # 어차피 2개니까
        return (p + q) * abs(p - q)
    
    # case 4 : 2개는 같고(p) 나머지는 각각 다르면(q, r)
    elif len(numbers) == 3: # p, q, r 3개
        print("case 4")
        for num in numbers:
            if dice.count(num) == 2:  
                p = num
                break
        q, r = set(dice) - {p}
        return q * r

    # case 5 : 그 외
    else:
        print("case 5")
        return min(dice)

a = 2
b = 5
c = 2
d = 6
print(solution(a, b, c, d))

'''
다른 풀이
'''

def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        answer=1111*a
    elif a==b==c:
        answer=(10*a+d)**2
    elif a==b==d:
        answer=(10*a+c)**2
    elif a==c==d: 
        answer=(10*a+b)**2
    elif b==c==d:
        answer=(10*d+a)**2
    elif a==b and c==d:
        answer=(a+c)*abs(a-c)
    elif a==c and b==d:
        answer=(a+b)*abs(a-b)
    elif a==d and b==c:
        answer=(a+b)*abs(a-b)
    elif a==b:
        answer=c*d
    elif a==c:
        answer=b*d
    elif a==d:
        answer=b*c
    elif b==c:
        answer=a*d
    elif b==d:
        answer=a*c
    elif c==d:
        answer=a*b
    else:
        answer=min(a,b,c,d)

    return answer