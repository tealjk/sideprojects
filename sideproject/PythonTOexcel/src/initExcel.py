#!/usr/bin/python


import xlrd


wb = xlrd.open_workbook('/Users/junkim/Desktop/PythonTOexcel/staging/inputdata/dataexcel.xlsx')
wb2 = xlrd.open_workbook('/Users/junkim/Desktop/PythonTOexcel/staging/inputdata/dataexcel.xlsx')




def loadworkbookrow(wb2):

    ws = wb2.sheet_by_name(u'Wave 2 Attend. Data (Long)')




    num_rows = ws.nrows - 1
    curr_row = -1


    while curr_row < num_rows:
        curr_row += 1
        row = ws.row(curr_row)


        #put this row into a list: next idea

        print row







    return





loadworkbookrow(wb2)


