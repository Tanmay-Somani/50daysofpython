import timeit
a = range(10000000)
x = set(a)
y = list(a)
num = 9999999
list_time = timeit.timeit(lambda: num in y, number=1)
set_time = timeit.timeit(lambda: num in x, number=1)
if list_time > set_time:
    print(list_time, ":list_time")
else:
    print(set_time, ":set_time")
