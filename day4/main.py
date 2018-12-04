# -*- coding: utf-8 -*-
import datetime


def read_txt(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [_.replace('\n', '') for _ in data]
        return data


def solution1(data):
    data.sort(key=lambda x: x[:18])
    result_dict = {}
    today_asleep_set = set()
    guard_id = None
    for index, each_data in enumerate(data):
        dt_str = each_data.split(']')[0][1:]
        dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M')
        this_data_list = each_data.split(' ')
        now_minute = dt.minute
        print(each_data)
        if this_data_list[2] == 'Guard':
            if guard_id is not None:
                result_dict[guard_id]['count'] += len(today_asleep_set)
                for each_minute in today_asleep_set:
                    if result_dict[guard_id]['asleep'].get(each_minute) is None:
                        result_dict[guard_id]['asleep'][each_minute] = 0
                    result_dict[guard_id]['asleep'][each_minute] += 1
                today_asleep_set = set()
            guard_id = int(this_data_list[3][1:])
            if result_dict.get(guard_id) is None:
                result_dict[guard_id] = {
                    'count': 0,
                    'asleep': {}
                }
        elif this_data_list[2] == 'falls':
            asleep_start = now_minute
        elif this_data_list[2] == 'wakes':
            asleep_end = now_minute
            asleep_list = list(range(asleep_start, asleep_end))
            today_asleep_set = today_asleep_set.union(set(asleep_list))
    result_dict[guard_id]['count'] += len(today_asleep_set)
    for each_minute in today_asleep_set:
        if result_dict[guard_id]['asleep'].get(each_minute) is None:
            result_dict[guard_id]['asleep'][each_minute] = 0
        result_dict[guard_id]['asleep'][each_minute] += 1

    result_list = [[k, v] for k, v in result_dict.items()]
    result_list.sort(key=lambda x: -x[1]['count'])
    asleep_most_guard_list = result_list[0]
    asleep_most_guard_id = asleep_most_guard_list[0]
    asleep_most_guard_asleep_list = [[k, v] for k, v in asleep_most_guard_list[1]['asleep'].items()]
    asleep_most_guard_asleep_list.sort(key=lambda x: -x[1])
    print(asleep_most_guard_id * asleep_most_guard_asleep_list[0][0])


def solution2(data):
    data.sort(key=lambda x: x[:18])
    result_dict = {}
    today_asleep_set = set()
    guard_id = None
    for index, each_data in enumerate(data):
        dt_str = each_data.split(']')[0][1:]
        dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M')
        this_data_list = each_data.split(' ')
        now_minute = dt.minute
        print(each_data)
        if this_data_list[2] == 'Guard':
            if guard_id is not None:
                result_dict[guard_id]['count'] += len(today_asleep_set)
                for each_minute in today_asleep_set:
                    if result_dict[guard_id]['asleep'].get(each_minute) is None:
                        result_dict[guard_id]['asleep'][each_minute] = 0
                    result_dict[guard_id]['asleep'][each_minute] += 1
                today_asleep_set = set()
            guard_id = int(this_data_list[3][1:])
            if result_dict.get(guard_id) is None:
                result_dict[guard_id] = {
                    'count': 0,
                    'asleep': {}
                }
        elif this_data_list[2] == 'falls':
            asleep_start = now_minute
        elif this_data_list[2] == 'wakes':
            asleep_end = now_minute
            asleep_list = list(range(asleep_start, asleep_end))
            today_asleep_set = today_asleep_set.union(set(asleep_list))
    result_dict[guard_id]['count'] += len(today_asleep_set)
    for each_minute in today_asleep_set:
        if result_dict[guard_id]['asleep'].get(each_minute) is None:
            result_dict[guard_id]['asleep'][each_minute] = 0
        result_dict[guard_id]['asleep'][each_minute] += 1

    result_list = [[k, v] for k, v in result_dict.items()]
    most_minute = 0
    this_guard_id = 0
    this_minute = 0
    for guard_id, detail in result_list:
        for each_minute, count in detail['asleep'].items():
            if count > most_minute:
                this_guard_id = guard_id
                most_minute = count
                this_minute = each_minute
    print(this_guard_id * this_minute)


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    # solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
