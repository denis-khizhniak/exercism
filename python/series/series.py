def slices(series, length):
    if 0 < length <= len(series):
        return [series[i:i+length] for i in range(len(series) - length + 1)]
    else:
        raise ValueError('Length value is not valid!')
