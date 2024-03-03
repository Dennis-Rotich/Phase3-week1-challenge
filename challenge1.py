def solution(A):
    N = len(A)
    total_bricks = sum(A)
    min_bricks = min(A)
    max_bricks = max(A)

    if total_bricks % N != 0:
        return -1

    target_bricks = total_bricks // N
    min_moves = float('inf')

    for i in range(N):
        moves = 0
        current_bricks = A[i]

        while current_bricks < target_bricks:
            if i == 0:
                next_bricks = A[i + 1]
            elif i == N - 1:
                next_bricks = A[i - 1]
            else:
                next_bricks = min(A[i - 1], A[i + 1])

            if next_bricks == min_bricks:
                return -1

            moves += next_bricks - min_bricks
            current_bricks += next_bricks - min_bricks

            if current_bricks == target_bricks:
                break

        min_moves = min(min_moves, moves)

    return min_moves

print(solution([7, 15, 10, 8]))