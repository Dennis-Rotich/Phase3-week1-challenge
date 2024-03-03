def solution(N):
    if N == 1:
        return 'a'
    
    letters = 26
    target_count = N // letters
    remaining = N % letters
    
    result = []
    
    for i in range(letters):
        count = target_count
        if i < remaining:
            count += 1
        result.extend([chr(97 + i)] * count)
    
    return ''.join(result)

print(solution(5))