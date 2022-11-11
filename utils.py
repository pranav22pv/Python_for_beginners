def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


def get_input():
    list = []
    n = int(input("Enter the number of elements to be in the list: "))
    for i in range(n):
        ele = int(input(">"))
        list.append(ele)
    return list


def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min


def blank_lines():
    print("\n")