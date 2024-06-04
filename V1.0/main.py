"""
Brief: Return full list of first numbers from 0 to number you paste as argument.
Param: number: int - from zero to any positive number, that you want to find all prime numbers.
Return: list
"""
def prime_numbers(number:int) -> list:

    first_numbers_list = []

    i = 2
    while i <= number:
        flag = False
        for num in range(2, i+1):
            if num != 1 and num != i:
                if i % num == 0:
                    flag = True
                    break
        if flag is False:
            first_numbers_list.append(i)
        i += 1
        flag = False
    return first_numbers_list