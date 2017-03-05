import xlwt

xls_file = 'C:\\tmp\\sample.xls'
book = xlwt.Workbook()
sheet = book.add_sheet('NewSheet_1')
sheet.write(0,0,'あいうえお')
book.save(xls_file)