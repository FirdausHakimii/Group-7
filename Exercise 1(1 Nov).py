# Prompt for a number
number = int(input("Enter a number: "))

# Initialize a variable to store the sum of factors
factor_sum = 0

# Collect factors and calculate their sum
for i in range(1, number + 1):
    if number % i == 0:
        factor_sum += i

# Compare the sum with the original number
if factor_sum == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number. The sum of its factors is {factor_sum}.")

