
# Compute the sum of digits in all numbers from 1 to n
def sum(n):
    result_sum = 0
    for x in range(n + 1):
        result_sum += x
    return result_sum

test_data = 5
test_result = sum(test_data)
print(test_result)

#Find the max number from 3 values.
#124,21,32=124

def find_max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

result_number = find_max(32, 21 , 124)
print(result_number)



#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_odd_even(n):
    odds = 0
    even = 0

    while n != 0 :
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else :
            even += 1
        n = n // 10

    print(f"Even : {even}, Odds : {odds}")
test_number = 14570
count_odd_even(test_number)












