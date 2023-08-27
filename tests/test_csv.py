import csv
from conftest import RESOURCE_PATH, csv_path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_csv():
    with open(csv_path, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])


    with open(csv_path) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')

        names = []
        for row in csvreader:
            print(row)
            names.append(row)
    assert names == [['Bonny', 'Born', 'Peter'], ['Alex', 'Serj', 'Yana']]
    assert len(names) == 2
