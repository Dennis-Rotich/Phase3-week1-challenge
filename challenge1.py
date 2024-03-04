def solution(A):
    N = len(A)
    if sum(A)  % 10 != 0: return -1
    moves = 0
    while True:
        changed = False
        for i in range(N):
            if A[i] == 10:
                continue
            if i > 0 and A[i-1] > 0:
                moves += 1
                A[i] += 1
                A[i-1] -= 1
                changed = True
            elif i < N-1 and A[i+1] > 0:
                moves += 1
                A[i] += 1
                A[i+1] -= 1
                changed = True
        if not changed:
            break
    if all(a == 10 for a in A):
        return moves
    else:
        return -1
    
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))