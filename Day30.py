def repeated_name(names):

    name_counts = {}

    for name in names:
        if name not in name_counts:
            name_counts[name] = 1
        else:
            name_counts[name] += 1
    most_repeated_name = names[0]
    max_count = name_counts[most_repeated_name]

    for name, count in name_counts.items():
        if count > max_count:
            most_repeated_name = name
            max_count = count

    return most_repeated_name


names = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(names))
