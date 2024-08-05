import json
import re
from sys import argv

__INNER__PARAMS = argv[1:]


def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        obj = json.load(file)
        return obj


def write_report(path, obj):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(obj, file)


def check_path(path):
    return bool(re.match(r'^\S+.json$', path))


def find_test(test_id, obj_list):
    result = ''
    for obj in obj_list:
        if isinstance(obj, dict):
            if obj.get('id', None) == test_id:
                result = obj.get('value', '')
                return result
            else:
                for value in obj.values():
                    if isinstance(value, dict):
                        result = find_test(test_id=test_id, obj_list=[value])
                    if isinstance(value, list):
                        result = find_test(test_id=test_id, obj_list=value)

        elif isinstance(obj, list):
            result = find_test(test_id=test_id, obj_list=obj)

    else:
        return result


def forming_report(values, tests):
    for obj in tests:
        if isinstance(obj, dict):
            test_id = obj.get("id", None)

            if test_id is not None:
                obj["value"] = find_test(test_id=test_id, obj_list=[values])

            for value in obj.values():
                if isinstance(value, dict):
                    forming_report(values=values, tests=[value])
                if isinstance(value, list):
                    forming_report(values=values, tests=value)

        elif isinstance(obj, list):
            forming_report(values=values, tests=obj)

    return tests[0]


def main(test_result_path, tests_template_path, report_path):
    tests_result = read_file(path=test_result_path)
    tests_template = read_file(path=tests_template_path)
    report = forming_report(values=tests_result, tests=[tests_template])
    write_report(path=report_path, obj=report)


if __name__ == '__main__':
    if len(__INNER__PARAMS) != 3:
        print('Передайте три пути к фалам при запуске')
    else:
        if not all([check_path(path) for path in __INNER__PARAMS]):
            print("В названии путей используйте формат 'json'")
        else:
            result_path, tests_path, rep_path = __INNER__PARAMS
            main(test_result_path=result_path, tests_template_path=tests_path, report_path=rep_path)
