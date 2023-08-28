import os

PROJECT_ROOT_PATH = os.path.dirname(__file__)
print(PROJECT_ROOT_PATH)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resources'))
print(RESOURCE_PATH)
xlsx_path = os.path.join(RESOURCE_PATH,'file_example_XLSX_50.xlsx')
xls_path = os.path.join(RESOURCE_PATH, 'file_example_XLS_10.xls')
pdf_path = os.path.join(RESOURCE_PATH, 'docs-pytest-org-en-latest.pdf')
csv_path = os.path.join(RESOURCE_PATH, 'new_csv.csv')
zip_path = os.path.join(RESOURCE_PATH, 'new_zip.zip')
