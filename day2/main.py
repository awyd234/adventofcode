# -*- coding: utf-8 -*-


def read_txt(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def solution1(data):
    two_count = 0
    three_count = 0
    for each_data in data:
        two_flag = False
        three_flag = False
        this_letter_dict = {}
        for each_letter in each_data:
            if this_letter_dict.get(each_letter) is None:
                this_letter_dict[each_letter] = 0
            this_letter_dict[each_letter] += 1
        for _, count in this_letter_dict.items():
            if count == 2:
                two_flag = True
            elif count == 3:
                three_flag = True
        if two_flag:
            two_count += 1
        if three_flag:
            three_count += 1
    print(two_count * three_count)


def solution2(data):
    # O(n^2 * len)
    for index_one in range(len(data)):
        for index_two in range(index_one + 1, len(data)):
            difference = 0
            data_one = data[index_one]
            data_two = data[index_two]
            this_list = []
            for index, each_letter in enumerate(data_one):
                if data_two[index] != each_letter:
                    difference += 1
                    if difference > 1:
                        break
                else:
                    this_list.append(each_letter)
            if difference == 1:
                print(''.join(this_list))
                return


def solution2_2(data):
    # O(n * len^2)
    for index in range(len(data)):
        # len
        left_letters_set = set()
        for each_index, each_data in enumerate(data):
            # n
            left_letters_list = each_data[0: index] + each_data[index + 1:]
            left_letters_str = ''.join(left_letters_list)
            if left_letters_str not in left_letters_set:
                # len
                left_letters_set.add(left_letters_str)
            else:
                print(left_letters_str)
                return


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    data = [_.replace('\n', '') for _ in data]
    # solution1(data)
    # solution2(data)
    solution2_2(data)

if __name__ == '__main__':
    main()
