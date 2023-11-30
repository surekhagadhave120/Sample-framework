import xlrd
from Library.config import Config


def read_locators(sheetname):
    """retuns the headers of the testcase in comma seprated string"""
    wb = xlrd.open_workbook(Config.OBJECTS_FILE_PATH)
    ws = wb.sheet_by_name(sheetname)
    total_rows = ws.nrows
    objects = {}
    for index in range(1, total_rows):
        row = ws.row_values(index)
        objects[row[0]] = (row[1], row[2])
    return objects
