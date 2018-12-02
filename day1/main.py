# -*- coding: utf-8 -*-


def read_txt(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    result = 0
    result_set = set()
    flag = True
    while flag:
        for each_data in data:
            each_data = each_data.replace('\n', '')
            each_real_data = int(''.join(each_data[1:]))
            if each_data[0] == '+':
                result += each_real_data
            else:
                result -= each_real_data
            if result in result_set:
                print(result)
                flag = False
                break
            else:
                result_set.add(result)

if __name__ == '__main__':
    main()
