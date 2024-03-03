# def solution(A):
#     # Create a dictionary to store the sums of digits for each number in A
#     sums_of_digits = {}
#     # Create a set to store the numbers whose digits add up to an equal sum
#     equal_sum_numbers = set()

#     # Iterate over each number in A
#     for num in A:
#         # Calculate the sum of digits for the current number
#         sum_of_digits = sum(int(digit) for digit in str(num))
#         print(sum_of_digits)
#         sums_of_digits[sum_of_digits] = [num]


#     print(f'dict:{sums_of_digits}')
#     print(f'set:{equal_sum_numbers}')
#     # If there are no numbers with digits that add up to an equal sum, return -1
#     if not equal_sum_numbers:
#         return -1

#     # Initialize the maximum sum as -1
#     max_sum = -1

#     # Iterate over each pair of numbers in the equal_sum_numbers set
#     for num1 in equal_sum_numbers:
#         for num2 in equal_sum_numbers:
#             # If the numbers are the same, skip them
#             if num1 == num2:
#                 continue
#             # Calculate the sum of the two numbers
#             current_sum = num1 + num2
#             # If the current sum is greater than the maximum sum, update the maximum sum
#             if current_sum > max_sum:
#                 max_sum = current_sum

#     # Return the maximum sum
#     return max_sum 

def solution(A):
    # Create a dictionary to store the sums of digits for each number in A
    sums_of_digits = {}
    # Create a set to store the numbers whose digits add up to an equal sum
    equal_sum_numbers = set()

    # Iterate over each number in A
    for num in A:
        # Calculate the sum of digits for the current number
        sum_of_digits = sum(int(digit) for digit in str(num))
        sums_of_digits[sum_of_digits] = [num]
        
        if sum_of_digits in equal_sum_numbers:
            equal_sum_numbers.add(num)
        else:
            equal_sum_numbers.add(sum_of_digits)

    # If there are no numbers with digits that add up to an equal sum, return -1
    if len(equal_sum_numbers) < 2:
        return -1

    # Initialize the maximum sum as -1
    max_sum = -1

    # Iterate over each pair of numbers in the equal_sum_numbers set
    for num1 in equal_sum_numbers:
        for num2 in equal_sum_numbers:
            # If the numbers are the same, skip them
            if num1 == num2:
                continue
            # Calculate the sum of the two numbers
            current_sum = num1 + num2
            # If the current sum is greater than the maximum sum, update the maximum sum
            if current_sum > max_sum:
                max_sum = current_sum

    # Return the maximum sum
    return max_sum 

print(solution([51, 71, 17, 42]))
