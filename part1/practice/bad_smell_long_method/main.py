# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list(csv: csv):
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(data):
    return [d.split(";") for d in data.split("\n")]


def _sort(data):
    return sorted(data, key=lambda age: int(age[1]))


def _filter(data):
    return [user for user in data if int(user[1]) > 10]


if __name__ == '__main__':
    print(get_users_list(csv))
