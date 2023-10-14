import os
import xlrd

from openpyxl import load_workbook
from zipfile import ZipFile
from PyPDF2 import PdfReader

from utils import PDF_RESOURCES_PATH, TXT_RESOURCES_PATH, XLS_RESOURCES_PATH, XLSX_RESOURCES_PATH, TMP_PATH

def test_archive_files(tmp_dir):
    if os.path.exists("test.zip"):
        os.remove("test.zip")

    pdf_size = os.path.getsize(PDF_RESOURCES_PATH)
    pdf_name = os.path.basename(PDF_RESOURCES_PATH)
    text_size = os.path.getsize(TXT_RESOURCES_PATH)
    text_name = os.path.basename(TXT_RESOURCES_PATH)
    xls_size = os.path.getsize(XLS_RESOURCES_PATH)
    xls_name = os.path.basename(XLS_RESOURCES_PATH)
    xlsx_size = os.path.getsize(XLSX_RESOURCES_PATH)
    xlsx_name = os.path.basename(XLSX_RESOURCES_PATH)

    with ZipFile(os.path.join(TMP_PATH, 'test.zip'), mode='a') as zf:
        zf.write(filename=PDF_RESOURCES_PATH, arcname='Python Testing with Pytest (Brian Okken).pdf')
        zf.write(filename=TXT_RESOURCES_PATH, arcname='Hello, world.txt')
        zf.write(filename=XLS_RESOURCES_PATH, arcname='file_example_XLS_10.xls')
        zf.write(filename=XLSX_RESOURCES_PATH, arcname='file_example_XLSX_50.xlsx')

    with ZipFile(os.path.join(TMP_PATH, 'test.zip'), mode="r") as zf:
        pdf_archive_file = zf.getinfo("Python Testing with Pytest (Brian Okken).pdf")
        pdf_archive_file_name = pdf_archive_file.filename
        pdf_archive_file_size = pdf_archive_file.file_size
        with zf.open("Python Testing with Pytest (Brian Okken).pdf") as pdf_r:
            pdf_r = PdfReader(pdf_r)
            page = pdf_r.pages[1]
            assert 'Every precaution was taken' in page.extract_text()
            assert len(pdf_r.pages) == 256

        txt_archive_file = zf.getinfo("Hello, world.txt")
        txt_archive_file_name = txt_archive_file.filename
        txt_archive_file_size = txt_archive_file.file_size
        with zf.open('Hello, world.txt') as txt_r:
            text = txt_r.read().decode('utf-8')
            assert 'Hello' in text

        xls_archive_file = zf.getinfo("file_example_XLS_10.xls")
        xls_archive_file_name = xls_archive_file.filename
        xls_archive_file_size = xls_archive_file.file_size
        with zf.open('file_example_XLS_10.xls') as xls_r:
            book = xlrd.open_workbook(file_contents=xls_r.read())
            sheet = book.sheet_by_index(0)
            cell_value = sheet.cell_value(7, 5)
            assert cell_value == 56

        xlsx_archive_file = zf.getinfo("file_example_XLSX_50.xlsx")
        xlsx_archive_file_name = xlsx_archive_file.filename
        xlsx_archive_file_size = xlsx_archive_file.file_size
        with zf.open('file_example_XLSX_50.xlsx') as xlsx_r:
            workbook = load_workbook(xlsx_r)
            sheet = workbook.active
            assert len(sheet['A']) == 51


    assert pdf_name == pdf_archive_file_name, \
        f"Имя файла {pdf_name} не совпадает с именем {pdf_archive_file_name} в архиве"
    assert pdf_size == pdf_archive_file_size, \
        f"Размер файла {pdf_size} не совпадает с размером {pdf_archive_file_size} в архиве"
    assert text_name == txt_archive_file_name, \
        f"Имя файла {text_name} не совпадает с именем {txt_archive_file_name} в архиве"
    assert text_size == txt_archive_file_size, \
        f"Размер файла {text_size} не совпадает с размером {txt_archive_file_size} в архиве"
    assert xls_name == xls_archive_file_name,\
        f"Имя файла {xls_name} не совпадает с именем {xls_archive_file_name} в архиве"
    assert xls_size == xls_archive_file_size, \
        f"Размер файла {xls_size} не совпадает с размером {xls_archive_file_size} в архиве"
    assert xlsx_name == xlsx_archive_file_name, \
        f"Имя файла {xlsx_name} не совпадает с именем {xlsx_archive_file_name} в архиве"
    assert xlsx_size == xlsx_archive_file_size, \
        f"Имя файла {xlsx_size} не совпадает с размером {xlsx_archive_file_size}"