## VERSION == 1.0.0

import csv

def load_csv_dict(csvfile):
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
        header_row = next(csv_reader)
        print(f'header_row == {header_row}')

        for row in csv_reader:
            new_record = {}
            for i, value in enumerate(row):
                new_record[header_row[i]] = value
            dict_array.append(new_record)
            
    return dict_array