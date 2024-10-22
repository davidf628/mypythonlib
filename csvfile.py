## VERSION == 1.1.0

import csv
import dictarray as da

def load_dictarray(csvfile: str):
    """Loads a csv formatted file into an array of dict, which
    uses the first line as the keys, and each line of the file
    as values. Each line will get it's own dict structure and
    will be placed in an array.

    Args:
        csvfile (str): filepath of the data to load

    Returns:
        [dict]: a list containing dict key/value pairs for the
        data within the file
    """
    dict_array = []
    headers = []
    
    with open(csvfile, encoding='ISO-8859-1') as f:
        csv_reader = csv.reader(f, delimiter=',')

        # Get the first line
        headers = next(csv_reader)

        for row in csv_reader:
            new_record = {}
            for i, value in enumerate(row):
                new_record[headers[i]] = value
            dict_array.append(new_record)
            
    return dict_array


def _load_listarray(csvfile: str):
    None


def write_listarry(data: list, filename: str):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

###############################################################################
# Compares two different CSV files to see if any data between them is
#  different. It works by scanning both files based on a shared keyfield
#  (which defaults to column 1 if not specified) to see if the entries within
#  each are the same or not. The output is a third set of data that can be
#  written to disk containing only the changes between the two data sets

def csvdiff (file1, file2, keyfield=None):
    file1_data = load_dictarray(file1)
    file2_data = load_dictarray(file2)
    diff = []

    if keyfield == None:
        keyfield = list(file1_data[0].keys())[0]

    for data1_row in file1_data:
        cur_row_key = data1_row[keyfield]
        data2_row = da.query(file2_data, select=None, where=keyfield, equals=cur_row_key)
        diff_record = {}

        if data2_row != None:
            for item in data1_row:
                value_in_data1 = data1_row.get(item, None)
                value_in_data2 = data2_row.get(item, None)
                if value_in_data1 == None or value_in_data2 == None or (value_in_data1 != value_in_data2):
                    diff_record[keyfield] = cur_row_key
                    diff_record[item] = value_in_data1
        else:
            diff_record = data1_row
            
        if len(diff_record) > 0:
            print(diff_record)
            diff.append(diff_record)

    for data2_row in file2_data:
        cur_row_key = data2_row[keyfield]
        data1_row = da.query(file1_data, select=None, where=keyfield, equals=cur_row_key)
        diff_record = {}
        if data1_row != None:
            for item in data2_row:
                value_in_data1 = data1_row.get(item, None)
                value_in_data2 = data2_row.get(item, None)
                if value_in_data1 == None or value_in_data2 == None or (value_in_data1 != value_in_data2):
                    diff_record[keyfield] = cur_row_key
                    diff_record[item] = value_in_data2
        else:
            diff_record = data2_row
        
        if len(diff_record) > 0:
            print(diff_record)
            diff.append(diff_record)

