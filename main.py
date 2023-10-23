from itertools import groupby

def increasing_subsequences(sequence):
    current_sequence = []

    for number in sequence:
        if current_sequence and number >= current_sequence[-1]:
            current_sequence.append(number)
            if len(current_sequence) >= 2:
                yield current_sequence[:]
        else:
            current_sequence = [number]


while True:
    user_input = input("Введите последовательность чисел, разделенных пробелами: ")
    try:
        user_numbers = [int(x) for x in user_input.split()]
        user_numbers = [k for k, _ in groupby(user_numbers)]
        if len(user_numbers) == 1:
            print(user_numbers[0])
        else:
            previous_sequence = None
            for subsequence in increasing_subsequences(user_numbers):
                print(subsequence)
        break  
    except ValueError:
        print("Ошибка: Введите только целые числа, разделенные пробелами.")
