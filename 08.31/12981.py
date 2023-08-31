'''
https://school.programmers.co.kr/learn/courses/30/lessons/12981
영어 끝말잇기

가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇번째 차례에 탈락하는 지 return (탈락자 없으면 [0, 0] return)

예상 풀이
1. 사람 수 n만큼 리스트 생성
2. words를 for문으로 돌면서 본인 리스트에 넣어줌
3. 앞 단어의 끝 글자로 시작하지 않거나 이미 나온 단어를 말하는 사람 체크
4. 그 사람의 리스트에서 해당 단어가 몇 번 째인지 return
'''

def solution(n, words):
    answer = [0, 0]
    # 1
    P_list = [[] for _ in range(n)]
    wrong_word = None
    used_words = set() # 중복 체크용

    # 2, 3
    for i, word in enumerate(words): 
        # 단어가 중복이거나 혹은 현재 단어의 마지막 글자가 다음 단어의 첫번째 글자랑 같지 않다면
        if word in used_words or (i > 0 and words[i-1][-1] != word[0]):
            # 단어를 wrong_word에 저장
            wrong_word = word
        # 매 단어마다 각 참가자의 리스트와 사용한 단어 리스트에도 저장
        P_list[i % n].append(word)
        used_words.add(word)

    # 4
    # wrong_word에 값이 있으면 아래 로직대로 답 뽑고 아니면 초기화된 answer 사용 
    if wrong_word:
        for i, p in enumerate(P_list):
            if wrong_word in p:
                answer = [i + 1, p.index(wrong_word) + 1]
                
                break

    print(P_list[0])
    print(P_list[1])
    print(wrong_word)
    print(answer)
    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
solution(n, words)

'''
fail...
'''