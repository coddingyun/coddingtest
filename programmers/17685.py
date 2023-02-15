def solution(words):
    answer = 0
    for word in words:
        r = False      
        for j in range(len(word)):
            i = 0
            for i in range(len(words)):
                if word == words[i]:
                    continue
                if len(words[i]) > j and word[j] == words[i][j] and word[:j] == words[i][:j]:
                    answer += 1
                    if j == len(word) - 1:
                        r = True
                    break
                    
                if i == len(words) - 1:
                    break
        if r!= True:
            answer += 1
    if len(words) == 1:
      return len(words[0])
    return answer

print(solution(["go", "gone"]))
print(solution(["go","gone","guild"]))
print(solution(["word","war","warrior","world"]))