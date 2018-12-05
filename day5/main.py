# -*- coding: utf-8 -*-


def read_txt(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [_.replace('\n', '') for _ in data]
        return data


def solution1(data):
    data = data[0]
    remain_list = []
    for each_data in data:
        if len(remain_list) == 0:
            remain_list.append(each_data)
            continue
        if len(remain_list) != 0 and (
                                ord(remain_list[-1]) + ord('a') - ord('A') == ord(each_data) or
                                ord(remain_list[-1]) - ord('a') + ord('A') == ord(each_data)):
            remain_list.pop()
        else:
            remain_list.append(each_data)
    print(len(remain_list))


def solution2(data):
    data = data[0]
    this_min = 10000000
    for each_char_ord in range(ord('a'), ord('z') + 1):
        this_char = chr(each_char_ord)
        upper_char = this_char.upper()
        remain_list = []
        for each_data in data:
            if each_data == this_char or each_data == upper_char:
                continue
            if len(remain_list) == 0:
                remain_list.append(each_data)
                continue
            if len(remain_list) != 0 and (
                                    ord(remain_list[-1]) + ord('a') - ord('A') == ord(each_data) or
                                    ord(remain_list[-1]) - ord('a') + ord('A') == ord(each_data)):
                remain_list.pop()
            else:
                remain_list.append(each_data)
        if len(remain_list) < this_min:
            this_min = len(remain_list)
    print(this_min)


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    solution1(data)
    # solution2(data)


if __name__ == '__main__':
    main()
