def solution(A):
    # Create a dictionary to store the sums of digits for each number in A
    sums_of_digits = {}
    # Create another dictionary to store the sums of digits of the corresponding pair
    sums_of_digits2 = {}
    #Create a list to store sums of the pairs with digits of equal sum
    completed_sums = []
    # Iterate over each number in A
    for num in A:
       #Calculate sum of digits in each number
        sum_of_digits = sum(int(digit) for digit in str(num))
       #Check if the sum of diigits is present in sums_of_digits dictionary
        if sum_of_digits in sums_of_digits:
            sums_of_digits2[sum_of_digits] = num
        #Add the corresponding pair to sums_of_digits2 dictionary
        else:
            sums_of_digits[sum_of_digits] = num
    #Iterate over keys in sums_of_digits and sums_of_digits2
    for num in sums_of_digits:
        for num2 in sums_of_digits2:
            #If the keys are similar - meaning they have the same sum of digits, add the two numbers and store the sum in completed_sums
            if num == num2:
                result = sums_of_digits[num] + sums_of_digits2[num2]
                completed_sums.append(result)
    #Check if completed_sums is empty meaning their is no pair of numbers with similar sum of digits
    if completed_sums == []:
        return -1
    else:
        return max(completed_sums)



