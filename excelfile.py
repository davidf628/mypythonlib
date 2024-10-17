from openpyxl import load_workbook

def load_dictarray(wbfile):

    wb = load_workbook(wbfile)
    ws = wb.active

    dict_array = []
    headers = {}
    
    # Get all the row headers
    for col in range(1, ws.max_column + 1):
        value = ws.cell(row=1, column=col).value
        if value != None:
            headers[value] = col

    # Now get all the student data
    for row in range(2, ws.max_row + 1):
        record = {}
        for header in headers.keys():
            col = headers[header]
            value = ws.cell(row=row, column=col).value
            if value != None:
                record[header] = value
            else:
                record[header] = ''
        dict_array.append(record)

    wb.close()
            
    return dict_array
