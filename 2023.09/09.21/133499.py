'''
https://school.programmers.co.kr/learn/courses/30/lessons/133499
옹알이

조카가 할 수 있는 발음 
"aya"
"ye"
"woo"
"ma"
+ 얘네를 조합해서 만들 수 있는 발음 (한개를 연속으로 발음 x)

babbling 리스트가 주어질 때 발음할 수 있는 단어의 개수를 return

계획
babbling의 원소에서 발음할 수 있는 단어를 제거해서 최종적으로 공백이 아니면(문자가 남으면) 발음할 수 없는 단어
-> replace사용

한 가지 발음이 여러번 나오면 하나만 제거해야 함
-> replace의 3번째 인자 사용(최대 교체 횟수)
'''

# def solution(babbling):
#     answer = 0
#     remove_list = ["aya", "ye", "woo", "ma"]

#     for word in babbling:
#         for drop_word in remove_list:
#             word = word.replace(drop_word, "", 1)

#         if word == "":
#            answer += 1

#         print(f"발음 다 했나? : {word}")
#         print(f"발음한 단어 갯수 : {answer}")
    
#     return answer

# babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
# solution(babbling)

'''
1, 9, 10, 11, 14, 16, 17, 19, 20 실패
-> 연속해서 발음하는 게 아니라면 같은 발음이 2번 이상 들어가도 제거할 수 있다.
-> replace 3번째 인자를 사용하면 안됨

hint
연속될 경우 미리 만들어놓기

'''

def solution(babbling):
   
    says = ["aya", "ye", "woo", "ma"]
    answer = 0
   
    for i in range(len(babbling)):
   
        for say in says:
            if (say in babbling[i]) and (say*2 not in babbling[i]):
            # babbling[i] 안에 say가 있으면서도 say*2가 연속으로 있지 않을 시 
           
                babbling[i] = babbling[i].replace(say, "*")
                # babbling[i]안의 say를 "*"로 바꾼다
                # 예) "ayamwoo" => "*m*"
       
        if all(char == "*" for char in babbling[i]):
            # babbling[i] 가 "*"로만 이루어져 있을시 answer += 1
            answer += 1
   
    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
solution(babbling)