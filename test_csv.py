import csv
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
current = os.path.abspath(__file__)
print(current)
project_root = os.path.dirname(current)
print(project_root)
joined_path = os.path.join(project_root, 'resources', 'new_csv.csv')
print(joined_path)


def test_csv():
    with open(joined_path, 'w') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])



def test_csv2():
    with open(joined_path) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            print(row)
    assert row == ['Bonny', 'Born', 'Peter']
    assert row == ['Alex', 'Serj', 'Yana']
