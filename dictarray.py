## VERSION == 1.0.0

def rename_col(old_name: str, new_name: str, data: list): 
    """_summary_

    Args:
        old_name (str): _description_
        new_name (str): _description_
        data (list): _description_

    Returns:
        [dict]: modified set of data with a column renamed
    """
    
    for record in data:
        record[new_name] = record[old_name]
        del record[old_name]
    
    return data


def format_col(col_name, func, data):

    for record in data:
        record[col_name] = func(record[col_name])
    
    return data

def query(data, /, select, where, equals):
    """This will perform a simple query on a list of objects loaded into memory by 
    finding the item 'select' which corresponds to the item 'where == value'
    if the 'value' is not found, None is returned

    Args:
        data (object[]): the array of objects to search through
        select (str): the value within the record that matched 
        where (str): the field name to look through
        value (str): the value to search for

    Returns:
        object or None: the object that matched the query, or None
    """
    for record in data:
        if record[where] == equals:
            if select == None:
                return record
            else:
                return record[select]
    return None
