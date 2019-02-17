def collatz(number):
    steps = 1
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = 3 * number + 1
        steps += 1
    return steps
    
def longest_collatz_chain(starting_number):
    longest_sequence = 0
    longest_sequence_number = 0
    while starting_number > 0:
        current_steps = collatz(starting_number)
        if current_steps > longest_sequence:
            longest_sequence = current_steps
            longest_sequence_number = starting_number
        starting_number -= 1
    return longest_sequence, longest_sequence_number
    
print('Solution: longest collatz sequence: {}, product of number: {}'.format(*longest_collatz_chain(1000000)), sep='', end='\n')
