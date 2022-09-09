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

def count_values_by_time_of_day(data : list, tod : str) -> dict:
    """Convenience function to summarize calls by time of day and day of week.

    :param: data - a list of dicts
    :param: tod - the time of day to match for counting
    "returns: a dictionary of days of week and number of calls
    """
    result = {}

    for record in data:    
        day_of_week = record['DAY_OF_WEEK']
        time_of_day = record['TIME_OF_DAY']
        if time_of_day == tod:
            if day_of_week in result:
                result[day_of_week] += 1
            else:
                result[day_of_week] = 1
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
