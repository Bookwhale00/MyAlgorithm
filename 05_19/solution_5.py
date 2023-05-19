'''
https://school.programmers.co.kr/learn/courses/30/lessons/181837
커피 심부름
"americano" 들어가면 -> 4500
"cafelatte" 들어가면 -> 5000
"anything" 들어가면 -> 4500
'''

def solution(order):
    answer = 0
    # order리스트를 for문으로 돌려서 각 단어가 포함되는지 체크
    for menu in order:
        # if "americano" or "anything" in menu:
        if "americano" in menu or "anything" in menu:
            answer += 4500
            print(f"{menu} - 아메리카노주문")
        elif "cafelatte" in menu:
            answer += 5000
            print(f"{menu} - 카페라떼주문")
            
    print(answer)
    return answer

order1 = ["cafelatte", "americanoice", "hotcafelatte", "anything"]
order2 = ["americanoice", "americano", "iceamericano"]
solution(order1)

'''
if "americano" or "anything" in menu: 이렇게 했더니 전부 아메리카노 주문으로만 나옴. 찾아보니까 항상 "americano"가 True가 되고 있었음.
if "americano" in menu or "anything" in menu: 로 수정해서 해결
'''