def biggest_palindrome(digits):
    current_max = 0
    max = int('9' * digits)
    num_1 = num_2 = 0
    for number_2 in range(max, 10 * digits, -1):
        for number_1 in range(max, 10 * digits, -1):
            number = number_1 * number_2
            if number > current_max:
                number = str(number)
                number_len = len(number)
                if number_len % 2 == 0:
                    l_str = number[:int(number_len/2)]
                    r_str = number[int(number_len/2):]
                    if l_str == r_str[::-1]:
                        current_max = int(number)
                        num_1 = number_1
                        num_2 = number_2
                else:
                    l_str = number[:int((number_len-1)/2)]
                    r_str = number[int((number_len+1)/2):]
                    if l_str == r_str[::-1] and int(number) > current_max:
                        current_max = int(number)
                        num_1 = number_1
                        num_2 = number_2
    return current_max, num_1, num_2

print('Solution: {}, multiple of {}*{}'.format(*biggest_palindrome(3)), sep='', end='\n')
