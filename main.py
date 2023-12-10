def increasing_subsequences(sequence, current_sequence=None, result=None):
    if current_sequence is None:
        current_sequence = ()
    if result is None:
        result = []

    if not sequence:
        return result

    number, *rest = sequence

    if current_sequence and number >= current_sequence[-1]:
        new_sequence = current_sequence + (number,)
        if len(new_sequence) >= 2:
            result.append(new_sequence)
        increasing_subsequences(rest, new_sequence, result)
    else:
        increasing_subsequences(rest, (number,), result)

    return result

user_input = input("Введите последовательность чисел, разделенных пробелами: ")

try:
    user_numbers = [int(x) for x in user_input.split()]
    user_numbers = [k for i, k in enumerate(user_numbers) if i == 0 or k != user_numbers[i - 1]]
    if len(user_numbers) == 1:
        print(user_numbers[0])
    else:
        sequences = increasing_subsequences(user_numbers)
        for subsequence in sequences:
            print(subsequence)

except ValueError:
    print("Ошибка: Введите только целые числа, разделенные пробелами.")
