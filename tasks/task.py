def union(*args) -> set:
    my_set = set()
    for values in args:
        value = set(values)
        my_set = my_set.union(value)
    return my_set

def intersect(*args) -> set:
    new_set = set(args[0])
    for values in args:
        value = set(values)
        new_set = new_set.intersection(value)
    return new_set

