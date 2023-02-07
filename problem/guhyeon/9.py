def solution(s):
    answer = 0
    strlen = len(s)
    
    result = strlen
    
    for j in range(1,strlen//2+1):
        mid_length = strlen
        i=j
        prev = s[0:j]
        number = 0
        while i<strlen:
            if s[i:i+j] != prev:
                if number != 0:
                    if number >= 9:
                        mid_length -= j * number - 2
                    else:
                        #print("here",mid_length, j, number)
                        mid_length -= j * number - 1
                        #print(mid_length)
                    result = min(result, mid_length)
                    #print(i, j, result, number+1)
                prev = s[i:i+j]
                i = i + j
                number = 0
            else:
                number += 1
                #print(i+j)
                if (i+j>=strlen) :
                    if number >= 9:
                        mid_length -= j * number - 2
                    else:
                        mid_length -= j * number - 1
                    #print(j, result, number + 1)
                    result = min(result, mid_length)

                i = i + j
                    
                
    return result

print(solution("a"*15+"b"*10+"c"))