def value_predictor(value):
    # check length
    n = len(value)
    # check at least 6 elements and sort the list
    if n >= 6 and sorted(value):
        # check even number of value
        if n % 2 != 0:
            x = float(value[n / 2])
            return x
        return float(value[int(n / 2)] + value[int((n - 1) / 2)]) / 2.0

    else:
        return "List must have at least 6 elements"


print(value_predictor([1, 2, 3, 4, 5, 6]))
print(value_predictor([1, 1, 1, 6, 6, 6]))
