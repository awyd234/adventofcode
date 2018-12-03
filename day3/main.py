# -*- coding: utf-8 -*-


def read_txt(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [_.replace('\n', '') for _ in data]
        return data


def solution1(data):
    result_dict = {}
    location_set = set()
    for each_data in data:
        str_list = each_data.split(' ')
        this_id = int(''.join(str_list[0].split('#')[1:]))
        left_right_edges = str_list[2].replace(':', '')
        left_edge_str, top_edge_str = left_right_edges.split(',')
        left_edge = int(left_edge_str)
        top_edge = int(top_edge_str)
        width_str, height_str = str_list[3].split('x')
        width = int(width_str)
        height = int(height_str)
        for row in range(left_edge, left_edge + width):
            for col in range(top_edge, top_edge + height):
                index = row + col * 1000
                if index not in result_dict:
                    result_dict[index] = set([this_id])
                else:
                    location_set.add(index)
    print(len(location_set))


def solution2(data):
    result_dict = {}
    for each_data in data:
        str_list = each_data.split(' ')
        this_id = int(''.join(str_list[0].split('#')[1:]))
        left_right_edges = str_list[2].replace(':', '')
        left_edge_str, top_edge_str = left_right_edges.split(',')
        left_edge = int(left_edge_str)
        top_edge = int(top_edge_str)
        width_str, height_str = str_list[3].split('x')
        width = int(width_str)
        height = int(height_str)
        for row in range(left_edge, left_edge + width):
            for col in range(top_edge, top_edge + height):
                index = row + col * 1000
                if result_dict.get(index) is None:
                    result_dict[index] = set()
                result_dict[index].add(this_id)
    for each_data in data:
        str_list = each_data.split(' ')
        this_id = int(''.join(str_list[0].split('#')[1:]))
        left_right_edges = str_list[2].replace(':', '')
        left_edge_str, top_edge_str = left_right_edges.split(',')
        left_edge = int(left_edge_str)
        top_edge = int(top_edge_str)
        width_str, height_str = str_list[3].split('x')
        width = int(width_str)
        height = int(height_str)
        flag = True
        for row in range(left_edge, left_edge + width):
            if not flag:
                break
            for col in range(top_edge, top_edge + height):
                index = row + col * 1000
                if len(result_dict[index]) > 1:
                    flag = False
                    break
        if flag:
            print(this_id)


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    # solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
