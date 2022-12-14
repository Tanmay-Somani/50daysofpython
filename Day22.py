def add_hash(x):
    y = "#".join(x)
    return y


def add_underscore(y):
    y = y.replace('#', '_')
    return y


def remove_underscore(y):
    y = y.replace('_', '')
    return y


print(remove_underscore(add_underscore(add_hash("Python"))))
