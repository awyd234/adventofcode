# -*- coding: utf-8 -*-


def read_txt(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [_.replace('\n', '') for _ in data]
        return data


def solution1(data):
    result_dict = {}
    min_x = 100000
    min_y = 100000
    max_x = -100
    max_y = -100

    for each_data in data:
        x, y = each_data.split(', ')
        x = int(x)
        y = int(y)
        result_dict[each_data] = {
            'x': x,
            'y': y,
            'count': 0
        }
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    for this_x in range(min_x, max_x + 1):
        for this_y in range(min_y, max_y + 1):
            this_distance = 1000000
            this_point = ''
            flag = True
            for each_data, detail in result_dict.items():
                each_distance = abs(this_x - detail['x']) + abs(this_y - detail['y'])
                if each_distance < this_distance:
                    this_distance = each_distance
                    this_point = each_data
                    flag = True
                elif each_distance == this_distance:
                    flag = False
            if flag:
                result_dict[this_point]['count'] += 1
    this_list = [_['count'] for k, _ in result_dict.items()]
    this_list.sort(reverse=True)
    print(this_list)


def solution2(data):
    result_dict = {}
    min_x = 10000
    min_y = 10000
    max_x = -1000
    max_y = -1000

    for each_data in data:
        x, y = each_data.split(', ')
        x = int(x)
        y = int(y)
        result_dict[each_data] = {
            'x': x,
            'y': y,
            'count': 0
        }
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    count = 0
    for this_x in range(min_x, max_x + 1):
        for this_y in range(min_y, max_y + 1):
            this_distance = 0
            for each_data, detail in result_dict.items():
                each_distance = abs(this_x - detail['x']) + abs(this_y - detail['y'])
                this_distance += each_distance
                if this_distance > 10000:
                    break
            if this_distance < 10000:
                count += 1

    print(count)


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    # solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
