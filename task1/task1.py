from sys import argv

__INNER_PARAM = argv[1:]


def check_param(params):
    return len(params) == 2 and all(map(lambda x: x.isdigit() and x != '0', params))


def loop_array(params):
    loop_len, interval = map(int, params)
    loop_path = []

    loop = list(range(1, loop_len + 1))[:] * (1 + interval // loop_len)
    control_item = loop[0]

    while True:
        loop_path.append(loop[0])
        if loop[interval - 1] == control_item:
            print(*loop_path, sep='')
            break
        loop = loop[interval - 1:] + loop[:interval - 1]


if __name__ == '__main__':
    if check_param(params=__INNER_PARAM):
        loop_array(__INNER_PARAM)
    else:
        print(f'Передайте программе при запуске два параметра - целые положительные числа\nВведено: {__INNER_PARAM}')
