#!/usr/bin/python





import xlrd

from openpyxl import load_workbook

from openpyxl import Workbook

#This will load the excel document

wb = xlrd.open_workbook('/Users/junkim/Desktop/PythonTOexcel/staging/inputdata/dataexcel.xlsx')

#wb2 = xlrd.load_workbook('/Users/junkim/Desktop/PythonTOexcel/staging/finalendpoint/newMay16Method.xlsx')


#Reads each excel sheet prints name.

def loadworkbookbyname(wb):
    print wb.get_sheet_names()
    return

#this handles reading in the SHEETexcel and formatting each ROW





def loadworkbookrow(wb):

    ws = wb.sheet_by_name(u'Wave 2 Attend. Data (Long)')

    num_rows = ws.nrows - 1
    curr_row = -1


    while curr_row < num_rows:
        curr_row += 1
        row = ws.row(curr_row)


        #put this row into a list: next idea

        print row
    return



loadworkbookbyname(wb)





