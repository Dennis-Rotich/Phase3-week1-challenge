def solution(N):
    # if the number give is 1 it returns a and the function is done
    if N == 1:
        return 'a'
    
    letters = 26
    #Calculating the number of loops through the alphabet
    target_count = N // letters
    #Remainder after completing a loop
    remaining = N % letters
    print(f'remaining: {remaining}')
    print(f'target count: {target_count}')

    result = []
    
    for i in range(letters):
        count = target_count
        if i < remaining:
            count += 1
        # Adds copies of the characters to be repeated after a complete loop
        result.extend([chr(97 + i)] * count)
    # Joins all the elements into one string
    return ''.join(result)

print(solution(10))