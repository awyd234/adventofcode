# -*- coding: utf-8 -*-


def read_txt(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [_.replace('\n', '') for _ in data]
        return data


def solution1(data):
    this_list = list()
    result_dict = {}
    for each_data in data:
        start = each_data.split(' ')[1]
        stop = each_data.split(' ')[-3]
        if start not in result_dict:
            result_dict[start] = {
                'to': set(),
                'from': set()
            }
        result_dict[start]['to'].add(stop)
        if stop not in result_dict:
            result_dict[stop] = {
                'to': set(),
                'from': set()
            }
        result_dict[stop]['from'].add(start)
    this_set = set(result_dict.keys())
    while len(this_set) != 0:
        all_data = list(result_dict.keys())
        all_data.sort()
        for each_start in all_data:
            if each_start not in this_set:
                continue
            if len(result_dict[each_start]['from']) == 0:
                this_list.append(each_start)
                this_set.remove(each_start)
                for each_stop in result_dict[each_start]['to']:
                    result_dict[each_stop]['from'].remove(each_start)
                break
    print(''.join(this_list))


def solution2(data):
    this_list = list()
    result_dict = {}
    for each_data in data:
        start = each_data.split(' ')[1]
        stop = each_data.split(' ')[-3]
        if start not in result_dict:
            result_dict[start] = {
                'to': set(),
                'from': set()
            }
        result_dict[start]['to'].add(stop)
        if stop not in result_dict:
            result_dict[stop] = {
                'to': set(),
                'from': set()
            }
        result_dict[stop]['from'].add(start)
    this_set = set(result_dict.keys())
    workers = [
        {'left': 0, 'alpha': ''},
        {'left': 0, 'alpha': ''},
        {'left': 0, 'alpha': ''},
        {'left': 0, 'alpha': ''},
        {'left': 0, 'alpha': ''}
    ]
    count = 0
    while True:
        if len(this_set) == 0:
            flag = True
            for index, each_worker in enumerate(workers):
                if each_worker['left'] != 0:
                    flag = False
            if flag:
                break
        all_data = list(result_dict.keys())
        all_data.sort()
        for index, each_worker in enumerate(workers):
            if workers[index]['left'] == 0:
                for each_start in all_data:
                    if each_start not in this_set:
                        continue
                    if len(result_dict[each_start]['from']) == 0:
                        this_list.append(each_start)
                        this_set.remove(each_start)
                        workers[index]['left'] = ord(each_start) - ord('A') + 61
                        workers[index]['alpha'] = each_start
                        break
        for index, each_worker in enumerate(workers):
            if workers[index]['left'] == 0:
                continue
            workers[index]['left'] -= 1
            if workers[index]['left'] == 0:
                this_start = workers[index]['alpha']
                for each_stop in result_dict[this_start]['to']:
                    result_dict[each_stop]['from'].remove(this_start)
        count += 1
    print(count)


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    # solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
