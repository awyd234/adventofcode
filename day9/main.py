# -*- coding: utf-8 -*-


def read_txt(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [_.replace('\n', '') for _ in data]
        return data


def solution1(data):
    data = data[0]
    players_num = int(data.split(' ')[0])
    last_points = int(data.split(' ')[-2])
    scores = [0 for _ in range(players_num)]
    all_data = [0]
    now = 2
    if now > len(all_data):
        now = now - len(all_data)
    for count in range(1, last_points + 1):
        each_player = (count - 1) % players_num
        if count != 0 and count % 23 == 0:
            scores[each_player] += count
            now -= 9
            this_data = all_data.pop(now)
            scores[each_player] += this_data
            now += 2
            if now < 0:
                now = now + len(all_data) + 1
            continue
        all_data.insert(now, count)
        now += 2
        if now > len(all_data):
            now = now - len(all_data)
    print(max(scores))


def solution2(data):
    data = data[0]
    players_num = int(data.split(' ')[0])
    last_points = int(data.split(' ')[-2])
    last_points *= 100
    scores = [0 for _ in range(players_num)]
    all_data = [{
        'value': 0,
        'prev': 0,
        'next': 0
    }]
    now = 0
    for count in range(1, last_points + 1):
        each_player = (count - 1) % players_num
        if count % 23 == 0:
            scores[each_player] += count
            for _ in range(7):
                now = all_data[now]['prev']
            all_data[all_data[now]['prev']]['next'] = all_data[now]['next']
            all_data[all_data[now]['next']]['prev'] = all_data[now]['prev']
            scores[each_player] += now
            now = all_data[now]['next']
            all_data.append([])
        else:
            old_now = now
            old_now_next = all_data[old_now]['next']
            old_now_next_next = all_data[old_now_next]['next']
            now = count
            if now == old_now_next:
                now = count
            all_data[old_now_next]['next'] = count
            all_data[old_now_next_next]['prev'] = count
            all_data.append({
                'value': count,
                'prev': old_now_next,
                'next': old_now_next_next
            })
    print(max(scores))


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    solution1(data)
    # solution2(data)


if __name__ == '__main__':
    main()
