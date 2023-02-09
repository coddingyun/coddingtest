def check_bal(p):
    num0 = 0
    num1 = 0
    for i in p:
        if i == '(':
            num0 += 1
        else:
            num1 += 1
    if num0 == num1:
        return True
    return False

def check_cor(p):
    while len(p) > 0:
        if '()' not in p:
            return False
        p = p.replace('()', '')
    return True

def subsol(p):
    if len(p) == 0:
        return p
    u = ''
    v = ''
    #print(p)
    #print(len(p))
    for i in range(2, len(p)+1):
        #print(i)
        if check_bal(p[:i]):
            u = p[:i]
            v = p[i:]
            #print(u,v)
            break
    if check_cor(u):
        #print("yes")
        return u + subsol(v)
    else:
        solution = '('+subsol(v)+')'
        substr = u[1:-1]
        for i in substr:
            if i == '(':
                solution += ')'
            else:
                solution += '('
        return solution

def solution(p):
    answer = subsol(p)
    return answer

#print(check_cor("()"))
print(solution("()))((()"))
print(solution("(()())()"))