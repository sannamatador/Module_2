data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


list_all =[]
def calculate_structure_sum(*args):
    for i in args:
        if type(i) == int:
            list_all.append(i)
        elif type(i) == str:
            list_all.append(len(i))
        elif isinstance(i, (tuple, list, set)):
            for j in i:
                j = calculate_structure_sum(j)
        elif isinstance(i, dict):
            i = set(i.items())
            for j in args :
                j = calculate_structure_sum(i)
   # print(list_all)
    return sum(list_all)


result1 = calculate_structure_sum(data_structure)
print(result1)

