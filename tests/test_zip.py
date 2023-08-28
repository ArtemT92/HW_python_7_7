
from zipfile import ZipFile
from conftest import RESOURCE_PATH, pdf_path, xls_path, xlsx_path, csv_path, zip_path

def test_zip_file():
    with ZipFile(zip_path, 'w') as newzip:
        newzip.write(pdf_path, 'docs-pytest-org-en-latest.pdf')
        newzip.write(xls_path, 'file_example_XLS_10.xls')
        newzip.write(xlsx_path, 'file_example_XLS_50.xlsx')
        newzip.write(csv_path, 'new_csv.csv')



    with ZipFile(zip_path, 'r') as newzip:

        names = []
        for item in newzip.namelist():
            print(item)
            names.append(item)

        assert names == ['docs-pytest-org-en-latest.pdf', 'file_example_XLS_10.xls', 'file_example_XLS_50.xlsx', 'new_csv.csv']














