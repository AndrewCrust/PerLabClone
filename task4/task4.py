from sys import argv


def main(nums):
    steps_dct = {num: sum([abs(item - num) * nums.count(item) for item in set(nums) if item != num]) for num in nums}
    return min(steps_dct.values())


if __name__ == '__main__':
    try:
        path = argv[1]
        with open(path, 'r', encoding='utf-8') as file:
            data = list(map(int, file.readlines()))
            print(main(nums=data))

    except Exception as e:
        print(e)
