from bisect import bisect_left, bisect_right

def count_by_range(array, x, y):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, y)
    return right_index - left_index
        

def solution(words, queries):
    answer = []
    array = [[]for _ in range(10001)]
    reversed_array = [[]for _ in range(10001)]
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    for query in queries:
        if query[-1] == '?':
            count = count_by_range(array[len(query)], query.replace('?','a'), query.replace('?','z'))
        elif query[0] == '?':
            count = count_by_range(reversed_array[len(query)], query[::-1].replace('?','a'), query[::-1].replace('?','z'))
        answer.append(count)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))