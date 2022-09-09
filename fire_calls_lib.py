def count_values(data : list, key : str) -> dict:
    """Convenience function to count the occurances of values for a key in a 
    list of dict objects

    :param: data - a list of dict objects
    :param: key - the key to be counted
    :return: - a dict of each value found and the number of occurances
    """
    result = {}
    for record in data:
        if record[key] not in result:
            result[record[key]] = 1
        else:
            result[record[key]] += 1
    return result

def get_unique_values(data : list, key : str) -> list:
    """Convenience function to get the unique values for a key in a list of 
    dict objects

    :param: data - a list of dict objects
    :param: key - the key to be counted
    :return: - a dict of each unique value found 
    """
    result = []
    for record in data:
        value = record[key]
        if value not in result:
            result.append(value)
    return result

if __name__ == '__main__':
    pass
