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