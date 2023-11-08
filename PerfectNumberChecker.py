#1 nov 2023
while True:
# Prompt for a number
    num = int(input("Enter a number (or type 0 to exit): "))
    if num == 0:
        break
    
    # Collect all factors
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    # Sum up the factors
    factor_sum = sum(factors)

    # Compare the sum and the number and respond accordingly
    if factor_sum == num:
        print(f"The factors of {num} is {factors} \nThe sum of its factors is {factor_sum}. \n{num} is a perfect number. \n")
    else:
        print(f"The factors of {num} is {factors} \nThe sum of its factors is {factor_sum}. \n{num} is NOT a perfect number. \n")
