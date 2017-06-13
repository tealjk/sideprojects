#!/usr/bin/python

import xlsxwriter


def createnewworkbook():


    workbook = xlsxwriter.Workbook('/Users/junkim/Desktop/PythonTOexcel/staging/finalendpoint/newdoc.xlsx')

    worksheet = workbook.add_worksheet('New')
    worksheet = workbook.add_worksheet('New 2')
    worksheet = workbook.add_worksheet('New 3')

    worksheet.set_column('A:A', 20)
    worksheet.write('A1','Hello')
    workbook.close()


    return

createnewworkbook()




