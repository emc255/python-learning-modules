from collections import Counter

if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4]
    counter_numbers = Counter(numbers)
    print(counter_numbers)

    letters = "aaaaabbbbbcccccccccccddddddddd"
    counter_letters = Counter(letters)
    print(counter_letters)
    print(counter_letters.most_common())
    letters_list = list(counter_letters)
    print(letters_list)
