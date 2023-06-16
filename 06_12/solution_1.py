'''
https://school.programmers.co.kr/learn/courses/30/lessons/120884
치킨 쿠폰
서비스 치킨에도 쿠폰이 발급된다 -> 중요
'''

def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        s_chicken = coupon // 10 
        answer += s_chicken
        
        coupon = coupon % 10 + s_chicken
        print(answer) 

    print(answer)  
    return answer

chicken = 1081
solution(chicken)