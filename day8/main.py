# -*- coding: utf-8 -*-


def read_txt(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [_.replace('\n', '') for _ in data]
        return data


def solution1(data):
    data = data[0]
    data_list = data.split(' ')
    this_list = []

    this_index = 0
    children_num = int(data_list[this_index])
    meta_data_num = int(data_list[this_index + 1])
    this_index += 2
    this_list.append({
        'children': children_num,
        'meta_num': meta_data_num,
        'meta_data': []
    })
    all_data_list = []
    while this_index < len(data_list):
        if this_list[-1]['children'] != 0:
            this_list[-1]['children'] -= 1
            children_num = int(data_list[this_index])
            meta_data_num = int(data_list[this_index + 1])
            this_list.append({
                'children': children_num,
                'meta_num': meta_data_num,
                'meta_data': []
            })
            this_index += 2
        if this_list[-1]['children'] == 0:
            this_list[-1]['meta_data'] = data_list[this_index:this_index + this_list[-1]['meta_num']]
            this_index += this_list[-1]['meta_num']
            all_data_list.append(this_list[-1])
            this_list.pop()
    count = 0
    for each_data in all_data_list:
        for each_num in each_data['meta_data']:
            count += int(each_num)
    print(count)


def solution2(data):
    data = data[0]
    data_list = data.split(' ')
    this_list = []

    this_index = 0
    children_num = int(data_list[this_index])
    meta_data_num = int(data_list[this_index + 1])
    this_index += 2
    this_list.append({
        'children': children_num,
        'meta_num': meta_data_num,
        'children_dict': {
            'this_list': [],
            'this_set': set(),
            'num': {}
        },
        'parent': -1,
        'index': 100000,
        'value': 0,
    })
    all_data_count = 0
    all_data_list = []
    while this_index < len(data_list):
        if this_list[-1]['children'] != 0:
            this_list[-1]['children'] -= 1
            this_list[-1]['children_dict']['this_list'].append(all_data_count)
            this_list[-1]['children_dict']['this_set'].add(all_data_count)
            this_list[-1]['children_dict']['num'][all_data_count] = 0
            children_num = int(data_list[this_index])
            meta_data_num = int(data_list[this_index + 1])
            this_list.append({
                'children': children_num,
                'meta_num': meta_data_num,
                'parent': this_list[-1]['index'],
                'children_dict': {
                    'this_list': [],
                    'this_set': set(),
                    'num': {}
                },
                'index': all_data_count,
                'value': 0
            })
            all_data_count += 1
            this_index += 2
        if this_list[-1]['children'] == 0:
            for each_meta in data_list[this_index:this_index + this_list[-1]['meta_num']]:
                each_meta_int = int(each_meta)
                if len(this_list[-1]['children_dict']['this_list']) == 0:
                    this_list[-1]['value'] += each_meta_int
                if each_meta_int <= len(this_list[-1]['children_dict']['this_list']):
                    this_list[-1]['children_dict']['num'][this_list[-1]['children_dict']['this_list'][each_meta_int - 1]] += 1
            this_index += this_list[-1]['meta_num']
            all_data_list.append(this_list[-1])
            this_list.pop()
    all_data_list.sort(key=lambda x: x['index'])

    all_index_set = set([_['index'] for _ in all_data_list])
    all_index_set.remove(100000)
    while len(all_index_set) != 0:
        left_index_list = list(all_index_set)
        for each_index in left_index_list:
            if len(all_data_list[each_index]['children_dict']['this_set']) == 0:
                parent = all_data_list[each_index]['parent']
                if parent == 100000:
                    parent = -1
                all_data_list[parent]['children_dict']['this_set'].remove(each_index)
                all_data_list[parent]['value'] += all_data_list[each_index]['value'] \
                                                      * all_data_list[parent]['children_dict']['num'][each_index]
                all_index_set.remove(each_index)
                break

    print(all_data_list[-1]['value'])


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    # solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
